import pytesseract
import cv2
import os
import numpy as np
from PIL import Image
import re
from processing.open_image import *

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def clean_text(text):
    """
    The function `clean_text` takes a string as input and removes all non-alphabetic characters and
    whitespace, returning the cleaned text.
    
    :param text: The `text` parameter is a string that represents the text that needs to be cleaned
    :return: the cleaned text, which is a string with all non-alphabetic characters and non-space
    characters removed.
    """
    cleaned_text = re.sub(r'[^A-Za-z\sÁÉÍÓÚáéíóú]', '', text)
    return cleaned_text

def clean_number(text):
    """
    The function clean_number takes a text input and removes all non-numeric characters and spaces from
    it.
    
    :param text: The input text that needs to be cleaned
    :return: the cleaned text, which is a string with all non-numeric characters and whitespace removed.
    """
    cleaned_text = re.sub(r'[^0-9\s]', '', text)
    return cleaned_text

def clean_invalid_characters(text):
    """
    The function `clean_invalid_characters` removes any characters that are not letters, numbers, or
    whitespace from the input text.
    
    :param text: The parameter "text" is a string that represents the text that needs to be cleaned from
    invalid characters
    :return: the cleaned text, which is a string with all invalid characters removed.
    """
    cleaned_text = re.sub(r'[^A-Za-z0-9\sÁÉÍÓÚáéíóú]', '', text)
    return cleaned_text

def change_color(section):
    """
    The function "change_color" converts an image section to grayscale and applies a Gaussian blur.
    
    :param section: The "section" parameter is an image section or region that you want to change the
    color of
    :return: the section after converting it to grayscale and applying Gaussian blur.
    """
    section = cv2.cvtColor(section, cv2.COLOR_BGR2GRAY)
    section = cv2.GaussianBlur(section, (1, 1), 0)
    return section

def clean_bad_space(text_list):
    """
    The function `clean_bad_space` removes empty strings from a given list of strings.
    
    :param text_list: A list of strings that may contain empty strings or strings consisting only of
    whitespace characters
    :return: a new list that contains all the elements from the input list, except for any elements that
    are empty strings.
    """
    new_list = [elemento for elemento in text_list if elemento != '']
    return new_list

def get_text_img_identity(image_path):
    """
    The function `get_text_img_identity` takes an image path as input, extracts text from specific
    regions of the image using OCR (Optical Character Recognition), and returns the extracted text as a
    dictionary.
    
    :param image_path: The `image_path` parameter is the path to the image file that you want to process
    and extract text from. It should be a string representing the file path of the image file
    :return: a dictionary named "data" which contains the extracted information from the image. The
    dictionary has the following keys: "name", "lastname1", "lastname2", and "id". The values associated
    with these keys are the extracted text from the corresponding sections of the image.
    """
    #image = cv2.imread(image_path)
    img = np.array(Image.open(image_path))

    norm_img = np.zeros((img.shape[0], img.shape[1]))
    image = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    image = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    image = cv2.GaussianBlur(img, (1, 1), 0)

    #(X,Y, Width, Height)

    roi_number = (670, 265, 490, 110)
    roi_name = (680, 820, 600, 75)
    roi_lastname = (675, 890, 420, 110)

    number_section = image[roi_number[1]:roi_number[1]+roi_number[3], roi_number[0]:roi_number[0]+roi_number[2]]
    name_section = image[roi_name[1]:roi_name[1]+roi_name[3], roi_name[0]:roi_name[0]+roi_name[2]]
    lastname_section = image[roi_lastname[1]:roi_lastname[1]+roi_lastname[3], roi_lastname[0]:roi_lastname[0]+roi_lastname[2]]

    text_name = pytesseract.image_to_string(name_section, lang='spa', config=r'--oem 1 --psm 8')
    text_lastname = pytesseract.image_to_string(lastname_section, lang='spa', config=r'--oem 1 --psm 6')
    text_number = pytesseract.image_to_string(number_section, config=r'--oem 1 --psm 7')

    lastname_lines = clean_text(text_lastname)

    lastname_lines = lastname_lines.split("\n")
    lastname_lines = clean_bad_space(lastname_lines)
    text_name.replace('!', 'I')
    text_name = clean_text(text_name)
    text_name = re.split(r'[ \n]+', text_name)
    text_name = clean_bad_space(text_name)
    text_number = clean_number(text_number)
    text_number = text_number.split("\n")

    if len(lastname_lines) == 1 or len(lastname_lines) == 0:
        data = {
            "name": "Error",
            "lastname1": "Error",
            "lastname2": "Error",
            "id": "Error"
        }
    elif len(text_name) == 1:
        data = {
            "name": text_name[0],
            "lastname1": lastname_lines[0],
            "lastname2": lastname_lines[1],
            "id": text_number[0]
        }
    else:
        data = {
            "name": text_name[0]+ " " + text_name[1],
            "lastname1": lastname_lines[0],
            "lastname2": lastname_lines[1],
            "id": text_number[0]
        }
    
    return data

