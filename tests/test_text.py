import sys
sys.path.insert(0, 'my_dost')

import unittest
from text import *

class tests(unittest.TestCase):
    def test_string_extract_only_alphabets(self):
        self.assertEqual(string_extract_only_alphabets("hello123:l;,") , 'hellol')
        
    
    def test_string_extract_only_numbers(self):
        self.assertEqual(string_extract_only_numbers("hello123:l;,") , '123')
        
    
    def test_string_remove_special_characters(self):
        self.assertEqual(string_remove_special_characters("hello123:l;,") , 'hello123l')
    
if __name__ == '__main__':
    unittest.main()
