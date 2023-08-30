from pymongo import MongoClient
from datetime import datetime

print("HOLA")
# Cadena de conexión a MongoDB Atlas
uri = "mongodb+srv://gaburolo:66wlbrvuGxid8xDI@cluster0.uptei.mongodb.net/documentosIdentidad?retryWrites=true&w=majority"

# Conectar a la base de datos
client = MongoClient(uri)
db = client.get_database()

# Seleccionar una colección
collection = db["carnet"]

# Datos a insertar
datos = datos_ejemplo = [
    
    {
        "fecha_vencimiento": "06/24",
        "nombre_completo": "García Mora Juan",
        "carnet": "2001987654",
        "fecha_cofeccion": "08/05/2023",
        "codigo_identificativo": "# 12345B67890 12345678901"
    },
    {
        "fecha_vencimiento": "09/25",
        "nombre_completo": "Hernández Ramírez Ana María",
        "carnet": "1998765432",
        "fecha_cofeccion": "06/15/2023",
        "codigo_identificativo": "# 54321B09876 98765432109"
    },
    {
        "fecha_vencimiento": "03/23",
        "nombre_completo": "López Soto Diego",
        "carnet": "1985432109",
        "fecha_cofeccion": "02/03/2023",
        "codigo_identificativo": "# 98765B43210 21098765432"
    },
    {
        "fecha_vencimiento": "11/24",
        "nombre_completo": "Morales Vargas María",
        "carnet": "2016789054",
        "fecha_cofeccion": "10/18/2022",
        "codigo_identificativo": "# 45678B90123 98765432101"
    },
    {
        "fecha_vencimiento": "07/22",
        "nombre_completo": "Ramírez Castro Luis",
        "carnet": "1983123456",
        "fecha_cofeccion": "12/05/2022",
        "codigo_identificativo": "# 76543B21098 65432109876"
    },
    {
        "fecha_vencimiento": "06/24",
        "nombre_completo": "García Mora Juan",
        "carnet": "2001987654",
        "fecha_cofeccion": "08/05/2023",
        "codigo_identificativo": "# 12345B67890 12345678901"
    },
    {
        "fecha_vencimiento": "09/25",
        "nombre_completo": "Hernández Ramírez Ana María",
        "carnet": "1998765432",
        "fecha_cofeccion": "06/15/2023",
        "codigo_identificativo": "# 54321B09876 98765432109"
    },
    {
        "fecha_vencimiento": "03/23",
        "nombre_completo": "López Soto Diego",
        "carnet": "1985432109",
        "fecha_cofeccion": "02/03/2023",
        "codigo_identificativo": "# 98765B43210 21098765432"
    },
    {
        "fecha_vencimiento": "11/24",
        "nombre_completo": "Morales Vargas María",
        "carnet": "2016789054",
        "fecha_cofeccion": "10/18/2022",
        "codigo_identificativo": "# 45678B90123 98765432101"
    },
    {
        "fecha_vencimiento": "07/22",
        "nombre_completo": "Ramírez Castro Luis",
        "carnet": "1983123456",
        "fecha_cofeccion": "12/05/2022",
        "codigo_identificativo": "# 76543B21098 65432109876"
    },
     {
        "fecha_vencimiento": "10/25",
        "nombre_completo": "Ramírez Soto Martín",
        "carnet": "1998123456",
        "fecha_cofeccion": "06/18/2023",
        "codigo_identificativo": "# 56789B76543 23456789012"
    },
    {
        "fecha_vencimiento": "04/23",
        "nombre_completo": "Martínez Vargas Carla",
        "carnet": "2012345678",
        "fecha_cofeccion": "02/28/2023",
        "codigo_identificativo": "# 12345B65432 34567890123"
    },
    {
        "fecha_vencimiento": "11/24",
        "nombre_completo": "López Hernández Daniel",
        "carnet": "2005432109",
        "fecha_cofeccion": "09/10/2022",
        "codigo_identificativo": "# 98765B78901 45678901234"
    },
    {
        "fecha_vencimiento": "06/22",
        "nombre_completo": "González Morales Laura",
        "carnet": "1996789054",
        "fecha_cofeccion": "11/23/2022",
        "codigo_identificativo": "# 87654B89012 56789012345"
    },
    {
        "fecha_vencimiento": "01/24",
        "nombre_completo": "Hernández Soto Mario",
        "carnet": "1997123456",
        "fecha_cofeccion": "05/22/2023",
        "codigo_identificativo": "# 23456B78901 67890123456"
    },
    {
        "fecha_vencimiento": "12/25",
        "nombre_completo": "García Vargas Sofia",
        "carnet": "2018432109",
        "fecha_cofeccion": "03/08/2023",
        "codigo_identificativo": "# 87654B01234 78901234567"
    },
    {
        "fecha_vencimiento": "07/23",
        "nombre_completo": "Ramírez López Valeria",
        "carnet": "2006234567",
        "fecha_cofeccion": "01/10/2023",
        "codigo_identificativo": "# 45678B56789 89012345678"
    },
    {
        "fecha_vencimiento": "03/25",
        "nombre_completo": "Morales Hernández Andrés",
        "carnet": "1999321098",
        "fecha_cofeccion": "09/18/2022",
        "codigo_identificativo": "# 78901B67890 90123456789"
    },
    {
        "fecha_vencimiento": "10/24",
        "nombre_completo": "Vargas Ramírez Lucia",
        "carnet": "2012234567",
        "fecha_cofeccion": "07/05/2022",
        "codigo_identificativo": "# 23456B78901 01234567890"
    },
    {
        "fecha_vencimiento": "06/23",
        "nombre_completo": "López Castro Felipe",
        "carnet": "2005432109",
        "fecha_cofeccion": "11/15/2022",
        "codigo_identificativo": "# 98765B21098 12345678901"
    },
    # ... más datos ...
]

# Insertar los datos en la colección
result = collection.insert_many(datos)
print("Datos insertados:", result.inserted_ids)

# Cerrar la conexión
client.close()
