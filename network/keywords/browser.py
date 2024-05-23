from logging import Logger, getLogger
from pathlib import Path
from typing import Union, Tuple

from browser_hz import open_browser
from seleniumwire.request import Request

from network.banner.default import BannerAd
from network.banner.factory import create_html_page_with_default_ad
from network.config.configuration import Configuration
from network.web_server.server import WebServer

CONFIG: Configuration = Configuration()
LOGGER: Logger = getLogger(__name__)


class BrowserActions:

    def __init__(self, path: Path) -> None:
        self.__tmp_path: Path = path

    def display_ad_and_get_network_traffic(self,
                                           ad: BannerAd,
                                           requests_paths_to_wait: Union[list[str], None] = None,
                                           click_locator: Union[Tuple[str, str], None] = None) -> list[Request]:
        page_path: Path = create_html_page_with_default_ad(ad=ad, directory=self.__tmp_path)
        with open_browser(CONFIG.browser) as browser:
            with WebServer(page_path) as server:
                browser.open_page(server.get_url())
                if click_locator:
                    with browser.click_with_redirect_to_new_tab(click_locator):
                        LOGGER.info('The ad has been clicked')
                return browser.get_network_helpers().get_network_traffic(requests_paths_to_wait)
