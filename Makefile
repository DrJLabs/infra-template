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
.PHONY: install-dev install-test lint type sec test check agent \
        up down logs grafana

# -------- INSTALL --------
install-dev: $(VENV_PY)               ## dev + lint/type/sec tooling
	$(PIP) install -r requirements-test.txt
	$(PIP) install -e .
	$(PIP) install ruff black mypy bandit

install-test: $(VENV_PY)              ## test-only deps
	$(PIP) install -r requirements-test.txt
	$(PIP) install -e .

# -------- QUALITY GATES --------
lint:  $(VENV_PY) ; $(RUFF)   check .
type:  $(VENV_PY) ; $(MYPY)   src
sec:   $(VENV_PY) ; $(BANDIT) -r src -q
test:  $(VENV_PY) ; $(PYTEST) -q tests
check: lint type sec test                ## all gates

# -------- AGENT ORCHESTRATOR --------
agent: $(VENV_PY)                        ## run AutoGen GroupChat
	@set -a; test -f .env && . .env; set +a; \
	$(VENV_PY) ai/runner.py $(TICKET)

# -------- DOCKER OBSERVABILITY STACK --------
up:                                    ## start full stack incl. OTLP
	docker compose up -d

down:                                  ## stop all containers
	docker compose down

logs:                                  ## tail compose logs
	docker compose logs -f --tail=50

grafana:                               ## quick link to Grafana UI
	@echo "Open http://localhost:3000 (user: admin / pass: admin)"
