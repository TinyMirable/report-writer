# 课程设计报告撰写 Skill 设计

## 背景

本项目要交付一个可复用的 Codex skill，使未来智能体能够读取一个已有代码仓库，依据项目真实代码和测试结果，撰写符合课程设计报告模板的 Markdown 与 DOCX 报告。

事实源优先级如下：

1. `spec/课程设计报告撰写skill.md`
2. `spec/skill功能阐述.md`
3. `spec/绘图准则.md`
4. `课程设计报告书模板.md`
5. `课程设计报告书模板.docx`

## 目标

实现一个完整 skill，并同时交付两个位置：

- 仓库内交付物：`my_skill/class-design-report-writer/`
- Codex 可发现安装副本：优先 `$CODEX_HOME/skills/class-design-report-writer/`；若 `$CODEX_HOME` 未设置，则使用 `C:/Users/SKY/.codex/skills/class-design-report-writer/`

两个位置必须保持内容一致，并通过验证脚本检查。

## 非目标

- 不在本项目中生成某个具体课程报告。
- 不把报告模板改写成新的学校模板。
- 不要求自动完成所有可能项目类型的业务推断；skill 必须要求智能体以用户给定代码仓库为唯一事实依据。

## Skill 结构

推荐目录结构：

```text
my_skill/class-design-report-writer/
  SKILL.md
  agents/
    openai.yaml
  assets/
    course-design-report-template.docx
  references/
    report-template.md
    report-writing-rules.md
    diagram-policy.md
    evidence-and-verification.md
  scripts/
    validate_skill.py
    sync_to_codex_skills.py
```

### SKILL.md

`SKILL.md` 是入口，保持精简，重点说明智能体必须按阶段工作：

1. 识别目标项目与输出路径。
2. 分析项目结构、功能、架构、核心代码、运行环境、测试方式和测试结果。
3. 将理解到的事实写入目标项目的 `tmp/` 目录，作为后续报告唯一事实依据。
4. 根据必需图表清单生成和校验图。
5. 运行测试、收集截图或关键结果表。
6. 按模板写 Markdown 报告。
7. 使用模板资产生成 DOCX，并检查格式要求。
8. 输出证据清单，说明哪些内容来自代码、测试、截图、图表和模板。

### references

引用文件承载较长规则，避免 `SKILL.md` 过重。

- `report-template.md`：来自 `课程设计报告书模板.md`，保留章节结构和格式要求。
- `report-writing-rules.md`：说明五个正文章节分别写什么、章节间如何组织、图前图后说明如何写。
- `diagram-policy.md`：整合 `spec/绘图准则.md` 和必需图表清单。
- `evidence-and-verification.md`：说明项目事实文档、测试证据、截图、图表文件、报告文件如何构成可验证证据。

### assets

`assets/course-design-report-template.docx` 复制自仓库根目录的 `课程设计报告书模板.docx`。未来智能体生成 DOCX 时应优先复用该模板，而不是凭空新建格式。

### scripts

脚本只做可重复、确定性的辅助工作：

- `validate_skill.py`：验证 skill 结构、frontmatter、引用文件、模板资产、脚本文件是否存在。
- `sync_to_codex_skills.py`：把仓库内 skill 同步到 Codex 个人 skills 目录，并可检查同步后文件哈希一致。

## 报告工作流

skill 应要求未来智能体在目标项目中创建 `tmp/` 事实文档，例如：

```text
tmp/course-report-facts/
  01-project-overview.md
  02-requirements-analysis.md
  03-system-design.md
  04-implementation-analysis.md
  05-testing-evidence.md
  06-report-evidence-map.md
```

这些文档必须记录来源文件、命令、截图和结论。报告正文只能基于这些文档和可验证证据撰写。

## 必需图表

skill 必须要求至少生成以下图表：

- 需求分析：用例图。
- 系统设计：系统架构图、顶层数据流图、一层数据流图、二层数据流图、包图。
- 系统实现：核心代码流程图。

其他图表可按项目需要增加，例如类图、模块依赖图、数据库 ER 图、页面流程图、部署图。

绘图必须遵守 `Diagram Layout Policy`：层级布局、节点和标签不重叠、连接线尽量正交、连接线不得穿过节点、相邻节点至少 100 px 间距、导出前必须检查布局质量。

## 测试和证据

skill 必须要求未来智能体亲自运行项目测试或合理的验证命令。

- 如果项目包含前端，必须保存测试结果截图、关键页面截图或交互验证截图，并在报告中说明。
- 如果项目无前端，必须保存测试运行关键结果表和命令输出摘要。
- 所有报告结论必须能映射到代码文件、测试命令、图表文件、截图或事实文档。

## DOCX 格式要求

生成 DOCX 时必须复用模板资产，并保留或实现以下格式要点：

- 题目：二号、黑体、加粗、居中。
- 章节标题：宋体、四号、加粗、两端对齐。
- 正文：宋体、小四、两端对齐、首行缩进 2 字符、固定行距 20 磅。
- 图号和图名放图下方，居中。
- 表号和表名放表上方，居中。
- 关键代码块使用等宽字体，如 Consolas 或 Cascadia Code，10.5pt，浅灰或深灰背景，保留缩进。

## 验证设计

本项目完成后至少运行以下验证：

1. `python my_skill/class-design-report-writer/scripts/validate_skill.py my_skill/class-design-report-writer`
2. `python my_skill/class-design-report-writer/scripts/sync_to_codex_skills.py --check my_skill/class-design-report-writer`
3. 同步安装后再次运行一致性检查。
4. 手动检查 `SKILL.md` 是否明确触发条件、事实沉淀、图表清单、测试证据、MD/DOCX 输出和格式要求。

验证证据必须记录到 `feature_list.json` 或 `claude-progress.md`。

## 风险

- 未来智能体可能跳过事实沉淀直接写报告，因此 `SKILL.md` 要把 `tmp/` 事实文档设为硬性门禁。
- 图表生成工具在不同环境中可用性不同，因此 skill 应优先指导使用 Next AI Draw.io，并允许在工具不可用时使用 Mermaid、draw.io XML 或其他可导出的图表流程，但仍必须满足布局质量。
- DOCX 格式验证难以完全自动化，因此脚本验证结构和资产，人工/渲染检查格式质量。

## 自审结果

- 无 TBD/TODO 占位。
- 设计同时覆盖仓库交付和 Codex 安装副本。
- 范围聚焦于创建 skill，不扩展到生成具体课程报告。
- 验证路径明确，但实现阶段仍需根据实际脚本名和环境路径记录真实命令输出。
