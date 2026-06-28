# 课程设计报告模板

This reference mirrors the required course design report structure. Use it when planning sections and checking final formatting.

## 封面

Word/DOCX 模板第一页是封面，不需要编辑。不要修改模板第一页的版式、段落、页眉页脚或已有文字，除非用户明确提供封面字段并要求填写。

## 个人信息

Word/DOCX 模板第二页是个人信息页，不需要编辑。不要修改模板第二页的版式、表格、段落、页眉页脚或已有文字，除非用户明确提供个人信息字段并要求填写。

## DOCX 填充边界

- 第三页开始才是要撰写的正文。
- 模板中已经存在正文标题：`一、选题背景`、`二、方案论证(设计理念)`、`三、过程论述`、`四、结果分析`、`五、课程设计总结`。
- 只在既有章节标题下方填充正文、图片、表格、代码块和图表说明。
- 不要重复创建同名章节标题。
- 不要删除、改名、重排模板已有章节标题。
- 若 Markdown 版本需要完整展示结构，也保持同样章节名和顺序。
- 不能把完整报告追加到第4页之后；最终 DOCX 必须清理第3页和第4页中未替换的模板残留、示例正文、多余空页和重复章节。

## Main Sections

### 课题名称

题目格式：宋体，3号，加粗，居中对齐，上下空一行。替换word中的"课题名称"并调整格式。
最终检查时必须确认 `课题名称` 前有一个空行，后有一个空行。
生成产物后必须删除模板中原本的 `课题名称` 占位文字。最终 Markdown 和 DOCX 只能保留真实课题名称，不得同时残留占位文字和真实题目。

### 一、选题背景

格式：宋体，4号，加粗，两端对齐，首行缩进2字符。

Explain the main problems this project should solve, the technical requirements it should meet, and the guiding idea of the design.

正文必须放在 `一、选题背景` 标题下方。
### 二、方案论证(设计理念)

格式：宋体，4号，加粗，两端对齐，首行缩进2字符。

Explain the design principles, design choices, why the chosen plan is appropriate, and the characteristics of the selected approach. Include functionality and requirements, security, data integrity, runtime environment, and performance requirements.

正文必须放在 `二、方案论证(设计理念)` 标题下方。包含需求分析思路和系统设计思路：用例图、系统功能结构图、系统组件图、用户活动图、关键功能时序图、系统约束和规范、系统架构图、顶层数据流图、一层数据流图、二层数据流图、包图，以及项目适用时的类图。

### 三、过程论述

格式：宋体，4号，加粗，两端对齐，首行缩进2字符。

Explain how the design is implemented. Keep the discussion layered, accurate, and evidence-backed. Every figure must have explanatory text before and after it.

正文必须放在 `三、过程论述` 标题下方。包含核心实现思路、核心代码流程图、关键逻辑源代码摘录和代码作用说明。每个图前说明为什么使用该图及其主要作用，图后说明图中成分、交互、依赖或流程。

### 四、结果分析

格式：宋体，4号，加粗，两端对齐，首行缩进2字符。

Analyze the main data, phenomena, test results, or verification results from the project, and draw conclusions.

正文必须放在 `四、结果分析` 标题下方。包含测试方法、测试目的、测试命令或交互路径、实际结果和结果说明。前端项目插入截图并说明截图证明的内容；无前端项目插入测试运行关键结果表和命令摘要。

### 五、课程设计总结

格式：宋体，4号，加粗，两端对齐，首行缩进2字符。

Summarize gains from the course design, problems encountered, how problems were solved, thoughts on debugging ability, and implementation reflections.
以及，课程设计过程的收获、遇到的问题，遇到问题解决问题过程的思考、程序调试能力的思考，课程设计实现过程中的收获和体会等。
### 参考文献 
（参考文献标题为三号，宋体，加粗，居中，上下空一行）
（参考文献正文为五号，宋体，行距为固定值20磅,重要资料必须注明具体出处，详细到页码；网上资料注明日期。）

最终报告必须保留 `参考文献` 结构。即使项目没有参考文献，也保留标题并让具体文献条目为空；不要编造不存在的书籍、论文、网址或访问日期。

## Body Formatting

- 正文：宋体，小4号，不加粗，两端对齐，固定行距 20 磅。
- 首行缩进 2 字符。
- 左右缩进 0 字符。
- 段前、段后为 0 行。
- 5个标题 `一、选题背景`、`二、方案论证(设计理念)`、`三、过程论述`、`四、结果分析`、`五、课程设计总结` 均必须首行缩进两字符。

## Captions

- 图号和图名放在图下方，居中对齐，例如：`图1 模拟计费系统用例图`。
- 表号和表名放在表上方，居中对齐，例如：`表1 计费功能测试数据和预期结果`。
- 公式编号用括号写在右边行末，不加虚线。

## References

If references are included, use sequential numeric citations. Important sources must include concrete source information. Online sources should include access or publication dates when available.
If there are no references, keep the `参考文献` heading and leave the entries blank.

## Final Template Residue Check

Before delivery, inspect the generated Markdown and DOCX:

- 第3页和第4页不得残留模板占位正文、示例说明、未替换的 `课题名称`、重复章节标题或多余空页。
- 真实题目写入后，必须再次扫描并删除 `课题名称` 占位文字；不能把占位文字作为普通正文留在报告中。
- 正文不得追加到模板第4页之后再开始；内容应从第三页正文区域进入既有章节。
- 封面页和个人信息页保持模板原貌，除非用户明确提供字段并要求填写。
- 5个标题首行缩进两字符，`课题名称` 上下空一行，报告末尾有 `参考文献` 结构。
