import os
import pytest
import tempfile
from bs4 import BeautifulSoup
from page_loader.html_changer import (
    change_file_path,
    change_html,
    create_file_info,
    get_file_path,
    get_items
)

content = b'123213testtest'
root = 'https://ru.hexlet.io'


class FakeClient:
    def __init__(self, content, text, status_code):
        self.content = content
        self.text = text
        self.status_code = status_code

    def get(self, link):
        return self


@pytest.fixture()
def soup_fixture():
    with open('tests/fixtures/before.html') as file:
        html = file.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def test_change_html(soup_fixture):
    text = 'test text'
    image_name = 'ru-hexlet-io-assets-professions-nodejs.png'
    html = soup_fixture.prettify()
    name = 'ru-hexlet-io-courses'
    dir_name = name + '_files'
    with open('tests/fixtures/after.html') as file:
        after = file.read()
    with tempfile.TemporaryDirectory() as tmpdirname:
        updated_html = change_html(
            html,
            root,
            name,
            tmpdirname,
            client=FakeClient(content, text, 200))
        path = os.path.join(tmpdirname, dir_name)
        full_image_path = os.path.join(path, image_name)
        assert updated_html == after
        assert os.path.exists(os.path.join(tmpdirname, dir_name))
        with open(full_image_path, 'rb') as file:
            image_content = file.read()
        assert os.path.isfile(full_image_path)
        assert image_content == content


def test_change_file_path(soup_fixture):
    soup = soup_fixture
    image = soup.find('img')
    new_path = '/local/dir/123.png'
    change_file_path(new_path, image)
    assert image.get('src') == new_path


def test_get_file_path(soup_fixture):
    soup = soup_fixture
    tag = soup.img
    path = tag.get('src')
    assert get_file_path(tag, root) == path


def test_get_items(soup_fixture):
    soup = soup_fixture
    items = soup.find_all(['img', 'script', 'link'])
    assert get_items(soup) == items


def test_create_file_info():
    path = '/var/tmp/'
    file_path = '/content/25.jpg'
    result = {
        'path': '/var/tmp/ru-hexlet-io-content-25.jpg',
        'name': 'ru-hexlet-io-content-25.jpg',
        'url': 'https://ru.hexlet.io/content/25.jpg'
    }
    assert create_file_info(path, root, file_path) == result
