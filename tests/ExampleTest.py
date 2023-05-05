from pathlib import Path

from browser import open_browser
from browser.browser_type import BrowserType
from network.banner.default import BannerAd
from network.banner.factory import create_html_page_with_default_ad
from network.web_server.server import WebServer


def test_example(tmp_path: Path):
    # Given
    ad: BannerAd = BannerAd.REGULAR_AD
    page_path: Path = create_html_page_with_default_ad(ad=ad, directory=tmp_path)

    with open_browser(BrowserType.CHROME) as browser:
        with WebServer(directory=page_path) as tmp_server:
            # When
            requests = browser.open_page(
                url=tmp_server.get_url(),
                # Then
                requests_paths_to_wait=[
                    ad.get_dsp_notification_url()
                ]
            )
