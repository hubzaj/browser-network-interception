install-dependencies:
	poetry install

run-all-tests-in-parallel:
	poetry run pytest -n auto

run-browser-tests-in-parallel:
	poetry run pytest -n auto -m browser
