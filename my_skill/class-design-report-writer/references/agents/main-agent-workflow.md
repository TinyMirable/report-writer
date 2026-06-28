# 主代理工作流

主代理负责证据边界、任务分发、结果整合和最终验收。主代理不把事实发现、报告撰写、绘图、截图、质量检查全部混在一个步骤里完成；在 subagent tools 可用时，必须把报告制作拆分给子代理。

## 输入

- 用户给出的目标项目根目录、报告题目、学生信息和输出目录。
- 目标项目中的源码、配置、README、测试、运行脚本和已有文档。
- Skill references: `references/report/`, `references/diagram/`, `references/evidence-and-verification.md`, and `references/agents/`.

## 主代理职责

1. Identify the target project root, report title, student metadata if provided, and desired output directory.
2. Read the project files needed to understand goals, features, architecture, code structure, core logic, runtime environment, and tests.
3. Create `tmp/course-report-facts/` in the target project and write:
   - `01-project-overview.md`
   - `02-requirements-analysis.md`
   - `03-system-design.md`
   - `04-implementation-analysis.md`
   - `05-testing-evidence.md`
   - `06-report-evidence-map.md`
4. 分发给子代理完成 A-I 角色任务，并在 prompt 中明确输入、输出目录、可读 references、禁止越界事项和停止标准。
5. 收回子代理产物后进行冲突处理，确保报告正文、图像、截图和证据图谱一致。
6. 在报告写作代理A产出初稿后，必须先调度报告初稿审查代理I，确认内容是否足以阐述清楚课程设计项目，是否需要新增章节、图和阐述，是否存在漏图或缺失信息。
7. 在图像、截图、测试证据和图像质量检查完成后，必须调度报告文案增强代理H，对报告文案进行逐章增强，再交给代理F汇总产出。
8. 在代理F产出最终 Markdown 和 DOCX 后，必须调度交付检查智能体G进行最后的全面审查和修复。
9. 在最终交付前运行 skill 验收清单，确认 Markdown、DOCX、图片、测试证据、代理H/代理I/代理G检查记录和 evidence map 均存在。

## 子代理分工

- 报告写作代理A: 负责 Markdown 正文草稿和需要绘制的图像清单。
- UML图像绘制代理B: 负责 PlantUML 或等价 UML source 和导出图像。
- D2绘图代理C: 负责 D2 source 和导出图像，不绘制 UML 图。
- 测试截图代理D: 负责运行测试、截图和测试结果文档。
- 图像质量检验代理E: 负责检验代理B、检验代理C、检验代理D 的图片质量。
- 报告初稿审查代理I: 负责在代理A之后进行初稿审查，判断内容是否丰富实在、章节和图像需求是否完整、课程设计思路是否讲清楚，并提出方案补充。
- 报告文案增强代理H: 负责在代理F和交付检查智能体G之前润色和增强报告文案，逐章检查图的阐述、分析逻辑和教授视角下的表达充分性；代理H不检查图像质量和DOCX格式。
- 汇总产出代理F: 负责最终 Markdown、DOCX、图片插入、格式和语言检查，输入应以代理H增强后的文稿为准。
- 交付检查智能体G: 负责在代理F之后检查并修复最终交付物中的违规表述、图前说明僵硬、标题缩进、课题名称空行、课题名称占位文字残留、模板残留和参考文献结构问题。

## 工作边界

- 主代理不得让子代理直接编造未在 fact base 中出现的功能、测试、图像或结论。
- 主代理不得把同一个文件的写入权限同时交给多个子代理。若必须合并，主代理或代理F统一合并。
- 子代理输出冲突时，以项目事实、测试证据和 `06-report-evidence-map.md` 为准。
- 若当前环境不能启动子代理，主代理必须按 A-I 角色顺序模拟执行，并在 evidence map 中记录“环境未提供子代理工具，已按相同角色边界顺序执行”。

## 交付物

- 完整 `tmp/course-report-facts/` 六个事实文件。
- 子代理产物目录，建议为 `tmp/course-report-work/agents/`。
- 代理I产出的 `tmp/course-report-work/agents/I-draft-review.md`。
- 代理H产出的 `tmp/course-report-work/agents/H-copy-enhancement.md`。
- 汇总后的 Markdown report。
- 使用 DOCX 模板生成的 final report。
- 代理G产出的 `tmp/course-report-work/agents/G-delivery-review.md`。
- 图片 source、导出图片、截图和质量检查报告。

## 停止标准

- A-I 子代理产物齐全，且每项产物能映射到 fact base。
- 报告初稿审查代理I 已确认初稿内容足以进入绘图和文案增强阶段，或已记录并退回需要补充的章节、图像和阐述。
- 图像质量检验代理E 已确认所有图像和截图通过，或已记录无法修复的原因。
- 报告文案增强代理H 已逐章增强报告文字，尤其是图前图后阐述、分析思路和章节承接。
- 汇总产出代理F 已完成 Markdown、DOCX 和最终检查。
- 交付检查智能体G 已检查并修复最终交付物，或已记录无法自动修复的具体原因。
- 主代理已确认 `06-report-evidence-map.md` 覆盖每个章节的主要事实声明。

## 未达标准处理

- 缺少 fact base: 停止分发，先补齐事实文件。
- 缺少图像或截图: 重新分配给 B、C 或 D。
- 初稿内容单薄、章节逻辑不足、漏图或缺失信息: 先由代理I列出方案补充，再退回代理A或主代理补充事实和文稿。
- 图像质量不合格: 让 E 标明原因，再把对应任务退回 B、C 或 D 重做。
- 图的阐述不详实、章节承接不足或教授视角下表达不充分: 退回代理H增强文案，代理H不得用格式检查或图像检查替代文案增强。
- 正文与证据不一致: 退回 A 或 F 修改正文，禁止修改证据来迁就正文。
- DOCX 格式不合格: 退回 F，保持模板第一页和第二页不变，只修正文页内容。
- 代理G发现违规表述、图前说明僵硬、参考文献结构缺失或模板残留: 先由代理G直接修复；无法修复时退回 F 或主代理。
