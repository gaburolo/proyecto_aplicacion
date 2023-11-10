from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
uri = os.getenv("uri")

client = MongoClient(uri)
db = client.get_database()


def identitycard_compare(data):
    """
    The function `identitycard_compare` compares the data provided with the data stored in a MongoDB
    collection to check if the name and last names match.
    
    :param data: The "data" parameter is a dictionary that contains the following keys:
    :return: a boolean value. It returns True if the data provided matches the data stored in the
    "cedula" collection in the database, and False otherwise.
    """
    collection = db["cedula"]
    result = collection.find_one({"numero": data["id"]})
    if result != None:
        if data["name"] == result["nombre"].upper():
            if data["lastname1"] == result["apellido1"].upper():
                if data["lastname2"] == result["apellido2"].upper():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return False


def studentcard_compare(data):
    """
    The function `studentcard_compare` compares the data provided with the data stored in a database
    collection to check if the student card information matches.
    
    :param data: The `data` parameter is a dictionary that contains the following keys:
    :return: a boolean value. It returns True if the student card data matches the data stored in the
    database, and False otherwise.
    """
    collection = db["carnet"]
    result = collection.find_one({"carnet": data["id"]})
    if result != None:
        if data["name"] == result["nombre_completo"].upper():
            if data["date"] == result["fecha_vencimiento"].upper():
                return True
            else:
                return False
        else:
            return False
    return False

def license_compare(data):
    """
    The function `license_compare` compares the data provided with a license stored in a database and
    returns True if all the data matches, otherwise it returns False.
    
    :param data: The parameter "data" is a dictionary that contains the following keys:
    :return: a boolean value. It returns True if all the conditions in the nested if statements are met,
    indicating that the data provided matches the corresponding fields in the "licencia" collection in
    the database. If any of the conditions are not met, it returns False. If the result from the
    database query is None, it also returns False.
    """
    collection = db["licencia"]
    result = collection.find_one({"codigo": data["code"]})
    if result != None:
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
        else:
            return False
    return False