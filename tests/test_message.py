from message import *
import sys
import unittest

# adding Folder_2/subfolder to the system path
sys.path.insert(0, 'dost')


class tests(unittest.TestCase):
    def test_info(self):
        info('This is a demo message.')
        info('')

    def test_error(self):
        error('This is a demo message.')
        error('')

    def test_warning(self):
        warning('This is a demo message.')
        warning('')


if __name__ == '__main__':
    unittest.main()
