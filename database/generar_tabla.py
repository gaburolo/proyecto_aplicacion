import random
import datetime
import json

def generar_numero_aleatorio():
    """
    The function generates a random 9-digit number as a string.
    :return: a randomly generated number as a string.
    """
    return str(random.randint(100_000_000, 999_999_999))

def generar_fecha_aleatoria(año_inicio, año_fin):
    """
    The function `generar_fecha_aleatoria` generates a random date within a given range and returns it
    in the format "dd-mm-yyyy".
    
    :param o_inicio: The parameter "año_inicio" represents the starting year from which the random date
    will be generated
    :param o_fin: The parameter "año_inicio" represents the starting year from which the random date
    will be generated
    :return: a randomly generated date in the format "dd-mm-yyyy".
    """
    año = random.randint(año_inicio, año_fin)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28) 
    fecha = datetime.date(año, mes, dia)
    return fecha.strftime("%d-%m-%Y")

def generar_tipo_sanguineo():
    """
    The function "generar_tipo_sanguineo" generates a random blood type from a list of blood types.
    :return: a randomly chosen blood type from the list of blood types.
    """
    tipos_sanguineos = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    return random.choice(tipos_sanguineos)

def generar_nombre():
    """
    The function generates a random full name by combining a random first name from a list of names and
    two random last names from a list of last names.
    :return: a randomly generated full name in the format "Last Name1 Last Name2 First Name".
    """
    nombres = ["Ana", "Luis", "Carlos", "Laura", "Javier", "María", "Daniel", "Isabel", "Miguel", "Silvia"]
    apellidos = ["García", "Rojas", "Vargas", "Fuentes", "Herrera", "Sánchez", "López", "Jiménez", "Morales", "González"]
    nombre = random.choice(nombres)
    apellido1 = random.choice(apellidos)
    apellido2 = random.choice(apellidos)
    return f"{apellido1} {apellido2} {nombre}"

# Genera datos de ejemplo
datos_ejemplo = [
    {
        "Numero": f"DM - {generar_numero_aleatorio()}",
        "Expedicion": generar_fecha_aleatoria(2001, 2023),
        "Nacimiento": generar_fecha_aleatoria(1950, 1999),
        "Vencimiento": generar_fecha_aleatoria(2024, 2030),
        "TipoSanger": generar_tipo_sanguineo(),
        "Nombre": generar_nombre(),
        "Codigo": generar_numero_aleatorio(),
    }
    for _ in range(20)  # Genera 10 conjuntos de datos de ejemplo
]

# Nombre del archivo de texto
nombre_archivo = "datos_ejemplo.json"

# Guarda los datos en un archivo JSON
with open(nombre_archivo, "w") as archivo:
    json.dump(datos_ejemplo, archivo, indent=4)

print(f"Los datos se han guardado en {nombre_archivo}")
