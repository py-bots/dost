from clipboard import *
import sys
import unittest
sys.path.insert(0, 'dost')


class tests(unittest.TestCase):
    def test_clipboard_set_data(self):
        clipboard_set_data('Hello World!')
        self.assertEqual(clipboard_get_data(), 'Hello World!')

    def test_GetClipboardFormats(self):
        print(GetClipboardFormats())


if __name__ == '__main__':
    unittest.main()
