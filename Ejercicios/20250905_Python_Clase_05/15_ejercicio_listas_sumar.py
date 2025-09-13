#SUMAR LOS LEMENTOS DE UNA LISTA
numeros = input("Ingrese los numeros a sumar (separador=','):")
print(numeros)

lista_numeros = numeros.split(",")
print(lista_numeros)

resultado = 0
for n in lista_numeros:
    resultado = resultado + int(n)

print(resultado)
