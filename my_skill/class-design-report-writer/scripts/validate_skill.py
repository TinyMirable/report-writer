#!/usr/bin/env python3
"""Validate the class-design-report-writer skill package."""

from __future__ import annotations

import argparse
import io
import re
import sys
from pathlib import Path


if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


REQUIRED_FILES = [
    "SKILL.md",
    "agents/openai.yaml",
    "assets/course-design-report-template.docx",
    "references/report/report-template.md",
    "references/report/report-writing-rules.md",
    "references/report/report-style-guide.md",
    "references/diagram/diagram-policy.md",
    "references/diagram/diagram-layout-policy.md",
    "references/diagram/uml-diagram-standard.md",
    "references/diagram/system-architecture-diagram-standard.md",
    "references/evidence-and-verification.md",
    "references/agents/main-agent-workflow.md",
    "references/agents/writer-agent-a.md",
    "references/agents/uml-agent-b.md",
    "references/agents/d2-agent-c.md",
    "references/agents/testing-screenshot-agent-d.md",
    "references/agents/image-quality-agent-e.md",
    "references/agents/final-assembly-agent-f.md",
    "references/agents/delivery-review-agent-g.md",
    "references/agents/copy-enhancement-agent-h.md",
    "references/agents/draft-review-agent-i.md",
    "scripts/render_docx.py",
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
    "references/report/report-style-guide.md",
    "references/diagram/uml-diagram-standard.md",
    "references/diagram/system-architecture-diagram-standard.md",
    "references/diagram/diagram-layout-policy.md",
    "多个子代理合作",
    "报告写作代理A",
    "UML图像绘制代理B",
    "D2绘图代理C",
    "测试截图代理D",
    "图像质量检验代理E",
    "汇总产出代理F",
    "交付检查智能体G",
    "报告文案增强代理H",
    "报告初稿审查代理I",
    "references/agents/main-agent-workflow.md",
    "references/agents/delivery-review-agent-g.md",
    "references/agents/copy-enhancement-agent-h.md",
    "references/agents/draft-review-agent-i.md",
    "render_docx.py",
    "LibreOffice",
    "soffice",
    "Markdown",
    "DOCX",
]

