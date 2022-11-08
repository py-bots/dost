"""
Folder module for dost. This module contains functions for working with folders and files.

Examples:
    >>> from dost import folder
    >>> folder.create_folder('tests\\demo')
    >>> folder.delete_folder('tests\\demo')

It contains the following functions:

- `create_folder(path)`: Create a folder at the given path.
- `delete_folder(path)`: Delete a folder at the given path.
- `rename_folder(path, new_name)`: Rename a folder at the given path.
- `copy_folder(source, destination)`: Copy a folder from the source to the destination.
- `move_folder(source, destination)`: Move a folder from the source to the destination.
- `get_size(path) -> int`: Get the size of a folder in bytes.
- `get_size_human(path) -> str`: Get the size of a folder in human readable format.
- `get_contents(path) -> list`: Get a list of all files and folders in a folder.
- `get_contents_recursive(path) -> list`: Get a list of all files and folders in a folder and all subfolders.

"""

import os
from pathlib import WindowsPath

from typing import Union

from dost.helpers import dostify


@dostify(errors=[])
def create_folder(path: Union[str, WindowsPath]) -> None:
    """ Create a folder at the given path.

    Args:
        path (Union[str, WindowsPath]): The path to the folder.

    Examples:
        >>> folder.create_folder('tests\\demo')
        >>> os.path.exists('tests\\demo')
        True

    """
    os.mkdir(path)


@dostify(errors=[])
def delete_folder(path: Union[str, WindowsPath]) -> None:
    """ Delete a folder at the given path.

    Args:
        path (Union[str, WindowsPath]): The path to the folder.

    Examples:
        >>> folder.delete_folder('tests\\demo')
        >>> os.path.exists('tests\\demo')
        False

    """
    os.rmdir(path)


@dostify(errors=[])
def rename_folder(path: Union[str, WindowsPath], new_name: str) -> None:
    """ Rename a folder at the given path.

    Args:
        path (Union[str, WindowsPath]): The path to the folder.
        new_name (str): The new name of the folder.

    Examples:
        >>> folder.rename_folder('tests\\demo', 'demo2')
        >>> os.path.exists('tests\\demo2')
        True

    """
    os.rename(path, new_name)


@dostify(errors=[])
def copy_folder(source: Union[str, WindowsPath], destination: Union[str, WindowsPath]) -> None:
    """ Copy a folder from the source to the destination.

    Args:
        source (Union[str, WindowsPath]): The path to the source folder.
        destination (Union[str, WindowsPath]): The path to the destination folder.

    Examples:
        >>> folder.copy_folder('tests\\demo', 'tests\\demo2')
        >>> os.path.exists('tests\\demo2')
        True

    """
    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        if os.path.isdir(s):
            copy_folder(s, d)
        else:
            from dost.file import copy_file
            copy_file(s, d)


@dostify(errors=[])
def move_folder(source: Union[str, WindowsPath], destination: Union[str, WindowsPath]) -> None:
    """ Move a folder from the source to the destination.

    Args:
        source (Union[str, WindowsPath]): The path to the source folder.
        destination (Union[str, WindowsPath]): The path to the destination folder.

    Examples:
        >>> folder.move_folder('tests\\demo', 'tests\\demo2')
        >>> os.path.exists('tests\\demo')
        False
        >>> os.path.exists('tests\\demo2')
        True

    """
    copy_folder(source, destination)
    delete_folder(source)


@dostify(errors=[])
def get_size(path: Union[str, WindowsPath]) -> int:
    """ Get the size of a folder in bytes.

    Args:
        path (Union[str, WindowsPath]): The path to the folder.

    Returns:
        int: The size of the folder in bytes.

    Examples:
        >>> folder.get_size('tests')
        0

    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


@dostify(errors=[])
def get_size_human(path: Union[str, WindowsPath]) -> str:
    """ Get the size of a folder in human readable format.

    Args:
        path (Union[str, WindowsPath]): The path to the folder.

    Returns:
        str: The size of the folder in human readable format.

    Examples:
        >>> folder.get_size_human('tests')
        '0 bytes'

    """
    size = get_size(path)
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0


@dostify(errors=[])
def get_contents(path: Union[str, WindowsPath]) -> list:
    """ Get a list of all files and folders in a folder.

    Args:
        path (Union[str, WindowsPath]): The path to the folder.

    Returns:
        list: A list of all files and folders in the folder.

    Examples:
        >>> folder.get_contents('tests')
        ['demo', 'demo2', 'demo.txt']

    """
    return os.listdir(path)


@dostify(errors=[])
def get_contents_recursive(path: Union[str, WindowsPath]) -> list:
    """ Get a list of all files and folders in a folder and all subfolders.

    Args:
        path (Union[str, WindowsPath]): The path to the folder.

    Returns:
        list: A list of all files and folders in the folder and all subfolders.

    Examples:
        >>> folder.get_contents_recursive('tests')
        ['demo', 'demo2', 'demo.txt']

    """
    contents = []
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            contents.append(item)
            contents.extend(get_contents_recursive(
                os.path.join(path, item)))
        else:
            contents.append(item)
    return contents
