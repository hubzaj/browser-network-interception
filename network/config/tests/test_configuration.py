import os
from unittest import mock

import pytest
from browser_hz import BrowserType

from network.config.configuration import Configuration


@mock.patch.dict(os.environ, clear=True)
def test_default_configuration() -> None:
    config: Configuration = Configuration()
    assert config.browser == BrowserType.CHROME


@mock.patch.dict(os.environ, {"BROWSER": "CHROME_HEADLESS"})
@pytest.mark.skip('TODO: Fixme - Configuration instance is created before env mock is set')
def test_non_default_configuration() -> None:
    config: Configuration = Configuration()
    assert config.browser == BrowserType.CHROME_HEADLESS
