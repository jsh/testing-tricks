# Makefile for testing-tricks Python project

.PHONY: help all
PRE_COMMIT_ARGS := --hook-stage=manual --all-files --show-diff-on-failure --color=always
PYTHON_SOURCE := $(wildcard *.py tests/*.py)

help:
	@echo "Available targets:"
	@echo "  help        Print this message"
	@echo "  all         All targets except 'clean'"
	@echo "  install     Install project dependencies and pre-commit hooks"
	@echo "  lint        Run all pre-commit lint hooks"
	@echo "  format      Run all pre-commit formatting hooks"
	@echo "  test        Run pytest tests, including coverage report"
	@echo "  mutmut      Run mutation tests"
	@echo "  pre-commit  Run all pre-commit hooks on all files"
	@echo "  clean       Remove Python cache and build artifacts"

.PHONY: all clean

all: pre-commit

install: uv.lock .git/hooks/pre-commit .pre-commit-config.yaml
	uv sync
	uv run pre-commit install
	touch install

lint: install ${PYTHON_SOURCE}
	uv run pre-commit run ${PRE_COMMIT_ARGS} ruff-check
	touch lint

format: lint
	git add .
	uv run pre-commit run ${PRE_COMMIT_ARGS} ruff-format
	touch format

test: format
	uv run pytest
	touch test

pre-commit: test
	uv run pre-commit run ${PRE_COMMIT_ARGS} --all-files
	touch pre-commit

mutmut: test
	uv run mutmut run
	touch mutmut

clean:
	git clean -dfx -e .venv
