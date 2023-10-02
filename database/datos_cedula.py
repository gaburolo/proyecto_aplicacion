from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("uri")
# Conectar a la base de datos
client = MongoClient(uri)
db = client.get_database()

# Seleccionar una colección
collection = db["cedula"]

# Datos a insertar
datos = [
    {
        "nombre": "Ana",
        "apellido1": "García",
        "apellido2": "López",
        "numero": "1 2345 6789",
    },
    {
        "nombre": "Luis",
        "apellido1": "Rojas",
        "apellido2": "Ramírez",
        "numero": "2 3456 7890",
    },
    {
        "nombre": "Carlos",
        "apellido1": "Vargas",
        "apellido2": "Rojas",
        "numero": "5 6789 0123",
    },
    {
        "nombre": "Laura",
        "apellido1": "Fuentes",
        "apellido2": "Hernández",
        "numero": "6 7890 1234",
    },
    {
        "nombre": "Javier",
        "apellido1": "Herrera",
        "apellido2": "Castillo",
        "numero": "7 8901 2345",
    },
    {
        "nombre": "María",
        "apellido1": "Sánchez",
        "apellido2": "González",
        "numero": "8 9012 3456",
    },
    {
        "nombre": "Daniel",
        "apellido1": "López",
        "apellido2": "Chaves",
        "numero": "9 0123 4567",
    },
    {
        "nombre": "Isabel",
        "apellido1": "Jiménez",
        "apellido2": "Mora",
        "numero": "0 1234 5678",
    },
    {
        "nombre": "Miguel",
        "apellido1": "González",
        "apellido2": "López",
        "numero": "1 2345 0987",
    },
    {
        "nombre": "Silvia",
        "apellido1": "Ramírez",
        "apellido2": "Herrera",
        "numero": "2 3450 9876",
    },
    {
        "nombre": "Andrea",
        "apellido1": "Fuentes",
        "apellido2": "Vargas",
        "numero": "3 4509 8765",
    },
    {
        "nombre": "Gabriel",
        "apellido1": "Morales",
        "apellido2": "Sánchez",
        "numero": "4 5098 7654",
    },
    {
        "nombre": "María",
        "apellido1": "López",
        "apellido2": "Hernández",
        "numero": "5 0987 6543",
    },
    {
        "nombre": "Diego",
        "apellido1": "González",
        "apellido2": "Rojas",
        "numero": "6 7890 4567",
    },
    {
        "nombre": "Carolina",
        "apellido1": "Herrera",
        "apellido2": "Soto",
        "numero": "6 5409 8765",
    },
    {
        "nombre": "Manuel",
        "apellido1": "García",
        "apellido2": "Mora",
        "numero": "6 7895 4321",
    },
    {
        "nombre": "Isabella",
        "apellido1": "Hernández",
        "apellido2": "López",
        "numero": "7 8954 3210",
    },
    {
        "nombre": "Felipe",
        "apellido1": "Ramírez",
        "apellido2": "Castro",
        "numero": "5 4321 0987",
    },
    {
        "nombre": "Sofía",
        "apellido1": "Fuentes",
        "apellido2": "Morales",
        "numero": "4 3210 9876",
    },
    {
        "nombre": "Jorge",
        "apellido1": "López",
        "apellido2": "Hernández",
        "numero": "3 2109 8765",
    },
]

result = collection.insert_many(datos)
print("Datos insertados:", result.inserted_ids)

client.close()
