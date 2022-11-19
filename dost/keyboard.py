"""
Keyboard module for dost.This module contains functions for keyboard input and output.

Examples:
    >>> from dost import keyboard
    >>> keyboard.press(key_1='a')
    >>> keyboard.write(text='Hello World!')
    >>> keyboard.write(text='Hello World!', end='enter')
    >>> keyboard.hit_enter(window="Notepad")


This module contains the following functions:

- `press(key_1, key_2, key_3, window)`: Check if a key is pressed.
- `write(text, window, end)`: Write text and press enter.
- `hit_enter(window)`: Press enter.

"""


from dost.helpers import dostify


@dostify(errors=[])
def press(key_1: str, key_2: str = '', key_3: str = '', window: str = '') -> None:
    # sourcery skip: raise-specific-error
    """Press a key or a combination of keys.
    Args:
        key_1 (str): The first key to press.
        key_2 (str): The second key to press.
        key_3 (str): The third key to press.
        window (str): The window to press the key in.
        
    Examples:
        >>> keyboard.press(key_1='a', window='Notepad')
        >>> keyboard.press(key_1='ctrl', key_2='a')
        >>> keyboard.press(key_1='ctrl', key_2='shift',key_3='esc')
    """
    # Import Section
    import pywinauto as pwa
    from dost.windows import activate_window
    from typing import Union

    # Code Section
    if not key_1:
        raise Exception("Key 1 is empty.")

    def assign_key(shortcut: str) -> Union[str, bool]:
        shortcut = shortcut.lower()
        if shortcut == 'enter':
            return '{VK_RETURN}'
        elif shortcut == 'ctrl':
            return '{VK_CONTROL}'
        elif shortcut == 'alt':
            return '{VK_MENU}'
        elif shortcut == 'shift':
            return '{VK_SHIFT}'
        elif shortcut == 'win':
            return '{VK_RWIN}'
        elif shortcut == 'space':
            return '{VK_SPACE}'
        elif shortcut == 'tab':
            return '{VK_TAB}'
        else:
            return False

    def assign_number(shortcut: str) -> str:
        return f'{{VK_NUMPAD{shortcut}}}'

    special_keys = ['{SCROLLLOCK}', '{VK_SPACE}', '{VK_LSHIFT}', '{VK_PAUSE}', '{VK_MODECHANGE}',
                    '{BACK}', '{VK_HOME}', '{F23}', '{F22}', '{F21}', '{F20}', '{VK_HANGEUL}', '{VK_KANJI}',
                    '{VK_RIGHT}', '{BS}', '{HOME}', '{VK_F4}', '{VK_ACCEPT}', '{VK_F18}', '{VK_SNAPSHOT}',
                    '{VK_PA1}', '{VK_NONAME}', '{VK_LCONTROL}', '{ZOOM}', '{VK_ATTN}', '{VK_F10}', '{VK_F22}',
                    '{VK_F23}', '{VK_F20}', '{VK_F21}', '{VK_SCROLL}', '{TAB}', '{VK_F11}', '{VK_END}',
                    '{LEFT}', '{VK_UP}', '{NUMLOCK}', '{VK_APPS}', '{PGUP}', '{VK_F8}', '{VK_CONTROL}',
                    '{VK_LEFT}', '{PRTSC}', '{VK_NUMPAD4}', '{CAPSLOCK}', '{VK_CONVERT}', '{VK_PROCESSKEY}',
                    '{ENTER}', '{VK_SEPARATOR}', '{VK_RWIN}', '{VK_LMENU}', '{VK_NEXT}', '{F1}', '{F2}',
                    '{F3}', '{F4}', '{F5}', '{F6}', '{F7}', '{F8}', '{F9}', '{VK_ADD}', '{VK_RCONTROL}',
                    '{VK_RETURN}', '{BREAK}', '{VK_NUMPAD9}', '{VK_NUMPAD8}', '{RWIN}', '{VK_KANA}',
                    '{PGDN}', '{VK_NUMPAD3}', '{DEL}', '{VK_NUMPAD1}', '{VK_NUMPAD0}', '{VK_NUMPAD7}',
                    '{VK_NUMPAD6}', '{VK_NUMPAD5}', '{DELETE}', '{VK_PRIOR}', '{VK_SUBTRACT}', '{HELP}',
                    '{VK_PRINT}', '{VK_BACK}', '{CAP}', '{VK_RBUTTON}', '{VK_RSHIFT}', '{VK_LWIN}', '{DOWN}',
                    '{VK_HELP}', '{VK_NONCONVERT}', '{BACKSPACE}', '{VK_SELECT}', '{VK_TAB}', '{VK_HANJA}',
                    '{VK_NUMPAD2}', '{INSERT}', '{VK_F9}', '{VK_DECIMAL}', '{VK_FINAL}', '{VK_EXSEL}',
                    '{RMENU}', '{VK_F3}', '{VK_F2}', '{VK_F1}', '{VK_F7}', '{VK_F6}', '{VK_F5}', '{VK_CRSEL}',
                    '{VK_SHIFT}', '{VK_EREOF}', '{VK_CANCEL}', '{VK_DELETE}', '{VK_HANGUL}', '{VK_MBUTTON}',
                    '{VK_NUMLOCK}', '{VK_CLEAR}', '{END}', '{VK_MENU}', '{SPACE}', '{BKSP}', '{VK_INSERT}',
                    '{F18}', '{F19}', '{ESC}', '{VK_MULTIPLY}', '{F12}', '{F13}', '{F10}', '{F11}', '{F16}',
                    '{F17}', '{F14}', '{F15}', '{F24}', '{RIGHT}', '{VK_F24}', '{VK_CAPITAL}', '{VK_LBUTTON}',
                    '{VK_OEM_CLEAR}', '{VK_ESCAPE}', '{UP}', '{VK_DIVIDE}', '{INS}', '{VK_JUNJA}',
                    '{VK_F19}', '{VK_EXECUTE}', '{VK_PLAY}', '{VK_RMENU}', '{VK_F13}', '{VK_F12}', '{LWIN}',
                    '{VK_DOWN}', '{VK_F17}', '{VK_F16}', '{VK_F15}', '{VK_F14}']

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    if len(key_1) == 1 and key_1 in numbers:
        key_1 = assign_number(key_1)
    if len(key_2) == 1 and key_2 in numbers:
        key_2 = assign_number(key_2)
    if len(key_3) == 1 and key_3 in numbers:
        key_3 = assign_number(key_3)

    if not key_1.startswith('{') and len(key_1) > 1:
        key_1 = key_1.upper()
        real_key = assign_key(key_1)
        if not real_key:
            for key in special_keys:
                if key_1 in key:
                    key_1 = key
                    break
        else:
            key_1 = real_key

    if not key_2.startswith('{') and len(key_2) > 1:
        key_2 = key_2.upper()
        real_key = assign_key(key_2)
        if not real_key:
            for key in special_keys:
                if key_2 in key:
                    key_2 = key
                    break
        else:
            key_2 = real_key

    if not key_3.startswith('{') and len(key_3) > 1:
        key_3 = key_3.upper()
        real_key = assign_key(key_3)
        if not real_key:
            for key in special_keys:
                if key_3 in key:
                    key_3 = key
                    break
        else:
            key_3 = real_key

    def make_down(key):
        return key.replace('}', ' down}')

    def make_up(key):
        return key.replace('}', ' up}')

    case_0 = not key_2 and not key_3
    # Only 1 Special Key
    case_1 = key_1 in special_keys and key_2 not in special_keys and key_3 not in special_keys
    # 2 Special Keys
    case_2 = key_1 in special_keys and key_2 in special_keys and key_3 not in special_keys
    # 3 Special Keys
    case_3 = key_1 in special_keys and key_2 in special_keys and key_3 in special_keys

    if window:
        activate_window(window)

    if case_0:
        pwa.keyboard.send_keys(key_1)
    elif case_1:
        key_1_down = make_down(key_1)
        key_1_up = make_up(key_1)
        pwa.keyboard.send_keys(str(key_1_down + key_2 + key_3 + key_1_up))
    elif case_2:
        key_1_down = make_down(key_1)
        key_1_up = make_up(key_1)
        key_2_down = make_down(key_2)
        key_2_up = make_up(key_2)
        pwa.keyboard.send_keys(
            str(key_1_down + key_2_down + key_3 + key_2_up + key_1_up))
    elif case_3:
        key_1_down = make_down(key_1)
        key_1_up = make_up(key_1)
        key_2_down = make_down(key_2)
        key_2_up = make_up(key_2)
        key_3_down = make_down(key_3)
        key_3_up = make_up(key_3)
        pwa.keyboard.send_keys(
            str(key_1_down + key_2_down + key_3_down + key_3_up + key_2_up + key_1_up))


