#!/usr/bin/env python3
import argparse
import logging.config
import os
import sys
from page_loader import download
from page_loader.logger_config import get_logger_config
from page_loader.storage import StorageException
from page_loader.network import NetworkException


def main():
    """Saves the web page from the specified link
     to the specified directory"""
    parser = argparse.ArgumentParser(description='Page-loader')
    parser.add_argument('link', metavar='link', type=str)
    parser.add_argument('-o', '--output',
                        help='set the save path',
                        default=os.getcwd(),
                        required=False
                        )
    args = parser.parse_args()
    output = args.output
    link = args.link

    logging.config.dictConfig(get_logger_config())
    logger = logging.getLogger('best_logger')

    try:
        logger.warning(f'Trying to save the page: {link}')
        print(f'Page was downloaded as \'{download(link, output)}\'')
        sys.exit(0)
    except (NetworkException, StorageException) as error:
        logger.error(error, exc_info=sys.exc_info())
        logger.warning('Saving failed')
        sys.exit(1)


if __name__ == '__main__':
    main()
