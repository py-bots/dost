import sys
 
# adding Folder_2/subfolder to the system path
sys.path.insert(0, 'my_dost')
from windows import *
class tests():
    def test_active_window(self):
        print("active window",window_get_active_window())

    def launch_exe(self):
        launch_any_exe_bat_application('C:\\Windows\\System32\\notepad.exe')
        launch_any_exe_bat_application('C:\\Windows\\System32\\not.exe')
        launch_any_exe_bat_application('')

    def activate_window(self):
        window_activate_window('Chrome')
        window_activate_window('Chrme')
        window_activate_window('')

    def window_titles(self):
        print("All window titles",window_get_all_opened_titles_windows())

    def maximize(self):
        window_maximize_windows('notepad')
        window_maximize_windows('')
        window_maximize_windows('Notepad')

    def minimize(self):
        window_minimize_windows('not')
        window_minimize_windows('')
        window_minimize_windows('Notepad')

    def close(self):
        window_close_windows('Not')
        window_close_windows('')
        window_close_windows('Notepad')

    def show(self):
        window_show_desktop()

test=tests()

test.launch_exe()
print("Launch Tests Done\n\n")

test.maximize()
print("Maximize Tests Done\n\n")

test.minimize()
print("Minimize Tests Done\n\n")

test.activate_window()
print("Activate Tests Done\n\n")

test.test_active_window()
print("Active Window Tests Done\n\n")

test.window_titles()
print("Window Titles Tests Done\n\n")

test.close()
print("Close Tests Done\n\n")