def get_text_img_stundent(image_path):
    """
    The function `get_text_img_stundent` takes an image path as input, processes the image to extract
    specific sections, and uses OCR (Optical Character Recognition) to extract text from those sections,
    returning a dictionary with the extracted data.
    
    :param image_path: The image_path parameter is the path to the image file that you want to process
    and extract text from. It should be a string representing the file path, including the file name and
    extension
    :return: a dictionary containing the extracted text from the image. The dictionary has three keys:
    "name", "date", and "id". The values associated with these keys are the extracted text for the
    corresponding sections of the image.
    """
    #image = cv2.imread(image_path)
    img = np.array(Image.open(image_path))

    norm_img = np.zeros((img.shape[0], img.shape[1]))
    image = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    image = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    image = cv2.GaussianBlur(img, (1, 1), 0)

    #(X,Y, Width, Height)
    #For the litle image
    roi_data = (1400, 960, 230, 80)
    roi_number = (560, 825, 540, 115)
    roi_name = (565, 687, 1135, 68)

    data_section = image[roi_data[1]:roi_data[1]+roi_data[3], roi_data[0]:roi_data[0]+roi_data[2]]
    number_section = image[roi_number[1]:roi_number[1]+roi_number[3], roi_number[0]:roi_number[0]+roi_number[2]]
    name_section = image[roi_name[1]:roi_name[1]+roi_name[3], roi_name[0]:roi_name[0]+roi_name[2]]

    text_name = pytesseract.image_to_string(name_section, lang='spa', config=r'--oem 1 --psm 8')
    text_number = pytesseract.image_to_string(number_section, lang='spa', config=r'--oem 1 --psm 8 digits')
    text_data = pytesseract.image_to_string(data_section, lang='spa', config=r'--oem 1 --psm 8')

    text_name = clean_text(text_name).split("\n")
    text_number = text_number.split("\n")
    text_data = text_data.split("\n")

    data = {
        "name": text_name[0],
        "date": text_data[0],
        "id": text_number[0]
    }

    return data

def get_text_img_license(image_path):
    """
    The function `get_text_img_license` takes an image path as input, extracts specific regions of
    interest from the image, applies OCR (Optical Character Recognition) to extract text from each
    region, and returns a dictionary containing the extracted text for various fields of a driver's
    license.
    
    :param image_path: The image_path parameter is the path to the image file that contains the text of
    the license
    :return: a dictionary containing the extracted information from the image. The dictionary includes
    the following keys: "number", "expedition", "birth", "expiration", "blood_type", "type", "name", and
    "code". The corresponding values are the extracted text from the respective sections of the image.
    """
    image = cv2.imread(image_path)
    
    #(X,Y, Ancho, Alto)
    roi_number = (716, 299, 510, 70)
    roi_expedition = (856, 375, 334, 60)
    roi_birth = (856, 450, 334, 60)
    roi_expiration = (856, 515, 334, 70)
    roi_blood_type = (1095, 600, 125, 70)
    roi_type = (1533, 400, 125, 82)
    roi_name = (132, 680, 1313, 100)
    roi_code = (1460, 905, 200, 56)

    section_number = image[roi_number[1]:roi_number[1]+roi_number[3], roi_number[0]:roi_number[0]+roi_number[2]]
    section_expedition = image[roi_expedition[1]:roi_expedition[1]+roi_expedition[3], roi_expedition[0]:roi_expedition[0]+roi_expedition[2]]
    section_birth = image[roi_birth[1]:roi_birth[1]+roi_birth[3], roi_birth[0]:roi_birth[0]+roi_birth[2]]
    section_expiration = image[roi_expiration[1]:roi_expiration[1]+roi_expiration[3], roi_expiration[0]:roi_expiration[0]+roi_expiration[2]]
    section_blood_type = image[roi_blood_type[1]:roi_blood_type[1]+roi_blood_type[3], roi_blood_type[0]:roi_blood_type[0]+roi_blood_type[2]]
    section_type = image[roi_type[1]:roi_type[1]+roi_type[3], roi_type[0]:roi_type[0]+roi_type[2]]
    section_name = image[roi_name[1]:roi_name[1]+roi_name[3], roi_name[0]:roi_name[0]+roi_name[2]]
    section_code = image[roi_code[1]:roi_code[1]+roi_code[3], roi_code[0]:roi_code[0]+roi_code[2]]
    
    #Change color
    section_number = change_color(section_number)
    section_expiration = change_color(section_expiration)
    
    text_number = pytesseract.image_to_string(section_number, lang='spa', config=r'--psm 8')
    
    text_expedition = pytesseract.image_to_string(section_expedition, config=r'--psm 8 digits')
    text_birth = pytesseract.image_to_string(section_birth, config=r'--psm 8 digits')
    text_expiration = pytesseract.image_to_string(section_expiration, config=r'--oem 1 --psm 8 digits', )
    text_blood_type = pytesseract.image_to_string(section_blood_type, lang='spa', config=r'--oem 1 --psm 8')
    text_type = pytesseract.image_to_string(section_type, lang='spa', config=r'--oem 1 --psm 8')
    
    text_name = pytesseract.image_to_string(section_name, lang='spa', config=r'--oem 1 --psm 8')
    text_code = pytesseract.image_to_string(section_code, lang='spa', config=r'--oem 1 --psm 8 digits')
   
    text_number = text_number.replace('L', 'I')
    text_number = re.split(r'[ \n"]+', text_number)
    text_expedition =re.split(r'[ \n"]+', text_expedition)
    text_birth = text_birth.split("\n")
    text_expiration = re.split(r'[ \n"]+', text_expiration)
    text_blood_type = text_blood_type.split(".")
    text_type = clean_invalid_characters(text_type)
    text_type = text_type.split("\n")
    text_name = re.split(r'[\n".]+', text_name)
    text_code = text_code.split("\n")
    
    data = {
        "number": text_number[0],
        "expedition": text_expedition[0],
        "birth": text_birth[0],
        "expiration": text_expiration[0],
        "blood_type" : text_blood_type[0],
        "type" : text_type[0],
        "name" : text_name[0],
        "code" : text_code[0]
    }
    return data
