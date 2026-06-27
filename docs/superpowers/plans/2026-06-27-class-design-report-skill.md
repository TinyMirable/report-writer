# Class Design Report Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, and install a Codex skill that guides agents to generate course design reports from real project code.

**Architecture:** The repository copy under `my_skill/class-design-report-writer/` is the source of truth. A sync script copies that directory to Codex's personal skills directory and verifies file hashes. The skill keeps the main workflow in `SKILL.md`, long requirements in `references/`, reusable template material in `assets/`, and deterministic checks in `scripts/`.

**Tech Stack:** Markdown skill files, YAML metadata, Python standard library scripts, existing DOCX template asset.

---

### Task 1: Create Skill Files

**Files:**
- Create: `my_skill/class-design-report-writer/SKILL.md`
- Create: `my_skill/class-design-report-writer/agents/openai.yaml`
- Create: `my_skill/class-design-report-writer/references/report-template.md`
- Create: `my_skill/class-design-report-writer/references/report-writing-rules.md`
- Create: `my_skill/class-design-report-writer/references/diagram-policy.md`
- Create: `my_skill/class-design-report-writer/references/evidence-and-verification.md`
- Create: `my_skill/class-design-report-writer/assets/course-design-report-template.docx`

- [ ] **Step 1: Create directories**

Run:

```powershell
New-Item -ItemType Directory -Force `
  'my_skill/class-design-report-writer/agents', `
  'my_skill/class-design-report-writer/assets', `
  'my_skill/class-design-report-writer/references', `
  'my_skill/class-design-report-writer/scripts' | Out-Null
```

Expected: directories exist.

- [ ] **Step 2: Copy template asset**

Run:

```powershell
Copy-Item -LiteralPath '课程设计报告书模板.docx' -Destination 'my_skill/class-design-report-writer/assets/course-design-report-template.docx'
```

Expected: DOCX asset exists in the skill.

- [ ] **Step 3: Write skill instructions and references**

Use `apply_patch` to add the Markdown and YAML files. The skill must require fact extraction into `tmp/course-report-facts/`, mandatory diagrams, test evidence, Markdown output, DOCX output, and final evidence mapping.

### Task 2: Create Validation and Sync Scripts

**Files:**
- Create: `my_skill/class-design-report-writer/scripts/validate_skill.py`
- Create: `my_skill/class-design-report-writer/scripts/sync_to_codex_skills.py`

- [ ] **Step 1: Write `validate_skill.py`**

The script should check:

- `SKILL.md` exists and has `name` and `description` frontmatter.
- `agents/openai.yaml` exists.
- Required references exist.
- DOCX template asset exists and is non-empty.
- Required scripts exist.
- `SKILL.md` mentions the hard gates: `tmp/course-report-facts`, `用例图`, `系统架构图`, `顶层数据流图`, `一层数据流图`, `二层数据流图`, `包图`, `核心代码流程图`, `Markdown`, `DOCX`.

- [ ] **Step 2: Write `sync_to_codex_skills.py`**

The script should:

- Resolve the install root from `CODEX_HOME/skills` or `~/.codex/skills`.
- Copy the source skill directory to `class-design-report-writer`.
- Exclude transient cache files.
- Support `--check` to compare source and destination file hashes without copying.

### Task 3: Validate, Sync, and Record Evidence

**Files:**
- Modify: `feature_list.json`
- Modify: `claude-progress.md`
- Modify: `docs/index.md`

- [ ] **Step 1: Run repository validation**

Run:

```powershell
python my_skill/class-design-report-writer/scripts/validate_skill.py my_skill/class-design-report-writer
```

Expected: validation passes.

- [ ] **Step 2: Sync to Codex personal skills**

Run:

```powershell
python my_skill/class-design-report-writer/scripts/sync_to_codex_skills.py my_skill/class-design-report-writer
```

Expected: destination path is printed.

- [ ] **Step 3: Check sync consistency**

Run:

```powershell
python my_skill/class-design-report-writer/scripts/sync_to_codex_skills.py --check my_skill/class-design-report-writer
```

Expected: source and installed copy match.

- [ ] **Step 4: Update project records**

Record passed commands, installed path, and remaining risks in `feature_list.json` and `claude-progress.md`. Mark `chat-001` as `passing` only after all validation succeeds.

## Self-Review

- Spec coverage: The plan covers repository skill delivery, Codex personal installation, fact extraction, diagrams, testing evidence, MD/DOCX outputs, format guidance, and verification records.
- Placeholder scan: No unfinished placeholder markers remain.
- Type consistency: Script names and paths match the design document and feature list.
