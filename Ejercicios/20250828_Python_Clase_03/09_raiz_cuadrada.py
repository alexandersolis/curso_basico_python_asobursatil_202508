import math

def raiz_cuadrada_desde_math(numero):
    return math.sqrt(numero)


def raiz_cuadrada(numero):
    return numero**0.5


numero = int(input("Ingrese un numero:"))
resultado_1 = raiz_cuadrada_desde_math(numero=numero)
resultado_2 = raiz_cuadrada(numero=numero)

print("La Raiz cuadrada (Usando SQRT) de {} es:{}".format(numero, resultado_1))
print("La Raiz cuadrada (Usando **) de {} es:{}".format(numero, resultado_2))

