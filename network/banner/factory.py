from pathlib import Path

from network.banner.default import BannerAd
from network.utils.file import create_file

__HTML_PREFIX: str = '<!DOCTYPE html><head><title></title></head><html><body>'
__HTML_SUFFIX: str = '</body></html>'

__HTML_AD_SLOT_PREFIX: str = '<div id="ad_slot">'
__HTML_AD_SLOT_SUFFIX: str = '</div>'


def create_html_page_with_ad(ad_html: str, directory: Path) -> Path:
    ad_in_page_slot = ''.join([__HTML_AD_SLOT_PREFIX, ad_html, __HTML_AD_SLOT_SUFFIX])
    page_with_ad_in_slot = ''.join([__HTML_PREFIX, ad_in_page_slot, __HTML_SUFFIX])
    return create_file(
        directory=directory,
        file_name='page_with_ad.html',
        data=page_with_ad_in_slot
    )


def create_html_page_with_default_ad(ad: BannerAd, directory: Path) -> Path:
    return create_html_page_with_ad(ad.get_ad_snippet(), directory)
