from enum import Enum
from string import Template


class BannerAd(Enum):
    REGULAR_AD = Template(
        """
        <div id="dsp_display_ad_notification" style="position:absolute;left:0px;visibility:hidden;">
            <img src="$dsp_notification_url">
        </div>
        """
    )

    def get_ad_snippet(self) -> str:
        return self.value.safe_substitute(
            dsp_notification_url=self.get_dsp_notification_url()
        )

    @staticmethod
    def get_dsp_notification_url() -> str:
        return 'http://dsp.mock.url.org/win?partner=test_partner'
