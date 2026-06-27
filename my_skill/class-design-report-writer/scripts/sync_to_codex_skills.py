#!/usr/bin/env python3
"""Sync the repository skill copy to Codex's personal skills directory."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
from pathlib import Path


SKILL_NAME = "class-design-report-writer"
EXCLUDED_DIRS = {"__pycache__", ".pytest_cache"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def codex_skills_root() -> Path:
    codex_home = os.environ.get("CODEX_HOME")
    if codex_home:
        return Path(codex_home).expanduser() / "skills"
    return Path.home() / ".codex" / "skills"


def iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(part in EXCLUDED_DIRS for part in rel.parts):
            continue
        if path.is_file() and path.suffix not in EXCLUDED_SUFFIXES:
            files.append(rel)
    return sorted(files, key=lambda item: item.as_posix())


def file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def compare_trees(source: Path, destination: Path) -> list[str]:
    errors: list[str] = []
    if not destination.exists():
        return [f"destination does not exist: {destination}"]

    source_files = iter_files(source)
    destination_files = iter_files(destination)
    if source_files != destination_files:
        source_set = {item.as_posix() for item in source_files}
        destination_set = {item.as_posix() for item in destination_files}
        for rel in sorted(source_set - destination_set):
            errors.append(f"missing in destination: {rel}")
        for rel in sorted(destination_set - source_set):
            errors.append(f"extra in destination: {rel}")

    for rel in source_files:
        source_path = source / rel
        destination_path = destination / rel
        if destination_path.exists() and file_hash(source_path) != file_hash(destination_path):
            errors.append(f"hash mismatch: {rel.as_posix()}")
    return errors


def sync(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)
    ignore = shutil.ignore_patterns("__pycache__", ".pytest_cache", "*.pyc", "*.pyo")
    shutil.copytree(source, destination, ignore=ignore)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync a skill to Codex personal skills.")
    parser.add_argument("source", type=Path, help="Path to the source skill directory")
    parser.add_argument("--check", action="store_true", help="Only compare source and installed copy")
    parser.add_argument("--dest", type=Path, help="Override destination skill directory")
    args = parser.parse_args()

    source = args.source.resolve()
    if not source.exists() or not source.is_dir():
        print(f"source skill directory does not exist: {source}")
        return 1

    destination = args.dest.resolve() if args.dest else codex_skills_root() / SKILL_NAME

    if not args.check:
        sync(source, destination)
        print(f"Synced {source} -> {destination}")

    errors = compare_trees(source, destination)
    if errors:
        print("Skill sync check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill sync check passed: {destination}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

