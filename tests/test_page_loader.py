import os
import requests_mock
import tempfile
from page_loader.page_loader import (
    download,
    get_content,
    get_name,
    delete_extension
)


def test_get_content():
    text = 'successful'
    link = 'http://test.com'
    with requests_mock.Mocker() as m:
        m.get(link, text=text)
        assert get_content(link) == text


def test_get_filename():
    test_link = 'https://ru.hexlet.io/courses'
    result = 'ru-hexlet-io-courses'
    assert get_name(test_link) == result


def test_delete_extension():
    link = 'http://test.com/25.html'
    result = 'http://test.com/25'
    assert delete_extension(link) == result


def test_download():
    text = 'successful'
    link = 'http://test.com/testtest.html'
    filename = 'test-com-testtest.html'
    with requests_mock.Mocker() as m:
        m.get(link, text=text)
        with tempfile.TemporaryDirectory() as tmpdirname:
            download(link, tmpdirname)
            full_path = os.path.join(tmpdirname, filename)
            file = open(full_path)
            assert file.read() == text
