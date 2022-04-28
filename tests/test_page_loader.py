import os
import requests_mock
import tempfile
from page_loader.page_loader import (
    download,
    get_html
)


def test_get_html():
    text = 'successful'
    link = 'http://test.com'
    with requests_mock.Mocker() as m:
        m.get(link, text=text)
        assert get_html(link) == text


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
