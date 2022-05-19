import os
import tempfile

import pytest

from page_loader.storage import save_file, make_dir, StorageException


def test_make_dir():
    dir_name = 'test'
    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = os.path.join(tmpdirname, dir_name)
        make_dir(full_path)
        assert os.path.exists(full_path)


def test_create_dir_exceptions(tmpdir):
    with tempfile.TemporaryDirectory() as tmpdirname:
        test_dir = os.path.join(tmpdirname, 'test_dir')
        os.chmod(tmpdirname, 0x111)
        with pytest.raises(StorageException):
            make_dir(test_dir)


def test_save_file():
    with open('tests/fixtures/before.html', 'rb') as file:
        content = file.read()
    file_name = 'test-com-testtest.html'
    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = os.path.join(tmpdirname, file_name)
        save_file(content, full_path)
        file = open(full_path, 'rb')
        assert file.read() == content


def test_save_file_exceptions():
    with open('tests/fixtures/before.html', 'rb') as file:
        content = file.read()
    file_name = 'test-com-testtest.html'
    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = os.path.join(tmpdirname, file_name)
        os.chmod(tmpdirname, 0x111)
        with pytest.raises(StorageException):
            save_file(content, full_path)
