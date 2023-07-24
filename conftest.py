from pathlib import Path

from _pytest.fixtures import fixture

from src.keywords.browser import BrowserKeywords


@fixture
def browser_keywords(tmp_path: Path) -> BrowserKeywords:
    yield BrowserKeywords(tmp_path)
