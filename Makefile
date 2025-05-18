# -------- PHONY targets --------
.PHONY: install-dev install-test check lint type sec test agent-run

# ---------- TOOL VERSIONS ----------
PY        ?= python3.12
PIP       ?= python3.12 -m pip
RUFF      ?= ruff
BLACK     ?= black
MYPY      ?= mypy
BANDIT    ?= bandit
PYTEST    ?= pytest

# ---------- INSTALL ----------
install-dev:               ## install dev + lint/type/sec tooling
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-test.txt
	$(PIP) install -e .
	$(PIP) install ruff black mypy bandit

install-test:              ## install only test deps
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements-test.txt
	$(PIP) install -e .

# ---------- QUALITY GATES ----------
lint:                      ## ruff = fast lint & format check
	$(RUFF) check .

type:                      ## mypy static typing
	$(MYPY) src

sec:                       ## bandit security scan
	$(BANDIT) -r src -q

test:                      ## run pytest with quiet output
	$(PYTEST) -q tests

check: lint type sec test  ## run all gates

# ---------- AGENT ----------
agent-run:                 ## run an agent (e.g. make agent-run AGENT=coder TICKET=42)
	$(PY) ai/$(AGENT).py --ticket $(TICKET)
