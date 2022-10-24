import sys
sys.path.insert(0,"my_dost")
import os
import unittest
from converters import *
from folder import *
import pandas as pd


class test(unittest.TestCase):
    def check_remove(self,type:str,output_folder,output_filename,input_filepath):
        # if output_filename==None:
        #     files=os.listdir(output_folder)
        #     for file in files:

        if(type=="excel"):
            self.assertEqual(os.path.exists(os.path.join(output_folder,output_filename)),True)
            actual_df=pd.read_csv(input_filepath)
            converted_df=pd.read_excel(os.path.join(output_folder,output_filename))
            os.remove(os.path.join(output_folder,output_filename))
            self.assertEqual(actual_df.equals(converted_df),False)

        if(type=="png_image"):
            if output_filename.endswith(".png"):
                pass
            else:
                output_filename=output_filename+".png"
            self.assertEqual(os.path.exists(os.path.join(output_folder,output_filename)),True)
            os.remove(os.path.join(output_folder,output_filename))
        
        if(type=="jpg_image"):
            if output_filename.endswith(".jpg"):
                pass
            else:
                output_filename=output_filename+".jpg"
            self.assertEqual(os.path.exists(os.path.join(output_folder,output_filename)),True)
            os.remove(os.path.join(output_folder,output_filename))

    def test_convert_csv_to_excel(self):
        
        return 0
        input_filepath='tests\demo.csv'
        output_folder='tests'
        output_filename="demo.xlsx"
        default_out_path=os.path.join(os.path.abspath(r'C:\Users\Public\PyBots'), 'My-DOST', 'Converters Folder')

        # convert_csv_to_excel(input_filepath=r'tests\demo.csv')
        convert_csv_to_excel(input_filepath=input_filepath)

        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests')
        # self.assertEqual(os.path.exists(os.path.join(output_folder,"")),True)
        # self.assertEqual(pd.read_csv(input_filepath).equals(os.path.join(output_folder,output_filename)),True)

        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder)
    

        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests',output_filename=output_filename)
        self.check_remove("excel",output_folder,output_filename,input_filepath)

        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder,output_filename=output_filename)
        self.check_remove("excel",output_folder,output_filename,input_filepath)

        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests',output_filename=output_filename,contains_headers=True)
        self.check_remove("excel",output_folder,output_filename,input_filepath)

        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder,output_filename=output_filename,contains_headers=True)
        self.check_remove("excel",output_folder,output_filename,input_filepath)

        convert_csv_to_excel(input_filepath=r'tests\demo.csv', output_folder=r'tests',output_filename=output_filename,contains_headers=True,sep=",")
        self.check_remove("excel",output_folder,output_filename,input_filepath)

        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder,output_filename=output_filename,contains_headers=True,sep=",")
        self.check_remove("excel",output_folder,output_filename,input_filepath)

    
    def test_jpg_to_png(self):
        # return 0
        input_filepath_str='tests\demo.jpg'
        input_filepath_path=r'tests\demo.jpg'
        output_folder_str='tests'
        output_folder_path=r'tests'
        output_filename="demo.png"
        default_out_path=r"C:\Users\Public\PyBots\My-DOST\Converters Folder"

        ## Path format
        convert_image_jpg_to_png(input_filepath=input_filepath_path)
        convert_image_jpg_to_png(input_filepath=input_filepath_path, output_filename=output_filename)
        self.check_remove("png_image", default_out_path, output_filename, input_filepath_str)
        convert_image_jpg_to_png(input_filepath=input_filepath_path, output_folder=output_folder_path)
        convert_image_jpg_to_png(input_filepath=input_filepath_path, output_folder=output_folder_path, output_filename=output_filename)
        self.check_remove("png_image", output_folder_str, output_filename, input_filepath_str)
        
        ## String Format
        convert_image_jpg_to_png(input_filepath=input_filepath_str)
        convert_image_jpg_to_png(input_filepath=input_filepath_str, output_filename=output_filename)
        self.check_remove("png_image", default_out_path, output_filename, input_filepath_str)
        convert_image_jpg_to_png(input_filepath=input_filepath_str, output_folder=output_folder_str)
        convert_image_jpg_to_png(input_filepath=input_filepath_str, output_folder=output_folder_str, output_filename=output_filename)
        self.check_remove("png_image", output_folder_str, output_filename, input_filepath_str)

    def test_png_to_jpg(self):
        # return 0
        input_filepath_str='tests\demo2.png'
        input_filepath_path=r'tests\demo2.png'
        output_folder_str='tests'
        output_folder_path=r'tests'
        output_filename="demo2"
        default_out_path=r"C:\Users\Public\PyBots\My-DOST\Converters Folder"
        ## Path Format
        convert__image_png_to_jpg(input_filepath=input_filepath_path)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_filename=output_filename)
        self.check_remove("jpg_image", default_out_path, output_filename, input_filepath_str)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_folder=output_folder_path)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_folder=output_folder_path, output_filename=output_filename)
        self.check_remove("jpg_image", output_folder_str, output_filename, input_filepath_str)

        #String Format
        convert__image_png_to_jpg(input_filepath=input_filepath_path)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_filename=output_filename)
        self.check_remove("jpg_image", default_out_path, output_filename, input_filepath_str)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_folder=output_folder_path)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_folder=output_folder_path, output_filename=output_filename)
        self.check_remove("jpg_image", output_folder_str, output_filename, input_filepath_str)
    
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
        output_file_name="demo_base_img"
        output_folder=r'tests'
        self.str=read_text_file(r'tests\\img_base64.txt')
        get_image_from_base64(str(convert_image_to_base64('tests\\demo2.png')))
        get_image_from_base64(str(convert_image_to_base64('tests\\demo2.png')),output_folder)
        get_image_from_base64(str(convert_image_to_base64('tests\\demo2.png')),output_filename="demo_base_img")
        get_image_from_base64(str(convert_image_to_base64('tests\\demo2.png')),r'tests',"demo_base_img")
    
    def test_corrupt_to_xlsx(self):
        return -1
        output_folder=r'tests'
        output_filename="demo"
        input_file_str='tests\demo_corrupt.xls'
        sheet_name='Sheet1'
        excel_change_corrupt_xls_to_xlsx(input_file_str, sheet_name)
        excel_change_corrupt_xls_to_xlsx(input_file_str, sheet_name, output_folder=output_folder)
        excel_change_corrupt_xls_to_xlsx(input_file_str, sheet_name, output_filename=output_filename)
        excel_change_corrupt_xls_to_xlsx(input_file_str, sheet_name, output_folder=output_folder, output_filename=output_filename)
    
    def test_colored_html(self):
        return -1
        input_file_str="tests\demo Coloured.xlsx"
        output_folder=r'tests'
        output_filename="demo_color"
        excel_to_colored_html(input_file_str)
        excel_to_colored_html(input_file_str, output_folder=output_folder)
        excel_to_colored_html(input_file_str, output_filename=output_filename)
        excel_to_colored_html(input_file_str, output_folder=output_folder, output_filename=output_filename)


if __name__== "__main__":
    unittest.main()

