#ELEMENTOS UNICOS Y ORDENADOS
lista = [1, 2, 3, 4, 3, 2, 8, 0, 2, 8, 1]
set1 = set(lista)
print(set1) # {0, 1, 2, 3, 4, 8}

set1.add(5)
print(set1)

set1.add(1)
print(set1)
