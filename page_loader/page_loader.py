"""Download content from a web page and save it to a file"""
import os
import re
import requests
from page_loader.constants import EXTENSIONS


def download(link: str, output: str):
    content = get_content(link)
    link = delete_extension(link)
    name = get_name(link)
    filename = name + '.html'
    full_path = os.path.join(output, filename)
    with open(full_path, 'w') as file:
        file.write(content)
    return full_path


def get_content(link: str) -> str:
    """Gets content from web-page"""
    response = requests.get(link)
    text = response.text
    return text


def get_name(link: str) -> str:
    """Creates a filename from a link"""
    pattern = r'(?<=\:\/\/).*'
    host_and_path = re.search(pattern, link)
    host_and_path = host_and_path.group(0)
    pattern = r'[^a-zA-Z0-9]'
    name = re.sub(pattern, "-", host_and_path)
    return name


def delete_extension(link: str) -> str:
    """Removes the extension at the end of the link"""
    split = link.split('.')
    if split[-1] in EXTENSIONS:
        split.pop()
    return '.'.join(split)
