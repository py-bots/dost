import sys
import unittest
# adding Folder_2/subfolder to the system path
sys.path.insert(0, 'my_dost')
from windows import *

class tests(unittest.TestCase):
    def line_gap(self):
        print("\n\n")

    def test_launch_exe(self):
        launch_any_exe_bat_application('C:\\Windows\\System32\\notepad.exe')
        launch_any_exe_bat_application('C:\\Windows\\System32\\notepad1.exe')
        launch_any_exe_bat_application('')
        self.line_gap()

    def test_active_window(self):
        print("active window",window_get_active_window())
        self.line_gap()

    def test_activate_window(self):
        window_activate_window('Chrome')
        window_activate_window('Chr')
        window_activate_window('Chrd')
        window_activate_window('')
        self.line_gap()

    def test_window_titles(self):
        print("All window titles",window_get_all_opened_titles_windows())
        self.line_gap()

    def test_maximize(self):
        window_maximize_windows('notepad')
        window_maximize_windows('noted')
        window_maximize_windows('')
        window_maximize_windows('Notepad')
        self.line_gap()

    def test_minimize(self):
        window_minimize_windows('not')
        window_minimize_windows('noted')
        window_minimize_windows('')
        window_minimize_windows('Notepad')
        self.line_gap()

    def test_close(self):
        window_close_windows('Not')
        window_close_windows('Noted')
        window_close_windows('')
        window_close_windows('Notepad')
        self.line_gap()

    def test_show(self):
        window_show_desktop()
        self.line_gap()



if __name__ == '__main__':
    unittest.main()
line_gap()