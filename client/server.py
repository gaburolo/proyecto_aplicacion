import socket
import numpy as np
import cv2
from photo import *

camera_ip = input("Por favor, ingrese la dirección IP de la cámara: ")

# Configura el servidor
host = '0.0.0.0'  # Escucha en todas las interfaces
port = 12345  # Puerto para la conexión

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)  # Escuchar una conexión entrante

print(f"Esperando una conexión en {host}:{port}")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexión establecida desde {addr}")
    
    try:
        data = client_socket.recv(1024).decode()
        
        if not data:
            continue  # Continúa esperando la próxima conexión
    
        # Trabaja con los datos y responde al cliente
        if data == "take":
            photo = take_photo(camera_ip)
            if photo is not None:
                photo_bytes = cv2.imencode('.jpg', photo)[1].tobytes()
                
                # Envía los bytes de la imagen en bloques
                chunk_size = 4096
                total_sent = 0
                while total_sent < len(photo_bytes):
                    chunk = photo_bytes[total_sent:total_sent + chunk_size]
                    client_socket.send(chunk)
                    total_sent += len(chunk)
        
                # Marca el final de la transmisión
                client_socket.send(b'')
        elif data == "close":
            print("Deteniendo servidor")
            break
    except Exception as e:
        print(f"Error de conexión con el cliente: {e}")
    finally:
        client_socket.close()