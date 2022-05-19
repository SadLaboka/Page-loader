"""Download content from a web page and save it to a files"""
import logging.config
import os

from page_loader.filename_changer import get_name, add_extension
from page_loader.storage import save_file
from page_loader.html_changer import change_html
from page_loader.network import get_request

logger = logging.getLogger("best_logger")


def download(link: str, output: str):
    """Downloads web-page"""

    html = get_request(link).decode()

    page_name = get_name(link)
    updated_html = change_html(html, link, page_name, output)
    filename = add_extension(page_name, 'html')
    full_path = os.path.join(output, filename)

    save_file(bytes(updated_html, 'utf-8'), full_path)
    return full_path
