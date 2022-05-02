import requests


def get_request(link: str, mode: str, client=requests):
    """Makes a GET request and returns the required data"""
    response = client.get(link)
    if mode == 'text':
        return response.text
    elif mode == 'byte':
        return response.content
