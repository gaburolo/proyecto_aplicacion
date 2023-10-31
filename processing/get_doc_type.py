import tensorflow as tf
from PIL import Image
import requests
from io import BytesIO
import cv2
import numpy as np

# Ruta al directorio que contiene el modelo guardado
modelo_directorio = 'model/modelo_documentos/1'

# Carga el modelo
loaded_model = tf.keras.models.load_model(modelo_directorio)

def categorize(url):
  result = requests.get(url)
  img = Image.open(BytesIO(result.content))
  img = np.array(img).astype(float)/255

  img = cv2.resize(img, (224,224))
  imagen_pillow = Image.fromarray((img * 255).astype('uint8'))  # Asegúrate de que la imagen esté en el rango [0, 255]

  imagen_pillow.save('imagen_redimensionada.jpg')
  prediccion = loaded_model.predict(img.reshape(-1, 224, 224, 3))
  value = np.argmax(prediccion[0], axis=-1)
  if value == 0:
    return "carnet"
  elif value == 1:
    return "cedula"
  elif value == 2:
    return "licencia"
  

def categorize_local(url):


  image_png = cv2.imread(url, cv2.IMREAD_UNCHANGED)


  cv2.imwrite('photo/output.jpg', image_png, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
  img = Image.open('photo/output.jpg')
  img = np.array(img).astype(float)/255

  img = cv2.resize(img, (224,224))
  prediccion = loaded_model.predict(img.reshape(-1, 224, 224, 3))
  value = np.argmax(prediccion[0], axis=-1)
  if value == 0:
    return "carnet"
  elif value == 1:
    return "cedula"
  elif value == 2:
    return "licencia"
  