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

## DOCX Template Handling

Use `assets/course-design-report-template.docx` as a fill-in template, not as a document to restructure.

- 不要修改模板第一页: it is the cover page.
- 不要修改模板第二页: it is the personal/student information page.
- Start writing report body content from 第三页.
- Preserve the existing chapter headings in the template: `一、选题背景`, `二、方案论证(设计理念)`, `三、过程论述`, `四、结果分析`, and `五、课程设计总结`.
- 只在既有章节标题下方填充正文. Do not duplicate, rename, delete, or reorder the template headings unless the user explicitly asks.
- Insert figures, tables, captions, and code excerpts under the matching existing chapter heading.

## References

Read only the references needed for the current phase:

- For report sections and formatting, read `references/report-template.md`.
- For chapter content, figure captions, code blocks, and DOCX expectations, read `references/report-writing-rules.md`.
- For required diagrams and layout quality, read `references/diagram-policy.md`.
- Before drawing any report diagram, read `references/diagram-layout-policy.md`.
- Before drawing UML diagrams such as 用例图、类图、活动图、时序图、组件图、包图、部署图, read `references/uml-diagram-standard.md`.
- Before drawing 系统架构图 or D2 architecture diagrams, read `references/system-architecture-diagram-standard.md`.
- For fact gathering, verification, screenshots, and evidence mapping, read `references/evidence-and-verification.md`.

## Mandatory Report Content

The final report must include:

- 选题背景：project problem, technical requirements, and guiding idea.
- 方案论证(设计理念)：requirements analysis, standard use case diagram, system functionality structure diagram, system component diagram, user activity diagram, key function sequence diagram, system constraints and norms, architecture and technology choices, top-level/level-1/level-2 data flow, package/module design, class/object design when applicable.
- 过程论述：implementation process, core logic explanation, core code flowchart, key source code excerpts, and text before and after every figure.
- 结果分析：testing method, purpose, actual results, screenshots for frontend projects or result tables for non-frontend projects.
- 课程设计总结：project gains, encountered problems, debugging and implementation reflections.

## Mandatory Diagrams

At minimum, produce:

- 用例图
- 系统功能结构图
- 系统组件图
- 用户活动图
- 关键功能时序图
- 系统架构图
- 顶层数据流图
- 一层数据流图
- 二层数据流图
- 包图
- 核心代码流程图

Optional diagrams include class diagrams, ER diagrams, deployment diagrams, page flow diagrams, module dependency diagrams, or sequence diagrams when the project supports them.

Use PlantUML for UML diagrams such as 用例图, 类图, 用户活动图, 关键功能时序图, 组件图, 包图, 部署图, and 状态图. Use D2 for 系统架构图 and other architecture, infrastructure, enterprise, data pipeline, or agent architecture diagrams. Check every exported diagram against `references/diagram-policy.md` before inserting it into the report.

## Output Checklist

Before finishing, confirm:

- `tmp/course-report-facts/` contains the six fact documents.
- Required diagrams are generated, readable, exported as images, and referenced in the report.
- Tests or verification commands were run and recorded.
- Frontend projects include screenshots; non-frontend projects include result tables or command summaries.
- Markdown report exists.
- DOCX report exists and follows the template formatting as closely as the environment allows.
- `06-report-evidence-map.md` maps report sections to evidence.
