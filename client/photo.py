import requests
import cv2
import numpy as np

url_big_photo = "http://192.168.100.130:8080/photo.jpg"
#url = "http://192.168.1.111:8080/video"
url = "http://192.168.100.130:8080/video"

def take_photo():
    cap = cv2.VideoCapture(url)


    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        exit()


    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 4000)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
    cap.set(cv2.CAP_PROP_FPS, 30)  
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("imagen.jpg", frame)
        print("Imagen guardada como imagen.jpg")
        return frame
    else:
        print("Error al capturar la imagen.")

    cap.release()

    cv2.destroyAllWindows()

def take_big_photo():
    response = requests.get(url_big_photo)
    if response.status_code == 200:
        image_data = np.frombuffer(response.content, np.uint8)
        frame = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
        if frame is not None:
            cv2.imwrite("imagen_grande.jpg", frame)
            print("Imagen guardada como imagen_grande.jpg")
            return frame
        else:
            print("Error al decodificar la imagen.")
    else:
        print(f"Error al obtener la imagen. Código de estado: {response.status_code}")
