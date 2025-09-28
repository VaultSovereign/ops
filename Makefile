SHELL := /bin/bash
PY ?= python3
NODE ?= node
NPX ?= npx
ROOT := $(shell pwd)

DOCS_DIR := docs
PROMPTS_DIR := prompts
TOOLS_DIR := tools
EVAL_DIR := eval-results
COVERAGE_THRESHOLD ?= 80

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "make install        # install dev deps (jsonschema, mdformat, markdownlint)"
	@echo "make check          # run aggregate validation suite"
	@echo "make docs:index     # regenerate docs index"
	@echo "make lint:md        # markdown lint (mdformat --check)"
	@echo "make footer         # footer compliance gate"
	@echo "make validate:json  # schema validation for prompts/tools"
	@echo "make guardrails     # run guardrail validators"
	@echo "make evals          # run coverage + adversarial evals"
	@echo "make roe            # run ROE compliance check"
	@echo "make badges         # refresh README badges"
	@echo "make prompts:sync   # regenerate prompt index from metadata files"
	@echo "make prompts:lint   # validate prompt metadata contract"
	@echo "make docs:summon    # generate knowledge summon report"
	@echo "make pr:summary     # update PR auto-summary comment (needs GitHub token)"
	@echo "make pr:scan        # preview PR summary without posting"
	@echo "make protect:enable # enable branch protection for main (admin token)"
	@echo "make ssh:auto       # SSH automation (agent + test + tunnel + status)"
	@echo "make ssh:status     # show SSH connection status"
	@echo "make lint:md:fix    # auto-fix markdown issues (URLs, fences, spacing)"
	@echo "make lint:md:fix-all # complete markdown fix (URLs, fences, headings)"

.PHONY: install
install:
	@echo "[install] Installing Python + Node tooling..."
	-$(PY) -m pip install --upgrade jsonschema mdformat requests >/dev/null 2>&1 && echo "[install] Python deps installed" || echo "[install] Python deps skipped"
	@command -v $(NPX) >/dev/null 2>&1 && $(NPX) --yes markdownlint-cli2@0.13.0 --version >/dev/null 2>&1 && echo "[install] markdownlint-cli2 ready" || echo "[install] markdownlint-cli2 available via npx"
	@echo "[install] Done"

.PHONY: docs-index docs\:index
docs-index:
	@echo "[docs] Generating docs index"
	@if [ -f .github/workflows/scripts/generate-docs-index.js ]; then \
		$(NODE) .github/workflows/scripts/generate-docs-index.js; \
	else \
		echo "[docs] skip (script missing)"; \
	fi

docs\:index: docs-index

.PHONY: lint-md lint\:md
lint-md:
	@echo "[lint] Markdown formatting check"
	@if command -v mdformat >/dev/null 2>&1; then \
		mdformat --check README.md AGENTS.md $(DOCS_DIR) 2>/dev/null || mdformat --check $(DOCS_DIR) 2>/dev/null || true; \
	elif $(PY) -c "import mdformat" >/dev/null 2>&1; then \
		$(PY) -m mdformat --check README.md AGENTS.md $(DOCS_DIR) 2>/dev/null || $(PY) -m mdformat --check $(DOCS_DIR) 2>/dev/null || true; \
	else \
		echo "[lint] mdformat not installed; run 'make install'"; \
	fi
	@if command -v $(NPX) >/dev/null 2>&1; then \
		$(NPX) --yes markdownlint-cli2@0.13.0 "docs/**/*.md" || true; \
	else \
		echo "[lint] markdownlint-cli2 unavailable; skipping"; \
	fi

lint\:md: lint-md

.PHONY: lint-md-fix lint\:md\:fix
lint-md-fix:
	@echo "[md] auto-fixing with markdownlint --fix + mdformat"
	@$(NPX) --yes markdownlint-cli2 --fix "docs/**/*.md" || true
	@if command -v mdformat >/dev/null 2>&1; then \
		mdformat docs || true; \
	elif $(PY) -c "import mdformat" >/dev/null 2>&1; then \
		$(PY) -m mdformat docs || true; \
	else \
		echo "[md] mdformat not available; run 'make install'"; \
	fi
	@$(PY) scripts/fix_markdown.py || true

lint\:md\:fix: lint-md-fix

.PHONY: lint-md-fix-all lint\:md\:fix-all
lint-md-fix-all: lint-md-fix
	@echo "[md] fixing emphasis-as-headings (MD036)"
	@$(PY) scripts/fix_md_headings.py || true
	@if command -v mdformat >/dev/null 2>&1; then \
		mdformat docs || true; \
	elif $(PY) -c "import mdformat" >/dev/null 2>&1; then \
		$(PY) -m mdformat docs || true; \
	else \
		echo "[md] mdformat not available; run 'make install'"; \
	fi

