import os
import platform

if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")

# #Conocer la ruta en memoria de una variable, funcion id()
# dato = "Hola"
# id_dato = id(dato)
# print(f"El id de la variable dato es: {id_dato}")

# Numero_a = 8
# numero_b = 6

# resultado = Numero_a + numero_b

# nombre_a = nombre_b = nombre_c = "Juan"
# Logra el mismo efecto de..., pero en una sola linea de codigo.
# nombre_a = "Juan"
# nombre_b = "Juan"
# nombre_c = "Juan"

# print("Nombre_a = ", nombre_a)
# print("Nombre_b = ", nombre_b)
# print("Nombre_c = ", nombre_c)

# nombre_b = 'Pedro'

# print("Nombre_b = ", nombre_b)

# # Asignacion de valores a una variable
# people = 543345
# total_population = people

# print("Total de poblacion: ", total_population)
# print("Id de total_population: ", id(total_population))
# print("Id de people: ", id(people))

# # Conocer el tipo de dato almacenado en uan variable
# x = 24
# a = 'Hola'
# b = 3.5
# c = True
# d = 1_000_000_000_000

# s = int(c)  # Conversion de booleano a entero

# print("El tipo de dato de x es: ", type(x))
# print("El tipo de dato de a es: ", type(a))
# print("El tipo de dato de b es: ", type(b))
# print("El tipo de dato de c es: ", type(c))

# s = "Peter's house"
# print(s)

# f = """Hola
# Como estas?
# dfgsfgsffg
# sf
# sddfg"""

# print(f)

# nombre = input("Cual es tu nombre? ")
# print("Hola " + nombre + ", bienvenido a Python")

# edad = input("Cual es tu edad? ")
# edad_int = int(edad)
# print("Tu edad es: ", edad_int)


d = 'Hola pythonistas'
print(d)

s = 'Hola curso, Saludos'
print(type(s))
print(len(s))
