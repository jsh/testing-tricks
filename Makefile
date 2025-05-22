# Makefile for testing-tricks Python project

.PHONY: help test coverage pre-commit clean lint format
PRE_COMMIT_ARGS := --hook-stage=manual --all-files --show-diff-on-failure --color=always

help:
	@echo "Available targets:"
	@echo "  install     Install project dependencies and pre-commit hooks"
	@echo "  lint        Run all pre-commit lint hooks"
	@echo "  format      Run all pre-commit formatting hooks"
	@echo "  test        Run pytest tests"
	@echo "  coverage    Run pytest with coverage report"
	@echo "  prettier    Run pre-commit hook 'prettier' on all files"
	@echo "  pre-commit  Run all pre-commit hooks on all files"
	@echo "  clean       Remove Python cache and build artifacts"

install: uv.lock .git/hooks/pre-commit .pre-commit-config.yaml
	uv sync
	uv run pre-commit install
	touch install

lint: install
	uv run pre-commit run ${PRE_COMMIT_ARGS} ruff-check

format: install
	uv run pre-commit run ${PRE_COMMIT_ARGS} ruff-format

test: install
	uv run pytest

coverage: install
	uv run pytest --cov=.

prettier: install
	uv run pre-commit run ${PRE_COMMIT_ARGS} prettier --all-files

pre-commit: install
	uv run pre-commit run ${PRE_COMMIT_ARGS} --all-files

clean:
	git clean -dfx -e .venv
