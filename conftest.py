import os.path
from pathlib import Path

import pytest
from _pytest.fixtures import fixture

from network.keywords.browser import BrowserKeywords
from network.report.pytest_report import PytestReportConfig, pytest_publish_report


def pytest_configure(config: pytest.Config):
    """
    [https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest.hookspec.pytest_configure]

    :param config:
    :return:
    """
    results_dir: str = os.path.join(config.rootpath, PytestReportConfig.dir_name)
    config.option.report = [os.path.join(results_dir, PytestReportConfig.report_name)]
    config.option.template_dir = str(config.rootpath)
    config.option.template = [PytestReportConfig.template]


def pytest_sessionfinish(session: pytest.Session, exitstatus: pytest.ExitCode):
    """
    [https://docs.pytest.org/en/latest/reference/reference.html#pytest.hookspec.pytest_sessionfinish]

    :param session:
    :param exitstatus:
    :return:
    """
    pytest_publish_report(str(session.fspath))


@fixture
def browser_keywords(tmp_path: Path) -> BrowserKeywords:
    yield BrowserKeywords(tmp_path)
