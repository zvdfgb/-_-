#!/usr/bin/env bash
set -e

echo "[1/3] Checking code formatting with ruff format..."
ruff format --check .

echo "[2/3] Checking code linter with ruff check..."
ruff check .

echo "[3/3] Running test suite with pytest..."
pytest -v

echo ">>> All quality checks PASSED successfully! <<<"
