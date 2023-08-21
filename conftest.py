import os.path
from pathlib import Path

import pytest
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


@fixture
def browser_keywords(tmp_path: Path) -> BrowserKeywords:
    yield BrowserKeywords(tmp_path)
