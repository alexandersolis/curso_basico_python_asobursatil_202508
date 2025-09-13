lista = [7, 3, 9, 0, 2, 1]
print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#eliminar un elemento
elemento = lista.pop()
print(elemento)
print(lista)

n = lista.pop(1)
print(n)
print(lista)