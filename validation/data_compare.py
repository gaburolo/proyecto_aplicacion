from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("uri")

client = MongoClient(uri)
db = client.get_database()


def identitycard_compare(data):
    collection = db["cedula"]
    result = collection.find_one({"numero": data["id"]})
    if data["name"] == result["nombre"].upper():
        if data["lastname1"] == result["apellido1"].upper():
            if data["lastname2"] == result["apellido2"].upper():
                return True
            else:
                return False
        else:
            return False
    return False


def studentcard_compare(data):
    collection = db["carnet"]
    result = collection.find_one({"carnet": data["id"]})
    if data["name"] == result["nombre_completo"].upper():
        if data["date"] == result["fecha_vencimiento"].upper():
            return True
        else:
            return False
    return False

def license_compare(data):
    collection = db["licencia"]
    result = collection.find_one({"codigo": data["code"]})
    if data["name"] == result["nombre"].upper():
        if data["number"] == result["numero"]:
            if data["expedition"] == result["expedicion"]:
                if data["birth"] == result["nacimiento"]:
                    if data["expiration"] == result["vencimiento"]:
                        if data["blood_type"] == result["tipo_sangre"]:
                            if data["type"] == result["tipo"]:
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False               
        else:
            return False
    return False