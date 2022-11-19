"""
Converter module for dost. This module contains functions to convert between different data types.

Examples:
    >>> from dost import converter
    >>> converter.csv_to_excel(input_filepath='tests\\demo.csv', output_folder='tests')
    >>> converter.base64_to_image(input_filepath='tests\\demo.txt')
    >>> converter.image_to_base64(input_filepath='tests\\demo.png', output_folder='tests')
    >>> converter.jpg_to_png(input_filepath='tests\\demo.jpg', output_folder='tests')
    >>> converter.png_to_jpg(input_filepath='tests\\demo.png', output_folder='tests')
    >>> converter.excel_to_html(input_filepath='tests\\demo.xlsx', output_folder='tests')


The module contains the following functions:

- `csv_to_excel(input_filepath, output_folder, output_filename, contains_headers, sep)`: Convert a CSV file to an Excel file.
- `excel_to_html(input_filepath, output_folder, output_filename)`: Convert an Excel file to an HTML file.
- `image_to_base64(input_filepath)`: Convert an image to a base64 string.
- `base64_to_image(input_text, output_folder, output_filename)`: Convert a base64 string to an image.
- `jpg_to_png(input_filepath, output_folder, output_filename)`: Convert a JPG image to a PNG image.
- `png_to_jpg(input_filepath, output_folder, output_filename)`: Convert a PNG image to a JPG image.

"""


import os
from pathlib import WindowsPath
from dost.helpers import dostify
from typing import Union, List

# if not os.path.exists(output_folder_path):
#     os.makedirs(output_folder_path)


@dostify(errors=[(FileNotFoundError, ''),(OSError,'')])
def csv_to_excel(input_filepath: Union[str, WindowsPath], output_folder: Union[str, WindowsPath], output_filename: str = "", contains_headers: bool = True, sep: str = ","):
    """Convert a CSV file to an Excel file.

    Args:
        input_filepath (str || WindowsPath): The path to the CSV file.
        output_folder (str || WindowsPath): The path to the output folder.
        output_filename (str): The name of the output file.
        contains_headers (bool): Whether the CSV file contains headers.
        sep (str): The separator used in the CSV file.

    Examples:
        >>> converter.csv_to_excel(input_filepath='tests\\demo.csv', output_folder='tests')


    """
    # Import Section
    import os
    from pathlib import Path
    import pandas as pd
    import datetime

    output_folder = Path(str(output_folder))
    # Code Section
    if not input_filepath:
        raise ValueError("CSV File name cannot be empty")

    if not output_folder:
        raise ValueError("Output folder cannot be empty")

    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"File not found at path {input_filepath}")

    os.makedirs(output_folder,exist_ok=True)

    if not output_filename:
        output_filename = f"converted {str(Path(input_filepath).stem)}.xlsx"
        if os.path.exists(os.path.join(output_folder, output_filename)):
            output_filename = f"converted {str(Path(input_filepath).stem)} " + str(
                datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + ".xlsx"

    elif (output_filename.endswith(".xlsx")):
        output_filename = output_filename
    else:
        output_filename += ".xlsx"
    if not sep:
        raise ValueError("Separator cannot be empty")

    excel_file_path = os.path.join(
        output_folder, output_filename)
    excel_file_path = Path(excel_file_path)
    writer = pd.ExcelWriter(excel_file_path)
    headers = 'infer' if contains_headers else None
    df = pd.read_csv(input_filepath, sep=sep, header=headers)
    df.to_excel(writer, sheet_name='Sheet1',
                index=False, header=contains_headers)
    writer.save()
    writer.close()


@dostify(errors=[(FileNotFoundError, '')])
def excel_to_html(input_filepath: Union[str, WindowsPath], output_folder: Union[str, WindowsPath], output_filename: str = ""):
    # sourcery skip: raise-specific-error
    """Converts the excel file to colored html file

    Args:
        input_filepath (str || WindowsPath): Input excel file path
        output_folder (str || WindowsPath): Output folder path
        output_filename (str): Output file name

    Examples:
        >>> converter.excel_to_html(input_filepath='tests\\demo.xlsx', output_folder='tests')
    """
    # Import Section
    from pathlib import Path
    from xlsx2html import xlsx2html
    import datetime

    output_folder = Path(output_folder)
    # Code Section
    if not input_filepath:
        raise Exception("Please provide the excel path")

    if not output_folder:
        raise Exception("Please provide the output folder path")

    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"File not found at path {input_filepath}")

    os.makedirs(output_folder,exist_ok=True)

    if output_filename:
        output_filename = os.path.join(output_folder, output_filename) if (
            output_filename.endswith(".html")) else os.path.join(output_folder, f'{output_filename}.html')

    else:
        output_filename = os.path.join(
            output_folder, f"converted {str(Path(input_filepath).stem)}.html")

        if os.path.exists(output_filename):
            output_filename = os.path.join(output_folder, ((f"converted {str(Path(input_filepath).stem)} " + str(
                datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))) + ".html"))

    xlsx2html(input_filepath, output_filename)


