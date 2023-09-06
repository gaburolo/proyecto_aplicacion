import random

# Listas de nombres y apellidos
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


# Función para generar nombres aleatorios
def generar_nombre():
    nombre = random.choice(nombres)
    segundo_nombre = random.choice(nombres) if random.choice([True, False]) else ""
    return f"{nombre} {segundo_nombre}".strip()

# Función para generar apellido 1
def generar_apellido1():
    return random.choice(apellidos1)

# Función para generar apellido 2
def generar_apellido2():
    return random.choice(apellidos2)

def generar_numero():
    numero = str(random.randint(1, 9))  # Genera el primer dígito (1-9)
    numero += ' '  # Agrega un espacio
    for _ in range(2):  # Genera tres grupos de cuatro dígitos cada uno
        grupo = ''.join(str(random.randint(0, 9)) for _ in range(4))
        numero += grupo + ' '  # Agrega el grupo de cuatro dígitos y un espacio
    return numero.strip() 

numero_generado = generar_numero()
print(numero_generado)