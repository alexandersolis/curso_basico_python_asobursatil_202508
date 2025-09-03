lista = [1, 2, 3, 4, 5, 6, 7]

indice = -1
while indice < len(lista)-1:
    indice += 1

    #Si el numero en la posicion actual es 3, se salta la iteracion
    if lista[indice] == 3:
        continue

    #Si el indice es 3, se salta la iteracion (omite el numero 4)
    if indice == 3:
        continue

    #ESTA LINEA NO SE EJECUTA SI LLAMO, CONTINUE
    print(lista[indice])
