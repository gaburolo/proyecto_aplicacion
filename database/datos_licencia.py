from pymongo import MongoClient
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("uri")

client = MongoClient(uri)
db = client.get_database()

collection = db["licencia"]

datos = [
    {
        "numero": "DM-889330756",
        "expedicion": "17-07-2012",
        "nacimiento": "06-06-1984",
        "vencimiento": "08-05-2024",
        "tipo_sangre": "A+",
        "tipo":"E1",
        "nombre": "Vargas S\u00e1nchez Isabel",
        "codigo": "74043645"
    },
    {
        "numero": "DM-353027210",
        "expedicion": "18-02-2013",
        "nacimiento": "16-01-1997",
        "vencimiento": "05-06-2025",
        "tipo_sangre": "AB+",
        "tipo":"D4",
        "nombre": "Herrera S\u00e1nchez Laura",
        "codigo": "49211342"
    },
    {
        "numero": "DM-645936823",
        "expedicion": "18-06-2020",
        "nacimiento": "24-06-1966",
        "vencimiento": "10-04-2029",
        "tipo_sangre": "A-",
        "tipo":"D3",
        "nombre": "Vargas Garc\u00eda Daniel",
        "codigo": "45102703"
    },
    {
        "numero": "DM-320954109",
        "expedicion": "10-04-2002",
        "nacimiento": "24-06-1972",
        "vencimiento": "02-10-2029",
        "tipo_sangre": "AB+",
        "tipo":"C2",
        "nombre": "Herrera Gonz\u00e1lez Javier",
        "codigo": "61606705"
    },
    {
        "numero": "DM-114181500",
        "expedicion": "16-03-2005",
        "nacimiento": "20-10-1965",
        "vencimiento": "26-03-2027",
        "tipo_sangre": "B+",
        "tipo":"B2",
        "nombre": "Garc\u00eda L\u00f3pez Miguel",
        "codigo": "44446202"
    },
    {
        "numero": "DM-467494189",
        "expedicion": "10-05-2004",
        "nacimiento": "12-04-1992",
        "vencimiento": "03-09-2027",
        "tipo_sangre": "B-",
        "tipo":"A3",
        "nombre": "Herrera Gonz\u00e1lez Carlos",
        "codigo": "61153489"
    },
    {
        "numero": "DM-321988627",
        "expedicion": "04-02-2022",
        "nacimiento": "19-04-1974",
        "vencimiento": "20-11-2025",
        "tipo_sangre": "O+",
        "tipo":"E2",
        "nombre": "S\u00e1nchez Garc\u00eda Mar\u00eda",
        "codigo": "52099341"
    },
    {
        "numero": "DM-292644309",
        "expedicion": "13-12-2011",
        "nacimiento": "16-08-1956",
        "vencimiento": "25-01-2024",
        "tipo_sangre": "O+",
        "tipo":"E1",
        "nombre": "Gonz\u00e1lez Vargas Silvia",
        "codigo": "95514920"
    },
    {
        "numero": "DM-354827125",
        "expedicion": "28-01-2012",
        "nacimiento": "01-11-1984",
        "vencimiento": "18-12-2024",
        "tipo_sangre": "O+",
        "tipo":"D3",
        "nombre": "Fuentes Vargas Carlos",
        "codigo": "98796705"
    },
    {
        "numero": "DM-180050079",
        "expedicion": "22-10-2008",
        "nacimiento": "02-10-1996",
        "vencimiento": "16-09-2030",
        "tipo_sangre": "O-",
        "tipo":"D2",
        "nombre": "L\u00f3pez Gonz\u00e1lez Carlos",
        "codigo": "54967530"
    },
    {
        "numero": "DM-340216918",
        "expedicion": "15-03-2015",
        "nacimiento": "14-05-1987",
        "vencimiento": "25-02-2027",
        "tipo_sangre": "A+",
        "tipo":"D1",
        "nombre": "Rojas Jim\u00e9nez Javier",
        "codigo": "72136608"
    },
    {
        "numero": "DM-569996158",
        "expedicion": "15-10-2008",
        "nacimiento": "13-04-1978",
        "vencimiento": "15-03-2024",
        "tipo_sangre": "B-",
        "tipo":"C2",
        "nombre": "Fuentes S\u00e1nchez Silvia",
        "codigo": "37231442"
    },
    {
        "numero": "DM-110778353",
        "expedicion": "23-12-2004",
        "nacimiento": "03-04-1987",
        "vencimiento": "14-06-2028",
        "tipo_sangre": "B+",
        "tipo":"C1",
        "nombre": "Gonz\u00e1lez S\u00e1nchez Daniel",
        "codigo": "86565671"
    },
    {
        "numero": "DM-743999277",
        "expedicion": "19-06-2003",
        "nacimiento": "27-11-1985",
        "vencimiento": "28-08-2029",
        "tipo_sangre": "B+",
        "tipo":"B4",
        "nombre": "Fuentes Gonz\u00e1lez Mar\u00eda",
        "codigo": "47649243"
    },
    {
        "numero": "DM-757214824",
        "expedicion": "03-08-2015",
        "nacimiento": "19-07-1985",
        "vencimiento": "09-09-2025",
        "tipo_sangre": "AB-",
        "tipo":"B3",
        "nombre": "Morales Garc\u00eda Carlos",
        "codigo": "98768764"
    },
    {
        "numero": "DM-145718412",
        "expedicion": "24-04-2001",
        "nacimiento": "10-02-1979",
        "vencimiento": "06-07-2026",
        "tipo_sangre": "O+",
        "tipo":"B2",
        "nombre": "S\u00e1nchez Fuentes Carlos",
        "codigo": "42808866"
    },
    {
        "numero": "DM-504435747",
        "expedicion": "22-11-2020",
        "nacimiento": "12-05-1999",
        "vencimiento": "27-03-2026",
        "tipo_sangre": "A+",
        "tipo":"B1",
        "nombre": "Vargas Fuentes Silvia",
        "codigo": "94635923"
    },
    {
        "numero": "DM-655837181",
        "expedicion": "09-04-2020",
        "nacimiento": "28-11-1976",
        "vencimiento": "15-02-2026",
        "tipo_sangre": "B-",
        "tipo":"A3",
        "nombre": "Herrera Vargas Miguel",
        "codigo": "22136869"
    },
    {
        "numero": "DM-191332076",
        "expedicion": "07-04-2009",
        "nacimiento": "14-04-1957",
        "vencimiento": "19-06-2027",
        "tipo_sangre": "A-",
        "tipo":"A2",
        "nombre": "Morales L\u00f3pez Laura",
        "codigo": "31855383"
    },
    {
        "numero": "DM-608521174",
        "expedicion": "26-10-2006",
        "nacimiento": "21-07-1957",
        "vencimiento": "25-01-2024",
        "tipo_sangre": "O-",
        "tipo":"A1",
        "nombre": "Herrera Vargas Isabel",
        "codigo": "95163621"
    },
    {   "numero":"DM-977077290",
        "expedicion":"15-4-2019",
        "nacimiento":"12-10-1997",
        "vencimiento":"2-3-2027",
        "tipo_sangre":"RHA+",
        "tipo":"E2",
        "nombre":"Gutiérrez Ramírez Mia",
        "codigo":"89319646"
    }
]

# Insertar los datos en la colección
result = collection.insert_many(datos)
print("Datos insertados:", result.inserted_ids)

# Cerrar la conexión
client.close()
