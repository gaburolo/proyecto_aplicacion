import requests
import cv2
import numpy as np

def take_photo(camera_ip):
    """
    The `take_photo` function captures a photo from a camera with a given IP address and saves it as
    "imagen.jpg".
    
    :param camera_ip: The `camera_ip` parameter is the IP address of the camera you want to capture the
    photo from
    :return: the captured frame as a numpy array.
    """
    url = f"http://{camera_ip}:8080/video"
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
