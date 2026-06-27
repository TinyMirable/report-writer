# 课程设计报告表述风格约束

Use this guide before drafting or revising the final Markdown and DOCX report. It distills the project-level `spec/表述风格约束.md` into rules that fit a Chinese course design report.

## Reader and Voice

- 面向课程设计评审教师 writing: assume the reader understands software engineering basics, but has not opened the target repository.
- Write as the system designer, not as an outside code reader.
- 先说明设计目的 before explaining mechanisms in each major section.
- Do not expose analysis process, repository scanning, or AI behavior.

Prefer:

- `本系统采用前后端分离架构，将界面交互与业务处理解耦。`
- `用户管理模块负责用户注册、登录和权限校验。`

Avoid:

- `从源码可以看出系统采用前后端分离架构。`
- `根据项目文件可以发现用户管理模块比较重要。`

## Concrete Expression

- 使用具体术语 instead of broad nouns such as `方面`, `因素`, `内容`, `东西`, `问题`, or `模块很多`.
- Name the actual module, function, page, API, table, command, diagram, or test result.
- Explain the design value of each technology choice.

Prefer:

- `系统采用 JWT 保存登录状态，使服务端无需维护会话表。`
- `订单查询接口通过分页参数限制单次返回数量，降低列表页响应压力。`

Avoid:

- `系统在很多方面进行了优化。`
- `该设计有较好的效果。`

## Concision

- 删掉空话套话. Remove sentences that only announce importance or summarize without adding facts.
- Avoid filler such as `值得注意的是`, `总的来说`, `在一定程度上`, `具有重要意义`, `能够更好地`, and `进一步提升了系统水平` unless followed by concrete evidence.
- 避免泛泛总结句. Do not close every paragraph with a generic summary sentence.

Prefer:

- `角色校验在路由进入前完成，未登录用户会被重定向到登录页。`

Avoid:

- `总的来说，该功能的实现具有重要意义，并进一步提升了系统的整体水平。`

## Evidence and Calibration

- Every factual claim must have 事实依据: source file, configuration, command output, screenshot, diagram, or fact document.
- Do not overstate evidence. Use measured language when the project has only smoke tests or command-line verification.
- Do not write performance, security, concurrency, reliability, or usability claims unless evidence exists.

Prefer:

- `测试结果显示，登录接口在有效账号和错误密码两种输入下均返回预期状态。`
- `本次验证覆盖了主要命令路径，尚未包含压力测试。`

Avoid:

- `系统性能优异，安全性很高。`
- `所有功能都经过了充分测试。`

## Term Consistency

- 术语一致 across the whole report.
- Use one name for the same module, role, page, API, table, and diagram.
- Define abbreviations once, then use the same abbreviation consistently.

Examples:

- If the report uses `管理员`, do not later switch to `后台用户` for the same actor.
- If the report uses `订单管理模块`, do not later call it `订单中心` unless the code uses both names for different concepts.

## Sentence and Paragraph Shape

- Keep most sentences to one main idea.
- Split long sentences that combine background, mechanism, benefit, and result.
- Use paragraphs for explanation; use bullet lists only for real lists such as requirements, test cases, or module responsibilities.
- Avoid starting several consecutive sentences with the same phrase such as `本系统`.
- Use transitions sparingly; do not overuse `此外`, `同时`, `进一步`, `因此`.

## Figure Explanation Style

Every figure must have text before and after it.

- Before the figure: explain why the diagram is used.
- After the figure: explain what the diagram shows and how the parts cooperate.
- Do not write `从图中可以看出`. Use `图中展示` or directly describe the relationship.

Prefer:

- `为说明用户与系统功能之间的交互关系，绘制系统用例图。`
- `图中展示管理员和普通用户两个参与者。管理员负责用户管理和数据维护，普通用户完成信息查询和业务提交。`

## Final Language Check

Before delivery, run a final language pass on the Markdown and DOCX report:

- Remove AI or analysis traces: `AI`, `模型`, `阅读源码`, `根据代码`, `从源码可以看出`, `经过分析`, `可以发现`.
- Remove uncertainty when unsupported: `可能`, `大概`, `似乎`, `推测`, `猜测`.
- Replace vague claims with concrete project facts.
- Check term consistency for actors, modules, pages, APIs, tables, diagrams, and tests.
- Confirm every paragraph either explains design purpose, design mechanism, evidence, or result.
- 最终语言检查 must be completed before delivering the Markdown and DOCX files.
