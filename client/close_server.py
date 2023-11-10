import socket
import io
import os
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("host")
port = os.getenv("port")

def closeServer():
    """
    The closeServer function connects to a server and sends a "close" message to close the connection.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, int(port)))

    # Envía "take" al servidor
    client_socket.send("close".encode())

    client_socket.close()
closeServer()