import subprocess


def run_e2e_web_browser_tests() -> None:
    subprocess.run(
        ['pytest', '-n', 'auto', '-m', 'browser']
    )
