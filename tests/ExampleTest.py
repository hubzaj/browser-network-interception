from pathlib import Path

from selenium.webdriver.common.by import By

from browser import open_browser
from network.banner.default import BannerAd
from network.banner.factory import create_html_page_with_default_ad
from network.config.configuration import Configuration
from network.web_server.server import WebServer

config: Configuration = Configuration()


def test_example(tmp_path: Path):
    # Given
    ad: BannerAd = BannerAd.REGULAR_AD
    page_path: Path = create_html_page_with_default_ad(ad=ad, directory=tmp_path)

    with open_browser(config.browser_type) as browser:
        with WebServer(directory=page_path) as tmp_server:
            # When
            browser \
                .open_page(url=tmp_server.get_url()) \
                .wait_for_requests(requests_paths_to_wait=[ad.get_dsp_notification_url()]) \
                .click((By.ID, ad.get_ad_click_id_locator())) \
                .wait_for_requests(requests_paths_to_wait=[ad.get_click_redirection_url()]) \
                .close_newly_opened_tab()
