lista = [1, 2, 3, 4, "Hola", 3.8, True, ["a", "b", "c"]]
# print(lista)
# copia = lista
# print(copia)
# copia[2] = "Martes"
# print(copia)
# print(lista)  # La lista original también se ve afectada porque 'copia' es una referencia a la misma lista en memoria.

# Para crear una copia independiente, usamos el método copy()
copia_independiente = lista.copy()
#print(copia_independiente)
copia_independiente[3] = "Miercoles"
print(copia_independiente)
print(lista)  # La lista original no se ve afectada.
