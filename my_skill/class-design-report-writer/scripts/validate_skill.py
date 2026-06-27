#!/usr/bin/env python3
"""Validate the class-design-report-writer skill package."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "assets/course-design-report-template.docx",
    "references/report-template.md",
    "references/report-writing-rules.md",
    "references/report-style-guide.md",
    "references/diagram-policy.md",
    "references/diagram-layout-policy.md",
    "references/uml-diagram-standard.md",
    "references/system-architecture-diagram-standard.md",
    "references/evidence-and-verification.md",
    "scripts/validate_skill.py",
    "scripts/sync_to_codex_skills.py",
]

REQUIRED_SKILL_TERMS = [
    "tmp/course-report-facts",
    "不要修改模板第一页",
    "不要修改模板第二页",
    "第三页",
    "只在既有章节标题下方填充正文",
    "用例图",
    "系统功能结构图",
    "系统组件图",
    "用户活动图",
    "关键功能时序图",
    "系统架构图",
    "顶层数据流图",
    "一层数据流图",
    "二层数据流图",
    "包图",
    "核心代码流程图",
    "PlantUML",
    "D2",
    "references/report-style-guide.md",
    "references/uml-diagram-standard.md",
    "references/system-architecture-diagram-standard.md",
    "references/diagram-layout-policy.md",
    "Markdown",
    "DOCX",
]

REQUIRED_REFERENCE_TERMS = {
    "references/report-template.md": [
        "不要修改模板第一页",
        "不要修改模板第二页",
        "第三页",
        "只在既有章节标题下方填充正文",
        "一、选题背景",
        "二、方案论证(设计理念)",
        "三、过程论述",
        "四、结果分析",
    ],
    "references/report-writing-rules.md": [
        "系统功能结构图",
        "系统组件图",
        "用户活动图",
        "关键功能时序图",
        "系统约束和规范",
        "designer's point of view",
        "从源码可以看出",
        "AI分析得到",
        "Never invent modules",
        "references/report-style-guide.md",
        "具体表达",
        "删掉空话套话",
        "术语一致",
    ],
    "references/report-style-guide.md": [
        "课程设计报告表述风格约束",
        "面向课程设计评审教师",
        "先说明设计目的",
        "使用具体术语",
        "删掉空话套话",
        "避免泛泛总结句",
        "术语一致",
        "事实依据",
        "最终语言检查",
    ],
    "references/diagram-policy.md": [
        "PlantUML",
        "D2",
        "用例图",
        "系统架构图",
        "系统功能结构图",
        "用户活动图",
        "关键功能时序图",
        "系统组件图",
        "系统架构图绘制准则",
        "references/uml-diagram-standard.md",
        "references/system-architecture-diagram-standard.md",
        "references/diagram-layout-policy.md",
    ],
    "references/diagram-layout-policy.md": [
        "Diagram Layout Policy",
        "No overlapping shapes",
        "Use PlantUML",
        "Use D2",
        "Self Check",
    ],
    "references/uml-diagram-standard.md": [
        "UML图绘制标准",
        "活动图",
        "用例图",
        "时序图",
        "类图",
        "组件图",
        "包图",
    ],
    "references/system-architecture-diagram-standard.md": [
        "系统架构图绘制准则",
        "分层架构",
        "矩阵式扩展",
        "低饱和度",
        "使用 D2",
        "Checklist",
    ],
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_frontmatter(skill_text: str) -> list[str]:
    errors: list[str] = []
    match = re.match(r"^---\n(.*?)\n---\n", skill_text, re.DOTALL)
    if not match:
        return ["SKILL.md must start with YAML frontmatter delimited by ---"]

    frontmatter = match.group(1)
    fields: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if ":" not in line:
            errors.append(f"Invalid frontmatter line: {line}")
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip()

    if fields.get("name") != "class-design-report-writer":
        errors.append("frontmatter name must be class-design-report-writer")
    if not fields.get("description"):
        errors.append("frontmatter description is required")
    if len(frontmatter) > 1024:
        errors.append("frontmatter must be no more than 1024 characters")
    return errors


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    if not skill_dir.exists():
        return [f"skill directory does not exist: {skill_dir}"]
    if not skill_dir.is_dir():
        return [f"skill path is not a directory: {skill_dir}"]

    for rel_path in REQUIRED_FILES:
        path = skill_dir / rel_path
        if not path.exists():
            errors.append(f"missing required file: {rel_path}")
        elif path.is_file() and path.stat().st_size == 0:
            errors.append(f"required file is empty: {rel_path}")

    skill_path = skill_dir / "SKILL.md"
    if skill_path.exists():
        skill_text = read_text(skill_path)
        errors.extend(validate_frontmatter(skill_text))
        for term in REQUIRED_SKILL_TERMS:
            if term not in skill_text:
                errors.append(f"SKILL.md must mention required term: {term}")

    for rel_path, terms in REQUIRED_REFERENCE_TERMS.items():
        path = skill_dir / rel_path
        if path.exists():
            text = read_text(path)
            for term in terms:
                if term not in text:
                    errors.append(f"{rel_path} must mention required term: {term}")

    openai_yaml = skill_dir / "agents/openai.yaml"
    if openai_yaml.exists():
        openai_text = read_text(openai_yaml)
        for field in ("display_name:", "short_description:", "default_prompt:"):
            if field not in openai_text:
                errors.append(f"agents/openai.yaml missing field: {field}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Codex skill package.")
    parser.add_argument("skill_dir", type=Path, help="Path to the skill directory")
    args = parser.parse_args()

    errors = validate_skill(args.skill_dir.resolve())
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Skill validation passed: {args.skill_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
