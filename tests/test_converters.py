import sys
sys.path.insert(0,"my_dost")
import os
import unittest
from converters import *

class test(unittest.TestCase):
    def test_convert_csv_to_excel(self):
        
        convert_csv_to_excel(input_file=r'tests\\demo.csv', output_folder=r'tests',output_filename="demo_full.xlsx",contains_headers=True,sep=",")
        convert_csv_to_excel(input_file=r'tests\\demo.csv', output_folder=r'tests',output_filename="demo_nosep.xlsx",contains_headers=True)
        convert_csv_to_excel(input_file=r'tests\\demo.csv', output_folder=r'tests',output_filename="demo_nosephead.xlsx")
        convert_csv_to_excel(input_file=r'tests\\demo.csv', output_folder=r'tests')

        convert_image_jpg_to_png(input_filepath='tests\\demo.jpg')
if __name__== "__main__":
    unittest.main()