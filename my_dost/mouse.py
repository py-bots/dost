"""
Message module for my_dost. This module contains functions for mouse operations.
Examples:
    >>> from my_dost import mouse
    >>> mouse.click()
    >>> mouse.mouse_search_snip_return_coordinates_x_y('tests\\demo.png')

This module contains the following functions:
- `mouse_search_snip_return_coordinates_x_y(snip, x1, y1, x2, y2, precision=0.8, timeout=10, interval=0.5)`: Search for a snip in a region of the screen and return the coordinates of the snip.
- `mouse_click(x, y)`: Move the mouse to the given coordinates and click.
 
"""

from argparse import ArgumentError, ArgumentTypeError
from distutils.log import error
from tkinter import E
from helpers import dostify
from pathlib import WindowsPath

@dostify(errors=[(ValueError,'')])
def mouse_click(x:int, y:int, left_or_right:str="left", no_of_clicks:int=1, type_of_movement:str="abs"):
    """Clicks the mouse at the given co-ordinates.
    Args:
        x (int): X co-ordinate.
        y (int): Y co-ordinate.
        left_or_right (str): Whether to click the left or right mouse button. Defaults to "left".
        no_of_clicks (int): Number of times to click the mouse. Defaults to 1.
        type_of_movement (string): Whether the co-ordinates are absolute or relative. Defaults to "abs".
    Examples:
        >>> mouse_click(100, 100)
        >>> mouse_click(100, 100, left_or_right="right")
        >>> mouse_click(100, 100, no_of_clicks=2)
        >>> mouse_click(100, 100, type_of_movement="rel")
    """

    # import section
    import pywinauto as pwa
    import win32api

    # Validation section
    # if (x == "" and y == ""):
    #     x, y = win32api.GetCursorPos()
    if (type_of_movement!="abs" and type_of_movement!="rel"):
        raise ValueError(f'Invalid type of movement: {type_of_movement}')
    if (left_or_right != "left" and left_or_right != "right"):
        raise ValueError(f'Invalid left_or_right: {left_or_right}')
    # if x and y:
    if type_of_movement == "rel":
        current_x, current_y = win32api.GetCursorPos()
        # x, y = int(x), int(y)
        # current_x, current_y = int(current_x), int(current_y)
        x, y = (current_x + x), (current_y + y)

    if no_of_clicks == 1:
        pwa.mouse.click(coords=(x, y), button=left_or_right)
    elif no_of_clicks == 2:
        pwa.mouse.double_click(coords=(x, y), button=left_or_right)
    else:
        for i in range(no_of_clicks):
            pwa.mouse.click(coords=(x, y), button=left_or_right)

    """Above three if blocks can be replaced by the following line
        for i in range(no_of_clicks):
                pwa.mouse.click(coords=(x, y), button=left_or_right)
        """



@dostify(errors=[(FileNotFoundError,'')])
def mouse_search_snip_return_coordinates_x_y(img:WindowsPath, wait:int=10) -> tuple:
    """Searches for the given image and returns the co-ordinates of the image.

    Args:
        img (WindowsPath): The path to the image.
        wait (int): The time to wait for the image to appear. Defaults to 10.

    Returns:
        A tuple containing the X and Y co-ordinates of the image.

    Examples:
        >>> mouse_search_snip_return_coordinates_x_y('tests\\demo.png')
        (100, 100)
    """
    # import section
    import pyautogui as pag
    import time

    # Validation section
    if not isinstance(img, WindowsPath):
        raise FileNotFoundError(f'Image not found: {img}')

    # Body section
    time.sleep(wait)
    x, y = pag.locateCenterOnScreen(img)
    return (x, y)