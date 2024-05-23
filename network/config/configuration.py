import os
from logging import Logger, getLogger

from browser_hz import Browsers

from network.utils.singleton_meta import SingletonMeta

LOGGER: Logger = getLogger(__name__)


class Configuration(metaclass=SingletonMeta):
    browser: Browsers = None

    def __init__(self) -> None:
        self.browser = self.__load_browser_type()

    @staticmethod
    def __load_browser_type() -> Browsers:
        LOGGER.info('Loading configuration [BROWSER]')
        if browser_type := os.getenv("BROWSER"):
            return Browsers.get_browser(browser_type)
        return Browsers.CHROME
