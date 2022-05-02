from typing import Union


def save_file(content: Union[str, bytes], full_path: str) -> None:
    """Saves content to a local file"""
    if isinstance(content, str):
        with open(full_path, 'w') as f:
            f.write(content)
    else:
        with open(full_path, 'wb') as f:
            f.write(content)
