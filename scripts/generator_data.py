import random

nombres = [
    "Juan", "María", "Pedro", "Ana", "Luis", "Laura",
    "Carlos", "Sofía", "José", "Isabella", "Andrés", "Valentina",
    "Miguel", "Camila", "Alejandro", "Lucía", "Diego", "Valeria",
    "Javier", "Diana", "Fernando", "Paula", "Rafael", "Catalina",
    "Daniel", "Elena", "Adrián", "Natalia", "Simón", "Daniela",
    "Emilia", "Oliver", "Sophia", "Max", "Aria", "Ethan",
    "Ella", "Noah", "Mia", "Liam", "Ava", "Sebastian",
    "Grace", "Elijah", "Lily", "William", "Zoe", "Henry",
    "Nora", "James", "Charlotte", "Samuel", "Amelia", "Benjamin",
    "Scarlett", "Lucas", "Madison", "Alexander", "Chloe",
    "Daniel", "Evelyn", "Logan", "Harper", "Michael", "Abigail",
    "Isabella", "Liam", "Ava", "Noah", "Sophia", "Lucas",
    "Olivia", "Mason", "Emma", "Logan", "Mia", "Ethan",
    "Sophie", "Elijah", "Harper", "William", "Lily", "James",
    "Amelia", "Daniel", "Chloe", "Benjamin", "Aria", "Henry",
    "Grace", "Samuel", "Zoe", "Alexander", "Ella",
    "Michael", "Emily", "Jackson", "Scarlett", "David", "Avery",
]

apellidos1 = [
    "García", "López", "Martínez", "Rodríguez", "Fernández",
    "Pérez", "Gómez", "Sánchez", "Ramírez", "Díaz",
    "Hernández", "Torres", "González", "Vargas", "Jiménez",
    "Castro", "Ruiz", "Silva", "Ortiz", "Alvarez",
    "Molina", "Flores", "Rojas", "Cruz", "Reyes",
    "Smith", "Johnson", "Brown", "Jones", "Miller",
    "Davis", "García", "Rodríguez", "Martínez", "Hernández",
    "López", "González", "Pérez", "Williams", "Sánchez",
    "Ramírez", "Jackson", "Moore", "Taylor", "Anderson",
    "Thomas", "White", "Harris", "Martin", "Thompson",
    "Walker", "Hall", "Young", "King", "Wright",
    "Johnson", "Williams", "Jones", "Brown", "Davis",
    "Miller", "Wilson", "Moore", "Taylor", "Anderson",
    "Thomas", "Jackson", "White", "Harris", "Martin",
    "Thompson", "Robinson", "Walker", "Young", "Hall",
    "Lee", "Allen", "Hernandez", "King", "Wright", "Lewis",
    "Green", "Baker", "Adams", "Mitchell", "Evans",
]


apellidos2 = [
    "Pérez", "Gómez", "Sánchez", "Ramírez", "Díaz",
    "Hernández", "Torres", "González", "Vargas", "Jiménez",
    "Castro", "Ruiz", "Silva", "Ortiz", "Alvarez",
    "Molina", "Flores", "Rojas", "Cruz", "Reyes",
    "Gutiérrez", "Núñez", "Mendoza", "Guerrero", "Soto",
    "Smith", "Johnson", "Brown", "Jones", "Miller",
    "Davis", "García", "Rodríguez", "Martínez", "Hernández",
    "López", "González", "Pérez", "Williams", "Sánchez",
    "Ramírez", "Jackson", "Moore", "Taylor", "Anderson",
    "Thomas", "White", "Harris", "Martin", "Thompson",
    "Walker", "Hall", "Young", "King", "Wright",
    "Isabella", "Liam", "Ava", "Noah", "Sophia", "Lucas",
    "Olivia", "Mason", "Emma", "Logan", "Mia", "Ethan",
    "Sophie", "Elijah", "Harper", "William", "Lily", "James",
    "Amelia", "Daniel", "Chloe", "Benjamin", "Aria", "Henry",
    "Grace", "Samuel", "Zoe", "Alexander", "Ella",
    "Michael", "Emily", "Jackson", "Scarlett", "David", "Avery",
    
]

def generar_nombre():
    nombre = random.choice(nombres)
    segundo_nombre = random.choice(nombres) if random.choice([True, False]) else ""
    return f"{nombre} {segundo_nombre}".strip()

def generar_apellido1():
    return random.choice(apellidos1)

def generar_apellido2():
    return random.choice(apellidos2)

def generar_numero():
    numero = str(random.randint(1, 9)) 
    numero += ' ' 
    for _ in range(2): 
        grupo = ''.join(str(random.randint(0, 9)) for _ in range(4))
        numero += grupo + ' ' 
    return numero.strip() 

def generar_numero_con_año():
    año = random.randint(2000, 2023)
    numero = str(año) + ''.join(str(random.randint(0, 9)) for _ in range(6))
    return numero


def generar_numero_con_tipo():
    tipo = random.choice(["DM", "CI"]) 
    numero = tipo + '-' + ''.join(str(random.randint(0, 9)) for _ in range(9))
    return numero

def generar_fecha():
    mes = random.randint(1, 12)
    año = random.randint(2024, 2030) 
    fecha = f"{mes}/{año}"
    return fecha

def generar_texto_tipo():
    opciones = ["A1", "A2", "A3", "B1", "B2", "B3", "B4", "C1", "C2", "D1", "D2", "D3", "E1", "E2"]
    texto_aleatorio = random.choice(opciones)
    return texto_aleatorio


def generar_fechas():
    año_nacimiento = random.randint(1930, 2004)
    mes_nacimiento = random.randint(1, 12)
    dia_nacimiento = random.randint(1, 28)
    fecha_nacimiento = f"{dia_nacimiento}-{mes_nacimiento}-{año_nacimiento}"

    años_despues = random.randint(18, 25)
    año_expediente = año_nacimiento + años_despues
    mes_expediente = random.randint(1, 12)
    dia_expediente = random.randint(1, 28)
    fecha_expediente = f"{dia_expediente}-{mes_expediente}-{año_expediente}"

    año_vencimiento = random.randint(2024, 2030)
    mes_vencimiento = random.randint(1, 12)
    dia_vencimiento = random.randint(1, 28) 
    fecha_vencimiento = f"{dia_vencimiento}-{mes_vencimiento}-{año_vencimiento}"

    return {
        "Nacimiento": fecha_nacimiento,
        "Expediente": fecha_expediente,
        "Vencimiento": fecha_vencimiento
    }

def generar_codigos():
    codigo1 = ''.join(str(random.randint(0, 9)) for _ in range(8))

    numeros_primeros = ''.join(str(random.randint(0, 9)) for _ in range(8))
    numeros_ultimos = ''.join(str(random.randint(0, 9)) for _ in range(2))
    codigo2 = numeros_primeros + ' ' + numeros_ultimos
    
    return codigo1, codigo2 

def generar_tipo_sangre():
    tipos_sangre = ["A+", "NL", "RHA+", "RHO+", "O+"]
    tipo_sangre_seleccionado = random.choice(tipos_sangre)
    return tipo_sangre_seleccionado
