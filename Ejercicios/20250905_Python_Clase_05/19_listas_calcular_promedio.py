#CALCULAR EL PROMEDIO DE UNA LISTA DE NUMEROS

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)


lista_de_numeros = input("Ingrese la lista de numeros para calcular su promedio:")
enteros = []
for n in lista_de_numeros.split(','):
    enteros.append(int(n))

resultado = calcular_promedio(enteros)

print("El promedio de los numeros ingresados es:", resultado)
