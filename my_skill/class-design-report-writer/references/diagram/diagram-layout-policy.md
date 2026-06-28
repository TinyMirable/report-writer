# Diagram Layout Policy

Diagram readability has higher priority than generation speed.

Generate diagrams using a hierarchical top-down layout unless another layout is explicitly requested.

Requirements:

- No overlapping shapes.
- No overlapping labels.
- No intersecting connectors whenever possible.
- No connector may pass through any node.
- Maintain at least 100 px spacing between adjacent nodes.
- Align related nodes on a consistent grid.
- Prefer orthogonal (90° elbow) connectors.
- Minimize connector crossings.
- Minimize connector bends.
- Minimize connector lengths.
- Balance whitespace across the entire canvas.
- Avoid dense regions and isolated nodes.
- Keep parent nodes above child nodes.
- Keep data flow consistently from top to bottom or left to right.


The generated diagram should meet professional architecture documentation standards comparable to diagrams produced by senior solution architects using PlantUML, drawio, and D2.


## Using Guidelines
Use PlantUML for

✓ Use Case
✓ Class
✓ Activity
✓ Sequence
✓ State
✓ Deployment
✓ Component

Do NOT use PlantUML for

× Cloud Architecture
× Infrastructure
× Network Topology
× Microservice Overview

The required 系统架构图 must be implemented using drawio after inspecting `assets/系统架构图例.png`. Other cloud, infrastructure, network, and microservice diagrams can use D2 when they are not the required 系统架构图.


Use D2 when describing

• Distributed Systems
• Cloud Platforms
• Kubernetes
• AI Agent Architecture
• MCP Architecture
• Multi-Agent Systems
• Data Pipeline
• Event Flow
• Enterprise Systems

Use drawio when describing

• Required 系统架构图
• Layered application architecture that must follow `assets/系统架构图例.png`

Never use D2 to describe

• UML Class
• Sequence
• Activity
• State


## Diagram Style

Use professional architecture documentation style.

Requirements

- White background
- Sans-serif font
- Uniform font size
- Consistent node width
- Consistent node height
- Rounded rectangles for services
- Cylinders for databases
- Clouds for external systems
- Actors use UML actor notation
- Avoid decorative icons unless explicitly requested
- Use short labels
- Maximum 3 lines per node
- Avoid paragraph text inside nodes

## Self Check
Before finalizing any diagram, verify:

□ Correct diagram type selected
□ No overlapping nodes
□ No overlapping labels
□ No connector crossing
□ Correct notation
□ Professional naming
□ Consistent spacing
□ Proper hierarchy
□ Appropriate abstraction level
□ Suitable for academic report
□ Suitable for enterprise documentation
