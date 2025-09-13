#Este es ub comentario
"""
mi_variable = "Variable de texto"
#print(mi_variable)
"""
#numero_a = 5
#numero_b = 5.0

#global = 0.19

#print(numero_b)
#print("Saludos")
#print(type(True))
#nombre = input("digite su nombre:")
#print("Hola", nombre)

# numero = input("digite un numero:")
# print(type(numero))
# print(numero)
# numero_a = int(numero)
# print(type(numero_a))
# print(numero_a)

# a, b, c, d, e = 1, "3", True, 1.43, 15_000_000_000_000
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))
# print(e, type(e))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

iterador_pares = iter(numero for numero in numeros if numero % 2 == 0)

try:
    while True:
        numero = next(iterador_pares)
        print(numero)
except StopIteration:
    print("Iteración finalizada")


lista = list("1234")
print(lista)


numeros = [1, 2, 3, 4, 5]
resultado = ['par' if num % 2 == 0 else 'impar' for num in numeros]

print(resultado)
# Salida: ['impar', 'par', 'impar', 'par', 'impar']
