import socket
import io
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
port = os.getenv("port")

def requestPhoto():
    """
    The function `requestPhoto()` connects to a server, sends a request to take a photo, receives the
    photo data, saves it as a PNG file, and prints a message indicating that the image has been saved.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, int(port)))
    client_socket.send("take".encode())

    received_data = b''
    while True:
        chunk = client_socket.recv(4096)  
        if not chunk:
            break
        received_data += chunk

    if received_data:
        image = Image.open(io.BytesIO(received_data))
        image.save("client/photo.png", "PNG")
        print("Imagen guardada como photo.png")

    client_socket.close()

def closeServer():
    """
    The closeServer function creates a client socket, connects to a server using the specified host and
    port, sends a "close" message to the server, and then closes the client socket.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, int(port)))

    client_socket.send("close".encode())

    client_socket.close()