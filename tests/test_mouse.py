from mouse import *
import unittest
import sys
sys.path.insert(0, 'dost')


class tests(unittest.TestCase):

    def test_mouse_click(self):
        click(0, 0)
        # self.assertEqual((0, 0) , pyautogui.position())

    # def search('tests\\demo.png')
    #     (23, 17)
if __name__ == '__main__':
    unittest.main()
