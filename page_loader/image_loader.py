"""Works with images"""
import os
import requests
from bs4 import BeautifulSoup
from page_loader.filename_changer import get_name, add_extension


def download_images(
        html: str,
        root: str,
        name: str,
        output: str,
        client=requests) -> str:
    """Parse html page and download found images"""
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('img')
    if items:
        dir_name = name + '_files'
        path = os.path.join(output, dir_name)
        os.mkdir(path)
        for item in items:
            image_path = item.get('src')
            if image_path.startswith('/'):
                image_name = get_name(root) + get_name(image_path)
                image_url = root + image_path
            else:
                image_url = image_path
                image_name = get_name(image_path)
            image_extension = image_url.split('.')[-1]
            full_image_name = add_extension(image_name, image_extension)
            full_image_path = os.path.join(path, full_image_name)
            content = get_content(image_url, client)
            save_image(full_image_path, content)
            image_local_path = os.path.join(dir_name, full_image_name)
            change_image_path(image_local_path, item)
    updated_html = soup.prettify()
    return updated_html


def save_image(full_path: str, content: bytes) -> None:
    """Saves the image locally"""
    with open(full_path, 'wb') as file:
        file.write(content)


def change_image_path(local_path: str, item) -> None:
    """Changes the image link to a local path"""
    item['src'] = local_path


def get_content(link: str, client=requests) -> bytes:
    """Gets the image in bytes"""
    response = client.get(link)
    return response.content
