# Makefile for testing-tricks Python project

.PHONY: help install test coverage pre-commit clean lint format

help:
	@echo "Available targets:"
	@echo "  install     Install project dependencies and pre-commit hooks"
	@echo "  lint        Run all pre-commit lint hooks"
	@echo "  format      Run all pre-commit formatting hooks"
	@echo "  test        Run pytest tests"
	@echo "  coverage    Run pytest with coverage report"
	@echo "  pre-commit  Run all pre-commit hooks on all files"
	@echo "  clean       Remove Python cache and build artifacts"

install:
	uv venv .venv
	uv run pip install pre-commit
	uv run pre-commit install

lint:
	uv run pre-commit run --hook-stage=manual --all-files --show-diff-on-failure --color=always --hook-type=pre-commit

format:
	uv run pre-commit run --hook-stage=manual --all-files --show-diff-on-failure --color=always --hook-type=pre-commit

test:
	uv run pytest

coverage:
	uv run pytest --cov=.

pre-commit:
	uv run pre-commit run --all-files

clean:
	git clean -xfd
	git clean -Xfd
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -delete
