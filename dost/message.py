"""
Message module for dost. This module contains functions for displaying messages to the user.

Examples:
    >>> from dost import message
    >>> message.info(message='Hello World!')
    >>> message.error(message='Hello World!')
    >>> message.warning(message='Hello World!')


The module contains the following functions:

- `info(message, title)`: Display an info message to the user.
- `error(message, title)`: Display an error message to the user.
- `warning(message, title)`: Display a warning message to the user.

"""


from dost.helpers import dostify


@dostify(errors=[])
def info(message: str, title: str = "PyBOTs") -> None:
    """Display an info message to the user.
    Args:
        message (str): Message to display
        title (str): Title of the message
    Examples:
        >>> message.info(msg='Hello World!', title='PyBOTs')
    """
    # Import Section
    import ctypes

    # Code Section
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)


@dostify(errors=[])
def error(message: str, title: str = "PyBOTs") -> None:
    """Display an error message to the user.
    Args:
        message (str): Message to display
        title (str): Title of the message
    Examples:
        >>> message.error(msg='Bad news world!', title='PyBOTs')

    """
    # import section
    import ctypes

    # code section
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x10)


@dostify(errors=[])
def warning(message: str, title: str = "PyBOTs") -> None:
    """Display a warning message to the user.
    Args:
        message (str): Message to display
        title (str): Title of the message
    Examples:
        >>> message.error(msg='About to Boom World!', title='PyBOTs')

    """
    # import section
    import ctypes

    # code section
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x30)
