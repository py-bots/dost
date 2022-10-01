import sys
import unittest


sys.path.insert(0, 'my_dost')

from utility import *

class tests(unittest.TestCase):
    def test_pause(self):
        pause_program(5)
    
    def test_clipboard_set(self):
        clipboard_set_data("Hello World")
    
    def test_clipboard_get(self):
        clipboard_set_data("Hello World")
        self.assertEqual(str(clipboard_get_data()),"Hello World")
    
    def test_formats(self):
        GetClipboardFormats()
    
    def test_clear(self):
        clear_output()

    def test_uninstall_module(self):
        uninstall_module("requests")
    
    def test_install_module(self):
        install_module("pytesseract")

    def test_text_from_image(self):
        SEassertEQ(image_to_text("tests\demo2.png"))


if __name__ == '__main__':
    unittest.main()

