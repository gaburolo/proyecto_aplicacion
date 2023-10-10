import pytesseract
import cv2
import os
import numpy as np
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def clean_text(text):
    # Utilizar una expresión regular para mantener letras mayúsculas, minúsculas y espacios
    cleaned_text = re.sub(r'[^A-Za-z\sÁÉÍÓÚáéíóú]', '', text)
    return cleaned_text

def clean_number(text):
    # Utilizar una expresión regular para mantener solo números y espacios
    cleaned_text = re.sub(r'[^0-9\s]', '', text)
    return cleaned_text

def get_text_img_identity(image_path):
    #image = cv2.imread(image_path)
    img = np.array(Image.open(image_path))


    norm_img = np.zeros((img.shape[0], img.shape[1]))
    image = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    image = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    image = cv2.GaussianBlur(img, (1, 1), 0)

    #(X,Y, Width, Height)
    roi_number = (455, 185, 365, 70)
    roi_name = (430, 625, 445, 60)
    roi_lastname = (430, 680, 300, 100)

    number_section = image[roi_number[1]:roi_number[1]+roi_number[3], roi_number[0]:roi_number[0]+roi_number[2]]
    name_section = image[roi_name[1]:roi_name[1]+roi_name[3], roi_name[0]:roi_name[0]+roi_name[2]]
    lastname_section = image[roi_lastname[1]:roi_lastname[1]+roi_lastname[3], roi_lastname[0]:roi_lastname[0]+roi_lastname[2]]

    text_name = pytesseract.image_to_string(name_section, lang='spa')
    text_lastname = pytesseract.image_to_string(lastname_section, lang='spa')
    text_number = pytesseract.image_to_string(number_section, lang='spa')


    """
        carpeta_parts = 'parts'
        if not os.path.exists(carpeta_parts):
            os.makedirs(carpeta_parts)

        # Guardar las regiones recortadas en archivos individuales
        ruta_apellido_recortado = os.path.join(carpeta_parts, 'apellido.png')
        cv2.imwrite(ruta_apellido_recortado, lastname_section)
    """


    lastname_lines = clean_text(text_lastname)
    lastname_lines = lastname_lines.split("\n")
    text_name = clean_text(text_name)
    text_name = text_name.split("\n")
    text_number = clean_number(text_number)
    text_number = text_number.split("\n")

    data = {
        "name": text_name[0],
        "lastname1": lastname_lines[0],
        "lastname2": lastname_lines[1],
        "id": text_number[0]
    }
    
    return data

def get_text_img_stundent(image_path):
    #image = cv2.imread(image_path)
    img = np.array(Image.open(image_path))


    norm_img = np.zeros((img.shape[0], img.shape[1]))
    image = cv2.normalize(img, norm_img, 0, 255, cv2.NORM_MINMAX)
    image = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)[1]
    image = cv2.GaussianBlur(img, (1, 1), 0)

    #(X,Y, Width, Height)
    roi_data = (1015, 724, 145, 55)
    roi_number = (370, 620, 382, 80)
    roi_name = (380, 500, 855, 60)

    data_section = image[roi_data[1]:roi_data[1]+roi_data[3], roi_data[0]:roi_data[0]+roi_data[2]]
    number_section = image[roi_number[1]:roi_number[1]+roi_number[3], roi_number[0]:roi_number[0]+roi_number[2]]
    name_section = image[roi_name[1]:roi_name[1]+roi_name[3], roi_name[0]:roi_name[0]+roi_name[2]]

    text_name = pytesseract.image_to_string(name_section, lang='spa')
    text_number = pytesseract.image_to_string(number_section, lang='spa')
    text_data = pytesseract.image_to_string(data_section, lang='spa')

    text_name = text_name.split("\n")
    text_number = text_number.split("\n")
    text_data = text_data.split("\n")

    data = {
        "name": text_name[0],
        "date": text_data[0],
        "id": text_number[0]
    }

    return data

def get_text_img_license(image_path):
    image = cv2.imread(image_path)
    

    #(X,Y, Ancho, Alto)
    roi_number = (370, 150, 360, 50)
    roi_expedition = (500, 205, 220, 50)
    roi_birth = (500, 256, 220, 50)
    roi_expiration = (500, 305, 210, 50)
    roi_blood_type = (665, 360, 145, 60)
    roi_type = (950, 230, 100, 60)
    roi_name = (20, 410, 500, 60)
    roi_code = (870, 560, 240, 60)


    section_number = image[roi_number[1]:roi_number[1]+roi_number[3], roi_number[0]:roi_number[0]+roi_number[2]]
    section_expedition = image[roi_expedition[1]:roi_expedition[1]+roi_expedition[3], roi_expedition[0]:roi_expedition[0]+roi_expedition[2]]
    section_birth = image[roi_birth[1]:roi_birth[1]+roi_birth[3], roi_birth[0]:roi_birth[0]+roi_birth[2]]
    section_expiration = image[roi_expiration[1]:roi_expiration[1]+roi_expiration[3], roi_expiration[0]:roi_expiration[0]+roi_expiration[2]]
    section_blood_type = image[roi_blood_type[1]:roi_blood_type[1]+roi_blood_type[3], roi_blood_type[0]:roi_blood_type[0]+roi_blood_type[2]]
    section_type = image[roi_type[1]:roi_type[1]+roi_type[3], roi_type[0]:roi_type[0]+roi_type[2]]
    section_name = image[roi_name[1]:roi_name[1]+roi_name[3], roi_name[0]:roi_name[0]+roi_name[2]]
    section_code = image[roi_code[1]:roi_code[1]+roi_code[3], roi_code[0]:roi_code[0]+roi_code[2]]

    text_number = pytesseract.image_to_string(section_number, lang='spa')
    text_expedition = pytesseract.image_to_string(section_expedition, lang='spa')
    text_birth = pytesseract.image_to_string(section_birth, lang='spa')
    text_expiration = pytesseract.image_to_string(section_expiration, lang='spa')
    text_blood_type = pytesseract.image_to_string(section_blood_type, lang='spa')
    text_type = pytesseract.image_to_string(section_type, lang='spa')
    text_name = pytesseract.image_to_string(section_name, lang='spa')
    text_code = pytesseract.image_to_string(section_code, lang='spa')

   

    text_number = text_number.split("\n")
    text_expedition = text_expedition.split("\n")
    text_birth = text_birth.split("\n")
    text_expiration = text_expiration.split("\n")
    text_blood_type = text_blood_type.split("\n")
    text_type = text_type.split("\n")
    text_name = text_name.split("\n")
    text_code = text_code.split(" ")
    

    carpeta_parts = 'parts'
    if not os.path.exists(carpeta_parts):
        os.makedirs(carpeta_parts)

    # Guardar las regiones recortadas en archivos individuales
    ruta_apellido_recortado = os.path.join(carpeta_parts, 'apellido.png')


    cv2.imwrite(ruta_apellido_recortado, section_expiration)
    """
    print("number: " + text_number)
    print("expedition: " + text_expedition)
    print("birth: " + text_birth)
    print("expiration: " + text_expiration)
    print("blood_type: " + text_blood_type)
    print("type: " + text_type)
    print("name: " + text_name)
    print("code: " + text_code)"""
    

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
