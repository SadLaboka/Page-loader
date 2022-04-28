"""Works with filenames"""
import re
from page_loader.constants import EXTENSIONS


def get_name(link: str) -> str:
    """Creates a filename from a link"""
    cleaned_link = delete_extension(link)
    pattern = r'(?<=\:\/\/).*'
    host_and_path = re.search(pattern, cleaned_link)
    if host_and_path:
        host_and_path = host_and_path.group(0)
        host_and_path = remove_trailing_slash(host_and_path)
    else:
        host_and_path = cleaned_link
    pattern = r'[^a-zA-Z0-9]'
    name = re.sub(pattern, "-", host_and_path)
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
    return '.'.join([filename, extension])
