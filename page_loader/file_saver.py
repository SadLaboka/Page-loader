def save_file(content: bytes, full_path: str) -> None:
    """Saves content to a local file"""
    with open(full_path, 'wb') as f:
        f.write(content)
