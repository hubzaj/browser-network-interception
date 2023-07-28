import os

from browser import BrowserType

from network.utils.singleton_meta import SingletonMeta


class Configuration(metaclass=SingletonMeta):
    browser_type: BrowserType = None

    def __init__(self) -> None:
        self.browser_type = self.__load_browser_type()

    @staticmethod
    def __load_browser_type() -> BrowserType:
        if browser_type := os.getenv("BROWSER"):
            return BrowserType.get_browser(browser_type)
        else:
            return BrowserType.CHROME
