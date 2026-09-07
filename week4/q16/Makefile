.PHONY: all check build clean

all: check build

check:
	bash check.sh

build:
	python3 -m build --wheel

clean:
	rm -rf dist build src/*.egg-info .pytest_cache .ruff_cache
