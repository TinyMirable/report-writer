# 报告撰写规则

## Source Discipline

Write from the target project's actual source code and verification artifacts. If a feature, test, route, class, API, or data model cannot be found in the project, do not describe it as implemented.

## Final Report Voice

Write the final Markdown and DOCX reports as a course design final report from the designer's point of view. Do not expose the analysis process.

Before drafting final prose, read `references/report/report-style-guide.md` and apply its 表述风格约束. The guide is the detailed style reference for concrete expression, concise wording, term consistency, evidence calibration, and final language checks.

Use design statements:

- `本系统采用...`
- `系统将...划分为...`
- `为提高系统可维护性，系统采用...`

Do not use analyzer or AI-process statements in the final report:

- `从源码可以看出...`
- `根据代码可以发现...`
- `阅读项目后...`
- `经过分析...`
- `AI分析得到...`
- `仓库中...`
- `GitHub项目...`

Avoid uncertainty words such as `可能`, `推测`, `似乎`, `大概`, and `疑似`. If evidence cannot support a claim, omit the claim or mark it as a design item that still needs supplementation. Never invent modules, features, technologies, UML relationships, data flow, tests, screenshots, or performance data.

## Expression Style

Write for a course design evaluator who has not opened the repository. First state the design purpose, then explain the mechanism and evidence.

- 具体表达: name the actual module, function, page, API, table, command, diagram, or test result.
- 删掉空话套话: remove generic sentences such as `具有重要意义`, `进一步提升了系统水平`, `总的来说`, and `效果较好` unless the sentence gives concrete evidence.
- 术语一致: use the same names for actors, modules, pages, APIs, tables, diagrams, and tests throughout the report.
- Avoid unsupported claims about performance, security, usability, reliability, or completeness.
- Prefer paragraphs for explanation; use bullet lists only when the content is a real list.

## 选题背景

Include:

- The practical problem the project solves.
- The target users or usage scenario if the code or project docs support it.
- Main technical requirements.
- The design's guiding idea, such as modularity, maintainability, usability, data consistency, or performance.

## 方案论证(设计理念)

Include requirements analysis and system design in this chapter.

Requirements analysis must include:

- Functional goal summary.
- Required use case diagram / 用例图.
- Required system functionality structure diagram / 系统功能结构图.
- Required system component diagram / 系统组件图.
- Required user activity diagram / 用户活动图.
- Required key function sequence diagram / 关键功能时序图.
- System boundary.
- System constraints and norms / 系统约束和规范.
- Security requirements.
- Data integrity requirements.
- Runtime environment.
- Performance expectations if evidence exists.

System design must include:

- Architecture rationale.
- Technology stack selection and evidence from project files.
- Required system architecture diagram.
- Required top-level, level-1, and level-2 data flow diagrams.
- Required package diagram.
- Code structure explanation.
- Class and object design if the project language and architecture use classes or equivalent domain objects.

Place all of the above under the existing `二、方案论证(设计理念)` heading in the DOCX template. Do not create a separate top-level requirements-analysis chapter.

## 过程论述

Explain how the system is implemented.

For every figure:

1. Before the figure, explain why the figure is used and what it helps readers understand.
2. Add the figure and a centered caption.
3. After the figure, explain each major element and the interaction, dependency, or flow shown.

Implementation discussion must include:

- Core feature implementation idea.
- Required core code flowchart.
- Key logic source code excerpts.
- Explanation of the source code's role in the system.

If the project uses object-oriented code, include a class diagram for the key classes and explain class responsibilities and implementation ideas. If the project does not use object-oriented code, state the evidence and use package/module, function-flow, or component diagrams instead.

Code formatting in DOCX:

- Font: Consolas or Cascadia Code.
- Size: 10.5 pt.
- Background: light gray or dark gray.
- Preserve indentation.

Place this content under the existing `三、过程论述` heading in the DOCX template.

## 结果分析

Explain testing method and purpose.

For frontend projects:

- Include screenshots of test results, key pages, or interaction verification.
- Explain what each screenshot proves.

For non-frontend projects:

- Include a key result table and command output summary.
- Explain command, input, expected result, actual result, and conclusion.

Place this content under the existing `四、结果分析` heading in the DOCX template.

## 课程设计总结

Write a grounded reflection. It may include:

- What was learned during design and implementation.
- Problems encountered.
- How problems were diagnosed and solved.
- Thoughts on debugging, testing, and program design.
- Improvements that could be made with more time.

Do not invent personal experiences; keep reflection consistent with the project work and evidence.

## Final Language Check

Before delivery, scan the final Markdown and DOCX text for analysis traces and informal language. The report must:

- Use designer viewpoint throughout.
- Explain why each technical choice supports the design.
- Describe implementation ideas instead of line-by-line code reading.
- Provide text before and after every figure.
- Avoid `AI`, `模型`, `阅读源码`, `从源码可以看出`, `根据代码`, `可以看到`, `可以发现`, `可能`, `推测`, and similar wording in the final report body.
