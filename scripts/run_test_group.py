import subprocess

RUN_ALL_TESTS_IN_PARALLEL_CMD: list[str] = ['pytest', '--template=html1/index.html --report=report.html', '-n', 'auto']


def run_all_tests_in_parallel(params: list[str] | None = None) -> None:
    subprocess.run(
        RUN_ALL_TESTS_IN_PARALLEL_CMD + params if params else RUN_ALL_TESTS_IN_PARALLEL_CMD, check=True
    )


def run_e2e_web_browser_tests_in_parallel() -> None:
    run_all_tests_in_parallel(['-m', 'network'])
