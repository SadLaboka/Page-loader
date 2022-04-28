"""Download content from a web page and save it to a file"""
import os
import re
import requests
from page_loader.filename_changer import get_name, add_extension
from page_loader.image_loader import download_images


def download(link: str, output: str):
    html = get_html(link)
    page_name = get_name(link)
    root = get_root(link)
    updated_html = download_images(html, root, page_name, output)
    filename = add_extension(page_name, 'html')
    full_path = os.path.join(output, filename)
    with open(full_path, 'w') as file:
        file.write(updated_html.rstrip())
    return full_path


def get_root(link: str) -> str:
    """Gets link on host"""
    pattern1 = r'(?<=\:\/\/).*(?=/)'
    pattern2 = r'(?<=\:\/\/).*'
    path = re.search(pattern1, link)
    if path:
        return path.group(0)
    else:
        path = re.search(pattern2, link)
        return path.group(0)


def get_html(link: str) -> str:
    """Gets html from web-page"""
    response = requests.get(link)
    text = response.text
    return text
