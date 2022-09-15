import os
from pathlib import WindowsPath
from helpers import dostify
output_folder_path = os.path.join(
    os.path.abspath(r'C:\Users\Public\PyBots'), 'My-DOST', 'Converters Folder')

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

@dostify(errors=[])
def convert_csv_to_excel(input_file:WindowsPath, output_folder:WindowsPath, output_filename:str,contains_headers:bool=True,sep:str=","):
    # Import section
    from my_dost.CrashHandler import report_error
    import os
    from pathlib import Path
    import pandas as pd
    import datetime

    # Logic section
    if not input_file:
        raise Exception("CSV File name cannot be empty")

    if not output_folder:
        output_folder = output_folder_path

    if not output_filename:
        output_filename = "excel_" + \
            str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".xlsx"
    else:
        output_filename = output_filename.split(".")[0] + ".xlsx"
    if not sep:
        raise Exception("Separator cannot be empty")

    excel_file_path = os.path.join(
        output_folder, output_filename)
    excel_file_path = Path(excel_file_path)
    writer = pd.ExcelWriter(excel_file_path)
    headers='infer'
    if contains_headers==False:
        headers=None
    df = pd.read_csv(input_file, sep=sep,header=headers)
    df.to_excel(writer, sheet_name='Sheet1', index=False,header=contains_headers)
    writer.save()

        
@dostify(errors=[])
def get_image_from_base64(input_text:str, output_folder:WindowsPath, output_filename:str):
    # Import Section
    import base64
    import os
    import datetime
    from my_dost.CrashHandler import report_error


    # Logic Section
    if not input_text:
        raise Exception("Image base64 string cannot be empty")

    if not output_folder:
        output_folder = output_folder_path

    if not output_filename:
        output_filename = "image_" + \
            str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".png"
    else:
        if not str(output_filename).endswith(".*"):
            output_filename = output_filename + ".png"
        else:
            output_filename = output_filename

    input_text = bytes(input_text, 'utf-8')
    if os.path.exists(output_folder):
        try:
            img_binary = base64.decodebytes(input_text)
            with open(os.path.join(output_folder, output_filename), "wb") as f:
                f.write(img_binary)
        except Exception as ex:
            report_error(ex)
            error = ex
    else:
        raise Exception("Image folder path does not exist")

@dostify(errors=[])
def convert_image_to_base64(input_file:WindowsPath):

    # Import section
    import base64
    import os
    from my_dost.CrashHandler import report_error


    # Logic section
    if not input_file:
        raise Exception("Image file name cannot be empty")

    if os.path.exists(input_file):
        with open(input_file, "rb") as f:
            data = base64.b64encode(f.read())
    else:
        raise Exception("Image file does not exist")
    return data
# print(image_to_base64(r"C:\Users\PyBots\Desktop\images\image.jpg"))

@dostify(errors=[])
def excel_change_corrupt_xls_to_xlsx(input_file:WindowsPath, input_sheetname:str, output_folder:WindowsPath, output_filename:str):

    # Import section
    import os
    from my_dost.CrashHandler import report_error
    import io
    from xlwt import Workbook
    from xls2xlsx import XLS2XLSX
    import datetime
    from pathlib import Path



    # Logic section
    if not input_file:
        raise Exception("XLS File name cannot be empty")

    if not input_sheetname:
        raise Exception("XLS Sheet name cannot be empty")

    if not output_folder:
        output_folder = output_folder_path

    if not output_filename:
        output_filename = os.path.join(output_folder, str(Path(input_file).stem), str(
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".xlsx")
    else:
        output_filename = output_filename.split(".")[0] + ".xlsx"
        output_filename = os.path.join(
            output_folder, str(output_filename))

    # Opening the file
    file1 = io.open(input_file, "r")
    data = file1.readlines()

    # Creating a workbook object
    xldoc = Workbook()
    # Adding a sheet to the workbook object
    sheet = xldoc.add_sheet(input_sheetname, cell_overwrite_ok=True)
    # Iterating and saving the data to sheet
    for i, row in enumerate(data):
        # Two things are done here
        # Removing the '\n' which comes while reading the file using io.open
        # Getting the values after splitting using '\t'
        for j, val in enumerate(row.replace('\n', '').split('\t')):
            sheet.write(i, j, val)

    # Saving the file as a normal xls excel file
    xldoc.save(input_file)

    # checking the downloaded file is present or not
    if os.path.exists(input_file):
        # converting xls to xlsx
        x2x = XLS2XLSX(input_file)
        x2x.to_xlsx(output_filename)

@dostify(errors=[])
def excel_convert_xls_to_xlsx(input_file:WindowsPath, output_folder:WindowsPath, output_filename:str):
    # Import section
    from my_dost.CrashHandler import report_error
    import os
    from xls2xlsx import XLS2XLSX
    from pathlib import Path
    import datetime


    # Logic section
    if not input_file:
        raise Exception("XLS File name cannot be empty")

    if not output_folder:
        output_folder = output_folder_path

    if not output_filename:
        output_filename = os.path.join(output_folder, str(Path(input_file).stem), str(
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".xlsx")
    else:
        output_filename = os.path.join(
            output_folder, str(output_filename)+".xlsx")

    # Checking the path and then converting it to xlsx file
    if os.path.exists(input_file):
        # converting xls to xlsx
        x2x = XLS2XLSX(input_file)
        x2x.to_xlsx(output_filename)

@dostify(errors=[])
def convert_image_jpg_to_png(input_filepath:WindowsPath, output_folder:WindowsPath, output_filename:str):

    # import section

    from pathlib import Path
    import os
    from PIL import Image
    import datetime

    # Logic section
    if not input_filepath:
        raise Exception("Enter the valid input image path")
    if not output_folder:
        output_folder = output_folder_path
    if not output_filename:
        output_filename = os.path.join(output_folder, str(Path(input_filepath).stem), str(
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".png")
    else:
        output_filename = os.path.join(output_folder, str(output_filename) + ".png")

    im = Image.open(input_filepath)
    rgb_im = im.convert('RGB')
    rgb_im.save(output_filename)


@dostify(errors=[])
def convert__image_png_to_jpg(input_filepath:WindowsPath, output_folder:WindowsPath, output_filename:str):


    # import section

    from pathlib import Path
    import os
    from PIL import Image
    import datetime

   
    # Logic section

    if not input_filepath:
        raise Exception("Enter the valid input image path")
    if not output_folder:
        output_folder = output_folder_path
    if not output_filename:
        output_filename = os.path.join(output_folder, str(Path(input_filepath).stem), str(
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".jpg")
    else:
        output_filename = os.path.join(output_folder, str(output_filename) + ".jpg")

    im = Image.open(input_filepath)
    rgb_im = im.convert('RGB')
    rgb_im.save(output_filename)

   

@dostify(errors=[])
def excel_to_colored_html(input_filepath:WindowsPath, output_folder:WindowsPath, output_filename:str):

    # import section
    from pathlib import Path
    from xlsx2html import xlsx2html
    import datetime

    
    
    if not input_filepath:
        raise Exception("Please provide the excel path")
    if not output_folder:
        output_folder = output_folder_path
    if not output_filename:
        output_filename = os.path.join(output_folder, str(Path(input_filepath).stem)+'_'+str(
            datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".html")
    else:
        output_filename = os.path.join(
            output_folder, output_filename+'.html')

    xlsx2html(input_filepath, output_filename)
    os.startfile(output_folder)




# excel_to_colored_html(input_filepath=r"C:\Users\PyBots\Desktop\dummy.xlsx",
#                       output_folder=r"C:\Users\PyBots\My AutoPylot", output_filename="output")
