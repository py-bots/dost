import os
import unittest
from dost.chrome import *


class test(unittest.TestCase):
    def test_chrome(self):
        chrome_open()
        chrome_open(url="https://www.google.com")
        chrome_close()
