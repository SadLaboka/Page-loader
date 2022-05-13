"""Works with filenames"""
import re
from page_loader.constants import EXTENSIONS
from urllib.parse import urlparse


def get_name(link: str) -> str:
    """Creates a filename from a link"""
    cleaned_link = delete_extension(link)
    url = urlparse(cleaned_link)
    if url.scheme:
        path = f'{url.netloc}{url.path}'
    else:
        path = url.path
    pattern = r'[^a-zA-Z0-9]'
    name = re.sub(pattern, "-", path)
    return name


def delete_extension(link: str) -> str:
    """Removes the extension at the end of the link"""
    split = link.split('.')
    if split[-1] in EXTENSIONS:
        split.pop()
    return '.'.join(split)


def remove_trailing_slash(host_and_path: str) -> str:
    """Removes the trailing slash, if any"""
    if host_and_path[-1] == '/':
        return host_and_path[:-1]
    else:
        return host_and_path


def add_extension(filename: str, extension: str) -> str:
    """Adds extension to filename"""
    if '?' in extension:
        extension = extension.split('?')[0]
    return '.'.join([filename, extension])


def get_root(link: str) -> str:
    """Gets link on host"""
    url = urlparse(link)
    scheme = url.scheme
    netloc = url.netloc
    return f'{scheme}://{netloc}'


def get_path_from_link(link: str) -> str:
    """Gets path from full link"""
    url = urlparse(link)
    return url.path
