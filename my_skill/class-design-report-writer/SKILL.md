---
name: class-design-report-writer
description: Use when writing a Chinese course design report from an existing project repository, especially when the agent must coordinate multiple subagents to analyze source code, draft report prose, generate UML and D2 diagrams, collect screenshots or test evidence, inspect image quality, and deliver Markdown plus DOCX reports using the course design report template.
---

# Class Design Report Writer

## Core Rule

Treat the user's project repository as the only source of truth. Do not invent features, architecture, tests, results, screenshots, or diagrams. Before writing the report, create a fact base in the target project's `tmp/course-report-facts/` directory and write the report only from that fact base plus verifiable artifacts.

## Multi-Agent Rule

Use 多个子代理合作 to complete the report whenever subagent tools are available. The main agent owns planning, evidence control, integration, and final acceptance; subagents own bounded production tasks.

After the fact base exists, read `references/agents/main-agent-workflow.md` and dispatch these roles with the role reference attached or summarized in each prompt:

- 报告写作代理A: read `references/agents/writer-agent-a.md` and draft the Markdown report prose plus a diagram request list.
- UML图像绘制代理B: read `references/agents/uml-agent-b.md` and draw only UML diagrams with PlantUML or an equivalent editable UML source.
- D2绘图代理C: read `references/agents/d2-agent-c.md` and draw only D2 architecture, data-flow, and flowchart diagrams.
- 测试截图代理D: read `references/agents/testing-screenshot-agent-d.md` and run verification, screenshots, and testing evidence capture.
- 图像质量检验代理E: read `references/agents/image-quality-agent-e.md` and inspect diagram and screenshot quality before final assembly.
- 报告初稿审查代理I: read `references/agents/draft-review-agent-i.md` immediately after 代理A finishes, then check whether the draft explains the course design project fully enough and whether sections, diagrams, or explanations must be supplemented before drawing and final writing continue.
- 报告文案增强代理H: read `references/agents/copy-enhancement-agent-h.md` after diagram, screenshot, and quality evidence exists but before 代理F and 交付检查智能体G. 代理H revises only report prose, especially figure explanations and chapter logic; it does not check images or formatting.
- 汇总产出代理F: read `references/agents/final-assembly-agent-f.md` and assemble the H-enhanced Markdown, images, DOCX, and final checks.
- 交付检查智能体G: read `references/agents/delivery-review-agent-g.md` after 代理F finishes, then perform the final delivery review and directly repair Markdown/DOCX delivery artifacts when format, prose, template residue, references, or figure explanation checks fail.

If the environment cannot spawn subagents, execute the same roles sequentially, keep the same role boundaries, and record the limitation in `tmp/course-report-facts/06-report-evidence-map.md`.

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
4. Read `references/agents/main-agent-workflow.md`, then assign subagents A-I according to the Multi-Agent Rule.
5. Have 测试截图代理D run the project's available tests or verification commands. If no test command exists, record that absence and run the smallest meaningful build, lint, smoke, or script-level verification available.
6. Have 报告写作代理A draft the Markdown report according to `references/report/report-writing-rules.md`, `references/report/report-template.md`, and `references/report/report-style-guide.md`.
7. Have 报告初稿审查代理I review 代理A's draft before diagram production and final writing continue. If 代理I finds thin explanations, missing diagrams, missing section logic, or incomplete course-design reasoning, return the draft to 代理A or the main agent for supplementation.
8. Have UML图像绘制代理B and D2绘图代理C generate required diagrams and save editable sources plus exported images in the report workspace. Prefer Next AI Draw.io when available; otherwise use draw.io XML, Mermaid, PlantUML, D2, or another exportable diagram method. The final report must include images, not only source text.
9. Have 图像质量检验代理E check all exported diagrams and screenshots. Redraw or recapture any asset that fails quality checks before assembly.
10. Have 报告文案增强代理H revise the report prose before 代理F and 交付检查智能体G run. 代理H must strengthen the narrative around each figure and each chapter without checking image pixels or DOCX formatting.
11. Have 汇总产出代理F generate the DOCX report using `assets/course-design-report-template.docx` as the formatting template whenever possible.
12. Render the DOCX with `scripts/render_docx.py` for visual QA when LibreOffice/soffice is available. The script must search common Codex runtime, PATH, and Windows LibreOffice installation locations before reporting that rendering is unavailable.
13. Have 交付检查智能体G perform the final comprehensive delivery review after 代理F. 代理G must check and repair prohibited/lazy phrasing, figure lead-in logic, heading indentation, `课题名称` spacing, removal of the unreplaced `课题名称` placeholder text, template residue on pages 3-4, and the required `参考文献` structure.
14. Main agent verifies the outputs: every major claim must map back to source files, commands, screenshots, generated diagrams, or fact documents.

Do not proceed from analysis to report writing until the `tmp/course-report-facts/` files exist and contain source-backed evidence.

## DOCX Template Handling

Use `assets/course-design-report-template.docx` as a fill-in template, not as a document to restructure.

- 不要修改模板第一页: it is the cover page.
- 不要修改模板第二页: it is the personal/student information page.
- Start writing report body content from 第三页.
- 验证：第三页开头一行后是 `课题名称`，需要替换
- 最终产物中不得残留未替换的 `课题名称` 占位文字；填充后必须删除模板占位，只保留真实课题名称。
- Preserve the existing chapter headings in the template:`课程`, `一、选题背景`, `二、方案论证(设计理念)`, `三、过程论述`, `四、结果分析`, and `五、课程设计总结`.
- 只在既有章节标题下方填充正文. Do not duplicate, rename, delete, or reorder the template headings unless the user explicitly asks.
- Insert figures, tables, captions, and code excerpts under the matching existing chapter heading.

## References

Read only the references needed for the current phase:

- For multi-agent orchestration, read `references/agents/main-agent-workflow.md`, then the matching `references/agents/*.md` file for each subagent role.
- For draft completeness review after 代理A, read `references/agents/draft-review-agent-i.md`.
- For prose enhancement before final assembly, read `references/agents/copy-enhancement-agent-h.md`.
- For final delivery review after report assembly, read `references/agents/delivery-review-agent-g.md`.
- For report sections and formatting, read `references/report/report-template.md`.
- For chapter content, figure captions, code blocks, and DOCX expectations, read `references/report/report-writing-rules.md`.
- Before drafting or revising final report prose, read `references/report/report-style-guide.md`.
- For required diagrams and layout quality, read `references/diagram/diagram-policy.md`.
- Before drawing any report diagram, read `references/diagram/diagram-layout-policy.md`.
- Before drawing UML diagrams such as 用例图、类图、活动图、时序图、组件图、包图、部署图, read `references/diagram/uml-diagram-standard.md`.
- Before drawing 系统架构图 or D2 architecture diagrams, read `references/diagram/system-architecture-diagram-standard.md`.
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
- `scripts/render_docx.py` was run for DOCX visual QA when LibreOffice/soffice is available, or the absence of a runnable renderer was recorded with the exact failed lookup result.
- 报告初稿审查代理I has completed the draft review and written `tmp/course-report-work/agents/I-draft-review.md`.
- 报告文案增强代理H has completed prose enhancement and written `tmp/course-report-work/agents/H-copy-enhancement.md`.
- 交付检查智能体G has completed final review, repaired fixable delivery issues, and written `tmp/course-report-work/agents/G-delivery-review.md`.
- `06-report-evidence-map.md` maps report sections to evidence.
