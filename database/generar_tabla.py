import random
import datetime
import json

# Función para generar un número aleatorio de 9 dígitos
def generar_numero_aleatorio():
    return str(random.randint(100_000_000, 999_999_999))

# Función para generar una fecha aleatoria en un rango de años específico
def generar_fecha_aleatoria(año_inicio, año_fin):
    año = random.randint(año_inicio, año_fin)
    mes = random.randint(1, 12)
    dia = random.randint(1, 28)  # Asumiendo febrero como máximo 28 días
    fecha = datetime.date(año, mes, dia)
    return fecha.strftime("%d-%m-%Y")

# Función para generar un tipo sanguíneo aleatorio
def generar_tipo_sanguineo():
    tipos_sanguineos = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]
    return random.choice(tipos_sanguineos)

# Función para generar un nombre aleatorio
def generar_nombre():
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
