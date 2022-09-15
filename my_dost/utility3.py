from pathlib import WindowsPath
import win32clipboard
from my_dost.CrashHandler import report_error


def pause_program(seconds:int="5"):


    # import section
    import time
    
    
    seconds = int(seconds)
    time.sleep(seconds)

        # If the function returns a value, it should be assigned to the data variable.
        # data = value


def api_request(url: str, method='GET', body: dict = None, headers: dict = None):
    import requests
    import json

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


# api request todos free api
# print(api_request("https://todos.free.beeceptor.com/todos", body='', headers={}))
# print(api_request(url='https://todos.free.beeceptor.com/todos'))


def clipboard_set_data(data:str, format_id=win32clipboard.CF_UNICODETEXT):

    # Import Section
    from my_dost.CrashHandler import report_error
    import win32clipboard


    # Logic Section
    win32clipboard.OpenClipboard()
    try:
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(format_id, data)
    finally:
        if error is not None:
            raise Exception(error)
        win32clipboard.CloseClipboard()



def GetClipboardFormats():
    import win32clipboard

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


def clipboard_get_data(format_id=win32clipboard.CF_UNICODETEXT):

    # Import Section
    from my_dost.CrashHandler import report_error
    import win32clipboard


    # Logic Section

    if format_id not in GetClipboardFormats():
        raise RuntimeError("That format is not available")
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(format_id)
    win32clipboard.CloseClipboard()

    return data


def clear_output():
   
    # Import Section
    import os

    # Logic Section
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def install_module(module_name:str):
    if module_name != "my_dost":
        import subprocess
        import sys
        subprocess.call([sys.executable, "-m", "pip",
                        "install", module_name])


def uninstall_module(module_name:str):
    if module_name != "my_dost":
        import subprocess
        import sys
        subprocess.call([sys.executable, "-m", "pip",
                        "uninstall", "-y", module_name])
    else:
        raise Exception(
            "You cannot uninstall my_dost from here.")


def image_to_text(image_path:WindowsPath):
    # Imports
    from PIL import Image
    import pytesseract
    from my_dost.CrashHandler import report_error

    
    # Logic section
    image = Image.open(image_path)
    data = pytesseract.image_to_string(image)

    return data
