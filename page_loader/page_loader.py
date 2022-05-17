"""Download content from a web page and save it to a files"""
import logging.config
import os
import sys

from page_loader.filename_changer import get_name, add_extension
from page_loader.storage import save_file, StorageException
from page_loader.html_changer import change_html
from page_loader.network import get_request, NetworkException
from page_loader.logger_config import get_logger_config


def download(link: str, output: str):
    """Downloads web-page"""
    logging.config.dictConfig(get_logger_config(output))
    logger = logging.getLogger('best_logger')

    try:
        logger.warning(f'Trying to save the page: {link}')

        html = get_request(link).decode()
    except NetworkException as error:
        logger.error(error, exc_info=sys.exc_info())
        return

    page_name = get_name(link)
    updated_html = change_html(html, link, page_name, output)
    filename = add_extension(page_name, 'html')
    full_path = os.path.join(output, filename)

    try:
        save_file(bytes(updated_html, 'utf-8'), full_path)
        return full_path
    except StorageException as err:
        logger.error(err, exc_info=sys.exc_info())
