import requests


def get_request(link: str, client=requests):
    """Makes a GET request and returns the required data"""
    response = client.get(link)
    content = response.content
    return content
