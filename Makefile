bootstrap:
	./bootstrap.sh

test:
	pytest

run:
	sysmgr scan

lint:
	ruff check src

format:
	black src tests
