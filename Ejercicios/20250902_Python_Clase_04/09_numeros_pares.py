#CAPTURA UN NUMERO E IMPRIME LOS NUMEROS PARES DESDE CERO HASTA NUMERO-1
numeros_hasta = int(input("Ingrese limite:"))
for numero in range(numeros_hasta+1):
    if numero % 2 != 0:
        continue
    print(numero)
