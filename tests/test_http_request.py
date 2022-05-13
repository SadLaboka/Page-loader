import requests_mock
from page_loader.http_request import get_request

link = 'https://test.com'


def test_get_request_bytes():
    content = b'test content'
    with requests_mock.Mocker() as m:
        m.get(link, content=content)
        assert get_request(link) == content
