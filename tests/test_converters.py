import sys
sys.path.insert(0,"my_dost")
import os
import unittest
from converters import *

class test(unittest.TestCase):
    def test_convert_csv_to_excel(self):
        return 0
        convert_csv_to_excel(input_file=r'tests\demo.csv', output_folder=r'tests',output_filename="demo_full.xlsx",contains_headers=True,sep=",")
        convert_csv_to_excel(input_file=r'tests\demo.csv', output_folder=r'tests',output_filename="demo_nosep.xlsx",contains_headers=True)
        convert_csv_to_excel(input_file=r'tests\demo.csv', output_folder=r'tests',output_filename="demo_nosephead.xlsx")
        convert_csv_to_excel(input_file=r'tests\demo.csv', output_folder=r'tests')
    
    def test_jpg_to_png(self):
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg')
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg',output_folder=r'tests', output_filename="demo")
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg',output_folder=r'tests')

    def test_png_to_jpg(self):
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png')
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png',output_folder=r'tests', output_filename="demo2")
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png',output_folder=r'tests')
    
    
if __name__== "__main__":
    unittest.main()