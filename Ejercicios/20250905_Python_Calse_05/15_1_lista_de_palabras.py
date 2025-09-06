lista_palabras = ["Hola", "Mundo", "Python", "Es", "Genial"]
print(lista_palabras)

lista_filtrada = []
for palabra in lista_palabras:
    if len(palabra) > 5:
        lista_filtrada.append(palabra)

print(lista_filtrada)

#Usando comprensión de listas
lista_filtrada2 = [palabra for palabra in lista_palabras if len(palabra) > 5]
print(lista_filtrada2)


#Lista de nombres con duplicados
lista_nombres = ["Ana", "Luis", "Pedro", "Ana", "Maria", "Luis"]
print(lista_nombres)

#Version larga
set_2 = set()
for nombre in lista_nombres:
    set_2.add(nombre)
print(set_2)

#Version corta
set_3 = set(lista_nombres)
print(set_3)
