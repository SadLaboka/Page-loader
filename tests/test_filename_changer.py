from page_loader.filename_changer import (
    add_extension,
    delete_extension,
    get_name
)


def test_add_extension():
    name = 'ru-hexlet-io-courses'
    extension = 'html'
    result = 'ru-hexlet-io-courses.html'
    assert add_extension(name, extension) == result


def test_get_filename():
    test_link = 'https://ru.hexlet.io/courses'
    result = 'ru-hexlet-io-courses'
    assert get_name(test_link) == result


def test_delete_extension():
    link = 'http://test.com/25.html'
    result = 'http://test.com/25'
    assert delete_extension(link) == result


def test_delete_extension_without_extension():
    link = 'http://test.com/25/31213/dva'
    assert delete_extension(link) == link