@dostify(errors=[(FileNotFoundError, '')])
def image_to_base64(input_filepath: Union[str, WindowsPath]) -> str:
    # sourcery skip: raise-specific-error
    """Get a base64 encoded string from an image.

    Args:
        input_filepath (str || WindowsPath): The path to the image file.

    Returns:
        str: The base64 encoded string.

    Examples:
        >>> converter.image_to_base64(input_filepath='tests\\demo.png')

    """
    # Import section
    import base64
    import os

    # Code section
    if not input_filepath:
        raise Exception("Image file name cannot be empty")

    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"File not found at path {input_filepath}")

    if os.path.exists(input_filepath):
        with open(input_filepath, "rb") as f:
            data = base64.b64encode(f.read())
    else:
        raise Exception("Image file does not exist")
    return data


@dostify(errors=[(FileNotFoundError, "")])
def base64_to_image(input_text: str, output_folder: Union[str, WindowsPath], output_filename: str = ""):
    # sourcery skip: raise-specific-error
    """Get an image from a base64 encoded string.

    Args:
        input_text (str): The base64 encoded string.
        output_folder (str || WindowsPath): The path to the output folder.
        output_filename (str default ending with .png): The name of the output file.

    Examples:
        >>> converter.base64_to_image(input_text=base_64_string, output_folder='tests')

    """
    # Import Section
    import base64
    import os
    import datetime
    from pathlib import Path

    output_folder = Path(output_folder)
    # Code Section
    if not input_text:
        raise Exception("Image base64 string cannot be empty")

    if not output_folder:
        raise Exception("Output folder cannot be empty")

    os.makedirs(output_folder,exist_ok=True)

    if not output_filename:
        output_filename = "base64_image_" + \
            str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".png"
    elif output_filename.endswith(".png") or output_filename.endswith(".jpg"):
        output_filename = output_filename

    else:
        output_filename += ".png"
    if os.path.exists(output_folder):
        input_text = bytes(input_text, 'utf-8')
        img_binary = base64.decodebytes(input_text)
        with open(os.path.join(output_folder, output_filename), "wb") as f:
            f.write(img_binary)
    else:
        raise Exception("Image folder path does not exist")


@dostify(errors=[(FileNotFoundError, '')])
def jpg_to_png(input_filepath: Union[str, WindowsPath], output_folder: Union[str, WindowsPath], output_filename: str = ""):
    # sourcery skip: raise-specific-error
    """Convert a JPG image to a PNG image.

    Args:
        input_filepath (str || WindowsPath): The path to the JPG image.
        output_folder (str || WindowsPath): The path to the output folder.
        output_filename (str): The name of the output file.

    Examples:
        >>> converter.jpg_to_png(input_filepath='tests\\demo.jpg', output_folder='tests')

    """
    # import section
    from pathlib import Path
    import os
    from PIL import Image
    import datetime

    output_folder=Path(output_folder)
    # Code section
    if not input_filepath:
        raise Exception("Enter the valid input image path")

    if not output_folder:
        raise Exception("Enter the valid output folder path")

    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"File not found at path {input_filepath}")

    os.makedirs(output_folder,exist_ok=True)

    if output_filename:
        output_filename = os.path.join(output_folder, output_filename) if output_filename.endswith(
            ".png") else os.path.join(output_folder, f"{output_filename}.png")

    else:
        output_filename = os.path.join(
            output_folder, f"converted {str(Path(input_filepath).stem)}.png")

        if (os.path.exists(output_filename)):
            output_filename = os.path.join(
                output_folder, "converted " + str(datetime.datetime.now().strftime("%Y%m%d_%H%M %S")) + ".png")
    im = Image.open(input_filepath)
    rgb_im = im.convert('RGB')
    rgb_im.save(output_filename)


@dostify(errors=[(FileNotFoundError, '')])
def png_to_jpg(input_filepath: Union[str, WindowsPath], output_folder: Union[str, WindowsPath], output_filename: str = ""):
    # sourcery skip: raise-specific-error
    """Converts the image from png to jpg format

    Args:
        input_filepath (str || WindowsPath): Input image file path
        output_folder (str || WindowsPath): Output folder path
        output_filename (str): Output file name

    Examples:
        >>> converter.png_to_jpg(input_filepath='tests\\demo.png', output_folder='tests')

    """
    # Import Section
    from pathlib import Path
    import os
    from PIL import Image
    import datetime

    output_folder=Path(output_folder)
    # Code Section
    if not input_filepath:
        raise Exception("Enter the valid input image path")

    if not os.path.exists(input_filepath):
        raise FileNotFoundError(f"File not found at path {input_filepath}")

    if not output_folder:
        raise Exception("Enter the valid output folder path")

    os.makedirs(output_folder,exist_ok=True)

    if output_filename:
        output_filename = os.path.join(output_folder, output_filename) if output_filename.endswith(
            ".jpg") else os.path.join(output_folder, f"{output_filename}.jpg")

    else:
        output_filename = os.path.join(
            output_folder, f"converted {str(Path(input_filepath).stem)}.jpg")

        if (os.path.exists(output_filename)):
            output_filename = os.path.join(
                output_folder, "converted " + str(datetime.datetime.now().strftime("%Y%m%d_%H%M %S")) + ".jpg")
    im = Image.open(input_filepath)
    rgb_im = im.convert('RGB')
    rgb_im.save(output_filename)
