# Diagram Policy

## Required Diagrams

Produce at least:

| Chapter | Diagram | Purpose |
| --- | --- | --- |
| 方案论证(设计理念) | 用例图 | Show actors, system boundary, and user-visible functions. |
| 方案论证(设计理念) | 系统架构图 | Show major layers, modules, services, storage, and external dependencies. |
| 方案论证(设计理念) | 顶层数据流图 | Show the whole system as one process and its external entities/data stores. |
| 方案论证(设计理念) | 一层数据流图 | Decompose the top-level process into major functions. |
| 方案论证(设计理念) | 二层数据流图 | Decompose the most important level-1 function into lower-level processing. |
| 方案论证(设计理念) | 包图 | Show package/module organization and dependencies. |
| 过程论述 | 核心代码流程图 | Show the control flow of the most important implementation logic. |

Optional diagrams: class diagram, ER diagram, deployment diagram, sequence diagram, page flow diagram, module dependency diagram.

## Tool Preference

Prefer Next AI Draw.io when available. Save editable diagram sources and exported images. If unavailable, use draw.io XML, Mermaid, PlantUML, or another tool that can export image files suitable for DOCX insertion.

## Layout Requirements

Diagram readability has higher priority than generation speed.

- Use hierarchical top-down layout unless the user explicitly requests another layout.
- No overlapping shapes.
- No overlapping labels.
- No connector may pass through a node.
- Avoid intersecting connectors whenever possible.
- Maintain at least 100 px spacing between adjacent nodes.
- Align related nodes on a consistent grid.
- Prefer orthogonal 90-degree elbow connectors.
- Minimize connector crossings, bends, and lengths.
- Balance whitespace across the canvas.
- Avoid dense regions and isolated nodes.
- Keep parent nodes above child nodes.
- Keep data flow consistently top-to-bottom or left-to-right.

## Before Exporting

1. Run automatic hierarchical layout if the tool supports it.
2. Run connector routing optimization if available.
3. Detect node overlap.
4. Detect label overlap.
5. Detect connector crossings.
6. Reposition nodes iteratively until constraints are satisfied.
7. Export only after quality checks pass.

Every diagram in the report must have text before and after it.

