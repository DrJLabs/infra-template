
---

## Ignored paths & their examples

| Path | Example file | Purpose |
|------|--------------|---------|
| `.env` | `.env.example` | Fill in secrets locally; never commit the real file. |
| `.venv/` | `.venv/.gitkeep` | Indicates project-local virtual env lives here. |
| `*.egg-info/` | `stub.egg-info/README.md` | Python build artefacts. |
| `__pycache__/` | `src/__pycache__/README.md` | Interpreter byte-code cache. |

Agents **must not** add real secrets or artefacts; update the examples instead.

## Offline setup

Run `scripts/setup.sh` to create a virtual environment. If `vendor/wheels` contains wheel files, they will be installed without network access. When the directory is empty the script simply creates the environment and relies on the packages preloaded in this workspace.

## Agent guidance

Instructions for automated agents live in `.codex/AGENTS.md`. They supersede any
other documentation. Review them before running automation.

Use `scripts/setup.sh` to prepare the Python environment. The script installs
any wheels found in `vendor/wheels` without requiring network access and is the
only setup method expected by automated tools.

