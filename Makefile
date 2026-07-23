.PHONY: bootstrap install test lint format clean run

bootstrap:
	./bootstrap.sh

install:
	pip install -e .

test:
	pytest

run:
	sysmgr scan

lint:
	ruff check src tests

format:
	black src tests

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache
	rm -rf build dist
