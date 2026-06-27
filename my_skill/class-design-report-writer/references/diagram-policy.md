# Diagram Policy

## Reference Routing

Use this file as the diagram checklist and routing map.

- Read `references/diagram-layout-policy.md` before drawing any diagram or exporting any diagram image.
- Read `references/uml-diagram-standard.md` before drawing UML diagrams, including 用例图、类图、用户活动图、关键功能时序图、系统组件图、包图、部署图、状态图.
- Read `references/system-architecture-diagram-standard.md` before drawing 系统架构图 or any D2 architecture/infrastructure diagram.
- Keep editable diagram source files and exported images together in the report workspace.
- Do not rely on this summary alone when creating final diagrams; use the full reference that matches the diagram type.

## Required Diagrams

Produce at least:

| Chapter | Diagram | Purpose |
| --- | --- | --- |
| 方案论证(设计理念) | 用例图 | Show actors, system boundary, and user-visible functions. |
| 方案论证(设计理念) | 系统功能结构图 | Show feature decomposition and functional hierarchy. |
| 方案论证(设计理念) | 系统组件图 | Show major components and component dependencies. |
| 方案论证(设计理念) | 用户活动图 | Show the user's operation flow and system responses. |
| 方案论证(设计理念) | 关键功能时序图 | Show the time sequence of a key function. |
| 方案论证(设计理念) | 系统架构图 | Show major layers, modules, services, storage, and external dependencies. |
| 方案论证(设计理念) | 顶层数据流图 | Show the whole system as one process and its external entities/data stores. |
| 方案论证(设计理念) | 一层数据流图 | Decompose the top-level process into major functions. |
| 方案论证(设计理念) | 二层数据流图 | Decompose the most important level-1 function into lower-level processing. |
| 方案论证(设计理念) | 包图 | Show package/module organization and dependencies. |
| 过程论述 | 核心代码流程图 | Show the control flow of the most important implementation logic. |

Optional diagrams: class diagram, ER diagram, deployment diagram, sequence diagram, page flow diagram, module dependency diagram.

## Tool Preference

Prefer Next AI Draw.io when available. Save editable diagram sources and exported images. If unavailable, use draw.io XML, PlantUML, D2, Mermaid, or another tool that can export image files suitable for DOCX insertion.

Use PlantUML for standard UML diagrams:

- 用例图
- 类图
- 用户活动图
- 关键功能时序图
- 系统组件图
- 包图
- 部署图
- 状态图

Use D2 for architecture and infrastructure diagrams:

- 系统架构图
- Cloud architecture
- Infrastructure or network topology
- Microservice overview
- Data pipeline
- Event flow
- AI agent or MCP architecture

Use D2 for 系统架构图 according to the 系统架构图绘制准则: layered top-down layout, low-saturation layer backgrounds, flat professional style, consistent module sizes, clear system boundaries, right-side vertical strips for cross-cutting services when useful, and simple arrows for data flow or dependency relationships.

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

## UML Notation Requirements

- 用例图 must show actors, use cases, system boundary, and associations; include/extend relationships only when the project evidence supports them.
- 用户活动图 must show start/end nodes, actions, control flow, decisions, and swimlanes when multiple participants exist.
- 关键功能时序图 must show lifelines, time-ordered messages, activations when useful, and return or error paths when visible in code.
- 系统组件图 must show components, interfaces or dependencies, and clear component names.
- 包图 must show package/module boundaries and dependency directions.
- 类图 is required when the project uses object-oriented implementation; include key attributes, methods, and relationships only when supported by code.

## System Architecture Diagram Requirements

- Use white background and sans-serif font.
- Use rounded rectangles for services/modules, cylinders for databases, and cloud shapes for external systems when the tool supports them.
- Use short labels, maximum three lines per node.
- Group modules by layers such as frontend, access/API, business service, basic service, and data storage when those layers exist.
- Keep each layer visually distinct with low-saturation colors.
- Avoid decorative icons unless explicitly requested.
- Do not put paragraph text inside nodes.

## Before Exporting

1. Run automatic hierarchical layout if the tool supports it.
2. Run connector routing optimization if available.
3. Detect node overlap.
4. Detect label overlap.
5. Detect connector crossings.
6. Reposition nodes iteratively until constraints are satisfied.
7. Verify notation, abstraction level, professional naming, and suitability for an academic course design report.
8. Export only after quality checks pass.

Every diagram in the report must have text before and after it.
