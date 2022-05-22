import logging
import os

logger = logging.getLogger("best_logger")


class StorageException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


def make_dir(path: str) -> None:
    """Creates a directory to save files"""
    try:
        logger.debug(f'Trying to create directory {path}')
        os.mkdir(path)
    except FileExistsError:
        logger.warning(f'Directory {path} already exists')
    except PermissionError as err:
        raise StorageException(
            f'Can\'t create dir {path}. Permission denied'
        ) from err
    else:
        logger.debug('Directory created successfully')


def save_file(content: bytes, full_path: str) -> None:
    """Saves content to a local file"""
    logger.debug(f'Trying to save {full_path}')
    if not os.path.exists(full_path):
        try:
            with open(full_path, 'wb') as f:
                f.write(content)
        except (FileNotFoundError, PermissionError) as err:
            raise StorageException(
                f'Can\'t save file {full_path}'
            ) from err
        else:
            logger.debug('Save was successful')
    else:
        logger.debug(f'File {full_path} already exists')
