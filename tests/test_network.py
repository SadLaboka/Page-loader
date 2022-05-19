import pytest
import requests_mock
from page_loader.network import get_request, NetworkException

link = 'https://test.com'


def test_get_request_bytes():
    content = b'test content'
    with requests_mock.Mocker() as m:
        m.get(link, content=content, status_code=200)
        assert get_request(link) == content


@pytest.mark.parametrize(
    'url',
    [
        'https://#wronglink.com',
        ' ',
    ],
)
def test_network_failed_connection(url):
    with pytest.raises(NetworkException):
        get_request(url)


@pytest.mark.parametrize(
    'url',
    [
        'https://httpbin.org/status/301',
        'https://httpbin.org/status/302',
    ],
)
@pytest.mark.xfail
def test_redirects(url):
    with pytest.raises(NetworkException):
        get_request(url)


@pytest.mark.parametrize(
    'url',
    [
        'https://httpbin.org/status/403',
        'https://httpbin.org/status/404',
    ],
)
def test_client_connection_errors(url):
    with pytest.raises(NetworkException):
        get_request(url)


@pytest.mark.parametrize(
    'url',
    [
        'https://httpbin.org/status/500',
        'https://httpbin.org/status/502',
    ],
)
def test_server_connection_errors(url):
    with pytest.raises(NetworkException):
        get_request(url)
