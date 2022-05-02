"""Download content from a web page and save it to a files"""
import os
from page_loader.filename_changer import get_name, add_extension
from page_loader.file_saver import save_file
from page_loader.html_changer import change_html
from page_loader.http_request import get_request


def download(link: str, output: str):
    """Downloads web-page"""
    html = get_request(link, 'text')
    page_name = get_name(link)
    updated_html = change_html(html, link, page_name, output)
    filename = add_extension(page_name, 'html')
    full_path = os.path.join(output, filename)
    save_file(updated_html, full_path)
    return full_path
