"""Download content from a web page and save it to a file"""
import os
import requests
from page_loader.filename_changer import get_name, add_extension


def download(link: str, output: str):
    content = get_content(link)
    page_name = get_name(link)
    filename = add_extension(page_name, 'html')
    full_path = os.path.join(output, filename)
    with open(full_path, 'w') as file:
        file.write(content)
    return full_path


def get_content(link: str) -> str:
    """Gets content from web-page"""
    response = requests.get(link)
    text = response.text
    return text
