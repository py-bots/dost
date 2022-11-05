"""
Windows module for dost.This module contains functions that are specific to Windows.

Examples:
    >>> from dost import windows
    >>> windows._window_find_exact_name('Notepad')
    'Notepad'
    >>> windows.show_desktop()
    >>> windows.get_active_window()
    'Notepad'
    >>> window.get_all_opened_window_titles()
    ['Notepad', 'Program Manager', 'Desktop']
    >>> windows.maximize_window('Notepad')
    >>> windows.minimize_window('Notepad')
    >>> windows.close_window('Notepad')
    >>> windows.launch_app('notepad')


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
        >>> _window_find_exact_name('Notepad')

    """
    # Import Section
    import pygetwindow as gw

    # Code Section
    if not window_name:
        raise ValueError(f'Window name cannot be empty')

    lst = gw.getAllTitles()
    win = ""
    for item in lst:
        if str(item).strip():
            if str(window_name).lower() in str(item).lower():
                win = item
                break
    return win


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
        Union[str,List[str]]: Active window

    Examples:
        >>> windows.get_active_window()
    """

    # Import Section
    import win32gui
    import pygetwindow as gw

    # Code Section
    _title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    data = _title

    return data


@dostify(errors=[(ValueError, '')])
def activate_window(window_name: str) -> None:
    """Activate window

    Args:
        window_name (str): Window title

    Examples:
        >>> windows.activate_window('Notepad')
    """

    # Import Section
    import pygetwindow as gw

    # Code Section
    if not window_name:
        raise ValueError('Window title name is empty.')

    item = _window_find_exact_name(window_name)
    if item != "":
        windw = gw.getWindowsWithTitle(item)[0]

        try:
            windw.activate()
        except:
            windw.minimize()
            windw.maximize()
    else:
        raise ValueError(f'Window title name {window_name} not found')


@dostify(errors=[])
def get_all_opened_window_titles() -> Union[str, List[str]]:
    """Get all opened titles windows

    Returns:
        Union[str, List[str]]: All opened titles windows

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
    data = allTitles_lst
    return data


@dostify(errors=[(ValueError, '')])
def maximize_window(window_name: str) -> None:
    """Maximize windows
    Args:
        window_name (str, optional): Window name. Defaults to "".
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
    if item != "":
        windw = gw.getWindowsWithTitle(item)[0]
        windw.maximize()
    else:
        raise ValueError(f'Window title name {window_name} not found')


@dostify(errors=[(ValueError, '')])
def minimize_window(window_name: str) -> None:
    """Minimize windows
    Args:
        window_name (str): Window name
    Examples:
        >>> windows.minimize_window('Notepad')
    """

    # Import Section
    import pygetwindow as gw

    # Code Section
    if not window_name:
        raise ValueError(f'Window title name is empty.')

    item = _window_find_exact_name(window_name)
    if item != "":
        windw = gw.getWindowsWithTitle(item)[0]
        windw.minimize()
    else:
        raise ValueError(f'Window title name {window_name} not found')


@dostify(errors=[(ValueError, '')])
def close_window(window_name: str) -> None:
    """Close windows
    Args:
        window_name (str): Window name
    Examples:
        >>> windows.close_window('Notepad')
    """

    # Import Section
    import pygetwindow as gw

    # Code Section
    if not window_name:
        raise ValueError('Window title name is empty.')

    item = _window_find_exact_name(window_name)
    if item != "":
        windw = gw.getWindowsWithTitle(item)[0]
        windw.close()
    else:
        raise ValueError(f'Window title name {window_name} not found')


@dostify(errors=[(FileNotFoundError, ''), (ValueError, '')])
def launch_app(path: Union[str, WindowsPath]) -> None:
    """Launch any exe/bat application
    Args:
        path (Union[str, WindowsPath]): Path to exe/bat application or application name

    Raises:
        FileNotFoundError: If path is not found
        ValueError: If path is empty

    Examples:
        >>> windows.launch_app(notepad)
    """

    # Import Section
    import win32gui
    import win32con
    import os
    import time

    # Code Section
    if not path:
        raise ValueError('Path of the exe file is empty.')

    try:
        abs_path = os.path.abspath(path)
        os.startfile(abs_path)
        time.sleep(2)
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

    except Exception:
        raise FileNotFoundError(f'No file found at {path}')
