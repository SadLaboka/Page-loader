#!/usr/bin/env python3
import argparse
import os
from page_loader import download


def main():
    """Saves the web page from the specified link
     to the specified directory"""
    parser = argparse.ArgumentParser(description='Page-loader')
    parser.add_argument('link', metavar='link', type=str)
    parser.add_argument('--output',
                        help='set the save path',
                        default=os.getcwd(),
                        required=False
                        )
    args = parser.parse_args()

    print(download(args.link, args.output))


if __name__ == '__main__':
    main()
