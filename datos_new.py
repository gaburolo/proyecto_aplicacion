from pymongo import MongoClient
from datetime import datetime

print("HOLA")
# Cadena de conexión a MongoDB Atlas
uri = "mongodb+srv://gaburolo:66wlbrvuGxid8xDI@cluster0.uptei.mongodb.net/documentosIdentidad?retryWrites=true&w=majority"

# Conectar a la base de datos
client = MongoClient(uri)
db = client.get_database()

# Seleccionar una colección
collection = db["cedulanueva"]

# Datos a insertar
datos = datos_ejemplo = [
    {
        "nombre": "Carlos",
        "apellido1": "Hernández",
        "apellido2": "García",
        "numero": "4321098",
        "fecha_nacimiento": datetime(1990, 11, 8),
        "lugar_nacimiento": "San José San José",
        "domicilio_electoral": "San José",
        "vencimiento": datetime(2059, 4, 15),
        "sexo": "M",
        "tse": "5432109"
    },
    {
        "nombre": "Luisa",
        "apellido1": "Morales",
        "apellido2": "Ramírez",
        "numero": "3210987",
        "fecha_nacimiento": datetime(2002, 6, 25),
        "lugar_nacimiento": "Heredia Heredia",
        "domicilio_electoral": "Heredia",
        "vencimiento": datetime(2060, 7, 22),
        "sexo": "F",
        "tse": "6543210"
    },
    {
        "nombre": "Andrea",
        "apellido1": "Vargas",
        "apellido2": "López",
        "numero": "2109876",
        "fecha_nacimiento": datetime(1998, 3, 12),
        "lugar_nacimiento": "Liberia Guanacaste",
        "domicilio_electoral": "Nicoya",
        "vencimiento": datetime(2061, 8, 5),
        "sexo": "F",
        "tse": "7654321"
    },
    {
        "nombre": "José",
        "apellido1": "González",
        "apellido2": "Herrera",
        "numero": "1098765",
        "fecha_nacimiento": datetime(1997, 10, 2),
        "lugar_nacimiento": "Limón Limón",
        "domicilio_electoral": "Limón",
        "vencimiento": datetime(2062, 3, 30),
        "sexo": "M",
        "tse": "8765432"
    },
    {
        "nombre": "María",
        "apellido1": "Ramírez",
        "apellido2": "Morales",
        "numero": "0987654",
        "fecha_nacimiento": datetime(2003, 4, 18),
        "lugar_nacimiento": "Alajuela Alajuela",
        "domicilio_electoral": "Alajuela",
        "vencimiento": datetime(2063, 1, 10),
        "sexo": "F",
        "tse": "9876543"
    },
    {
        "nombre": "Daniel",
        "apellido1": "López",
        "apellido2": "Hernández",
        "numero": "9876543",
        "fecha_nacimiento": datetime(1995, 6, 10),
        "lugar_nacimiento": "Carmen Central San José",
        "domicilio_electoral": "Desamparados",
        "vencimiento": datetime(2064, 9, 15),
        "sexo": "M",
        "tse": "5432109"
    },
    {
        "nombre": "Lorena",
        "apellido1": "González",
        "apellido2": "Ramírez",
        "numero": "8765432",
        "fecha_nacimiento": datetime(1999, 8, 22),
        "lugar_nacimiento": "San Juan Central Heredia",
        "domicilio_electoral": "Heredia",
        "vencimiento": datetime(2065, 2, 28),
        "sexo": "F",
        "tse": "6543210"
    },
    {
        "nombre": "Marcelo",
        "apellido1": "Martínez",
        "apellido2": "Vargas",
        "numero": "7654321",
        "fecha_nacimiento": datetime(2001, 3, 12),
        "lugar_nacimiento": "Liberia Guanacaste",
        "domicilio_electoral": "Nicoya",
        "vencimiento": datetime(2066, 7, 5),
        "sexo": "M",
        "tse": "7654321"
    },
    {
        "nombre": "Raquel",
        "apellido1": "Herrera",
        "apellido2": "García",
        "numero": "6543210",
        "fecha_nacimiento": datetime(1997, 10, 2),
        "lugar_nacimiento": "Río Claro Limón",
        "domicilio_electoral": "Limón",
        "vencimiento": datetime(2067, 3, 30),
        "sexo": "F",
        "tse": "8765432"
    },
    {
        "nombre": "José",
        "apellido1": "Ramírez",
        "apellido2": "Morales",
        "numero": "5432109",
        "fecha_nacimiento": datetime(2003, 4, 18),
        "lugar_nacimiento": "Zarcero Alajuela",
        "domicilio_electoral": "Alajuela",
        "vencimiento": datetime(2068, 1, 10),
        "sexo": "M",
        "tse": "9876543"
    },
     {
        "nombre": "Natalia",
        "apellido1": "Hernández",
        "apellido2": "García",
        "numero": "4321098",
        "fecha_nacimiento": datetime(1998, 11, 8),
        "lugar_nacimiento": "Los Chiles Alajuela",
        "domicilio_electoral": "Los Chiles",
        "vencimiento": datetime(2069, 4, 15),
        "sexo": "F",
        "tse": "5432109"
    },
    {
        "nombre": "Héctor",
        "apellido1": "Morales",
        "apellido2": "Ramírez",
        "numero": "3210987",
        "fecha_nacimiento": datetime(2002, 6, 25),
        "lugar_nacimiento": "Puriscal San José",
        "domicilio_electoral": "Puriscal",
        "vencimiento": datetime(2070, 7, 22),
        "sexo": "M",
        "tse": "6543210"
    },
    {
        "nombre": "Carla",
        "apellido1": "Vargas",
        "apellido2": "López",
        "numero": "2109876",
        "fecha_nacimiento": datetime(1999, 3, 12),
        "lugar_nacimiento": "San Pablo Heredia",
        "domicilio_electoral": "San Pablo",
        "vencimiento": datetime(2071, 8, 5),
        "sexo": "F",
        "tse": "7654321"
    },
    {
        "nombre": "Mario",
        "apellido1": "González",
        "apellido2": "Herrera",
        "numero": "1098765",
        "fecha_nacimiento": datetime(1997, 10, 2),
        "lugar_nacimiento": "Nicoya Guanacaste",
        "domicilio_electoral": "Nicoya",
        "vencimiento": datetime(2072, 3, 30),
        "sexo": "M",
        "tse": "8765432"
    },
    {
        "nombre": "Lucía",
        "apellido1": "Ramírez",
        "apellido2": "Morales",
        "numero": "0987654",
        "fecha_nacimiento": datetime(2003, 4, 18),
        "lugar_nacimiento": "Siquirres Limón",
        "domicilio_electoral": "Siquirres",
        "vencimiento": datetime(2073, 1, 10),
        "sexo": "F",
        "tse": "9876543"
    },
    {
        "nombre": "Ricardo",
        "apellido1": "Hernández",
        "apellido2": "García",
        "numero": "4321098",
        "fecha_nacimiento": datetime(1995, 6, 10),
        "lugar_nacimiento": "Sarapiquí Heredia",
        "domicilio_electoral": "Sarapiquí",
        "vencimiento": datetime(2074, 9, 15),
        "sexo": "M",
        "tse": "5432109"
    },
    {
        "nombre": "Valeria",
        "apellido1": "Morales",
        "apellido2": "Ramírez",
        "numero": "3210987",
        "fecha_nacimiento": datetime(2002, 6, 25),
        "lugar_nacimiento": "Cañas Guanacaste",
        "domicilio_electoral": "Cañas",
        "vencimiento": datetime(2075, 7, 22),
        "sexo": "F",
        "tse": "6543210"
    },
    {
        "nombre": "Federico",
        "apellido1": "Vargas",
        "apellido2": "López",
        "numero": "2109876",
        "fecha_nacimiento": datetime(1999, 3, 12),
        "lugar_nacimiento": "Pérez Zeledón San José",
        "domicilio_electoral": "Pérez Zeledón",
        "vencimiento": datetime(2076, 8, 5),
        "sexo": "M",
        "tse": "7654321"
    },
    {
        "nombre": "Ana",
        "apellido1": "González",
        "apellido2": "Herrera",
        "numero": "1098765",
        "fecha_nacimiento": datetime(1997, 10, 2),
        "lugar_nacimiento": "Desamparados Alajuela",
        "domicilio_electoral": "Desamparados",
        "vencimiento": datetime(2077, 3, 30),
        "sexo": "F",
        "tse": "8765432"
    },
    {
        "nombre": "Javier",
        "apellido1": "Ramírez",
        "apellido2": "Morales",
        "numero": "0987654",
        "fecha_nacimiento": datetime(2003, 4, 18),
        "lugar_nacimiento": "Esparza Puntarenas",
        "domicilio_electoral": "Esparza",
        "vencimiento": datetime(2078, 1, 10),
        "sexo": "M",
        "tse": "9876543"
    },


    # ... más datos ...
]

# Insertar los datos en la colección
result = collection.insert_many(datos)
print("Datos insertados:", result.inserted_ids)

# Cerrar la conexión
client.close()
