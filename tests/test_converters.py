import sys
sys.path.insert(0,"my_dost")
import os
import unittest
from converters import *
from folder import *
import pandas as pd
import datetime
from pathlib import Path

class test(unittest.TestCase):
    def check_remove(self,type:str,output_folder="",output_filename="",input_filepath=""):
        if not output_folder:
            output_folder=r"C:\Users\Public\PyBots\My-DOST\Converters Folder"

        if(type=="excel"):
            if not output_filename:
                start_name="excel_"
                mid_part=datetime.datetime.now().strftime("%Y")
                start_name=start_name+mid_part
                files_list=os.listdir(output_folder)
                for file in files_list:
                    if file.startswith(start_name) and file.endswith(".xlsx"):
                        output_filename=file
                        break
            self.assertEqual(os.path.exists(os.path.join(output_folder,output_filename)),True)
            actual_df=pd.read_csv(input_filepath)
            converted_df=pd.read_excel(os.path.join(output_folder,output_filename))
            os.remove(os.path.join(output_folder,output_filename))
            self.assertEqual(actual_df.equals(converted_df),True)

        if(type=="png_image"):
            if not output_filename:
                start_name=Path(input_filepath).stem
                mid_part=datetime.datetime.now().strftime("%Y")
                start_name=start_name+mid_part
                files_list=os.listdir(output_folder)
                for file in files_list:
                    if file.startswith(start_name) and file.endswith(".png"):
                        output_filename=file
                        break
            if output_filename.endswith(".png"):
                pass
            else:
                output_filename=output_filename+".png"
            self.assertEqual(os.path.exists(os.path.join(output_folder,output_filename)),True)
            os.remove(os.path.join(output_folder,output_filename))
        
        if(type=="jpg_image"):
            if not output_filename:
                start_name=Path(input_filepath).stem
                mid_part=datetime.datetime.now().strftime("%Y")
                start_name=start_name+mid_part
                files_list=os.listdir(output_folder)
                for file in files_list:
                    if file.startswith(start_name) and file.endswith(".jpg"):
                        output_filename=file
                        break
            if output_filename.endswith(".jpg"):
                pass
            else:
                output_filename=output_filename+".jpg"
            self.assertEqual(os.path.exists(os.path.join(output_folder,output_filename)),True)
            os.remove(os.path.join(output_folder,output_filename))

        if(type=="base_image"):
            if not output_filename:
                start_name="image_"
                mid_part=datetime.datetime.now().strftime("%Y")
                start_name=start_name+mid_part
                files_list=os.listdir(output_folder)
                for file in files_list:
                    if file.startswith(start_name) and (file.endswith(".jpg") or file.endswith(".png")):
                        output_filename=file
                        break
            if output_filename.endswith(".png") or output_filename.endswith(".jpg"):
                pass
            else:
                output_filename=output_filename+".png"
            self.assertEqual(os.path.exists(os.path.join(output_folder,output_filename)),True)
            os.remove(os.path.join(output_folder,output_filename))
        
        if(type=="colored_html"):
            if not output_filename:
                start_name=Path(input_filepath).stem
                mid_part=datetime.datetime.now().strftime("%Y")
                start_name=start_name+"_"+mid_part
                files_list=os.listdir(output_folder)
                for file in files_list:
                    if file.startswith(start_name) and file.endswith(".html") :
                        output_filename=file
                        break
            if output_filename.endswith(".html"):
                pass
            else:
                output_filename=output_filename+".html"
            self.assertEqual(os.path.exists(os.path.join(output_folder,output_filename)),True)
            os.remove(os.path.join(output_folder,output_filename))

    def test_convert_csv_to_excel(self):
        
        # return 0
        input_filepath='tests\demo.csv'
        input_filepath_path=r'tests\demo.csv'
        output_folder='tests'
        output_folder_path=r'tests'
        output_filename="demo.xlsx"

        # convert_csv_to_excel(input_filepath=r'tests\demo.csv')
        convert_csv_to_excel(input_filepath=input_filepath)
        self.check_remove(type="excel",input_filepath=input_filepath)
        convert_csv_to_excel(input_filepath=input_filepath_path, output_folder=output_folder_path)
        self.check_remove(type="excel",output_folder=output_folder,input_filepath=input_filepath)
        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder)
        self.check_remove(type="excel",output_folder=output_folder,input_filepath=input_filepath)
        convert_csv_to_excel(input_filepath=input_filepath_path, output_folder=output_folder_path,output_filename=output_filename)
        self.check_remove("excel",output_folder,output_filename,input_filepath)
        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder,output_filename=output_filename)
        self.check_remove("excel",output_folder,output_filename,input_filepath)
        convert_csv_to_excel(input_filepath=input_filepath_path, output_folder=output_folder_path,output_filename=output_filename,contains_headers=True)
        self.check_remove("excel",output_folder,output_filename,input_filepath)
        convert_csv_to_excel(input_filepath=input_filepath, output_folder=output_folder,output_filename=output_filename,contains_headers=True)
        self.check_remove("excel",output_folder,output_filename,input_filepath)
        convert_csv_to_excel(input_filepath=input_filepath_path, output_folder=output_folder_path,output_filename=output_filename,contains_headers=True,sep=",")
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
    
        ## Path format
        convert_image_jpg_to_png(input_filepath=input_filepath_path)
        self.check_remove("png_image",input_filepath= input_filepath_path)
        convert_image_jpg_to_png(input_filepath=input_filepath_path, output_filename=output_filename)
        self.check_remove("png_image", output_filename=output_filename, input_filepath=input_filepath_str)
        convert_image_jpg_to_png(input_filepath=input_filepath_path, output_folder=output_folder_path)
        self.check_remove("png_image",output_folder=output_folder_path , input_filepath= input_filepath_path)
        convert_image_jpg_to_png(input_filepath=input_filepath_path, output_folder=output_folder_path, output_filename=output_filename)
        self.check_remove("png_image", output_folder_str, output_filename, input_filepath_str)
        
        ## String Format
        convert_image_jpg_to_png(input_filepath=input_filepath_str)
        self.check_remove("png_image",input_filepath= input_filepath_path)
        convert_image_jpg_to_png(input_filepath=input_filepath_str, output_filename=output_filename)
        self.check_remove("png_image", output_filename=output_filename, input_filepath=input_filepath_str)
        convert_image_jpg_to_png(input_filepath=input_filepath_str, output_folder=output_folder_str)
        self.check_remove("png_image",output_folder=output_folder_path , input_filepath= input_filepath_path)
        convert_image_jpg_to_png(input_filepath=input_filepath_str, output_folder=output_folder_str, output_filename=output_filename)
        self.check_remove("png_image", output_folder_str, output_filename, input_filepath_str)

    def test_png_to_jpg(self):
        # return 0
        input_filepath_str='tests\demo2.png'
        input_filepath_path=r'tests\demo2.png'
        output_folder_str='tests'
        output_folder_path=r'tests'
        output_filename="demo2"

        ## Path Format
        convert__image_png_to_jpg(input_filepath=input_filepath_path)
        self.check_remove("jpg_image",input_filepath= input_filepath_path)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_filename=output_filename)
        self.check_remove("jpg_image", output_filename=output_filename, input_filepath=input_filepath_str)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_folder=output_folder_path)
        self.check_remove("jpg_image",output_folder=output_folder_path , input_filepath= input_filepath_path)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_folder=output_folder_path, output_filename=output_filename)
        self.check_remove("jpg_image", output_folder_str, output_filename, input_filepath_str)

        #String Format
        convert__image_png_to_jpg(input_filepath=input_filepath_path)
        self.check_remove("jpg_image",input_filepath= input_filepath_path)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_filename=output_filename)
        self.check_remove("jpg_image", output_filename=output_filename, input_filepath=input_filepath_str)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_folder=output_folder_path)
        self.check_remove("jpg_image",output_folder=output_folder_path , input_filepath= input_filepath_path)
        convert__image_png_to_jpg(input_filepath=input_filepath_path, output_folder=output_folder_path, output_filename=output_filename)
        self.check_remove("jpg_image", output_folder_str, output_filename, input_filepath_str)
    
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
        output_folder=r'tests'
        output_filename="demo_base_img"
        
        input_img_base64=str(convert_image_to_base64(r'tests\demo2.png'))
        input_img_base64=input_img_base64[2:-1]
        get_image_from_base64(input_img_base64)
        self.check_remove("base_image",input_filepath= input_img_base64)
        get_image_from_base64(input_img_base64,output_folder)
        self.check_remove("base_image",output_folder=output_folder , input_filepath= input_img_base64)
        get_image_from_base64(input_img_base64,output_filename=output_filename)
        self.check_remove("base_image", output_filename=output_filename, input_filepath=input_img_base64)
        get_image_from_base64(input_img_base64,output_folder,output_filename)
        self.check_remove("base_image",output_folder,output_filename,input_img_base64)
    
    def test_corrupt_to_xlsx(self):
        # return -1
        output_folder=r'tests'
        output_filename="demo"
        input_file_str='tests\demo_corrupt.xls'
        sheet_name='Sheet1'
        excel_change_corrupt_xls_to_xlsx(input_file_str, sheet_name)
        excel_change_corrupt_xls_to_xlsx(input_file_str, sheet_name, output_folder=output_folder)
        excel_change_corrupt_xls_to_xlsx(input_file_str, sheet_name, output_filename=output_filename)
        excel_change_corrupt_xls_to_xlsx(input_file_str, sheet_name, output_folder=output_folder, output_filename=output_filename)
    
    def test_colored_html(self):
        # return -1

        #String format
        input_file_str="tests\demo_Coloured.xlsx"
        output_folder_str='tests'
        output_filename="demo_color"
        default_out_path=r"C:\Users\Public\PyBots\My-DOST\Converters Folder"
        excel_to_colored_html(input_file_str)
        self.check_remove("colored_html",input_filepath= input_file_str)
        excel_to_colored_html(input_file_str, output_folder=output_folder_str)
        self.check_remove("colored_html",output_folder=output_folder_str , input_filepath= input_file_str)
        excel_to_colored_html(input_file_str, output_filename=output_filename)
        self.check_remove("colored_html", default_out_path, output_filename, input_file_str)
        excel_to_colored_html(input_file_str, output_folder=output_folder_str, output_filename=output_filename)
        self.check_remove("colored_html", output_folder_str, output_filename, input_file_str)

        ##Path Format
        input_file_path=r"tests\demo_Coloured.xlsx"
        output_folder_path=r'tests'

        excel_to_colored_html(input_file_path)
        self.check_remove("colored_html",input_filepath= input_file_str)
        excel_to_colored_html(input_file_path, output_folder=output_folder_path)
        self.check_remove("colored_html",output_folder=output_folder_str , input_filepath= input_file_str)
        excel_to_colored_html(input_file_path, output_filename=output_filename)
        self.check_remove("colored_html", default_out_path, output_filename, input_file_str)
        excel_to_colored_html(input_file_path, output_folder=output_folder_path, output_filename=output_filename)
        self.check_remove("colored_html", output_folder_str, output_filename, input_file_str)
        



if __name__== "__main__":
    unittest.main()

