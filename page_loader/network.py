import logging
import requests

logger = logging.getLogger("best_logger")


class NetworkException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def get_request(link: str, client=requests):
    """Makes a GET request and returns the required data"""
    # logger.debug(f'Trying to connect: {link}')
    try:
        logger.debug(f'Trying to connect: {link}')

        response = client.get(link)
        response.raise_for_status()
    except (requests.RequestException, requests.exceptions.HTTPError) as err:
        raise NetworkException(f'Can\'t connect to {link}') from err
    else:
        logger.debug(f'Connection status - {response.status_code}')

    content = response.content
    return content
