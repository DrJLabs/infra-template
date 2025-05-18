
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
