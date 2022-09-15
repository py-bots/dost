import win32clipboard
from helpers import dostify

@dostify(errors=[])
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
        win32clipboard.CloseClipboard()


@dostify(errors=[])
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

@dostify(errors=[])
def clipboard_get_data(format_id=win32clipboard.CF_UNICODETEXT) -> str:

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
