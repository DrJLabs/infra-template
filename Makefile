# -------- CONFIG --------
VENV_DIR := .venv
VENV_PY  := $(VENV_DIR)/bin/python
PIP      := $(VENV_DIR)/bin/pip
RUFF     := $(VENV_DIR)/bin/ruff
BLACK    := $(VENV_DIR)/bin/black
MYPY     := $(VENV_DIR)/bin/mypy
BANDIT   := $(VENV_DIR)/bin/bandit
PYTEST   := $(VENV_DIR)/bin/pytest

# -------- INTERNAL --------
$(VENV_PY):
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip

# -------- PHONY TARGETS --------
.PHONY: install-dev install-test check lint type sec test agent-run

install-dev: $(VENV_PY)
	$(PIP) install -r requirements-test.txt
	$(PIP) install -e .
	$(PIP) install ruff black mypy bandit

install-test: $(VENV_PY)
	$(PIP) install -r requirements-test.txt
	$(PIP) install -e .

lint:  $(VENV_PY) ; $(RUFF)   check .
type:  $(VENV_PY) ; $(MYPY)   src
sec:   $(VENV_PY) ; $(BANDIT) -r src -q
test:  $(VENV_PY) ; $(PYTEST) -q tests
check: lint type sec test

agent-run: $(VENV_PY)
	$(VENV_PY) ai/$(AGENT).py --ticket $(TICKET)
