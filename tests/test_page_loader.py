import os
import requests_mock
import tempfile
from page_loader.page_loader import download


def test_download():
    content = b'successful'
    link = 'http://test.com/testtest.html'
    filename = 'test-com-testtest.html'
    with requests_mock.Mocker() as m:
        m.get(link, content=content)
        with tempfile.TemporaryDirectory() as tmpdirname:
            download(link, tmpdirname)
            full_path = os.path.join(tmpdirname, filename)
            file = open(full_path, 'rb')
            assert file.read() == content + b'\n'
