from pathlib import Path

from network.utils.file import create_file
from .default import BannerAd

__HTML_PREFIX: str = '<!DOCTYPE html><head><title></title></head><html><body>'
__HTML_SUFFIX: str = '</body></html>'

__HTML_FRAME_PREFIX: str = ''
__HTML_FRAME_SUFFIX: str = ''


def create_html_page_with_ad(ad_html: str, directory: Path) -> Path:
    ad_in_frame = ''.join([__HTML_FRAME_PREFIX, ad_html, __HTML_FRAME_SUFFIX])
    page_with_ad_in_frame = ''.join([__HTML_PREFIX, ad_in_frame, __HTML_SUFFIX])
    return create_file(
        directory=directory,
        file_name='page_with_ad.html',
        data=page_with_ad_in_frame
    )


def create_html_page_with_default_ad(ad: BannerAd, directory: Path) -> Path:
    return create_html_page_with_ad(ad.get_ad_snippet(), directory)
