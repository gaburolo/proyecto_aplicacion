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
print(tf.__version__)

def categorizar(url):
  respuesta = requests.get(url)
  img = Image.open(BytesIO(respuesta.content))
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
def categorizar_local(url):
  img = Image.open(url)
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
  
#0 = carnet, 1 = cedula, 2 = licencia
url = "processed_photos\enhanced_image.png"
prediccion = categorizar_local(url)
print(prediccion)

#0 = carnet, 1 = cedula, 2 = licencia
url = "salida\carnet\TEC0.png"
prediccion = categorizar_local(url)
print(prediccion)

url = "https://cloudfront-us-east-1.images.arcpublishing.com/gruponacion/LXELPE5IQFCL7BKCHFVVI7QZ6A.jpeg"
prediccion = categorizar(url)
print(prediccion)