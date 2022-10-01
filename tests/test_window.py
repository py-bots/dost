
from my_dost.windows import *
class tests():
    def test_active_window():
        print("active window",window_get_active_window())

    def launch_exe():
        launch_any_exe_bat_application(('C:\\Windows\\System32\\notepad.exe'))
        launch_any_exe_bat_application(('C:\\Windows\\System32\\not.exe'))

    def activate_window():
        window_activate_window('Chrome')
        window_activate_window('Chrme')

    def window_titles():
        print("All window titles",window_get_all_opened_titles_windows())

    def maximize():
        window_maximize_windows('max')
        window_maximize_windows('Notepad')

    def minimize():
        window_minimize_windows('mini')
        window_minimize_windows('Notepad')

    def close():
        window_close_windows('Not')
        window_close_windows('Notepad')

    def show():
        window_show_desktop()

test=tests()
test.launch_exe()
test.maximize()
test.minimize()
test.activate_window()
test.test_active_window()
test.window_titles()
test.close()