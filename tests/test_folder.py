# test the folder module
from my_dost import folder


def test_folder_read_text_file():
    """Test folder_read_text_file."""
    # test the function
    # create a text file
    txt_file_path = "test.txt"
    with open(txt_file_path, "w") as file:
        file.write("Hello world!")
    # read the text file
    assert folder.folder_read_text_file(txt_file_path) == "Hello world!"
