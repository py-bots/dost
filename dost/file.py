"""
File module for dost. This module is used to interact with files.

Examples:
    >>> from dost import file
    >>> file.read_text(path='tests\\demo.txt')
    'This is a demo text file.'

It contains the following functions:

- `read_text(path)`: Read a text file and return the content as a string.
- `write_text(path, content)`: Write a text file with the given content.
- `copy(source, destination)`: Copy a file from the source to the destination.
- `move(source, destination)`: Move a file from the source to the destination.
- `delete(path)`: Delete a file at the given path.
- `rename(path, new_name)`: Rename a file at the given path.
- `create(path)`: Create a file at the given path.

"""

import os
from pathlib import WindowsPath
from typing import List, Union
from dost.helpers import dostify


@dostify(errors=[(FileNotFoundError, '')])
def read_text(path: Union[str, List[str], WindowsPath, List[WindowsPath]]) -> Union[str, List[str]]:
    """Reads a text file and returns its contents as a string.

    Args:
        path (Union[str, List[str], WindowsPath, List[WindowsPath]]): The path to the text file.

    Returns:
         The contents of the text file. If a list of paths is provided, a list of strings is returned. 

    Examples:
        >>> file.read_text(path='tests\\demo.txt')
        'This is a demo text file.'

        >>> file.read_text(path=['tests\\demo.txt', 'tests\\demo2.txt'])
        ['This is a demo text file.', 'This is a demo2 text file.']

    """
    if isinstance(path, list):
        return [read_text(path) for path in path]

    file_path = os.path.abspath(path)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    with open(path, 'r') as f:
        return f.read()


@dostify(errors=[])
def write_text(path: Union[str, WindowsPath], contents: str) -> None:
    """ Write a text file with the given contents.

    Args:
        path (Union[str, WindowsPath]): The path to the text file.
        contents (str): The contents of the text file.

    Examples:
        >>> file.write_text(path='tests\\demo.txt',contents= 'This is a demo text file.')
        >>> file.read_text(path='tests\\demo.txt')
        'This is a demo text file.'

    """
    with open(path, 'w') as f:
        f.write(contents)


@dostify(errors=[])
def copy(source: Union[str, WindowsPath], destination: Union[str, WindowsPath]) -> None:
    """ Copy a file from source to destination.

    Args:
        source (Union[str, WindowsPath]): The path to the source file.
        destination (Union[str, WindowsPath]): The path to the destination file.

    Examples:
        >>> file.copy(source='tests\\demo.txt',destination= 'tests\\demo2.txt')
        >>> file.read_text(path='tests\\demo2.txt')
        'This is a demo text file.'

    """
    with open(source, 'rb') as f:
        content = f.read()
    with open(destination, 'wb') as f:
        f.write(content)


@dostify(errors=[])
def move(source: Union[str, WindowsPath], destination: Union[str, WindowsPath]) -> None:
    """ Move a file from source to destination.

    Args:
        source (Union[str, WindowsPath]): The path to the source file.
        destination (Union[str, WindowsPath]): The path to the destination file.

    Examples:
        >>> file.move(source='tests\\demo.txt',destination='tests\\demo2.txt')
        >>> file.read_text(path='tests\\demo2.txt')
        'This is a demo text file.'

    """
    copy(source, destination)
    os.remove(source)


@dostify(errors=[])
def delete(path: Union[str, WindowsPath]) -> None:
    """ Delete a file.

    Args:
        path (Union[str, WindowsPath]): The path to the file.

    Examples:
        >>> file.delete(path='tests\\demo.txt')
        >>> os.path.exists("tests\\demo.txt")
        False

    """
    os.remove(path)


@dostify(errors=[])
def rename(path: Union[str, WindowsPath], new_name: str) -> None:
    """ Rename a file.

    Args:
        path (Union[str, WindowsPath]): The path to the file.
        new_name (str): The new name of the file.

    Examples:
        >>> file.rename(path='tests\\demo.txt',new_name= 'demo2.txt')
        >>> file.read_text(path='tests\\demo2.txt')
        'This is a demo text file.'

    """
    os.rename(path, new_name)


@dostify(errors=[])
def create(path: Union[str, WindowsPath]) -> None:
    """ Create a file.

    Args:
        path (Union[str, WindowsPath]): The path to the file.

    Examples:
        >>> file.create(path='tests\\demo.txt')
        >>> file.read_text(path='tests\\demo.txt')
        ''

    """
    with open(path, 'w') as f:
        pass
