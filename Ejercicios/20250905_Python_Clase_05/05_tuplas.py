tupla = (4, 3, 9, 6, 1)
print(tupla)

#los elementos de una tupla no se peden modificar
tupla[0] = 8

#ordemar una tupla
tupla_ordenada = sorted(tupla)
print(tupla_ordenada)
#lista.sort()

#reversar u orden descendente
tupla_reverse = tuple(reversed(tupla_ordenada))
print(tupla_reverse)