import cv2


url = "http://192.168.100.130:8080/video"

def take_photo():
    cap = cv2.VideoCapture(url)


    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        exit()


    cap.set(3, 1920)  
    cap.set(4, 1080)  
    cap.set(5, 30)  
    ret, frame = cap.read()

    if ret:
        cv2.imwrite("imagen.jpg", frame)
        print("Imagen guardada como imagen.jpg")
        return frame
    else:
        print("Error al capturar la imagen.")

    cap.release()

    cv2.destroyAllWindows()
