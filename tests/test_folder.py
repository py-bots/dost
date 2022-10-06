
import sys
sys.path.insert(0,"my_dost")

import unittest
from folder import *
class test(unittest.TestCase):
    
    def test_write_text_file(self):
        write_text_file('tests\\demo.txt', 'This is a demo text fileddd.')
    
    def test_read_text_file(self):
        write_text_file('tests\\demo.txt', 'This is a demo text filed.')
        self.assertEqual(read_text_file('tests\\demo.txt'), 'This is a demo text filed.')

if __name__ == '__main__':
    unittest.main()

# # test the folder module
# from my_dost import folder


# def test_folder_read_text_file():
#     """Test folder_read_text_file."""
#     # test the function
#     # create a text file
#     txt_file_path = "test.txt"
#     with open(txt_file_path, "w") as file:
#         file.write("Hello world!")
#     # read the text file
#     assert folder.folder_read_text_file(txt_file_path) == "Hello world!"
