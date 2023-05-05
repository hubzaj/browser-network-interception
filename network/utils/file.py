import os

from pathlib import Path


def create_file(directory: Path, file_name, data: str) -> Path:
    file_path: Path = __create_file(directory=directory, file_name=file_name)
    file_path.write_text(data=data)
    return file_path


def __create_file(directory: Path, file_name: str) -> Path:
    file_path: Path = directory / file_name

    if not os.path.exists(directory):
        os.makedirs(directory)

    return file_path
