from page_loader.filename_changer import (
    add_extension,
    delete_extension,
    get_name,
    remove_trailing_slash,
    get_root
)


def test_add_extension():
    name = 'ru-hexlet-io-courses'
    extension = 'html'
    result = 'ru-hexlet-io-courses.html'
    assert add_extension(name, extension) == result


def test_get_name():
    test_link = 'https://ru.hexlet.io/courses'
    result = 'ru-hexlet-io-courses'
    assert get_name(test_link) == result


def test_get_name_without_scheme():
    test_path = '/files/static/123.png'
    result = '-files-static-123'
    assert get_name(test_path) == result


def test_delete_extension():
    link = 'http://test.com/25.html'
    result = 'http://test.com/25'
    assert delete_extension(link) == result


def test_delete_extension_without_extension():
    link = 'http://test.com/25/31213/dva'
    assert delete_extension(link) == link


def test_delete_extension_with_other():
    link = 'http://test.com/jnlp'
    assert delete_extension(link) == link


def test_remove_trailing_slash():
    link = 'http://test.com/'
    result = 'http://test.com'
    assert remove_trailing_slash(link) == result
    assert remove_trailing_slash(result) == result


def test_get_root():
    link = 'https://test.com/content/add.png'
    result = 'https://test.com'
    assert get_root(link) == result
