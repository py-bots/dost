from http.client import InvalidURL
from pathlib import WindowsPath
from typing import Dict, List, Union
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
        >>> pdf_to_audio('tests\\demo1.pdf')

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


@dostify(errors=[(InvalidURL,'')])
def is_url_valid(url:str) -> bool:
    """
    Checks if the given URL is valid.
    Args:
        url (str): The URL to check.
        
    Returns:
        bool: True if the URL is valid, False otherwise.
    
    Examples:
        >>> is_url_valid('https://www.google.com')
        True
        >>> is_url_valid('https://www.google.com/invalid')
        False

    """
    # Import Section
    from urllib.request import urlopen

    # Validation section
    if not isinstance(url, str):
        raise TypeError(f'Expected str, got {type(url)}')

    # Code Section
    try:
        urlopen(url)
        return True
    except:
        return False


@dostify(errors=[(InvalidURL,'')])
def generate_qr_code(url:str, show_output: bool = True) -> None:
    """
    Generates a QR code from the given URL.
    Args:
        url (str): The URL to be converted to QR code.
        
    Returns:
        None
    
    Examples:
        >>> generate_qr_code('https://www.pybots.ai')
        
        
    """
    # >>> generate_qr_code('https://www.google.com', show_output=False)

    # Import Section
    import pyqrcode
    from pyqrcode import QRCode
    import png
    from pathlib import Path
    import os

    # Code Section
    if is_url_valid(url):            
        url = pyqrcode.create(url)
        url.png('tests\\my_qr_code.png', scale=8)

        if show_output:
            os.startfile(Path('tests\\my_qr_code.png'))

    else:
        raise InvalidURL(f'Invalid URL: {url}')

@dostify(errors=[(FileNotFoundError,'')])
def decode_qr_code(image_path:Union[str, WindowsPath]) -> str:
    """
    Decodes the QR code from the given image.
    Args:
        image_path (Union[str, WindowsPath]): The path to the image file.
        
    Returns:
        str: The decoded text.
    
    Examples:
        >>> decode_qr_code('tests\\my_qr_code.png')
        'https://www.pybots.ai'
        
    """

    # Import Section
    import pyzbar.pyzbar as pyzbar
    from PIL import Image
    import os

    # Validation section
    path = os.path.abspath(image_path)
    if not os.path.isfile(path):
        raise FileNotFoundError(f'File not found: {path}')

    # Code Section
    decoded_objects = pyzbar.decode(Image.open(path))
    return decoded_objects[0].data.decode('ascii')  


@dostify(errors=[(FileNotFoundError,'')])
def create_gifs_from_images(image_paths:List[Union[str, WindowsPath]], output_path:Union[str, WindowsPath], show_output: bool = True) -> None:
    """
    Creates GIFs from the given images.
    Args:
        image_paths (List[Union[str, WindowsPath]]): The paths to the images.
        output_path (Union[str, WindowsPath]): The path to the output GIF file.
        show_output (bool): Whether to show the output GIF file or not.
        
    Returns:
        None
    
    Examples:
        >>> create_gifs_from_images(['tests\\demo2.png', 'tests\\demo.png'], 'tests\\my_gif.gif')
        >>> create_gifs_from_images(['tests\\demo2.png', 'tests\\demo.png'], 'tests\\my_gif.gif', show_output=False)
        
    """

    # Import Section
    import imageio
    import os

    # Validation section
    for path in image_paths:
        path = os.path.abspath(path)
        if not os.path.isfile(path):
            raise FileNotFoundError(f'File not found: {path}')

    # Code Section
    images = []
    for path in image_paths:
        images.append(imageio.imread(path))
    imageio.mimsave(output_path, images)

    if show_output:
        os.startfile(output_path)

@dostify(errors='')
def get_address_from_zipcode(zipcode:str) -> str:
    """
    Gets the address from the given zipcode.
    Args:
        zipcode (str): The zipcode to get the address from.
        
    Returns:
        str: The address.
    
    # Examples:
        >>> get_address_from_zipcode('581106')
        'Byadagi taluk, Haveri district, Karnataka, 581106, India'
        
    """

    # Import Section
    from geopy import Nominatim

    try:
        # Code Section
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode(zipcode)
        return location.address
    except:
        return 'Invalid Zipcode'

@dostify(errors=[(FileNotFoundError,'')])
def download_youtube_videos(urls:List[str], output_path:Union[str, WindowsPath], hd_video: bool = True, show_output: bool = False) -> None:
    """
    Downloads the given YouTube videos.
    Args:
        urls (List[str]): The URLs of the YouTube videos.
        output_path (Union[str, WindowsPath]): The path to the output folder.
        show_output (bool): Whether to show the output folder or not.
        
    Returns:
        None
    
    Examples:
        # >>> download_youtube_videos(['https://www.youtube.com/watch?v=9bZkp7q19f0'], 'tests\\my_videos')
        >>> download_youtube_videos(['https://www.youtube.com/watch?v=80tihBplovU&t=3s'], 'tests\\my_videos', show_output=True)
        
    """

    # Import Section
    from pytube import YouTube
    import os

    # Validation section
    if not os.path.isdir(output_path):
        #create the folder
        os.mkdir(output_path)
        
    # Code Section
    for url in urls:
        if is_url_valid(url):
            yt = YouTube(url)
            #download HD video
            if hd_video:
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path)
            else:
                yt.streams.first().download(output_path)
        
    if show_output:
        os.startfile(output_path)

