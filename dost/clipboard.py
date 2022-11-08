"""
Clipboard module for dost. This module is used to interact with the Windows clipboard.

Examples:
    >>> from dost import clipboard
    >>> clipboard.set_data('Hello World!')
    >>> clipboard.get_data()
    'Hello World!'


It contains the following functions:

- `set_data(data, format_id)`: Set the clipboard data to the given string.
- `get_data(format_id) -> str`: Get the clipboard data as a string.
"""


import win32clipboard
from dost.helpers import dostify


@dostify(errors=[])
def set_data(data: str, format_id=win32clipboard.CF_UNICODETEXT) -> None:
    """Set the clipboard data to the given string.

    Args:
        data (str): The data to set the clipboard to.
        format_id (int): The format of the data. Defaults to CF_UNICODETEXT.

    Examples:
        >>> clipboard.set_data('Hello World!')
        >>> clipboard.get_data()
        'Hello World!'

    """
    # Import Section
    import win32clipboard

    # Code Section
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(format_id, data)
    finally:
        win32clipboard.CloseClipboard()


@dostify(errors=[])
def _GetClipboardFormats() -> list:
    """Get a list of all available clipboard formats.

    Returns:
        A list of all available clipboard formats.

    Examples:
        >>> _GetClipboardFormats()
        [49317, 13, 49797, 16, 1, 7]

    """
    # Import Section
    import win32clipboard

    # Code Section
    win32clipboard.OpenClipboard()
    available_formats = []
    current_format = 0
    while True:
        current_format = win32clipboard.EnumClipboardFormats(current_format)
        if not current_format:
            break
        available_formats.append(current_format)
    win32clipboard.CloseClipboard()
    return available_formats


@dostify(errors=[])
def get_data(format_id=win32clipboard.CF_UNICODETEXT) -> str:
    """Get the clipboard data as a string.

    Args:
        format_id (int): The format of the data. Defaults to CF_UNICODETEXT.

    Returns:
        The clipboard data as a string.

    Examples:
        >>> clipboard.get_data()
        'Hello World!'
    """
    # Import Section
    import win32clipboard

    # Code Section
    if format_id not in _GetClipboardFormats():
        raise RuntimeError("That format is not available")
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(format_id)
    win32clipboard.CloseClipboard()

    return data


print(_GetClipboardFormats())
