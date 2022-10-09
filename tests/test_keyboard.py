import sys
import unittest
sys.path.insert(0, 'my_dost')
from keyboard import *

class TestKeyboard(unittest.TestCase):


    def test_key_write_enter(self):
        # return 0
        key_press('Notepad', key_1='a')
        key_press('Notepad', '{VK_CONTROL}', 'S')
        key_press('Notepad', '{VK_CONTROL}', 'S',"enter")

    # def test_key_write_enter(self):
        # return -1
        key_write_enter("Notepad", "Hello World")
        key_write_enter("Notepad", "Hello World","t")
        key_write_enter("Notepad", "Hello World","e")
    
    def test_key_hit_enter(self):
        # return 0
        key_hit_enter("Notepad")

if __name__=="__main__":
    unittest.main()