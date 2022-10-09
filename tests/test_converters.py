import sys
sys.path.insert(0,"my_dost")
import os
import unittest
from converters import *
from folder import *
class test(unittest.TestCase):
    def test_convert_csv_to_excel(self):
        # return 0
        convert_csv_to_excel(input_filepath=r'tests\demo.csv')
        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests')
        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests',output_filename="demo_nosephead.xlsx")
        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests',output_filename="demo_nosep.xlsx",contains_headers=True)
        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests',output_filename="demo.xlsx",contains_headers=True,sep=",")
    
    def test_jpg_to_png(self):
        # return 0
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg')
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg', output_filename="demo")
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg', output_folder=r'tests')
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg', output_folder=r'tests', output_filename="demo")

    def test_png_to_jpg(self):
        # return 0
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png')
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png', output_filename="demo2")
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png', output_folder=r'tests')
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png', output_folder=r'tests', output_filename="demo2")
    
    def test_xls_to_xlsx(self):
        # return -1
        excel_convert_xls_to_xlsx(input_filepath=r'tests\demo.xls')
        excel_convert_xls_to_xlsx(input_filepath=r'tests\demo.xls', output_folder=r'tests')
        excel_convert_xls_to_xlsx(input_filepath=r'tests\demo.xls', output_filename="demo_xls")
        excel_convert_xls_to_xlsx(input_filepath=r'tests\demo.xls', output_folder=r'tests', output_filename="demo_xls")
    
    def test_img_to_base(self):
        # return -1
        self.str=convert_image_to_base64('tests\\demo2.png')
        write_text_file(r'tests\\base64.txt',str(self.str))
        print(self.str)
    
    def test_base_to_img(self):
        # return 0
        self.str=read_text_file(r'tests\\img_base64.txt')
        get_image_from_base64(self.str)
        get_image_from_base64(self.str,r'tests')
        get_image_from_base64(self.str,output_filename="demo_base_img")
        get_image_from_base64(self.str,r'tests',"demo_base_img")
    
    def test_corrupt_to_xlsx(self):
        # return -1
        excel_change_corrupt_xls_to_xlsx('tests\\demo_corrupt.xls', 'Sheet1')
        excel_change_corrupt_xls_to_xlsx('tests\\demo_corrupt.xls', 'Sheet1', output_folder=r'tests')
        excel_change_corrupt_xls_to_xlsx('tests\\demo_corrupt.xls', 'Sheet1', output_filename="demo")
        excel_change_corrupt_xls_to_xlsx('tests\\demo_corrupt.xls', 'Sheet1', output_folder=r'tests', output_filename="demo")
    
    def test_colored_html(self):
        # return -1
        excel_to_colored_html('tests\\demo.xlsx')
        excel_to_colored_html('tests\\demo.xlsx', output_folder=r'tests')
        excel_to_colored_html('tests\\demo.xlsx', output_filename="demo_color")
        excel_to_colored_html('tests\\demo.xlsx', output_folder=r'tests', output_filename="demo_color")


if __name__== "__main__":
    unittest.main()