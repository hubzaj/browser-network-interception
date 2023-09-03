import subprocess


def run_linters() -> None:
    subprocess.run(
        ['poetry', 'run', 'mypy'], check=True
    )
    subprocess.run(
        ['poetry', 'run', 'pylint', 'network', 'tests', 'scripts'], check=True
    )
