from pymongo import MongoClient
from datetime import datetime

print("HOLA")
# Cadena de conexión a MongoDB Atlas
uri = "mongodb+srv://gaburolo:66wlbrvuGxid8xDI@cluster0.uptei.mongodb.net/documentosIdentidad?retryWrites=true&w=majority"

# Conectar a la base de datos
client = MongoClient(uri)
db = client.get_database()

# Seleccionar una colección
collection = db["cedula"]

# Datos a insertar
datos = datos_ejemplo = [
    {
        "nombre": "Ana",
        "apellido1": "García",
        "apellido2": "López",
        "numero": "1234567",
        "fecha_nacimiento": datetime(1995, 3, 15),
        "lugar_nacimiento": "San José",
        "nombre_padre": "Carlos",
        "nombre_madre": "María",
        "domicilio_electoral": "San José",
        "vencimiento": datetime(2031, 12, 31),
        "sexo": "F",
        "tse": "9876543"
    },
    {
        "nombre": "Luis",
        "apellido1": "Rojas",
        "apellido2": "Ramírez",
        "numero": "2345678",
        "fecha_nacimiento": datetime(1988, 7, 10),
        "lugar_nacimiento": "Heredia",
        "nombre_padre": "Manuel",
        "nombre_madre": "Laura",
        "domicilio_electoral": "Barva",
        "vencimiento": datetime(2033, 6, 30),
        "sexo": "M",
        "tse": "8765432"
    },
    {
        "nombre": "Carlos",
        "apellido1": "Vargas",
        "apellido2": "Rojas",
        "numero": "5678901",
        "fecha_nacimiento": datetime(1983, 8, 5),
        "lugar_nacimiento": "Puntarenas",
        "nombre_padre": "Miguel",
        "nombre_madre": "Silvia",
        "domicilio_electoral": "Esparza",
        "vencimiento": datetime(2036, 4, 25),
        "sexo": "M",
        "tse": "5432109"
    },
    {
        "nombre": "Laura",
        "apellido1": "Fuentes",
        "apellido2": "Hernández",
        "numero": "6789012",
        "fecha_nacimiento": datetime(1998, 11, 18),
        "lugar_nacimiento": "Guanacaste",
        "nombre_padre": "Andrés",
        "nombre_madre": "Patricia",
        "domicilio_electoral": "Liberia",
        "vencimiento": datetime(2037, 2, 10),
        "sexo": "F",
        "tse": "4321098"
    },
    {
        "nombre": "Javier",
        "apellido1": "Herrera",
        "apellido2": "Castillo",
        "numero": "7890123",
        "fecha_nacimiento": datetime(2002, 4, 22),
        "lugar_nacimiento": "Limón",
        "nombre_padre": "Ricardo",
        "nombre_madre": "Ana",
        "domicilio_electoral": "Limón",
        "vencimiento": datetime(2038, 7, 5),
        "sexo": "M",
        "tse": "3210987"
    },
    {
        "nombre": "María",
        "apellido1": "Sánchez",
        "apellido2": "González",
        "numero": "8901234",
        "fecha_nacimiento": datetime(1994, 2, 10),
        "lugar_nacimiento": "San José",
        "nombre_padre": "José",
        "nombre_madre": "Sofía",
        "domicilio_electoral": "Curridabat",
        "vencimiento": datetime(2039, 9, 15),
        "sexo": "F",
        "tse": "2109876"
    },
    {
        "nombre": "Daniel",
        "apellido1": "López",
        "apellido2": "Chaves",
        "numero": "9012345",
        "fecha_nacimiento": datetime(1986, 6, 30),
        "lugar_nacimiento": "San José",
        "nombre_padre": "Juan",
        "nombre_madre": "María",
        "domicilio_electoral": "Santa Ana",
        "vencimiento": datetime(2040, 5, 8),
        "sexo": "M",
        "tse": "1098765"
    },
    {
        "nombre": "Isabel",
        "apellido1": "Jiménez",
        "apellido2": "Mora",
        "numero": "0123456",
        "fecha_nacimiento": datetime(1999, 12, 5),
        "lugar_nacimiento": "Heredia",
        "nombre_padre": "Fernando",
        "nombre_madre": "Luisa",
        "domicilio_electoral": "San Rafael",
        "vencimiento": datetime(2041, 8, 20),
        "sexo": "F",
        "tse": "0987654"
    },
    {
        "nombre": "Miguel",
        "apellido1": "González",
        "apellido2": "López",
        "numero": "1234509",
        "fecha_nacimiento": datetime(2000, 9, 18),
        "lugar_nacimiento": "Cartago",
        "nombre_padre": "Carlos",
        "nombre_madre": "Elena",
        "domicilio_electoral": "La Unión",
        "vencimiento": datetime(2042, 11, 10),
        "sexo": "M",
        "tse": "9876540"
    },
    {
        "nombre": "Silvia",
        "apellido1": "Ramírez",
        "apellido2": "Herrera",
        "numero": "2345098",
        "fecha_nacimiento": datetime(1991, 4, 7),
        "lugar_nacimiento": "Limón",
        "nombre_padre": "Héctor",
        "nombre_madre": "Rosa",
        "domicilio_electoral": "Talamanca",
        "vencimiento": datetime(2043, 3, 15),
        "sexo": "F",
        "tse": "8765409"
    },
    {
        "nombre": "Andrea",
        "apellido1": "Fuentes",
        "apellido2": "Vargas",
        "numero": "3450987",
        "fecha_nacimiento": datetime(1993, 7, 12),
        "lugar_nacimiento": "Guanacaste",
        "nombre_padre": "Hugo",
        "nombre_madre": "Catalina",
        "domicilio_electoral": "Nicoya",
        "vencimiento": datetime(2044, 9, 5),
        "sexo": "F",
        "tse": "7654098"
    },
    {
        "nombre": "Gabriel",
        "apellido1": "Morales",
        "apellido2": "Sánchez",
        "numero": "4509876",
        "fecha_nacimiento": datetime(2003, 1, 25),
        "lugar_nacimiento": "San José",
        "nombre_padre": "Luis",
        "nombre_madre": "Patricia",
        "domicilio_electoral": "Curridabat",
        "vencimiento": datetime(2045, 6, 18),
        "sexo": "M",
        "tse": "6540987"
    },
    {
        "nombre": "María",
        "apellido1": "López",
        "apellido2": "Hernández",
        "numero": "5098765",
        "fecha_nacimiento": datetime(1989, 11, 2),
        "lugar_nacimiento": "Heredia",
        "nombre_padre": "José",
        "nombre_madre": "Ana",
        "domicilio_electoral": "Barva",
        "vencimiento": datetime(2046, 2, 21),
        "sexo": "F",
        "tse": "5430987"
    },
    {
        "nombre": "Diego",
        "apellido1": "González",
        "apellido2": "Rojas",
        "numero": "5678904",
        "fecha_nacimiento": datetime(2001, 5, 8),
        "lugar_nacimiento": "San José",
        "nombre_padre": "Jorge",
        "nombre_madre": "María",
        "domicilio_electoral": "San José",
        "vencimiento": datetime(2047, 12, 15),
        "sexo": "M",
        "tse": "8765430"
    },
    {
        "nombre": "Carolina",
        "apellido1": "Herrera",
        "apellido2": "Soto",
        "numero": "6540987",
        "fecha_nacimiento": datetime(1997, 10, 30),
        "lugar_nacimiento": "Limón",
        "nombre_padre": "Roberto",
        "nombre_madre": "Sofía",
        "domicilio_electoral": "Limón",
        "vencimiento": datetime(2048, 8, 7),
        "sexo": "F",
        "tse": "3210987"
    },
    {
        "nombre": "Manuel",
        "apellido1": "García",
        "apellido2": "Mora",
        "numero": "6789543",
        "fecha_nacimiento": datetime(1992, 4, 18),
        "lugar_nacimiento": "San José",
        "nombre_padre": "Ricardo",
        "nombre_madre": "Isabel",
        "domicilio_electoral": "Escazú",
        "vencimiento": datetime(2049, 7, 22),
        "sexo": "M",
        "tse": "4321098"
    },
    {
        "nombre": "Isabella",
        "apellido1": "Hernández",
        "apellido2": "López",
        "numero": "7895432",
        "fecha_nacimiento": datetime(1996, 11, 7),
        "lugar_nacimiento": "Cartago",
        "nombre_padre": "Javier",
        "nombre_madre": "Carolina",
        "domicilio_electoral": "Oreamuno",
        "vencimiento": datetime(2050, 5, 13),
        "sexo": "F",
        "tse": "8765432"
    },
    {
        "nombre": "Felipe",
        "apellido1": "Ramírez",
        "apellido2": "Castro",
        "numero": "5432109",
        "fecha_nacimiento": datetime(1997, 8, 30),
        "lugar_nacimiento": "Alajuela",
        "nombre_padre": "Andrés",
        "nombre_madre": "María",
        "domicilio_electoral": "Alajuela",
        "vencimiento": datetime(2051, 4, 9),
        "sexo": "M",
        "tse": "7654321"
    },
    {
        "nombre": "Sofía",
        "apellido1": "Fuentes",
        "apellido2": "Morales",
        "numero": "4321098",
        "fecha_nacimiento": datetime(2004, 1, 12),
        "lugar_nacimiento": "Heredia",
        "nombre_padre": "Luis",
        "nombre_madre": "Patricia",
        "domicilio_electoral": "San Pablo",
        "vencimiento": datetime(2052, 9, 30),
        "sexo": "F",
        "tse": "2109876"
    },
    {
        "nombre": "Jorge",
        "apellido1": "López",
        "apellido2": "Hernández",
        "numero": "3210987",
        "fecha_nacimiento": datetime(1998, 6, 22),
        "lugar_nacimiento": "San José",
        "nombre_padre": "Mario",
        "nombre_madre": "Carmen",
        "domicilio_electoral": "Goicoechea",
        "vencimiento": datetime(2053, 3, 5),
        "sexo": "M",
        "tse": "5432109"
    },



    # ... más datos ...
]

# Insertar los datos en la colección
result = collection.insert_many(datos)
print("Datos insertados:", result.inserted_ids)

# Cerrar la conexión
client.close()