lint\:md\:fix-all: lint-md-fix-all

.PHONY: footer
footer:
	@echo "[docs] Footer compliance"
	@if [ -f scripts/check_footer.py ]; then \
		$(PY) scripts/check_footer.py .; \
	elif [ -f .github/workflows/scripts/footer-check.js ]; then \
		$(NODE) .github/workflows/scripts/footer-check.js; \
	else \
		echo "[docs] footer script missing"; \
	fi

.PHONY: validate-json validate\:json
validate-json:
	@echo "[json] Schema validation"
	@if [ -f scripts/validate_json.py ]; then \
		$(PY) scripts/validate_json.py; \
	else \
		echo "[json] validation script missing"; \
	fi

validate\:json: validate-json

.PHONY: guardrails
guardrails:
	@echo "[guardrails] ROE + patterns"
	@if [ -f .github/workflows/scripts/roe-compliance.js ]; then \
		$(NODE) .github/workflows/scripts/roe-compliance.js; \
	else \
		echo "[guardrails] roe script missing"; \
	fi
	@if [ -f guardrails/patterns.json ]; then \
		echo "[guardrails] patterns present (manual review)"; \
	fi

.PHONY: evals evals\:adversarial
evals:
	@echo "[evals] Coverage gate (threshold $(COVERAGE_THRESHOLD)%)"
	@if [ -f .github/workflows/scripts/coverage-gate.js ]; then \
		if [ -f $(EVAL_DIR)/coverage-results.json ]; then \
			$(NODE) .github/workflows/scripts/coverage-gate.js $(EVAL_DIR)/coverage-results.json --threshold $(COVERAGE_THRESHOLD); \
		else \
			$(NODE) .github/workflows/scripts/coverage-gate.js --threshold $(COVERAGE_THRESHOLD); \
		fi; \
	else \
		echo "[evals] coverage script missing"; \
	fi
	$(MAKE) evals:adversarial

evals\:adversarial:
	@echo "[evals] adversarial suite"
	@$(PY) -c "print('[adversarial] stub -- plug your runner here')"

.PHONY: roe
roe:
	@echo "[roe] compliance"
	@if [ -f .github/workflows/scripts/roe-compliance.js ]; then \
		$(NODE) .github/workflows/scripts/roe-compliance.js; \
	else \
		echo "[roe] script missing"; \
	fi

.PHONY: badges
badges:
	@echo "[badges] updating"
	@if [ -f .github/workflows/scripts/update-badges.js ]; then \
		$(NODE) .github/workflows/scripts/update-badges.js; \
	else \
		echo "[badges] script missing"; \
	fi

.PHONY: prompts-sync prompts\:sync
prompts-sync:
	@echo "[prompts] syncing metadata"
	@$(PY) scripts/prompts_sync.py

prompts\:sync: prompts-sync

.PHONY: prompts-lint prompts\:lint
prompts-lint:
	@echo "[prompts] linting metadata"
	@$(PY) scripts/prompts_lint.py

prompts\:lint: prompts-lint

.PHONY: docs-summon docs\:summon
docs-summon:
	@echo "[docs] generating knowledge summon"
	@$(PY) scripts/mcp_knowledge_summon.py
	@$(MAKE) footer

docs\:summon: docs-summon

.PHONY: pr-summary pr\:summary
pr-summary:
	@echo "[pr] auto-summary"
	@if [ -f scripts/pr_summary.py ]; then \
		$(PY) scripts/pr_summary.py; \
	else \
		echo "[pr] summary script missing"; \
	fi

pr\:summary: pr-summary

.PHONY: pr-scan pr\:scan
pr-scan:
	@echo "[pr] impact scan (preview)"
	@if [ -f scripts/pr_summary.py ]; then \
		$(PY) scripts/pr_summary.py --no-post; \
	else \
		echo "[pr] summary script missing"; \
	fi

pr\:scan: pr-scan

.PHONY: protect-enable protect\:enable
protect-enable:
	@echo "[protect] enabling branch protection (requires admin token)"
	@if [ -f scripts/set_branch_protection.py ]; then \
		$(PY) scripts/set_branch_protection.py; \
	else \
		echo "[protect] helper script missing"; \
	fi

protect\:enable: protect-enable

.PHONY: ssh-auto ssh\:auto
ssh-auto:
	@echo "[ssh] auto setup (agent + test + tunnel + status)"
	@$(PY) scripts/ssh_auto.py all

ssh\:auto: ssh-auto

.PHONY: ssh-status ssh\:status
ssh-status:
	@echo "[ssh] connection status"
	@$(PY) scripts/ssh_auto.py status

ssh\:status: ssh-status

.PHONY: check
check: validate-json prompts-lint lint-md footer guardrails
	@echo "[check] aggregate checks finished"
