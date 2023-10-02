texto = "CALDERON BLANCO MARTIN"

# Dividir la cadena en palabras
palabras = texto.split()

# Asignar las palabras a las variables
lastname1 = palabras[0]
lastname2 = palabras[1]
name = " ".join(palabras[2:])  # Une las palabras restantes para obtener el nombre

# Imprimir las variables resultantes
print("name =", name)
print("lastname1 =", lastname1)
print("lastname2 =", lastname2)