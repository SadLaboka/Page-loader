"""Works with files and their paths"""
import os

import bs4.element
import requests
from bs4 import BeautifulSoup
from page_loader.filename_changer import (
    get_name,
    get_path_from_link,
    get_root,
    add_extension
)
from page_loader.file_saver import save_file
from page_loader.http_request import get_request


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
    if items:
        dir_name = name + '_files'
        path = os.path.join(output, dir_name)
        os.mkdir(path)

        for item in items:
            file_path = get_file_path(item, root)
            if file_path.startswith('/'):
                file_info = create_file_info(path, root, file_path)
                content = get_request(
                    file_info.get('url'),
                    'byte', client)
                save_file(content, file_info.get('path'))
                file_local_path = os.path.join(
                    dir_name,
                    file_info.get('name'))
                change_file_path(file_local_path, item)

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
