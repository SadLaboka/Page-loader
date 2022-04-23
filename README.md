# Page-loader
[![Actions Status](https://github.com/SadLaboka/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/SadLaboka/python-project-lvl3/actions)
[![flake8 and pytest](https://github.com/SadLaboka/python-project-lvl3/actions/workflows/main.yml/badge.svg)](https://github.com/SadLaboka/python-project-lvl3/actions/workflows/main.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/ccc0b00a72d0274b8fa4/maintainability)](https://codeclimate.com/github/SadLaboka/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ccc0b00a72d0274b8fa4/test_coverage)](https://codeclimate.com/github/SadLaboka/python-project-lvl3/test_coverage)

-

## Installing

```
-
```

## Usage

### As library

```python
from page_loader import download

file_path = download('https://ru.hexlet.io/courses', '/var/tmp')
print(file_path)  # => '/var/tmp/ru-hexlet-io-courses.html'
```

### As CLI tool
