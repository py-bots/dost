"""
Windows module for dost.This module contains functions that are specific to Windows.

Examples:
    >>> from dost import windows
    >>> windows.show_desktop()
    >>> windows.get_active_window()
    'Notepad'
    >>> windows.get_all_opened_window_titles()
    ['Notepad', 'Program Manager', 'Desktop']
    >>> windows.maximize_window(window_name='Notepad')
    >>> windows.minimize_window(window_name='Notepad')
    >>> windows.close_window(window_name='Notepad')
    >>> windows.launch_app(path='Notepad')


The module contains the following functions:

- `show_desktop()`: Show the desktop.
- `get_active_window()`: Get the active window.
- `get_all_opened_window_titles()`: Get all opened windows.
- `maximize_window(window_name)`: Maximize a window.
- `minimize_window(window_name)`: Minimize a window.
- `close_window(window_name)`: Close a window.
- `launch_app(path)`: Launch any windows application by its path or name.
"""


from pathlib import WindowsPath
from typing import List, Union
from dost.helpers import dostify


@dostify(errors=[ValueError, ''])
def _window_find_exact_name(window_name: str) -> str:
    """Find window by exact name
    Args:
        window_name (str): Window name
    Returns:
        str: Window handle
    Examples:
        >>> _window_find_exact_name(window_name='Notepad')

    """
    # Import Section
    import pygetwindow as gw

    # Code Section
    if not window_name:
        raise ValueError('Window name cannot be empty')

    lst = gw.getAllTitles()
    return next((item for item in lst if str(item).strip() and window_name.lower() in str(item).lower()), "")


@dostify(errors=[])
def show_desktop() -> None:
    """Minimize all windows and show the desktop.

    Examples:
        >>> windows.show_desktop()
    """

    # Import Section
    import pywinauto as pwa

    # Code Section
    pwa.keyboard.send_keys('{VK_RWIN down} d {VK_RWIN up}')


@dostify(errors=[])
def get_active_window() -> str:
    """Get active window

    Returns:
        str : Active window

    Examples:
        >>> windows.get_active_window()
    """

    # Import Section
    import win32gui
    import pygetwindow as gw

    return win32gui.GetWindowText(win32gui.GetForegroundWindow())


@dostify(errors=[(ValueError, '')])
def activate_window(window_name: str) -> None:
    """Activate window

    Args:
        window_name (str): Window title

    Examples:
        >>> windows.activate_window(window_name='Notepad')
    """

    # Import Section
    import pygetwindow as gw

    # Code Section
    if not window_name:
        raise ValueError('Window title name is empty.')

    item = _window_find_exact_name(window_name)
    if item == "":
        raise ValueError(f'Window title name {window_name} not found')
    window = gw.getWindowsWithTitle(item)[0]

    if not window.isActive:
        window.activate()

    if window.isMinimized:
        window.restore()
        window.activate()


@dostify(errors=[])
def get_all_opened_window_titles() -> Union[str, List[str]]:
    """Get all opened titles windows

    Returns:
        (str || list): All opened titles windows

    Examples:
        >>> windows.get_all_opened_window_titles()
    """

    # Import Section
    import pygetwindow as gw

    # Code Section
    allTitles_lst = []
    lst = gw.getAllTitles()
    for item in lst:
        if str(item).strip() != "" and str(item).strip() not in allTitles_lst:
            allTitles_lst.append(str(item).strip())
    return allTitles_lst


@dostify(errors=[(ValueError, '')])
def maximize_window(window_name: str) -> None:
    """Maximize windows
    Args:
        window_name (str): Window name.
    Examples:
        >>> windows.maximize_window()
    """

    # Import Section
    import time
    import pygetwindow as gw

    # Code Section
    if not window_name:
        raise ValueError('Window title name is empty.')
    item = _window_find_exact_name(window_name)
    if item == "":
        raise ValueError(f'Window title name {window_name} not found')
    window = gw.getWindowsWithTitle(item)[0]
    window.maximize()


@dostify(errors=[(ValueError, '')])
def minimize_window(window_name: str) -> None:
    """Minimize windows
    Args:
        window_name (str): Window name
    Examples:
        >>> windows.minimize_window(window_name='Notepad')
    """

    # Import Section
    import pygetwindow as gw

    # Code Section
    if not window_name:
        raise ValueError('Window title name is empty.')

    item = _window_find_exact_name(window_name)
    if item == "":
        raise ValueError(f'Window title name {window_name} not found')
    window = gw.getWindowsWithTitle(item)[0]
    window.minimize()


@dostify(errors=[(ValueError, '')])
def close_window(window_name: str) -> None:
    """Closes the window
    Args:
        window_name (str): Window name
    Examples:
        >>> windows.close_window(window_name='Notepad')
    """

    # Import Section
    import pygetwindow as gw

    # Code Section
    if not window_name:
        raise ValueError('Window title name is empty.')

    item = _window_find_exact_name(window_name)
    if item == "":
        raise ValueError(f'Window title name {window_name} not found')
    window = gw.getWindowsWithTitle(item)[0]
    window.close()


@dostify(errors=[(FileNotFoundError, ''), (ValueError, '')])
def launch_app(path: Union[str, WindowsPath]) -> None:
    """Launch any exe/bat application
    Args:
        path (str || WindowsPath): Path to exe/bat application or application name

    Raises:
        FileNotFoundError: If path is not found
        ValueError: If path is empty

    Examples:
        >>> windows.launch_app(path=notepad)
    """

    # Import Section
    import win32gui
    import win32con
    import os
    import time

    # Code Section
    if not path:
        raise ValueError('Path of the exe file is empty.')

    os.startfile(path)
    time.sleep(1)
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
