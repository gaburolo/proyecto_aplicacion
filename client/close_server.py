import socket

host = input("Por favor, ingrese la dirección IP del servidor: ")
port = input("Por favor, ingrese la puerto del servidor: ")

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
