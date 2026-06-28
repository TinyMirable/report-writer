#!/usr/bin/env python3
"""Render DOCX reports to page PNGs for visual QA.

This script is bundled with the class-design-report-writer skill so future
agents do not need to guess how to locate LibreOffice/soffice in CODEX desktop,
Windows, programfiles, or PATH-based environments.
"""

from __future__ import annotations

import argparse
import glob
import os
import re
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET
from os import makedirs, replace
from os.path import abspath, basename, exists, expanduser, join, splitext
from pathlib import Path
from typing import Sequence, cast
from zipfile import ZipFile

from pdf2image import convert_from_path, pdfinfo_from_path

TWIPS_PER_INCH: int = 1440


def _default_macos_tmpdir_for_soffice() -> None:
    if sys.platform != "darwin":
        return
    if not os.path.isdir("/private/tmp"):
        return
    tmpdir = os.environ.get("TMPDIR", "")
    tmpdir_norm = os.path.realpath(tmpdir.rstrip(os.sep) or tmpdir)
    if tmpdir_norm == "/private/tmp":
        return
    os.environ["TMPDIR"] = "/private/tmp"
    os.environ["TEMP"] = "/private/tmp"
    os.environ["TMP"] = "/private/tmp"
    tempfile.tempdir = "/private/tmp"


def _candidate_soffice_paths() -> list[str]:
    candidates: list[str] = []
    names = ["soffice.exe", "soffice.com", "soffice"] if os.name == "nt" else ["soffice"]

    env_keys = ["SOFFICE_PATH", "LIBREOFFICE_PATH"]
    for key in env_keys:
        value = os.environ.get(key)
        if value:
            candidates.append(value)

    python_root = Path(sys.executable).resolve().parent.parent
    if python_root.name.lower() == "python":
        dependencies_root = python_root.parent
        if dependencies_root.name.lower() == "dependencies":
            for name in names:
                candidates.append(str(dependencies_root / "bin" / name))

    current = Path(__file__).resolve()
    for parent in current.parents:
        if parent.name == "codex-primary-runtime":
            for name in names:
                candidates.append(str(parent / "dependencies" / "bin" / name))
            break

    which = shutil.which("soffice")
    if which:
        candidates.append(which)

    if os.name == "nt":
        program_roots = [
            os.environ.get("PROGRAMFILES"),
            os.environ.get("PROGRAMFILES(X86)"),
            os.environ.get("LOCALAPPDATA"),
        ]
        for root in program_roots:
            if not root:
                continue
            candidates.extend(
                [
                    str(Path(root) / "LibreOffice" / "program" / "soffice.exe"),
                    str(Path(root) / "LibreOffice" / "program" / "soffice.com"),
                ]
            )
        candidates.extend(
            [
                r"C:\Program Files\LibreOffice\program\soffice.exe",
                r"C:\Program Files\LibreOffice\program\soffice.com",
                r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
                r"C:\Program Files (x86)\LibreOffice\program\soffice.com",
            ]
        )

    seen: set[str] = set()
    unique: list[str] = []
    for candidate in candidates:
        norm = os.path.normcase(os.path.abspath(os.path.expanduser(candidate)))
        if norm in seen:
            continue
        seen.add(norm)
        unique.append(candidate)
    return unique


def find_soffice() -> str:
    """Return a runnable LibreOffice/soffice path or raise with lookup details."""

    checked: list[str] = []
    for candidate in _candidate_soffice_paths():
        expanded = os.path.abspath(os.path.expanduser(candidate))
        checked.append(expanded)
        if os.path.isfile(expanded):
            return expanded

    path_text = os.environ.get("PATH", "")
    checked_text = "\n".join(f"- {path}" for path in checked) or "- <no candidates>"
    raise FileNotFoundError(
        "LibreOffice/soffice was not found. Checked SOFFICE_PATH, LIBREOFFICE_PATH, "
        "Codex dependencies/bin, PATH, and Windows Program Files locations.\n"
        f"Checked candidates:\n{checked_text}\nPATH={path_text}"
    )


def calc_dpi_via_ooxml_docx(input_path: str, max_w_px: int, max_h_px: int) -> int:
    with ZipFile(input_path, "r") as zf:
        xml = zf.read("word/document.xml")
    root = ET.fromstring(xml)
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}

    sect_pr = root.find(".//w:sectPr", ns)
    if sect_pr is None:
        raise RuntimeError("Section properties not found in document.xml")
    pg_sz = sect_pr.find("w:pgSz", ns)
    if pg_sz is None:
        raise RuntimeError("Page size not found in section properties")

    w_twips_str = pg_sz.get(f"{{{ns['w']}}}w") or pg_sz.get("w")
    h_twips_str = pg_sz.get(f"{{{ns['w']}}}h") or pg_sz.get("h")
    if not w_twips_str or not h_twips_str:
        raise RuntimeError("Page size attributes missing in pgSz")

    width_in = int(w_twips_str) / TWIPS_PER_INCH
    height_in = int(h_twips_str) / TWIPS_PER_INCH
    if width_in <= 0 or height_in <= 0:
        raise RuntimeError("Invalid page size values in document.xml")
    return round(min(max_w_px / width_in, max_h_px / height_in))


