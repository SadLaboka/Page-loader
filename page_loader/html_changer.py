import bs4.element
import logging
import os
import re
import requests
import sys
from bs4 import BeautifulSoup
from page_loader.filename_changer import (
    add_extension, get_name, get_root, get_path_from_link
)
from page_loader.network import get_request
from page_loader.storage import make_dir, save_file, StorageException

logger = logging.getLogger("best_logger")


def change_html(
        html: str,
        link: str,
        name: str,
        output: str,
        client=requests) -> str:
    """Parse html page, downloads files and changes html"""
    soup = BeautifulSoup(html, 'html.parser')
    root = get_root(link)
    tags = get_tags(soup, root)

    if tags:
        dir_name = name + '_files'
        path = os.path.join(output, dir_name)
        try:
            make_dir(path)
        except StorageException as error:
            logger.error(error, exc_info=sys.exc_info())

        change_links_to_local(tags, dir_name, path, root, client)

    updated_html = soup.prettify()
    return updated_html


def create_file_info(path: str,
                     root: str,
                     tag: bs4.element.Tag) -> dict:
    """Creates the url, path and name of a file"""
    file_link = get_file_link(tag, root)
    file_name = get_name(root) + get_name(file_link)
    url = root + file_link
    if '.' in file_link:
        extension = file_link.split('.')[-1]
    else:
        extension = 'html'
    full_file_name = add_extension(file_name, extension)
    full_path = os.path.join(path, full_file_name)
    file_info = {
        'path': full_path,
        'name': full_file_name,
        'url': url
    }
    return file_info


def change_links_to_local(
        tags: list, dir_name: str, path: str, root: str, client
):
    """Saves a static files from a tags locally.
    Changes the links of a static files in a tags to a local paths"""
    for tag in tags:
        file_info = create_file_info(path, root, tag)
        content = get_request(
            file_info.get('url'),
            client
        )
        try:
            save_file(content, file_info.get('path'))
        except StorageException as err:
            logger.error(err, exc_info=sys.exc_info())
        file_local_path = os.path.join(
            dir_name,
            file_info.get('name'))

        if tag.get('src'):
            tag['src'] = file_local_path
        elif tag.get('href'):
            tag['href'] = file_local_path


def get_tags(soup: bs4.BeautifulSoup, root: str) -> list:
    """Gets list of desired tags"""
    items = soup.find_all(['img', 'script', 'link'])
    tags = []
    for tag in items:
        if is_third(tag, root):
            tags.append(tag)

    return tags


def is_third(tag: bs4.element.Tag, root: str) -> bool:
    """Checks if files are on a third party host"""
    re_pattern = r'^/{1}[a-zA-Z0-9]'
    file_link = get_file_link(tag, root)
    if file_link.startswith(root):
        return True
    elif re.match(re_pattern, file_link):
        return True
    return False


def remove_root(tag: bs4.element.Tag, attr: str) -> None:
    """Removes root from link in a tag"""
    link = tag.get(attr)
    path = get_path_from_link(link)
    tag[attr] = path


def get_file_link(tag: bs4.element.Tag, root: str) -> str:
    """Gets file-link from a tag"""
    for attr in ('href', 'src'):
        if tag.has_attr(attr):
            link = tag.get(attr)
            if link.startswith(root):
                remove_root(tag, attr)
            return tag.get(attr)
    return ''
