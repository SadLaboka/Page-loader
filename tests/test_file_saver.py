import os
import tempfile
from page_loader.file_saver import save_file


def test_save_bytes_file():
    content = b'123123sadasd'
    file_name = 'test-com-testtest.png'
    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = os.path.join(tmpdirname, file_name)
        save_file(content, full_path)
        file = open(full_path, 'rb')
        assert file.read() == content


def test_save_text_file():
    text = 'test text'
    file_name = 'test-com-testtest.css'
    with tempfile.TemporaryDirectory() as tmpdirname:
        full_path = os.path.join(tmpdirname, file_name)
        save_file(text, full_path)
        file = open(full_path, 'r')
        assert file.read() == text
