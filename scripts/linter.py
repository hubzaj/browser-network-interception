import subprocess


def run_linters() -> None:
    subprocess.run(
        ['poetry', 'run', 'flake8']
    )
    subprocess.run(
        ['poetry', 'run', 'mypy', 'src', 'tests', 'scripts']
    )
