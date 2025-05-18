#!/usr/bin/env bash
set -euo pipefail

python3 -m venv .venv
. .venv/bin/activate

WHEELHOUSE="$PWD/vendor/wheels"

if [ -d "$WHEELHOUSE" ] && compgen -G "$WHEELHOUSE/*.whl" > /dev/null; then
    export PIP_FIND_LINKS="$WHEELHOUSE"
    export PIP_NO_INDEX=1
    pip install -r requirements-test.txt
    pip install -e .
    pip install ruff black mypy bandit
else
    echo "No local wheel files found; skipping dependency installation."
fi

echo "Environment ready."