@dostify(errors=[(InvalidURL,'')])
def url_shortner(url:str) -> str:
    """
    Shortens the given URL.
    Args:
        url (str): The URL to be shortened.
        show_output (bool): Whether to show the output or not.
        
    Returns:
        str: The shortened URL.
        
    Examples:
        >>> url_shortner('https://www.pybots.ai')
        'https://tinyurl.com/2khuxcvx'
        
    """

    # Import Section
    import pyshorteners
    import os

    # Code Section
    s = pyshorteners.Shortener()

    if is_url_valid(url):
        short_url = s.tinyurl.short(url)
        return short_url
    else:
        raise InvalidURL(f'Invalid URL: {url}')


@dostify(errors=[(FileNotFoundError,'')])
def convert_csv_to_json(csv_path:Union[str, WindowsPath], show_output: bool = True) -> None:
    """
    Converts the given CSV file to JSON.
    Args:
        csv_path (Union[str, WindowsPath]): The path to the CSV file.
        show_output (bool): Whether to show the output or not.
        
    Returns:
        None
    
    Examples:
        >>> convert_csv_to_json('tests\\demo.csv')
        >>> convert_csv_to_json('tests\\demo.csv', show_output=True)
 
    """

    # Import Section
    import pandas as pd
    import os

    # Validation section
    path = os.path.abspath(csv_path)
    if not os.path.isfile(path):
        raise FileNotFoundError(f'File not found: {path}')

    # Code Section
    df = pd.read_csv(path)
    df.to_json(path.replace('.csv','.json'), orient='records')

    if show_output:
        os.startfile(path.replace('.csv','.json'))

# zip all the files of a folder
@dostify(errors=[(FileNotFoundError,'')])
def zip_folder(folder_path:Union[str, WindowsPath], show_output: bool = True) -> None:
    """
    Zips the given folder.
    Args:
        folder_path (Union[str, WindowsPath]): The path to the folder.
        show_output (bool): Whether to show the output or not.
        
    Returns:
        None
    
    Examples:
        >>> zip_folder('tests\\zip-test')
        >>> zip_folder('tests\\zip-test', show_output=True)
    """

    # Import Section
    import shutil
    import os

    # Validation section
    path = os.path.abspath(folder_path)
    if not os.path.isdir(path):
        raise FileNotFoundError(f'Folder not found: {path}')
    
    # Code Section
    shutil.make_archive(path, 'zip', path)

    if show_output:
        os.startfile(path+'.zip')
    
@dostify(errors=[(FileNotFoundError,'')])
def text_to_handwriting(text: str, output_path:Union[str, WindowsPath], show_output: bool = True) -> None:
    """
    Converts the given text to handwriting.
    Args:
        text (str): The text to convert to handwriting.
        output_path (Union[str, WindowsPath]): The path to the output folder.
        show_output (bool): Whether to show the output folder or not.
        
    Returns:
        None
    
    Examples:
        >>> text_to_handwriting('Hello World', 'tests\\my_handwritten_text.png')
        >>> text_to_handwriting('Hello MMV', 'tests\\my_handwritten_text.png', show_output=True)
 
    """

    # Import Section
    import pywhatkit
    import os

    # Validation section
    path = os.path.abspath(output_path)

    # Code Section
    pywhatkit.text_to_handwriting(text, save_to=path)

    if show_output:
        os.startfile(path)

@dostify(errors=[(FileNotFoundError,'')])
def image_watermark(image_path:Union[str, WindowsPath],watermark_text:str, output_path:Union[str, WindowsPath], show_output: bool = True) -> None:
    """
    Adds a watermark to the given image.
    Args:
        image_path (Union[str, WindowsPath]): The path to the image.
        watermark_text (str): The text to add as watermark.
        output_path (Union[str, WindowsPath]): The path to the output folder.
        show_output (bool): Whether to show the output folder or not.
        
    Returns:
        None
    
    Examples:
        >>> image_watermark('tests\\demo3.jpeg', 'Hello World', 'tests\\my_watermarked_image1.png')
        >>> image_watermark('tests\\demo3.jpeg', 'Hi World', 'tests\\my_watermarked_image2.png', show_output=True)
        
    """

    # Import Section
    from PIL import Image, ImageDraw, ImageFont
    import os


    # Validation section
    path = os.path.abspath(image_path)
    if not os.path.isfile(path):
        raise FileNotFoundError(f'File not found: {path}')

    img = Image.open(image_path)

    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('arial.ttf', 50)

    textwidth, textheight = draw.textsize(watermark_text, font)

    #color as grey
    color = 'rgb(114, 114, 114)'

    # add opacity to rgb
    
    width, height = img.size

    x = width/2 - textwidth/2
    y = height - textheight - 50

    draw.text((x, y), watermark_text, font=font, fill=color, align='center')

    img.save(output_path)

    if show_output:
        os.startfile(output_path)


