import cv2
import pyocr
import pyocr.builders
from PIL import Image
from io import BytesIO

# Función para procesar una ROI utilizando PyOCR
def procesar_roi(roi):
    # Convertir la ROI a escala de grises
    roi_gris = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Guardar la ROI en un objeto BytesIO
    roi_io = BytesIO()
    Image.fromarray(roi_gris).save(roi_io, format='PNG')

    # Convertir la ROI a formato PIL
    roi_pil = Image.open(roi_io)

    # Realizar OCR en la ROI en escala de grises
    texto_roi = tool.image_to_string(
        roi_pil,
        lang='spa',  # Idioma (cambiar según sea necesario)
        builder=pyocr.builders.TextBuilder()
    )

    # Cerrar el objeto BytesIO
    roi_io.close()

    # Imprimir el texto reconocido en la ROI
    print(texto_roi)

# Inicializar PyOCR con el motor Tesseract (asegúrate de que Tesseract esté instalado)
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No se encontraron motores OCR compatibles. Asegúrate de tener Tesseract instalado.")
    exit()

# Utilizar el primer motor (Tesseract)
tool = tools[0]

# Ruta completa de la imagen
ruta_imagen = 'processed_photos/enhanced_image_test.jpg'

# Cargar la imagen con OpenCV
imagen = cv2.imread(ruta_imagen)

# Coordenadas de las ROI
roi_datos = (0, 0, 720, 496)

# Procesar cada ROI
procesar_roi(imagen[roi_datos[1]:roi_datos[1]+roi_datos[3], roi_datos[0]:roi_datos[0]+roi_datos[2]])
