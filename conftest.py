import os.path
from pathlib import Path

import pytest
import time
from _pytest.fixtures import fixture

from network.keywords.browser import BrowserKeywords


def pytest_configure(config: pytest.Config):
    """
    [https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest.hookspec.pytest_configure]

    :param config:
    :return:
    """
    results_dir: str = os.path.join(config.rootpath, 'results')
    config.option.report = [os.path.join(results_dir, 'pytest_report.html')]
    config.option.template_dir = str(config.rootpath)
    config.option.template = ['html1/index.html']


def pytest_sessionfinish(session, exitstatus):
    """
    [https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_sessionfinish]

    :param session:
    :param exitstatus:
    :return:
    """
    __publish_pytest_report(session.fspath)


@fixture
def browser_keywords(tmp_path: Path) -> BrowserKeywords:
    yield BrowserKeywords(tmp_path)


def __publish_pytest_report(project_root_dir: str) -> None:
    pytest_report_path: str = os.path.join(project_root_dir, 'results', 'pytest_report.html')

    while not os.path.exists(pytest_report_path):
        time.sleep(0.1)

    if os.path.isfile(pytest_report_path):
        # TODO: Publish test report to the QA related bucket (e.g. GCS, S3)
        print('\nReport has been published to [GCS_PATH] bucket within [GCP_PROJECT]\n')
        pass
    else:
        raise Exception(f'[{pytest_report_path}] is not a valid file path')
