"""Works with files and their paths"""
import logging
import os
import re
import sys

import bs4.element
import requests
from bs4 import BeautifulSoup
from page_loader.filename_changer import (
    get_name,
    get_path_from_link,
    get_root,
    add_extension
)
from page_loader.storage import make_dir, save_file, StorageException
from page_loader.network import get_request

logger = logging.getLogger("best_logger")


def change_html(
        html: str,
        link: str,
        name: str,
        output: str,
        client=requests) -> str:
    """Parse html page, downloads files and changes html"""
    soup = BeautifulSoup(html, 'html.parser')
    items = get_items(soup)
    root = get_root(link)
    re_pattern = r'^/{1}[a-zA-Z0-9]'
    if items:
        dir_name = name + '_files'
        path = os.path.join(output, dir_name)
        try:
            make_dir(path)
        except StorageException as error:
            logger.error(error, exc_info=sys.exc_info())

        for item in items:
            file_path = get_file_path(item, root)
            if re.match(re_pattern, file_path):
                change_item_to_local(
                    file_path, dir_name, path, root, item, client
                )

    updated_html = soup.prettify()
    return updated_html


def change_file_path(local_path: str, item: bs4.element.Tag) -> None:
    """Changes the file link to a local path"""
    if item.get('src'):
        item['src'] = local_path
    elif item.get('href'):
        item['href'] = local_path


def get_items(soup: BeautifulSoup) -> bs4.element.ResultSet:
    """Gets a list of elements with the desired tags"""
    tag_list = ['img', 'script', 'link']
    items = soup.find_all(tag_list)
    return items


def get_file_path(item: bs4.element.Tag, root: str) -> str:
    """Gets relative file path from html-tag"""
    if item.get('src'):
        file_path = item['src']
    elif item.get('href'):
        file_path = item['href']
    else:
        file_path = ''
    if file_path.startswith(root):
        file_path = get_path_from_link(file_path)
    return file_path


def create_file_info(path: str,
                     root: str,
                     file_path: str) -> dict:
    """Creates the url, path and name of a file"""
    file_name = get_name(root) + get_name(file_path)
    url = root + file_path
    if '.' in file_path:
        extension = file_path.split('.')[-1]
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


def change_item_to_local(
        file_path: str,
        dir_name: str,
        path: str,
        root: str,
        item: bs4.element.Tag,
        client):
    """Saves a static file from a tag locally.
    Changes the link of a static file in a tag to a local path"""
    file_info = create_file_info(path, root, file_path)
    content = get_request(
        file_info.get('url'),
        client)
    try:
        save_file(content, file_info.get('path'))
    except StorageException as err:
        logger.error(err, exc_info=sys.exc_info())
    file_local_path = os.path.join(
        dir_name,
        file_info.get('name'))
    change_file_path(file_local_path, item)
