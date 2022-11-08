"""
String Module for dost.This module contains functions for working with strings.

Examples:
    >>> from dost import text
    >>> text.get_alphabets("hello123:l;,")
    'hellol'
    >>> text.get_numbers("hello123:l;,")
    '123
    >>> text.remove_special_characters("hello123:l;,")
    'hello123l'

The module contains the following functions:

- `get_alphabets(string)`: Extract only alphabets from the given string.
- `get_numbers(string)`: Extract only numbers from the given string.
- `remove_special_characters(string)`: Remove special characters from the given string.
"""


from dost.helpers import dostify


@dostify(errors=[])
def get_alphabets(text: str) -> str:
    """Extracts alphabets from the given string.
    Args:
        text (str): The string from which alphabets are to be extracted.

    Returns:
        str: Alphabets from the given string.

    Examples:
        >>> text.get_alphabets("hello123:l;,")
        'hellol'
    """
    return ''.join(e for e in text if e.isalpha())


@dostify(errors=[])
def get_numbers(text: str) -> str:
    """Extracts alphabets from the given string.
    Args:
        text (str): The string from which numbers are to be extracted.

    Returns:
        str: Numbers extracted from the given string.

    Examples:
        >>> text.get_numbers("hello123:l;,")
        '123'
    """

    return ''.join(e for e in text if e.isnumeric())


@dostify(errors=[])
def remove_special_characters(text: str) -> str:
    """Removes special characters from the given string.
    Args:
        text (str): The string from which special characters are to be removed.

    Returns:
        str: The string without special characters.

    Examples:
        >>> text.extract_only_alphabets("hello123:l;,")
        'hello123l'
    """
    return ''.join(e for e in text if e.isalnum())
