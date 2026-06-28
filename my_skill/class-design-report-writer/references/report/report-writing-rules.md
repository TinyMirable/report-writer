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

## Figure Lead-In Rules

Figures support the design explanation; they are not inserted for their own sake. Before each figure, explain what the report is trying to prove or clarify, why this view is needed, and how it connects to the previous paragraph. The paragraph above a figure must 起承上启下.

Do not use stiff placeholder wording such as:

- `为说明系统组件图所对应的设计内容，报告插入如下图示`
- `图中内容均来自项目的`
- `如下图所示`
- `为了画出该图`

Prefer natural design reasoning:

- `根据原始需求，系统需要同时支持用户操作、业务处理和数据持久化，因此用例分析先明确参与者与功能边界。`
- `在明确功能边界后，系统组件图用于说明界面层、业务层和数据访问层之间的依赖关系。`
- `为展示核心功能从输入到持久化的处理路径，流程图将请求接收、参数校验、业务处理和结果返回串联起来。`

After each figure, explain the main elements, relationships, dependencies, or flow shown in the figure. Do not only say that the figure comes from the project; describe the design idea represented by the figure.

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

## 参考文献

The final report must keep a `参考文献` section after `五、课程设计总结`.

- If the project has references or external sources, list them using sequential numeric citations.
- If the project has no references, keep the `参考文献` heading and leave the concrete reference entries blank.
- Do not fabricate books, papers, URLs, publication years, or access dates.

## Final Format Check

Before delivery, check the final Markdown and DOCX formatting:

- The five chapter headings `一、选题背景`, `二、方案论证(设计理念)`, `三、过程论述`, `四、结果分析`, and `五、课程设计总结` must use 首行缩进两字符.
- `课题名称` must have one blank line before it and one blank line after it.
- The original `课题名称` placeholder in the Word template must be replaced and deleted. Final Markdown and DOCX must not contain an unreplaced `课题名称` placeholder next to or instead of the real project title.
- The body must start on the third page of the DOCX template; do not append the real report after page 4.
- Pages 3 and 4 must not contain leftover template residue, sample paragraphs, unreplaced placeholders, duplicate headings, or extra blank pages.
- The final report must include the `参考文献` structure even when no concrete references exist.

## Final Language Check

Before delivery, scan the final Markdown and DOCX text for analysis traces and informal language. The report must:

- Use designer viewpoint throughout.
- Explain why each technical choice supports the design.
- Describe implementation ideas instead of line-by-line code reading.
- Provide text before and after every figure.
- Avoid `AI`, `模型`, `阅读源码`, `从源码可以看出`, `根据代码`, `可以看到`, `可以发现`, `可能`, `推测`, `为说明系统组件图所对应的设计内容，报告插入如下图示`, `图中内容均来自项目的`, and similar wording in the final report body.
