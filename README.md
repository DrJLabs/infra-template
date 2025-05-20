
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

A startup script is available at `.codex/startup.sh` for preparing the Python
environment using only the wheels provided in `vendor/wheels`. If no wheels are
present, the script skips installation to avoid network access. Run it before
the environment loses connectivity.

## Montfort integration

Set `DISABLE_MONTFORT=1` to force the application to load a stub client and skip tests marked with `@pytest.mark.montfort`. To run the real integration tests, unset the variable and include the marker:

```bash
pytest -m montfort
```

