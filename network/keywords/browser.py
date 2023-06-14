from pathlib import Path

from selenium.webdriver.common.by import By
from seleniumwire.request import Request

from browser import open_browser
from network.banner.default import BannerAd
from network.banner.factory import create_html_page_with_default_ad
from network.config.configuration import Configuration
from network.web_server.server import WebServer

config: Configuration = Configuration()


class BrowserKeywords:

    def __init__(self, path: Path) -> None:
        self.__tmp_path: Path = path

    def display_ad_and_get_network_traffic(self,
                                           ad: BannerAd,
                                           requests_paths_to_wait: list[str] = None,
                                           click_locator: (By, str) = None) -> list[Request]:
        page_path: Path = create_html_page_with_default_ad(ad=ad, directory=self.__tmp_path)

        with open_browser(config.browser_type) as browser:
            with WebServer(directory=page_path) as server:
                browser.open_page(url=server.get_url())
                if click_locator:
                    with browser.click_with_redirect_to_new_tab(locator=click_locator):
                        pass
                return browser.get_network_traffic(requests_paths_to_wait=requests_paths_to_wait)
