"""
Folder module for my_dost. This module contains functions for working with folders and files.

Examples:
    >>> from my_dost import folder
    >>> folder.folder_read_text_file('tests\\demo.txt')
    'This is a demo text file.'


The module contains the following functions:

- `folder_read_text_file(txt_file_path)`: Read a text file and return the content as a string.

"""

import os
from pathlib import WindowsPath
from typing import List, Union
from my_dost.helpers import dostify


@dostify(errors=[(FileNotFoundError,'')])
def folder_read_text_file(txt_file_path: Union[str, List[str], WindowsPath, List[WindowsPath]]) -> Union[str, List[str]]:
    """Reads a text file and returns its contents as a string.

    Args:
        txt_file_path (Union[str, List[str], WindowsPath, List[WindowsPath]]): The path to the text file.

    Returns:
         The contents of the text file. If a list of paths is provided, a list of strings is returned. 
    
    Examples:
        >>> folder_read_text_file('tests\\demo.txt')
        'This is a demo text file.'

        >>> folder_read_text_file(['tests\\demo.txt', 'tests\\demo2.txt'])
        ['This is a demo text file.', 'This is a demo2 text file.']

    """
    if isinstance(txt_file_path, list):
        return [folder_read_text_file(path) for path in txt_file_path]
    
    file_path = os.path.abspath(txt_file_path)

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')
    with open(txt_file_path, 'r') as f:
        return f.read()

@dostify(errors=[])
def folder_write_text_file(txt_file_path: Union[str, WindowsPath], contents: str):
    # Description:
    """ Write a text file with the given contents.

    Args:
        txt_file_path (Union[str, WindowsPath]): The path to the text file.
        contents (str): The contents of the text file.

    Examples:
        >>> folder_write_text_file('tests\\demo.txt', 'This is a demo text file.')
        >>> folder_read_text_file('tests\\demo.txt')
        'This is a demo text file.'
    """
    # Body section
    txt_file_path = os.path.abspath(txt_file_path)

    with open(txt_file_path, 'w') as f:
        f.write(contents)

