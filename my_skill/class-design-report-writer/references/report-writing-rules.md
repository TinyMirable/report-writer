# 报告撰写规则

## Source Discipline

Write from the target project's actual source code and verification artifacts. If a feature, test, route, class, API, or data model cannot be found in the project, do not describe it as implemented.

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
- Required use case diagram.
- System boundary.
- System constraints and norms.
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

Code formatting in DOCX:

- Font: Consolas or Cascadia Code.
- Size: 10.5 pt.
- Background: light gray or dark gray.
- Preserve indentation.

## 结果分析

Explain testing method and purpose.

For frontend projects:

- Include screenshots of test results, key pages, or interaction verification.
- Explain what each screenshot proves.

For non-frontend projects:

- Include a key result table and command output summary.
- Explain command, input, expected result, actual result, and conclusion.

## 课程设计总结

Write a grounded reflection. It may include:

- What was learned during design and implementation.
- Problems encountered.
- How problems were diagnosed and solved.
- Thoughts on debugging, testing, and program design.
- Improvements that could be made with more time.

Do not invent personal experiences; keep reflection consistent with the project work and evidence.

