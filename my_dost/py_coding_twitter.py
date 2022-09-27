from pathlib import WindowsPath
from typing import List, Union
from helpers import dostify

@dostify(errors=[(FileNotFoundError,'')])
def pdf_to_audio(pdf_file_path:Union[str, WindowsPath]) -> None:
    """
    Reads aloud the given PDF file.
    Args:
        pdf_file_path (Union[str, WindowsPath]): The path to the PDF file.
        
    Returns:
        None
    
    Examples:
        >>> pdf_to_audio('tests\\demo2.pdf')

    """

    # Import Section
    import PyPDF2, pyttsx3, os

    # Validation section
    path = os.path.abspath(pdf_file_path)
    if not os.path.isfile(path):
        raise FileNotFoundError(f'File not found: {path}')

    # Code Section
    pdf_file_path = open(pdf_file_path, 'rb')

    #Creating a pdf reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_path)

    #Get speech engine ready
    speaker = pyttsx3.init()

    for page in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
    
    pdf_file_path.close()
    speaker.stop()

# python -m doctest my_dost\py_coding_twitter.py -v
