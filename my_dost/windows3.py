from ctypes import Union
from pathlib import WindowsPath
from typing import List
from xml.etree.ElementTree import QName
from my_dost.CrashHandler import report_error
from helpers import dostify


@dostify(errors=[ValueError,''])
def _window_find_exact_name(windowName:str="") -> str:

    import pygetwindow as gw

    if not windowName:
        raise ValueError(f'Window name cannot be empty')

    lst = gw.getAllTitles()

    for item in lst:
        if str(item).strip():
            if str(windowName).lower() in str(item).lower():
                win = item
                break
    return win

@dostify(errors=[])
def window_show_desktop():

    # import section
    import pywinauto as pwa

    pwa.keyboard.send_keys('{VK_RWIN down} d {VK_RWIN up}')

    
@dostify(errors=[])
def window_get_active_window() -> Union[str,List[str]]:


    # import section
    import win32gui
    import pygetwindow as gw


    
    _title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    data = _title

    return data

@dostify(errors=[])
def window_activate_window(window_title:str=''):


    # import section
    import pygetwindow as gw


    if not window_title:
        raise Exception('Window title name is empty.')

    item, window_found = _window_find_exact_name(window_title)
    if window_found:
        windw = gw.getWindowsWithTitle(item)[0]

        try:
            windw.activate()
        except:
            windw.minimize()
            windw.maximize()

    else:
        raise Exception(
            'Window title name {} not found'.format(window_title))

    

@dostify(errors=[])
def window_get_all_opened_titles_windows() -> Union[str, List[str]]:

    

    # import section
    import pygetwindow as gw


    allTitles_lst = []
    lst = gw.getAllTitles()
    for item in lst:
        if str(item).strip() != "" and str(item).strip() not in allTitles_lst:
            allTitles_lst.append(str(item).strip())
    data = allTitles_lst

    return data

@dostify(errors=[])
def window_maximize_windows(windowName:str=""):

    # import section
    import time
    import pygetwindow as gw


  
    if not windowName:
        raise Exception('Window title name is empty.')

    item, window_found = _window_find_exact_name(windowName)
    if window_found:
        windw = gw.getWindowsWithTitle(item)[0]
        windw.maximize()

    else:
        Exception('Window title name {} not found'.format(windowName))

@dostify(errors=[])
def window_minimize_windows(windowName=""):


    # import section
    import pygetwindow as gw

    
    if not windowName:
        raise Exception('Window title name is empty.')

    item, window_found = _window_find_exact_name(windowName)
    if window_found:
        windw = gw.getWindowsWithTitle(item)[0]
        windw.minimize()
    else:
        Exception('Window title name {} not found'.format(windowName))



@dostify(errors=[])
def window_close_windows(windowName:str=""):


    # import section
    import pygetwindow as gw


    if not windowName:
        raise Exception('Window title name is empty.')

    item, window_found = _window_find_exact_name(windowName)
    if window_found:
        windw = gw.getWindowsWithTitle(item)[0]
        windw.close()
    else:
        Exception('Window title name {} not found'.format(windowName))



@dostify(errors=[])
def launch_any_exe_bat_application(pathOfExeFile:WindowsPath):


    # import section
    import win32gui
    import win32con
    import os
    import time


    if not pathOfExeFile:
        raise ValueError('Path of the exe file is empty.')

    try:
        os.startfile(pathOfExeFile)
        time.sleep(2)
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        status = True
    except Exception:
        os.startfile(pathOfExeFile)

