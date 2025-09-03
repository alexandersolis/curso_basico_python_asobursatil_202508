texto = "Estamos aprendiendo a trabajar con cadenas de texto en Python"

# print(f"El texto tiene {len(texto)} caracteres")
# print(f"El tercer carácter del texto es: {texto[2]}")
# print(f"El último carácter del texto es: {texto[-1]}")
# print(f"Los primeros 5 caracteres del texto son: {texto[:5]}")
# print(f"Los últimos 5 caracteres del texto son: {texto[-5:]}")

# print(texto[2:25:3])

# print(texto[-6:])

# Contar cuántas veces aparece la letra 'p'
s = texto.count('p')
print(s)
# Reemplazar la letra 'a' por '--'
print(texto.replace('a', '--'))
print(texto.upper()) # Convertir a mayúsculas
print(texto.lower()) # Convertir a minúsculas
lista = texto.split() # Por defecto separa por espacios
print(lista)
print(texto.replace('cadena', '@@@@@@@@@@@@@@@@'))

