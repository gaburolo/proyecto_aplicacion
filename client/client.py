import socket
import io
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

# Configura el cliente
host = os.getenv("host")
port = os.getenv("port")
def requestPhoto():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, int(port)))

    # Envía "take" al servidor
    client_socket.send("take".encode())

    received_data = b''
    while True:
        chunk = client_socket.recv(4096)  # Recibir en bloques
        if not chunk:
            break
        received_data += chunk

    # Convierte los bytes en una imagen y guárdala como "photo.png"
    if received_data:
        image = Image.open(io.BytesIO(received_data))
        image.save("photo.png", "PNG")
        print("Imagen guardada como photo.png")

    client_socket.close()

def closeServer():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, int(port)))

    # Envía "take" al servidor
    client_socket.send("close".encode())

    received_data = b''
    client_socket.close()
requestPhoto()
closeServer()