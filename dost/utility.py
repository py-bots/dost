""" 
Utility module for dost. This module contains utility functions. 

Examples:
    >>> import dost.utility as utility
    >>> utility.pause_program(seconds=5)
    >>> utility.api_request(url="https://google.com")
    >>> utility.clear_output()
    >>> utility.install_module(module_name="requests")
    >>> utility.uninstall_module(module_name="requests")
    >>> utility.get_module_version(module_name="requests")
    >>> utility.image_to_text(image_path="image.png")


This module contains the following functions:

- `pause_program(seconds)`: Pauses the program for the specified number of seconds
- `api_request(url , method, body, headers)`: Makes an API request to the specified URL
- `clear_output()`: Clears the output of the console
- `install_module(module_name)`: Installs the specified module
- `uninstall_module(module_name)`: Uninstalls the specified module 
- `get_module_version(module_name)`: Gets the version of the specified module
- `image_to_text(image_path)`: Converts the specified image to text
"""


from multiprocessing.sharedctypes import Value
from pathlib import WindowsPath
import win32clipboard
import typing as typing
from typing import List, Union
from dost.helpers import dostify


@dostify(errors=[(OverflowError, "Time is too large")])
def pause_program(seconds: int = "5") -> None:
    """Pauses the program for the specified number of seconds

    Args:
        seconds (int, optional): Number of seconds to pause the program. Defaults to "5".

    Examples:
        >>> utility.pause_program(seconds=5)
    """

    # Import Section
    import time

    # Code Section
    if seconds > 4294967:
        raise OverflowError

    time.sleep(seconds)


@dostify(errors=[])
def api_request(url: str, method='GET', body: dict = None, headers: dict = None) -> dict:
    # sourcery skip: raise-specific-error
    """Makes an API request to the specified URL

    Args:
        url (str): URL to make request to
        method (str, optional): HTTP method to use. Defaults to 'GET'.
        body (dict, optional): Body of the request. Defaults to None.
        headers (dict, optional): Headers of the request. Defaults to None.

    Returns:
        dict: Response from the API

    Examples:
        >>> utility.api_request(url="https://google.com")
    """

    # Import Section
    import requests
    import json

    # Code Section
    if headers is None:
        headers = {"charset": "utf-8", "Content-Type": "application/json"}

    if method == 'GET':
        response = requests.get(
            url, headers=headers, params=body)
    elif method == 'POST':
        response = requests.post(
            url, data=json.dumps(body), headers=json.dumps(headers))
    elif method == 'PUT':
        response = requests.put(
            url, data=json.dumps(body), headers=json.dumps(headers))
    elif method == 'DELETE':
        response = requests.delete(
            url, data=json.dumps(body), headers=json.dumps(headers))
    else:
        raise Exception("Invalid method")
    if response.status_code in [200, 201, 202, 203, 204]:
        data = response.json()
    else:
        raise Exception(response.text)
    return data


@dostify(errors=[])
def clear_output() -> None:
    """Clears the output of the console

    Examples:
        >>> utility.clear_output()
    """

    # Import Section
    import os

    command = 'cls' if os.name in ('nt', 'dos') else 'clear'
    os.system(command)


@dostify(errors=[])
def install_module(module_name: str) -> None:
    """Installs the specified module

    Args:
        module_name (str): Name of the module to install

    Examples:
        >>> utility.install_module(module_name="requests")
    """
    # Code Section
    if module_name != "dost":
        import subprocess
        import sys
        subprocess.call([sys.executable, "-m", "pip",
                        "install", module_name])


@dostify(errors=[])
def uninstall_module(module_name: str) -> None:
    """Uninstalls the specified module

    Args:
        module_name (str): Name of the module to uninstall

    Examples:
        >>> utility.uninstall_module(module_name="requests")
    """
    if module_name == "dost":
        raise ModuleNotFoundError("You cannot uninstall dost from here.")
    import subprocess
    import sys
    subprocess.call([sys.executable, "-m", "pip",
                    "uninstall", "-y", module_name])


@dostify(errors=[])
def get_module_version(module_name: str) -> str:
    """Gets the version of the specified module

    Args:
        module_name (str): Name of the module to get the version of

    Returns:
        str: Version of the specified module

    Examples:
        >>> utility.get_module_version(module_name="requests")
    """
    import importlib
    module = importlib.import_module(module_name)
    return module.__version__


@dostify(errors=[(FileNotFoundError, '')])
def image_to_text(image_path: Union[str, WindowsPath]) -> str:
    """Converts the specified image to text

    Args:
        image_path (WindowsPath): Path to the image

    Returns:
        string: Text from the image

    Examples:
        >>> utility.image_to_text(image_path="tests\demo2.png")
    """
    # Import Section
    from PIL import Image
    import pytesseract

    image_path = WindowsPath(image_path)

    # Validation
    if not image_path.exists():
        raise FileNotFoundError(f"File not found at path {image_path}")

    # Code Section
    image = Image.open(image_path)
    return pytesseract.image_to_string(image)
