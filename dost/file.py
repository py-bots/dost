"""
File module for dost. This module is used to interact with files.

Examples:
    >>> from dost import file
    >>> file.read_text_file('tests\\demo.txt')
    'This is a demo text file.'

It contains the following functions:

- `read_text_file(path)`: Read a text file and return the content as a string.
- `write_text_file(path, content)`: Write a text file with the given content.
- `copy_file(source, destination)`: Copy a file from the source to the destination.
- `move_file(source, destination)`: Move a file from the source to the destination.
- `delete_file(path)`: Delete a file at the given path.
- `rename_file(path, new_name)`: Rename a file at the given path.
- `create_file(path)`: Create a file at the given path.

"""

import os
from pathlib import WindowsPath
from typing import List, Union
from dost.helpers import dostify


@dostify(errors=[(FileNotFoundError, '')])
def read_text_file(path: Union[str, List[str], WindowsPath, List[WindowsPath]]) -> Union[str, List[str]]:
    """Reads a text file and returns its contents as a string.

    Args:
        path (Union[str, List[str], WindowsPath, List[WindowsPath]]): The path to the text file.

    Returns:
         The contents of the text file. If a list of paths is provided, a list of strings is returned. 

    Examples:
        >>> read_text_file('tests\\demo.txt')
        'This is a demo text file.'

        >>> read_text_file(['tests\\demo.txt', 'tests\\demo2.txt'])
        ['This is a demo text file.', 'This is a demo2 text file.']

    """
    if isinstance(path, list):
        return [read_text_file(path) for path in path]

    file_path = os.path.abspath(path)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    with open(path, 'r') as f:
        return f.read()


@dostify(errors=[])
def write_text_file(path: Union[str, WindowsPath], contents: str) -> None:
    """ Write a text file with the given contents.

    Args:
        path (Union[str, WindowsPath]): The path to the text file.
        contents (str): The contents of the text file.

    Examples:
        >>> write_text_file('tests\\demo.txt', 'This is a demo text file.')
        >>> read_text_file('tests\\demo.txt')
        'This is a demo text file.'

    """
    with open(path, 'w') as f:
        f.write(contents)


@dostify(errors=[])
def copy_file(source: Union[str, WindowsPath], destination: Union[str, WindowsPath]) -> None:
    """ Copy a file from source to destination.

    Args:
        source (Union[str, WindowsPath]): The path to the source file.
        destination (Union[str, WindowsPath]): The path to the destination file.

    Examples:
        >>> copy_file('tests\\demo.txt', 'tests\\demo2.txt')
        >>> read_text_file('tests\\demo2.txt')
        'This is a demo text file.'

    """
    with open(source, 'rb') as f:
        content = f.read()
    with open(destination, 'wb') as f:
        f.write(content)


@dostify(errors=[])
def move_file(source: Union[str, WindowsPath], destination: Union[str, WindowsPath]) -> None:
    """ Move a file from source to destination.

    Args:
        source (Union[str, WindowsPath]): The path to the source file.
        destination (Union[str, WindowsPath]): The path to the destination file.

    Examples:
        >>> move_file('tests\\demo.txt', 'tests\\demo2.txt')
        >>> read_text_file('tests\\demo2.txt')
        'This is a demo text file.'

    """
    copy_file(source, destination)
    os.remove(source)


@dostify(errors=[])
def delete_file(path: Union[str, WindowsPath]) -> None:
    """ Delete a file.

    Args:
        path (Union[str, WindowsPath]): The path to the file.

    Examples:
        >>> delete_file('tests\\demo.txt')
        >>> read_text_file('tests\\demo.txt')
        ''

    """
    os.remove(path)


@dostify(errors=[])
def rename_file(path: Union[str, WindowsPath], new_name: str) -> None:
    """ Rename a file.

    Args:
        path (Union[str, WindowsPath]): The path to the file.
        new_name (str): The new name of the file.

    Examples:
        >>> rename_file('tests\\demo.txt', 'demo2.txt')
        >>> read_text_file('tests\\demo2.txt')
        'This is a demo text file.'

    """
    os.rename(path, new_name)


@dostify(errors=[])
def create_file(path: Union[str, WindowsPath]) -> None:
    """ Create a file.

    Args:
        path (Union[str, WindowsPath]): The path to the file.

    Examples:
        >>> create_file('tests\\demo.txt')
        >>> read_text_file('tests\\demo.txt')
        ''

    """
    with open(path, 'w') as f:
        pass