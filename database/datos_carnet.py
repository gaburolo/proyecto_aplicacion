from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("uri")

client = MongoClient(uri)
db = client.get_database()

collection = db["carnet"]

datos = [
    
    {
        "fecha_vencimiento": "06/24",
        "nombre_completo": "García Mora Juan",
        "carnet": "2001987654"
    },
    {
        "fecha_vencimiento": "09/25",
        "nombre_completo": "Hernández Ramírez Ana María",
        "carnet": "1998765432"
    },
    {
        "fecha_vencimiento": "03/23",
        "nombre_completo": "López Soto Diego",
        "carnet": "1985432109"
    },
    {
        "fecha_vencimiento": "11/24",
        "nombre_completo": "Morales Vargas María",
        "carnet": "2016789054"
    },
    {
        "fecha_vencimiento": "07/22",
        "nombre_completo": "Ramírez Castro Luis",
        "carnet": "1983123456"
    },
    {
        "fecha_vencimiento": "06/24",
        "nombre_completo": "García Mora Juan",
        "carnet": "2001987654"
    },
    {
        "fecha_vencimiento": "09/25",
        "nombre_completo": "Hernández Ramírez Ana María",
        "carnet": "1998765432"
    },
    {
        "fecha_vencimiento": "03/23",
        "nombre_completo": "López Soto Diego",
        "carnet": "1985432109"
    },
    {
        "fecha_vencimiento": "11/24",
        "nombre_completo": "Morales Vargas María",
        "carnet": "2016789054"
    },
    {
        "fecha_vencimiento": "07/22",
        "nombre_completo": "Ramírez Castro Luis",
        "carnet": "1983123456"
    },
     {
        "fecha_vencimiento": "10/25",
        "nombre_completo": "Ramírez Soto Martín",
        "carnet": "1998123456"
    },
    {
        "fecha_vencimiento": "04/23",
        "nombre_completo": "Martínez Vargas Carla",
        "carnet": "2012345678"
    },
    {
        "fecha_vencimiento": "11/24",
        "nombre_completo": "López Hernández Daniel",
        "carnet": "2005432109"
    },
    {
        "fecha_vencimiento": "06/22",
        "nombre_completo": "González Morales Laura",
        "carnet": "1996789054"
    },
    {
        "fecha_vencimiento": "01/24",
        "nombre_completo": "Hernández Soto Mario",
        "carnet": "1997123456"
    },
    {
        "fecha_vencimiento": "12/25",
        "nombre_completo": "García Vargas Sofia",
        "carnet": "2018432109"
    },
    {
        "fecha_vencimiento": "07/23",
        "nombre_completo": "Ramírez López Valeria",
        "carnet": "2006234567"
    },
    {
        "fecha_vencimiento": "03/25",
        "nombre_completo": "Morales Hernández Andrés",
        "carnet": "1999321098"
    },
    {
        "fecha_vencimiento": "10/24",
        "nombre_completo": "Vargas Ramírez Lucia",
        "carnet": "2012234567"
    },
    {
        "fecha_vencimiento": "06/23",
        "nombre_completo": "López Castro Felipe",
        "carnet": "2005432109"
    },
    
]


result = collection.insert_many(datos)
print("Datos insertados:", result.inserted_ids)

client.close()