@dostify()
def track_phone_number(phone_number: str) -> Dict[str, str]:
    """
    Tracks the given phone number.
    Args:
        phone_number (str): The phone number to track.
        output_path (Union[str, WindowsPath]): The path to the output folder.
        show_output (bool): Whether to show the output folder or not.
        
    Returns:
        None
    
    Examples:
        >>> track_phone_number('+919876543210')
        {'location': 'India', 'carrier': 'Airtel'}

        >>> track_phone_number('+918500369435') 
        {'location': 'India', 'carrier': 'BSNL MOBILE'}
        
    """

    # Import Section
    import phonenumbers
    from phonenumbers import geocoder
    from phonenumbers import carrier

    a = phonenumbers.parse(phone_number)

    phonenumber = phonenumbers.parse(phone_number)

    carrirer_name = carrier.name_for_number(phonenumber, "en")

    location = geocoder.description_for_number(phonenumber, "en")

    result = {
        'location': location,
        'carrier': carrirer_name
    }

    return result

@dostify(errors=[(FileNotFoundError,'')])
def images_to_pdf(image_paths: List[Union[str, WindowsPath]], output_path:Union[str, WindowsPath], show_output: bool = True) -> None:
    """
    Converts the given images to pdf.
    Args:
        image_paths (List[Union[str, WindowsPath]]): The paths to the images.
        output_path (Union[str, WindowsPath]): The path to the output folder.
        show_output (bool): Whether to show the output folder or not.
        
    Returns:
        None
    
    Examples:
        >>> images_to_pdf(['tests\\demo.png', 'tests\\demo3.jpeg'], 'tests\\my_pdf.pdf')
        >>> images_to_pdf(['tests\\my_qr_code.png', 'tests\\demo3.jpeg'], 'tests\\my_pdf.pdf', show_output=True)
        
    """

    # Import Section
    from PIL import Image
    import os

    # Validation section
    paths = [os.path.abspath(path) for path in image_paths]
    for path in paths:
        if not os.path.isfile(path):
            raise FileNotFoundError(f'File not found: {path}')

    # Code Section
    images = [Image.open(image) for image in paths]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset,0))
        x_offset += im.size[0]

    new_im.save(output_path)

    if show_output:
        os.startfile(output_path)

@dostify(errors=[(FileNotFoundError,''), (ValueError, '')])
def generate_bar_code(data: int, output_path:Union[str, WindowsPath], show_output: bool = False) -> None:
    """
    Generates a bar code for the given data.
    Args:
        data (str): The data to generate bar code for.
        output_path (Union[str, WindowsPath]): The path to the output folder.
        show_output (bool): Whether to show the output folder or not.
        
    Returns:
        None
    
    Examples:
        >>> generate_bar_code(5901234123456, 'tests\\my_bar_code')
        >>> generate_bar_code(5901234123456, 'tests\\my_bar_code', show_output=True)
    
    """

    # Import Section
    import barcode
    from barcode.writer import ImageWriter
    import os

    # Validation section
    data = str(data)

    #check length of data
    if len(data) < 12:
        raise ValueError('EAN must have 12 digits, not {}'.format(len(data)))

    path = os.path.abspath(output_path)

    # Code Section
    EAN = barcode.get_barcode_class('ean13')
    ean = EAN(data, writer=ImageWriter())
    fullname = ean.save(path)
    
    if show_output:
        os.startfile(fullname)
    
# Open source Python library converting pdf to docx
@dostify(errors=[(FileNotFoundError,'')])
def convert_pdf_to_docx(pdf_path: Union[str, WindowsPath], output_path:Union[str, WindowsPath], show_output: bool = False) -> None:
    """
    Converts the given pdf to docx.
    Args:
        pdf_path (Union[str, WindowsPath]): The path to the pdf.
        output_path (Union[str, WindowsPath]): The path to the output folder.
        show_output (bool): Whether to show the output folder or not.

    Returns:
        None

    Examples:
        >>> convert_pdf_to_docx('tests\\demo1.pdf', 'tests\\demo.docx')
        >>> convert_pdf_to_docx('tests\\demo1.pdf', 'tests\\demo.docx', show_output=True)
        
    """
    # Import Section
    from pdf2docx import Converter
    import os
    
    # Validation section
    pdf_path = os.path.abspath(pdf_path)
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f'File not found: {pdf_path}')


    # Code Section
    cv = Converter(pdf_path)
    cv.convert(output_path, start=0, end=None)
    cv.close()

    if show_output:
        os.startfile(output_path)
    
# python -m doctest my_dost\py_coding_twitter.py -v
# https://twitter.com/clcoding
