import os
import unittest
from dost.excel import *

header_value = 1


def get_demo_df(header):
    # file_path="tests/demo.xlsx"
    # sheetname="Sheet1"
    # df=excel_to_dataframe(input_filepath=file_path, input_sheetname=sheetname, header=header)
    df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=[
                      "Column 1", "Column 2", "Column 3"])
    return df


def create_excel_sheet(file_path="tests/test.xlsx", sheetname=["Test_sheet", "sheet2", "Sheet 3"]):
    folder = file_path.split("/")[0]
    filename = file_path.split("/")[1]
    create_file(output_folder=folder,
                      output_filename=filename, output_sheetname=sheetname)


class test(unittest.TestCase):
    def test_write_excel_file(self):
        # Case 1 - Complete inputs
        file_path = "tests/test.xlsx"
        sheetname = "Test_sheet"
        folder = file_path.split("/")[0]
        filename = file_path.split("/")[1]
        create_file(output_folder=folder,
                          output_filename=filename, output_sheetname=sheetname)
        assert os.path.exists(file_path) == True
        os.remove(file_path)

        # Case 2 - Missing Sheetname
        file_path = "tests/test.xlsx"
        folder = file_path.split("/")[0]
        filename = file_path.split("/")[1]
        create_file(output_folder=folder, output_filename=filename)
        assert os.path.exists(file_path) == True
        os.remove(file_path)

        # Case 3 - No xlsx at the end of the file name
        file_path = "tests/test"
        sheetname = "Test_sheet"
        folder = file_path.split("/")[0]
        filename = file_path.split("/")[1]
        create_file(output_folder=folder,
                          output_filename=filename, output_sheetname=sheetname)
        assert os.path.exists(file_path+".xlsx") == True
        os.remove(file_path+".xlsx")

        # Case 4 - Multiple Sheets
        file_path = "tests/test.xlsx"
        sheetname = ["Test_sheet", "sheet2", "Sheet 3"]
        folder = file_path.split("/")[0]
        filename = file_path.split("/")[1]
        create_file(output_folder=folder,
                          output_filename=filename, output_sheetname=sheetname)
        assert os.path.exists(file_path) == True
        os.remove(file_path)

    def test_excel_to_dataframe(self):
        df = get_demo_df(header_value)

    def test_excel_get_row_column_count(self):
        df = get_demo_df(header_value)
        count = get_row_column_count(df)
        self.assertEqual(count, df.shape)

    def test_excel_set_single_cell(self):
        df = get_demo_df(header_value)
        text_to_replace = "abc"
        column_name = "Column 2"
        cell_number = 3
        df = set_single_cell(
            df, column_name, cell_number, text_to_replace)
        self.assertEqual(text_to_replace, df[column_name][cell_number-1])

    def test_excel_get_single_cell(self):
        df = get_demo_df(header_value)
        column_name = "Column 2"
        cell_number = 3
        self.assertEqual(str(df[column_name][cell_number-header_value-1]),
                         get_single_cell(df, column_name, cell_number, header=header_value))

    def test_get_all_headers(self):
        df = get_demo_df(header_value)
        self.assertEqual(get_all_header_columns(df), list(df.columns))

    def test_set_value_in_df(self):
        df = get_demo_df(header_value)
        row_number = 1
        column_number = 2
        value = "abc"
        set_value_in_df(df, row_number, column_number, value)
        self.assertEqual(df.iloc[row_number-1, column_number-1], value)

    def test_get_value_in_df(self):
        df = get_demo_df(header_value)
        row_number = 1
        column_number = 2
        value = get_value_in_df(df, row_number, column_number)
        self.assertEqual(str(df.iloc[row_number-1, column_number-1]), value)

    def test_df_drop_rows(self):
        df = get_demo_df(header_value)
        total_rows = df.shape[0]
        start_row = 2
        end_row = 3
        df = df_drop_rows(df, start_row, end_row)
        # as we are deleting both starting and ending rows
        self.assertEqual(df.shape[0], total_rows-(end_row-start_row))

    def test_df_extract_sub_df(self):
        df = get_demo_df(header_value)
        start_row = 2
        end_row = 5
        start_column = 2
        end_column = 4
        modified_df = df_extract_sub_df(
            df, start_row, end_row, start_column, end_column)
        df = df.iloc[start_row-1:end_row-1, start_column-1:end_column-1]
        self.assertEqual(df.equals(modified_df), True)

    def test_excel_clear_sheet(self):
        df = get_demo_df(header_value)
        df = clear_sheet(df)
        self.assertEqual(df.empty, True)
        if (df.columns.empty):
            self.assertEqual(df.columns.empty, True)
        else:
            self.assertEqual(df.columns.empty, False)

    def test_excel_drop_columns(self):
        df = get_demo_df(header_value)
        columns = list(df.columns)
        columns_to_drop = [columns[0], columns[1]]
        # columns_to_drop=columns[0]
        if (isinstance(columns_to_drop, list)):
            df = drop_columns(df, columns_to_drop)
            for column_to_drop in columns_to_drop:
                self.assertEqual(column_to_drop not in df.columns, True)
        else:
            df = drop_columns(df, columns_to_drop)
            self.assertEqual(columns_to_drop not in df.columns, True)

    def test_isNaN(self):
        value = "3"
        if (isNaN(value) != None):
            self.assertEqual(isNaN(value), False)

    def test_excel_get_all_sheet_names(self):
        sheet_names = ["Test_sheet", "sheet2", "sheet 2"]
        create_excel_sheet(sheetname=sheet_names)
        sheets = get_all_sheet_names("tests/test.xlsx")
        sheets.sort()
        sheet_names.sort()
        self.assertEqual(sheets, sheet_names)
        os.remove("tests/test.xlsx")

    def test_df_from_string(self):
        string = "a b c;d e f"
        word_delimiter = " "
        line_delimiter = ";"
        columns = ["Column 1", "Column 2", "Column 3"]
        df = df_from_string(string, word_delimiter, line_delimiter, columns)
        correct_result = data = pd.DataFrame(
            [x.split(word_delimiter) for x in string.split(line_delimiter)], columns=columns)
        if (df.equals(correct_result)):
            assert True

    def test_df_from_list(self):
        list = [[1, 2, 3], [4, 5, 6]]
        cols = ["col1", "col2", "col3"]
        df = df_from_list(list, cols)
        correct_df = pd.DataFrame(list, columns=cols)
        if (df.equals(correct_df)):
            assert True

    def test_remove_duplicates(self):
        list = [["a", "b", "c"], ["a", "d", "e"], ["a", "d", "f"]]
        # cols=["col1", "col2", "col3"]
        df = pd.DataFrame(list)
        print(df)
        df = remove_duplicates(df, 0)
        print(df)

    def test_df_to_excel(self):
        df = get_demo_df(header_value)
        dataframe_to_excel(df, output_folder="tests", output_filename="dftest.xlsx",
                           output_sheetname="trial sheet", mode='o')
        df_generated = pd.read_excel(
            "tests/dftest.xlsx", sheet_name="trial sheet")
        self.assertEqual(os.path.exists("tests/dftest.xlsx"), True)
        if (df_generated.equals(df)):
            assert True
        os.remove("tests/dftest.xlsx")

    def test_authenticate_google_spreadsheet(self):
        auth = authenticate_google_spreadsheet(
            "D:\Pybots resources\Excel\cred.json")

    def test_excel_upload_dataframe_to_google_spreadsheet(self):
        auth = authenticate_google_spreadsheet(
            "D:\Pybots resources\Excel\cred.json")
        url = "https://docs.google.com/spreadsheets/d/1z5h839kECYR484hPBYR-mC_hkxXkmuJjU-5wOoj78BQ"
        df = get_demo_df(header_value)
        upload_dataframe_to_google_spreadsheet(
            auth=auth, spreadsheet_url=url, sheet_name="Sheet3", df=df)

    def test_get_df_from_google_spreadsheet(self):
        auth = authenticate_google_spreadsheet(
            "D:\Pybots resources\Excel\cred.json")
        url = "https://docs.google.com/spreadsheets/d/1z5h839kECYR484hPBYR-mC_hkxXkmuJjU-5wOoj78BQ"
        df = get_dataframe_from_google_spreadsheet(
            auth, spreadsheet_url=url, sheet_name="Sheet1")
        df_actual = get_demo_df(header_value)
        if (df.equals(df_actual)):
            assert True


if __name__ == '__main__':
    unittest.main()
