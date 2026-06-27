---
name: class-design-report-writer
description: Use when writing a Chinese course design report from an existing project repository, especially when the agent must analyze source code, generate required diagrams, collect test evidence, and deliver Markdown plus DOCX reports using the course design report template.
---

# Class Design Report Writer

## Core Rule

Treat the user's project repository as the only source of truth. Do not invent features, architecture, tests, results, screenshots, or diagrams. Before writing the report, create a fact base in the target project's `tmp/course-report-facts/` directory and write the report only from that fact base plus verifiable artifacts.

## Required Workflow

1. Identify the target project root, report title, student metadata if provided, and desired output directory.
2. Read the project files needed to understand goals, features, architecture, code structure, core logic, runtime environment, and tests.
3. Create `tmp/course-report-facts/` in the target project and write these files:
   - `01-project-overview.md`
   - `02-requirements-analysis.md`
   - `03-system-design.md`
   - `04-implementation-analysis.md`
   - `05-testing-evidence.md`
   - `06-report-evidence-map.md`
4. Run the project's available tests or verification commands. If no test command exists, record that absence and run the smallest meaningful build, lint, smoke, or script-level verification available.
5. Generate required diagrams and save editable sources plus exported images in the report workspace. Prefer Next AI Draw.io when available; otherwise use draw.io XML, Mermaid, PlantUML, or another exportable diagram method. The final report must include images, not only source text.
6. Write the Markdown report according to `references/report-writing-rules.md` and `references/report-template.md`.
7. Generate the DOCX report using `assets/course-design-report-template.docx` as the formatting template whenever possible.
8. Verify the outputs: every major claim must map back to source files, commands, screenshots, generated diagrams, or fact documents.

Do not proceed from analysis to report writing until the `tmp/course-report-facts/` files exist and contain source-backed evidence.

## References

Read only the references needed for the current phase:

- For report sections and formatting, read `references/report-template.md`.
- For chapter content, figure captions, code blocks, and DOCX expectations, read `references/report-writing-rules.md`.
- For required diagrams and layout quality, read `references/diagram-policy.md`.
- For fact gathering, verification, screenshots, and evidence mapping, read `references/evidence-and-verification.md`.

## Mandatory Report Content

The final report must include:

- 选题背景：project problem, technical requirements, and guiding idea.
- 方案论证(设计理念)：requirements analysis, use case diagram, system constraints, architecture and technology choices, top-level/level-1/level-2 data flow, package/module design, class/object design when applicable.
- 过程论述：implementation process, core logic explanation, core code flowchart, key source code excerpts, and text before and after every figure.
- 结果分析：testing method, purpose, actual results, screenshots for frontend projects or result tables for non-frontend projects.
- 课程设计总结：project gains, encountered problems, debugging and implementation reflections.

## Mandatory Diagrams

At minimum, produce:

- 用例图
- 系统架构图
- 顶层数据流图
- 一层数据流图
- 二层数据流图
- 包图
- 核心代码流程图

Optional diagrams include class diagrams, ER diagrams, deployment diagrams, page flow diagrams, module dependency diagrams, or sequence diagrams when the project supports them.

## Output Checklist

Before finishing, confirm:

- `tmp/course-report-facts/` contains the six fact documents.
- Required diagrams are generated, readable, exported as images, and referenced in the report.
- Tests or verification commands were run and recorded.
- Frontend projects include screenshots; non-frontend projects include result tables or command summaries.
- Markdown report exists.
- DOCX report exists and follows the template formatting as closely as the environment allows.
- `06-report-evidence-map.md` maps report sections to evidence.

