import os
import pytest
import tempfile
from bs4 import BeautifulSoup
from page_loader.html_changer import (
    change_html,
    create_file_info,
    get_tags,
    is_third,
    get_file_link,
    remove_root
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

    def raise_for_status(self):
        return


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


def test_get_tags(soup_fixture):
    soup = soup_fixture
    items = soup.find_all(['img', 'script', 'link'])
    result_list = [items[1], items[2], items[3], items[5]]
    assert get_tags(soup, root) == result_list


def test_create_file_info(soup_fixture):
    tag = soup_fixture.find('img')
    path = '/var/tmp/'
    result = {
        'path': '/var/tmp/ru-hexlet-io-assets-professions-nodejs.png',
        'name': 'ru-hexlet-io-assets-professions-nodejs.png',
        'url': 'https://ru.hexlet.io/assets/professions/nodejs.png'
    }
    assert create_file_info(path, root, tag) == result


def test_is_third(soup_fixture):
    tags = soup_fixture.find_all(['img', 'script', 'link'])
    assert is_third(tags[0], root) is False
    assert is_third(tags[1], root) is True
    assert is_third(tags[5], root) is True


def test_get_file_link(soup_fixture):
    tags = soup_fixture.find_all(['img', 'script', 'link'])
    link1 = 'https://cdn2.hexlet.io/assets/menu.css'
    link2 = '/packs/js/runtime.js'
    assert get_file_link(tags[0], root) == link1
    assert get_file_link(tags[5], root) == link2
    assert tags[5]['src'] == link2


def test_remove_root(soup_fixture):
    tags = soup_fixture.find_all(['img', 'script', 'link'])
    result = '/packs/js/runtime.js'
    remove_root(tags[5], 'src')
    assert tags[5]['src'] == result
