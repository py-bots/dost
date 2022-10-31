from pdf import *
import unittest
import sys
sys.path.insert(0, 'dost')


class TestPDF(unittest.TestCase):

    def test_pdf_extract_all_tables(self):
        # return 0
        pdf_extract_all_tables(pdf_file_path="tests\demo2.pdf",
                               output_folder="C:\\Users\\user\\Desktop\\", output_file_name="demo")


if __name__ == '__main__':
    unittest.main()
