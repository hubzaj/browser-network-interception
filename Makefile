help:
	@echo "[install-deps] - install project dependencies (managed by poetry)"
	@echo "[lint] - check style with flake8 and mypy"
	@echo "[clean-pyc] - clean python cached files (e.g. *.pyc)"
	@echo "[run-all-tests-in-parallel] - run all tests in parallel"
	@echo "[run-browser-tests-in-parallel] - run all test marked with browser tag in parallel"

install-deps:
	poetry install

lint: flake8 mypy
	@echo LINT complited

flake8:
	poetry run flake8

mypy:
	poetry run mypy network tests

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

run-all-tests-in-parallel:
	PYTHONPATH=. poetry run pytest -n auto

run-browser-tests-in-parallel:
	PYTHONPATH=. poetry run pytest -n auto -m browser