@dostify(errors=[])
def write(text: str, window: str = '', end: str = "enter") -> None:
    # sourcery skip: raise-specific-error
    """Write text to window and press enter key

    Args:
        text (str): Text to write
        window (str, optional): The window to write to. Defaults to Active window
        end (str, optional): Key to press at end. Available options are 'enter', 'tab'. Defaults to "enter"

    Examples:
        >>> keyboard.write(text="Hello World", window="Notepad")
    """

    # Import Section
    import time
    import pywinauto as pwa
    from dost.windows import activate_window

    # Code Section
    if not text:
        raise Exception("Text to write is empty.")

    if window:
        activate_window(window)

    time.sleep(0.2)
    pwa.keyboard.send_keys(
        text, with_spaces=True, with_tabs=True, with_newlines=True)
    if end and end.lower() in {"e", "enter"}:
        pwa.keyboard.send_keys('{ENTER}')
    if end and end.lower() in {"t", "tab"}:
        pwa.keyboard.send_keys('{TAB}')


@dostify(errors=[])
def hit_enter(window: str = '') -> None:
    """Hit enter key

    Args:
        window (str, optional): The window to press enter key. Defaults to Active window

    Examples:
        >>> keyboard.hit_enter(window="Notepad")
        """

    # Import Section
    import pywinauto as pwa
    from dost.windows import activate_window

    # Code Section
    if window:
        activate_window(window)

    pwa.keyboard.send_keys('{ENTER}')
