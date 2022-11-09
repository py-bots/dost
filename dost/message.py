"""
Message module for dost. This module contains functions for displaying messages to the user.

Examples:
    >>> from dost import message
    >>> message.info(msg='Hello World!')
    >>> message.error(msg='Hello World!')
    >>> message.warning(msg='Hello World!')


The module contains the following functions:

- `info(msg)`: Display an info message.
- `error(msg)`: Display an error message.
- `warning(msg)`: Display a warning message.

"""


from dost.helpers import dostify


@dostify(errors=[])
def info(message: str, title: str = "PyBOTs") -> None:
    """Display a message box with an 'OK' button.

    Args:   
        message (str): The message to display to the user.
        title (str, optional): The title of the message box. Defaults to "PyBOTs".

    Examples:
        >>> message.info(msg='This is a demo message.')

    """
    # Import Section
    import ctypes

    # Code Section
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x40)


@dostify(errors=[])
def error(message: str, title: str = "PyBOTs") -> None:
    """Display a message box with an 'OK' button.

    Args:   
        message (str): The message to display to the user.

    Examples:
        >>> message.error(msg='This is a demo message.')

    """
    # import section
    import ctypes

    # code section
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x10)


@dostify(errors=[])
def warning(message: str, title: str = "PyBOTs") -> None:
    """Display a message box with an 'OK' button.

    Args:   
        message (str): The message to display to the user.

    Examples:
        >>> message.warning(msg='This is a demo message.')

    """
    # import section
    import ctypes

    # code section
    ctypes.windll.user32.MessageBoxW(0, message, title, 0x30)