REQUIRED_REFERENCE_TERMS = {
    "references/report/report-template.md": [
        "不要修改模板第一页",
        "不要修改模板第二页",
        "第三页",
        "只在既有章节标题下方填充正文",
        "一、选题背景",
        "二、方案论证(设计理念)",
        "三、过程论述",
        "四、结果分析",
    ],
    "references/report/report-writing-rules.md": [
        "系统功能结构图",
        "系统组件图",
        "用户活动图",
        "关键功能时序图",
        "系统约束和规范",
        "designer's point of view",
        "从源码可以看出",
        "AI分析得到",
        "Never invent modules",
        "references/report/report-style-guide.md",
        "具体表达",
        "删掉空话套话",
        "术语一致",
        "为说明系统组件图所对应的设计内容，报告插入如下图示",
        "图中内容均来自项目的",
        "起承上启下",
    ],
    "references/report/report-style-guide.md": [
        "课程设计报告表述风格约束",
        "面向课程设计评审教师",
        "先说明设计目的",
        "使用具体术语",
        "删掉空话套话",
        "避免泛泛总结句",
        "术语一致",
        "事实依据",
        "图前说明",
        "为说明系统组件图所对应的设计内容，报告插入如下图示",
        "图中内容均来自项目的",
        "起承上启下",
        "最终语言检查",
    ],
    "references/diagram/diagram-policy.md": [
        "PlantUML",
        "D2",
        "用例图",
        "系统架构图",
        "系统功能结构图",
        "用户活动图",
        "关键功能时序图",
        "系统组件图",
        "系统架构图绘制准则",
        "references/diagram/uml-diagram-standard.md",
        "references/diagram/system-architecture-diagram-standard.md",
        "references/diagram/diagram-layout-policy.md",
    ],
    "references/diagram/diagram-layout-policy.md": [
        "Diagram Layout Policy",
        "No overlapping shapes",
        "Use PlantUML",
        "Use D2",
        "Self Check",
    ],
    "references/diagram/uml-diagram-standard.md": [
        "UML图绘制标准",
        "活动图",
        "用例图",
        "时序图",
        "类图",
        "组件图",
        "包图",
    ],
    "references/diagram/system-architecture-diagram-standard.md": [
        "系统架构图绘制准则",
        "分层架构",
        "矩阵式扩展",
        "低饱和度",
        "使用 D2",
        "Checklist",
    ],
    "references/agents/main-agent-workflow.md": [
        "主代理",
        "tmp/course-report-facts",
        "分发给子代理",
        "报告写作代理A",
        "汇总产出代理F",
        "交付检查智能体G",
        "代理G",
        "报告文案增强代理H",
        "报告初稿审查代理I",
        "代理H",
        "代理I",
        "停止标准",
        "未达标准处理",
    ],
    "references/agents/writer-agent-a.md": [
        "报告写作代理A",
        "不画图",
        "表述风格约束",
        "写作规范",
        "需要绘制的图像",
        "报告初稿审查代理I",
        "停止标准",
        "未达标准处理",
    ],
    "references/agents/draft-review-agent-i.md": [
        "报告初稿审查代理I",
        "报告写作代理A",
        "初稿审查",
        "内容是否足以阐述清楚课程设计项目",
        "新增章节",
        "漏图",
        "缺失信息",
        "方案补充",
        "停止标准",
        "未达标准处理",
    ],
    "references/agents/uml-agent-b.md": [
        "UML图像绘制代理B",
        "PlantUML",
        "不绘制需要使用D2的图",
        "绘制情况",
        "停止标准",
        "未达标准处理",
    ],
    "references/agents/d2-agent-c.md": [
        "D2绘图代理C",
        "D2",
        "不需要绘制UML图",
        "系统架构图",
        "停止标准",
        "未达标准处理",
    ],
    "references/agents/testing-screenshot-agent-d.md": [
        "测试截图代理D",
        "完整测试",
        "截图",
        "测试结果文档",
        "不绘制UML图和D2图",
        "停止标准",
        "未达标准处理",
    ],
    "references/agents/image-quality-agent-e.md": [
        "图像质量检验代理E",
        "检验代理B",
        "检验代理C",
        "检验代理D",
        "不合格的原因",
        "重新绘制截图",
        "停止标准",
        "未达标准处理",
    ],
    "references/agents/final-assembly-agent-f.md": [
        "汇总产出代理F",
        "Markdown",
        "DOCX",
        "加入图像",
        "优化报告整体阐述风格",
        "最后的检验",
        "报告文案增强代理H",
        "交付检查智能体G",
        "停止标准",
        "未达标准处理",
    ],
    "references/agents/copy-enhancement-agent-h.md": [
        "报告文案增强代理H",
        "交付检查智能体G",
        "汇总产出代理F",
        "不检查图像",
        "不检查格式",
        "逐一审查各个章节",
        "教授的角度",
        "图的阐述",
        "选题背景",
        "方案论证",
        "过程论述",
        "结果分析",
        "课程设计总结",
        "停止标准",
        "未达标准处理",
    ],
    "references/agents/delivery-review-agent-g.md": [
        "交付检查智能体G",
        "汇总产出代理F",
        "报告文案增强代理H",
        "全面审查",
        "修复交付产物",
        "5个标题",
        "首行缩进两字符",
        "课题名称",
        "课题名称占位文字",
        "删除",
        "上下空一行",
        "模板残留",
        "参考文献",
        "为说明系统组件图所对应的设计内容，报告插入如下图示",
        "图中内容均来自项目的",
        "图前说明",
        "起承上启下",
        "停止标准",
        "未达标准处理",
    ],
    "scripts/render_docx.py": [
        "LibreOffice",
        "soffice",
        "find_soffice",
        "CODEX",
        "programfiles",
        "render",
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
