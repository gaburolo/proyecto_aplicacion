import pytesseract
import cv2
import os
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def get_text_img(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    #(X,Y, Ancho, Alto)
    roi_datos = (170, 0, 750, 160)
    roi_numero = (455, 185, 365, 70)  
    roi_nombre = (430, 625, 445, 60)  
    roi_apellido = (430, 680, 300, 100)

    datos_recortado = imagen[roi_datos[1]:roi_datos[1]+roi_datos[3], roi_datos[0]:roi_datos[0]+roi_datos[2]]

    numero_recortado = imagen[roi_numero[1]:roi_numero[1]+roi_numero[3], roi_numero[0]:roi_numero[0]+roi_numero[2]]

    nombre_recortado = imagen[roi_nombre[1]:roi_nombre[1]+roi_nombre[3], roi_nombre[0]:roi_nombre[0]+roi_nombre[2]]
    apellido_recortado = imagen[roi_apellido[1]:roi_apellido[1]+roi_apellido[3], roi_apellido[0]:roi_apellido[0]+roi_apellido[2]]

    texto_nombre = pytesseract.image_to_string(nombre_recortado, lang='spa')
    texto_apellido = pytesseract.image_to_string(apellido_recortado, lang='spa')
    texto_numero = pytesseract.image_to_string(numero_recortado, lang='spa')
    texto_datos = pytesseract.image_to_string(datos_recortado, lang='spa')


    #print("Texto en la región del nombre:")
    #print(texto_nombre)
    #print("Texto en la región del apellido:")
    #print(texto_apellido)
    #print("\nTexto en la región del número de identificación:")
    #print(texto_numero)
    #print("Texto en la región del tipo:")
    #print(texto_datos)


    lastname = texto_apellido.split("\n")
    texto_nombre = texto_nombre.split("\n")
    texto_numero = texto_numero.split("\n")
    data = {
        "name": texto_nombre[0],
        "lastname1": lastname[0],
        "lastname2": lastname[1],
        "id": texto_numero[0]
    }
    return data

def get_text_img_stundent(ruta_imagen):
    imagen = cv2.imread(ruta_imagen)

    #(X,Y, Ancho, Alto)
    roi_datos = (1015, 724, 145, 55)
    roi_numero = (370, 620, 382, 80)
    roi_nombre = (380, 500, 855, 60)  


    datos_recortado = imagen[roi_datos[1]:roi_datos[1]+roi_datos[3], roi_datos[0]:roi_datos[0]+roi_datos[2]]

    numero_recortado = imagen[roi_numero[1]:roi_numero[1]+roi_numero[3], roi_numero[0]:roi_numero[0]+roi_numero[2]]

    nombre_recortado = imagen[roi_nombre[1]:roi_nombre[1]+roi_nombre[3], roi_nombre[0]:roi_nombre[0]+roi_nombre[2]]
   
    texto_nombre = pytesseract.image_to_string(nombre_recortado, lang='spa')
    texto_numero = pytesseract.image_to_string(numero_recortado, lang='spa')
    texto_datos = pytesseract.image_to_string(datos_recortado, lang='spa')
   
    text_name = texto_nombre.split("\n")
    
    texto_numero = texto_numero.split("\n")
    texto_datos = texto_datos.split("\n")

    data = {
        "name": text_name[0],
        "date": texto_datos[0],
        "id": texto_numero[0]
    }

    return data