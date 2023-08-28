import pytesseract
import cv2
import os
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

ruta_imagen = 'processed_photos/enhanced_image.jpg'


imagen = cv2.imread(ruta_imagen)

#(X,Y, Ancho, Alto)
roi_datos = (105, 0, 410, 100)
roi_numero = (260, 110, 220, 50)  
roi_nombre = (250, 335, 250, 33)  
roi_apellido = (340, 440, 300, 110)

datos_recortado = imagen[roi_datos[1]:roi_datos[1]+roi_datos[3], roi_datos[0]:roi_datos[0]+roi_datos[2]]

numero_recortado = imagen[roi_numero[1]:roi_numero[1]+roi_numero[3], roi_numero[0]:roi_numero[0]+roi_numero[2]]

nombre_recortado = imagen[roi_nombre[1]:roi_nombre[1]+roi_nombre[3], roi_nombre[0]:roi_nombre[0]+roi_nombre[2]]
apellido_recortado = imagen[roi_apellido[1]:roi_apellido[1]+roi_apellido[3], roi_apellido[0]:roi_apellido[0]+roi_apellido[2]]

texto_nombre = pytesseract.image_to_string(nombre_recortado, lang='spa')
texto_apellido = pytesseract.image_to_string(apellido_recortado, lang='spa')
texto_numero = pytesseract.image_to_string(numero_recortado, lang='spa')
texto_datos = pytesseract.image_to_string(datos_recortado, lang='spa')


print("Texto en la región del nombre:")
print(texto_nombre)
print("Texto en la región del apellido:")
print(texto_apellido)
print("\nTexto en la región del número de identificación:")
print(texto_numero)
print("Texto en la región del tipo:")
print(texto_datos)


carpeta_parts = 'parts'
if not os.path.exists(carpeta_parts):
    os.makedirs(carpeta_parts)

# Guardar las regiones recortadas en archivos individuales
ruta_apellido_recortado = os.path.join(carpeta_parts, 'apellido.png')


cv2.imwrite(ruta_apellido_recortado, apellido_recortado)