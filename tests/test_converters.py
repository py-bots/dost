import sys
sys.path.insert(0,"my_dost")
import os
import unittest
from converters import *
from folder import *
import pandas as pd

class test(unittest.TestCase):
    def check_remove(type:str,output_folder,output_filename):
        self.assertEqual(os.path.exists(os.path.join(output_folder,output_filename)),True)
        if(type=="excel"):
            converted_df=pd.read_excel(os.path.join(output_folder,output_filename))
            self.assertEqual(actual_df.equals(converted_df),True)
            # os.remove(os.path.join(output_folder,output_filename))
    def test_convert_csv_to_excel(self):
        
        # return 0
        input_filepath='tests\demo.csv'
        output_folder='tests'
        output_filename="demo.xlsx"
        default_out_path=os.path.join(os.path.abspath(r'C:\Users\Public\PyBots'), 'My-DOST', 'Converters Folder')
        actual_df=pd.read_csv(input_filepath)

        # convert_csv_to_excel(input_filepath=r'tests\demo.csv')
        convert_csv_to_excel(input_filepath=input_filepath)

        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests')
        # self.assertEqual(os.path.exists(os.path.join(output_folder,"")),True)
        # self.assertEqual(pd.read_csv(input_filepath).equals(os.path.join(output_folder,output_filename)),True)

        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder)
    

        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests',output_filename=output_filename)
        check_remove("excel",output_folder,output_filename)

        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder,output_filename=output_filename)
        check_remove("excel",output_folder,output_filename)

        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests',output_filename=output_filename,contains_headers=True)
        check_remove("excel",output_folder,output_filename)

        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder,output_filename=output_filename,contains_headers=True)
        check_remove("excel",output_folder,output_filename)

        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests',output_filename=output_filename,contains_headers=True,sep=",")
        check_remove("excel",output_folder,output_filename)

        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder,output_filename=output_filename,contains_headers=True,sep=",")
        check_remove("excel",output_folder,output_filename)

    
    def test_jpg_to_png(self):
        # return 0
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg')
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg', output_filename="demo")
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg', output_folder=r'tests')
        convert_image_jpg_to_png(input_filepath=r'tests\demo.jpg', output_folder=r'tests', output_filename="demo")
        convert_image_jpg_to_png(input_filepath='tests\demo.jpg')
        convert_image_jpg_to_png(input_filepath='tests\demo.jpg', output_filename="demo")
        convert_image_jpg_to_png(input_filepath='tests\demo.jpg', output_folder='tests')
        convert_image_jpg_to_png(input_filepath='tests\demo.jpg', output_folder='tests', output_filename="demo")

    def test_png_to_jpg(self):
        # return 0
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png')
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png', output_filename="demo2")
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png', output_folder=r'tests')
        convert__image_png_to_jpg(input_filepath=r'tests\demo2.png', output_folder=r'tests', output_filename="demo2")
    
    # def test_xls_to_xlsx(self):
    #     # return -1
    #     excel_convert_xls_to_xlsx(input_filepath=r'tests\demo.xls')
    #     excel_convert_xls_to_xlsx(input_filepath=r'tests\demo.xls', output_folder=r'tests')
    #     excel_convert_xls_to_xlsx(input_filepath=r'tests\demo.xls', output_filename="demo_xls")
    #     excel_convert_xls_to_xlsx(input_filepath=r'tests\demo.xls', output_folder=r'tests', output_filename="demo_xls")
    
    def test_img_to_base(self):
        # return -1
        self.str=convert_image_to_base64('tests\\demo2.png')
        write_text_file(r'tests\\base64.txt',str(self.str))
        print(self.str)
    
    def test_base_to_img(self):
        # return 0
        self.str=read_text_file(r'tests\\img_base64.txt')
        get_image_from_base64(str(convert_image_to_base64('tests\\demo2.png')))
        get_image_from_base64(str(convert_image_to_base64('tests\\demo2.png')),r'tests')
        get_image_from_base64(str(convert_image_to_base64('tests\\demo2.png')),output_filename="demo_base_img")
        get_image_from_base64(str(convert_image_to_base64('tests\\demo2.png')),r'tests',"demo_base_img")
    
    def test_corrupt_to_xlsx(self):
        # return -1
        excel_change_corrupt_xls_to_xlsx('tests\\demo_corrupt.xls', 'Sheet1')
        excel_change_corrupt_xls_to_xlsx('tests\\demo_corrupt.xls', 'Sheet1', output_folder=r'tests')
        excel_change_corrupt_xls_to_xlsx('tests\\demo_corrupt.xls', 'Sheet1', output_filename="demo")
        excel_change_corrupt_xls_to_xlsx('tests\\demo_corrupt.xls', 'Sheet1', output_folder=r'tests', output_filename="demo")
    
    def test_colored_html(self):
        # return -1
        excel_to_colored_html("tests\demo Coloured.xlsx")
        excel_to_colored_html('tests\demo Coloured.xlsx', output_folder=r'tests')
        excel_to_colored_html('tests\demo Coloured.xlsx', output_filename="demo_color")
        excel_to_colored_html('tests\demo Coloured.xlsx', output_folder=r'tests', output_filename="demo_color")


if __name__== "__main__":
    unittest.main()

