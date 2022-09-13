from argparse import ArgumentError
import string
from helpers import dostify
from pathlib import WindowsPath

@dostify(errors=[(ArgumentError,'')])
def mouse_click(x:int, y:int, left_or_right:str="left", no_of_clicks:int=1, type_of_movement:string="abs"):
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
    if (type_of_movement not in ["abs", "rel"]):
        raise ArgumentError(f'Invalid type_of_movement: {type_of_movement}')
    if (left_or_right not in ["left", "right"]):
        raise ArgumentError(f'Invalid left_or_right: {left_or_right}')

    if x and y:
        if type_of_movement == "abs":
            x, y = int(x), int(y)
        elif type_of_movement == "rel":
            current_x, current_y = win32api.GetCursorPos()
            x, y = int(x), int(y)
            current_x, current_y = int(current_x), int(current_y)
            x, y = int(current_x + x), int(current_y + y)

        if no_of_clicks == 1:
            pwa.mouse.click(coords=(x, y), button=left_or_right)
        elif no_of_clicks == 2:
            pwa.mouse.double_click(coords=(x, y), button=left_or_right)
        else:
            for i in range(no_of_clicks):
                pwa.mouse.click(coords=(x, y), button=left_or_right)


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
mouse_click(x=100, y=100,left_or_right='a')