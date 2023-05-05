from enum import Enum
from string import Template


class BannerAd(Enum):
    REGULAR_AD = Template(
        """
        $win_notification_snippet
        $click_tracking_snippet
        """
    )

    def get_ad_snippet(self) -> str:
        return self.value.safe_substitute(
            win_notification_snippet=self.__get_win_notification_snippet(),
            click_tracking_snippet=self.__replace_click_url_macro(
                self.__get_click_tracking_snippet()
            )
        )

    @staticmethod
    def get_dsp_notification_url() -> str:
        return 'http://dsp.mock.url.org/win?partner=test_partner'

    @staticmethod
    def get_click_redirection_url() -> str:
        return 'http://ssp.mock.url.org/record?event=click&r=https://www.bmw.pl'

    @staticmethod
    def get_ad_click_id_locator() -> str:
        """
        ID locator [By.ID] required by Selenium in order to click on the AD area
        :return:
        """
        return 'test_banner_ad'

    def __get_win_notification_snippet(self) -> str:
        """
        Win snippet is responsible for sending notification about impression for example to DSP
        :return:
        """
        return Template(
            """
            <div id="dsp_display_ad_notification" style="position:absolute;left:0px;visibility:hidden;">
                <img src="$dsp_notification_url">
            </div>
            """
        ).safe_substitute(
            dsp_notification_url=self.get_dsp_notification_url(),
        )

    @classmethod
    def __get_click_tracking_snippet(cls) -> str:
        """
        {clickurl} is a macro which SSP replaces during ad delivery
        based on: https://support.google.com/admanager/answer/2376981?hl=en
        :return:
        """
        return Template(
            """
            <a target="_blank" href="{clickurl}">
                <img id="$id" src="$image_src">
            </a>
            """
        ).safe_substitute(
            id=cls.get_ad_click_id_locator(),
            image_src='https://drive.google.com/file/d/1RJ6-oCLeMdaBbhxiH_k53AwagTtpwO4W/view?usp=share_link'
        )

    @classmethod
    def __replace_click_url_macro(cls, click_tracking_snippet: str) -> str:
        """
        Simulate SSP which is responsible for replacement of such macros
        :return:
        """
        return click_tracking_snippet.replace('{clickurl}', cls.get_click_redirection_url())
