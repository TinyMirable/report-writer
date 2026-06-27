# Evidence and Verification

## Fact Base

Create `tmp/course-report-facts/` in the target project before writing the report.

Recommended files:

- `01-project-overview.md`: project goal, visible features, entry points, key docs, source files read.
- `02-requirements-analysis.md`: actors, use cases, system boundary, constraints, security/data/runtime/performance requirements.
- `03-system-design.md`: architecture, technology stack, data flow, packages/modules, classes/objects.
- `04-implementation-analysis.md`: core algorithms, key functions, source excerpts, code flow candidates.
- `05-testing-evidence.md`: commands run, environment, outputs, screenshots, failures, and interpretation.
- `06-report-evidence-map.md`: mapping from report sections to files, commands, screenshots, diagrams, and fact docs.

Each fact should cite a project file path, command, screenshot, diagram file, or direct observation.

## Testing Evidence

Run the project's normal test command when one exists. Look in files such as `package.json`, `pyproject.toml`, `pytest.ini`, `pom.xml`, `build.gradle`, `Makefile`, CI config, README, or project scripts.

If the normal test command is missing or broken, run the narrowest meaningful alternative:

- Build command.
- Lint command.
- Smoke command.
- Unit-level script.
- API or CLI invocation.
- Manual frontend interaction with screenshots.

Record failures honestly. A failing command can still be useful evidence if the report states the actual result and cause.

## Frontend Evidence

If the project has a frontend:

- Start the app if possible.
- Capture screenshots for key pages, workflows, or test results.
- Save screenshots in an `image/` or report image directory.
- Explain in the report what each screenshot proves.

## Non-Frontend Evidence

If the project has no frontend:

- Create a test results table.
- Include command, purpose, expected result, actual result, and conclusion.
- Summarize important command output instead of pasting excessive logs.

## Final Evidence Map

Before final delivery, update `06-report-evidence-map.md` with:

- Report section title.
- Claims made in that section.
- Supporting project files.
- Supporting commands and outputs.
- Supporting diagrams or screenshots.
- Any uncertainty or missing evidence.

Do not claim a section is verified until it appears in the evidence map.

