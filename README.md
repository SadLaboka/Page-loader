# Page-loader
[![Actions Status](https://github.com/SadLaboka/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/SadLaboka/python-project-lvl3/actions)
[![flake8 and pytest](https://github.com/SadLaboka/python-project-lvl3/actions/workflows/main.yml/badge.svg)](https://github.com/SadLaboka/python-project-lvl3/actions/workflows/main.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/ccc0b00a72d0274b8fa4/maintainability)](https://codeclimate.com/github/SadLaboka/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ccc0b00a72d0274b8fa4/test_coverage)](https://codeclimate.com/github/SadLaboka/python-project-lvl3/test_coverage)

Page-loader is a simple CLI tool for loading a web page and its static files on your local machine. The program changes the paths of static files in html to local ones and fixes extensions.

## Installing

```
pip install --user --index-url https://test.pypi.org/simple/ page-loader-sadlaboka
```

## Usage

### As library

```python
from page_loader import page_loader

file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
print(file_path)  # => '/var/tmp/ru-hexlet-io-courses.html'
```

### As CLI tool
```
page-loader -h
usage: page-loader [-h] [--output OUTPUT] link

Page-loader

positional arguments:
  link

options:
  -h, --help       show this help message and exit
  --output OUTPUT  set the save path
```

## Saving page:

[![asciicast](https://github.com/SadLaboka/python-project-lvl3/blob/main/docs/downloading_page.svg)](https://asciinema.org/a/veawVa4WKiEFLxr8NnOInqR2m)

