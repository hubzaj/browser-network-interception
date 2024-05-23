import os
from unittest import mock

from browser_hz import Browsers

from network.config.configuration import Configuration


@mock.patch.dict(os.environ, clear=True)
def test_default_configuration() -> None:
    config: Configuration = Configuration()
    assert config.browser == Browsers.CHROME
