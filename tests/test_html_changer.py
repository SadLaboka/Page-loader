import os
import pytest
import requests_mock
import tempfile
from bs4 import BeautifulSoup
from page_loader.html_changer import (
    save_image,
    change_image_path,
    change_html
)

content = b'123213testtest'


class FakeClient:
    def __init__(self, content):
        self.content = content

    def get(self, link):
        return self


@pytest.fixture()
def soup_fixture():
    with open('tests/fixtures/before.html') as file:
        html = file.read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def test_change_html(soup_fixture):
    root = 'https://ru.hexlet.io/'
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
            client=FakeClient(content))
        path = os.path.join(tmpdirname, dir_name)
        full_image_path = os.path.join(path, image_name)
        assert updated_html == after
        assert os.path.exists(os.path.join(tmpdirname, dir_name))
        with open(full_image_path, 'rb') as file:
            image_content = file.read()
        assert os.path.isfile(full_image_path)
        assert image_content == content


def test_change_image_path(soup_fixture):
    soup = soup_fixture
    image = soup.find('img')
    new_path = '/local/dir/123.png'
    change_image_path(new_path, image)
    assert image.get('src') == new_path


def test_save_image():
    file_name = 'test-com-testtest.png'
    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = os.path.join(tmpdirname, file_name)
        save_image(full_path, content)
        file = open(full_path, 'rb')
        assert file.read() == content
