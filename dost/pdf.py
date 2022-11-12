"""
PDF module for dost. This module is used to extract data from PDF files.

Examples:
    >>> pdf.extract_all_tables(pdf_file_path="C:\\Users\\user\\Desktop\\demo.pdf",output_folder="C:\\Users\\user\\Desktop\\",output_filename = "demo")


The module contains the following functions:

- `extract_all_tables(pdf_file_path, output_folder, output_filename, table_with_borders)`: Extracts all tables from a pdf file and saves them as csv files in the specified folder.

"""


import os
from pathlib import WindowsPath
from typing import Union
from dost.helpers import dostify


@dostify(errors=[(FileNotFoundError, "")])
def extract_all_tables(pdf_file_path: Union[str, WindowsPath], output_folder: Union[str, WindowsPath], output_filename: str, table_with_borders: bool = True) -> None:
    # sourcery skip: raise-specific-error
    """Extracts all tables from a pdf file and saves them as csv files in the specified folder.

    Args:
        pdf_file_path (str,WindowsPath): Path to the pdf file.
        output_folder (str,WindowsPath): Path to the output folder.
        output_filename (str): Name of the output file.
        table_with_borders (bool, optional): Whether the table has borders. Defaults to True.

    Examples:
        >>> pdf.extract_all_tables(pdf_file_path="C:\\Users\\user\\Desktop\\demo.pdf",output_folder="C:\\Users\\user\\Desktop\\",output_filename = "demo")

    """
    # Import Section
    import pdfplumber
    import pandas as pd
    import datetime
    from pathlib import Path

    output_folder = Path(output_folder)
    # Code Section
    if not pdf_file_path:
        raise Exception("PDF file path cannot be empty")

    if not os.path.exists(pdf_file_path):
        raise FileNotFoundError(f"File not found: {pdf_file_path}")

    if not output_folder:
        raise Exception("Output folder cannot be empty")

    os.makedirs(output_folder, exist_ok=True)

    if not output_filename:
        output_filename = "pdf_" + \
            str(datetime.datetime.now().strftime("%Y%m%d_%H%M%S")) + ".xlsx"
    elif not output_filename.endswith(".xlsx"):
        output_filename += ".xlsx"

    pdf = pdfplumber.open(pdf_file_path)

    tables = []

    if table_with_borders:
        tables.extend(each_page.extract_tables() for each_page in pdf.pages)
    else:
        table_settings = {
            "vertical_strategy": "text",
            "horizontal_strategy": "text"
        }
        tables.extend(each_page.extract_tables(table_settings)
                      for each_page in pdf.pages)

    # excel writer
    writer = pd.ExcelWriter(os.path.join(
        output_folder, output_filename), engine='openpyxl')

    for table in tables:
        df_main = []
        # list of the rows to dataframe
        for i in range(len(table)):
            df = pd.DataFrame(table[i])
            df_main.append(df)

        df_main = pd.concat(df_main)
        table_index = str(tables.index(table) + 1)

        df_main.to_excel(writer, sheet_name=table_index,
                         index=False, header=False)

    writer.save()

# write a function to extract desired table from desired page of pdf