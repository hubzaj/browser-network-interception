from selenium.webdriver.common.by import By

from network.banner.default import BannerAd
from network.keywords.browser_keywords import BrowserKeywords


class TestExample:

    def test_example(self, browser_keywords: BrowserKeywords):
        # Given
        ad: BannerAd = BannerAd.REGULAR_AD

        # When
        browser_keywords.display_ad_and_get_network_traffic(
            ad=ad,
            click_locator=(By.ID, ad.get_ad_click_id_locator()),
            # Then
            requests_paths_to_wait=[
                ad.get_dsp_notification_url(),
                ad.get_click_redirection_url()
            ],
        )
