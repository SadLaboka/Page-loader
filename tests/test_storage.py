import os
import tempfile
from page_loader.storage import save_file, make_dir


def test_make_dir():
    dir_name = 'test'
    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = os.path.join(tmpdirname, dir_name)
        make_dir(full_path)
        assert os.path.exists(full_path)


def test_save_file():
    with open('tests/fixtures/before.html', 'rb') as file:
        content = file.read()
    file_name = 'test-com-testtest.html'
    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = os.path.join(tmpdirname, file_name)
        save_file(content, full_path)
        file = open(full_path, 'rb')
        assert file.read() == content