def _build_lo_env(user_profile: str) -> dict[str, str]:
    env = os.environ.copy()
    env["HOME"] = user_profile
    env.setdefault("XDG_CONFIG_HOME", join(user_profile, "xdg_config"))
    env.setdefault("XDG_CACHE_HOME", join(user_profile, "xdg_cache"))
    os.makedirs(env["XDG_CONFIG_HOME"], exist_ok=True)
    os.makedirs(env["XDG_CACHE_HOME"], exist_ok=True)
    return env


def _profile_uri(user_profile: str) -> str:
    return Path(user_profile).resolve().as_uri()


def _run_cmd(
    cmd: list[str], env: dict[str, str], verbose: bool, timeout: int
) -> subprocess.CompletedProcess[str]:
    try:
        proc = subprocess.run(
            cmd,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ""
        stderr = exc.stderr or ""
        if isinstance(stdout, bytes):
            stdout = stdout.decode(errors="replace")
        if isinstance(stderr, bytes):
            stderr = stderr.decode(errors="replace")
        proc = subprocess.CompletedProcess(
            cmd,
            124,
            stdout=stdout,
            stderr=f"Command timed out after {timeout} seconds.\n{stderr}",
        )
    if verbose:
        print("[render_docx] $ " + " ".join(cmd))
        if proc.stdout:
            print(proc.stdout)
        if proc.stderr:
            print(proc.stderr)
    return proc


def convert_to_pdf(
    doc_path: str,
    user_profile: str,
    convert_tmp_dir: str,
    stem: str,
    verbose: bool,
    timeout: int,
) -> tuple[str, str]:
    _default_macos_tmpdir_for_soffice()
    soffice = find_soffice()
    env = _build_lo_env(user_profile)
    logs: list[str] = [f"SOFFICE: {soffice}"]

    def _log_result(label: str, cmd: list[str], proc: subprocess.CompletedProcess[str]) -> None:
        logs.append(f"--- {label} ---")
        logs.append("CMD: " + " ".join(cmd))
        logs.append(f"EXIT: {proc.returncode}")
        if proc.stdout:
            logs.append("STDOUT:\n" + proc.stdout.strip())
        if proc.stderr:
            logs.append("STDERR:\n" + proc.stderr.strip())

    def _nonempty(path: str) -> bool:
        try:
            return exists(path) and os.path.getsize(path) > 0
        except Exception:
            return exists(path)

    pdf_path = join(convert_tmp_dir, f"{stem}.pdf")
    cmd_pdf = [
        soffice,
        "-env:UserInstallation=" + _profile_uri(user_profile),
        "--invisible",
        "--headless",
        "--norestore",
        "--convert-to",
        "pdf",
        "--outdir",
        convert_tmp_dir,
        doc_path,
    ]
    proc = _run_cmd(cmd_pdf, env=env, verbose=verbose, timeout=timeout)
    _log_result("DOCX->PDF", cmd_pdf, proc)
    if _nonempty(pdf_path):
        return pdf_path, "\n".join(logs)

    pdf_glob = glob.glob(join(convert_tmp_dir, "*.pdf"))
    if pdf_glob:
        cand = min(pdf_glob)
        if _nonempty(cand):
            return cand, "\n".join(logs)

    cmd_odt = [
        soffice,
        "-env:UserInstallation=" + _profile_uri(user_profile),
        "--invisible",
        "--headless",
        "--norestore",
        "--convert-to",
        "odt",
        "--outdir",
        convert_tmp_dir,
        doc_path,
    ]
    proc = _run_cmd(cmd_odt, env=env, verbose=verbose, timeout=timeout)
    _log_result("DOCX->ODT", cmd_odt, proc)

    odt_path = join(convert_tmp_dir, f"{stem}.odt")
    if exists(odt_path):
        cmd_odt_pdf = [
            soffice,
            "-env:UserInstallation=" + _profile_uri(user_profile),
            "--invisible",
            "--headless",
            "--norestore",
            "--convert-to",
            "pdf",
            "--outdir",
            convert_tmp_dir,
            odt_path,
        ]
        proc = _run_cmd(cmd_odt_pdf, env=env, verbose=verbose, timeout=timeout)
        _log_result("ODT->PDF", cmd_odt_pdf, proc)
        if _nonempty(pdf_path):
            return pdf_path, "\n".join(logs)
        pdf_glob = glob.glob(join(convert_tmp_dir, "*.pdf"))
        if pdf_glob:
            cand = min(pdf_glob)
            if _nonempty(cand):
                return cand, "\n".join(logs)

    return "", "\n".join(logs)


def calc_dpi_via_pdf(
    input_path: str, max_w_px: int, max_h_px: int, verbose: bool, timeout: int
) -> int:
    _default_macos_tmpdir_for_soffice()
    with tempfile.TemporaryDirectory(prefix="soffice_profile_") as user_profile:
        with tempfile.TemporaryDirectory(prefix="soffice_convert_") as convert_tmp_dir:
            stem = splitext(basename(input_path))[0]
            pdf_path, debug = convert_to_pdf(
                input_path,
                user_profile,
                convert_tmp_dir,
                stem,
                verbose=verbose,
                timeout=timeout,
            )
            if not (pdf_path and exists(pdf_path)):
                raise RuntimeError("Failed to convert input to PDF for DPI computation.\n" + debug)

            info = pdfinfo_from_path(pdf_path)
            size_val = info.get("Page size")
            if not size_val:
                for k, v in info.items():
                    if isinstance(v, str) and "size" in k.lower() and "pts" in v:
                        size_val = v
                        break
            if not isinstance(size_val, str):
                raise RuntimeError("Failed to read PDF page size for DPI computation.")
            m = re.search(r"(\d+(?:\.\d+)?)\s*x\s*(\d+(?:\.\d+)?)\s*pts", size_val)
            if not m:
                raise RuntimeError("Unrecognized PDF page size format.")
            width_in = float(m.group(1)) / 72.0
            height_in = float(m.group(2)) / 72.0
            return round(min(max_w_px / width_in, max_h_px / height_in))


def rasterize(
    doc_path: str, out_dir: str, dpi: int, verbose: bool, emit_pdf: bool, timeout: int
) -> Sequence[str]:
    _default_macos_tmpdir_for_soffice()
    makedirs(out_dir, exist_ok=True)
    doc_path = abspath(doc_path)
    stem = splitext(basename(doc_path))[0]

    with tempfile.TemporaryDirectory(prefix="soffice_profile_") as user_profile:
        with tempfile.TemporaryDirectory(prefix="soffice_convert_") as convert_tmp_dir:
            pdf_path, debug = convert_to_pdf(
                doc_path,
                user_profile,
                convert_tmp_dir,
                stem,
                verbose=verbose,
                timeout=timeout,
            )
            if not pdf_path or not exists(pdf_path):
                raise RuntimeError(
                    "Failed to produce PDF for rasterization (direct and ODT fallback).\n"
                    + debug
                )
            if emit_pdf:
                dst_pdf = join(out_dir, f"{stem}.pdf")
                tmp_pdf = dst_pdf + ".tmp"
                shutil.copy2(pdf_path, tmp_pdf)
                replace(tmp_pdf, dst_pdf)

            paths_raw = cast(
                list[str],
                convert_from_path(
                    pdf_path,
                    dpi=dpi,
                    fmt="png",
                    thread_count=8,
                    output_folder=out_dir,
                    paths_only=True,
                    output_file="page",
                ),
            )

    pages: list[tuple[int, str]] = []
    for src_path in paths_raw:
        base = splitext(basename(src_path))[0]
        page_num = int(base.split("-")[-1])
        dst_path = join(out_dir, f"page-{page_num}.png")
        replace(src_path, dst_path)
        pages.append((page_num, dst_path))
    pages.sort(key=lambda t: t[0])
    return [path for _, path in pages]


def main() -> None:
    _default_macos_tmpdir_for_soffice()
    parser = argparse.ArgumentParser(
        description="Render DOCX-like file to PNG images (DOCX -> PDF -> PNG)."
    )
    parser.add_argument("input_path", type=str, help="Path to the input DOCX file.")
    parser.add_argument("--output_dir", type=str, default=None)
    parser.add_argument("--width", type=int, default=1600)
    parser.add_argument("--height", type=int, default=2000)
    parser.add_argument("--dpi", type=int, default=None)
    parser.add_argument("--emit_pdf", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument(
        "--timeout",
        type=int,
        default=60,
        help="Seconds to allow each LibreOffice conversion command before failing.",
    )
    args = parser.parse_args()

    input_path = abspath(expanduser(args.input_path))
    out_dir = abspath(expanduser(args.output_dir)) if args.output_dir else splitext(input_path)[0]

    if args.dpi is not None:
        dpi = int(args.dpi)
    else:
        try:
            if input_path.lower().endswith((".docx", ".docm", ".dotx", ".dotm")):
                dpi = calc_dpi_via_ooxml_docx(input_path, args.width, args.height)
            else:
                raise RuntimeError("Skip OOXML DPI; not a DOCX container")
        except Exception:
            dpi = calc_dpi_via_pdf(
                input_path,
                args.width,
                args.height,
                verbose=args.verbose,
                timeout=args.timeout,
            )

    rasterize(
        input_path,
        out_dir,
        dpi,
        verbose=args.verbose,
        emit_pdf=args.emit_pdf,
        timeout=args.timeout,
    )
    print("Pages rendered to " + out_dir)


if __name__ == "__main__":
    main()
