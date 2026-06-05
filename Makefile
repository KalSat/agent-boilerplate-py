.PHONY: format lint test run sync

sync:
	uv sync

format:
	uv run ruff format src tests
	uv run ruff check src tests --fix

lint:
	uv run ruff check src tests

type-check:
	uv run mypy

check: lint type-check

test:
	uv run pytest

run:
	uv run python -m agent_boilerplate.main
