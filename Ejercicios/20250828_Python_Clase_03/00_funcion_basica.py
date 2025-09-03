def saludar():
    print('Buenas noches curso de python')

#Pass no hace nada, solo permite tener una funcion con el el nombre.
def funcion_dummy():
    pass

def saludo_del_dia(nombre, edad):
    if edad < 18:
        return 'Hola ' + nombre + ' eres menor de edad'

    return 'Buenos días ' + nombre

# saludo = saludo_del_dia('Eliana', 24)
# print(saludo)

def dividir(a, b=2, c=1):
    return a / b / c

# En este llmamado b=2, aunque no se indique, se utiliza el valor por defecto
n = dividir(8)

# Utilizando parametros por nombre, no importa el orden en el que indiquen
n = dividir(b=5, c=1, a=10)

# Si utilizamos un argumento por nombre, podemos omitir los argumentos posicionales
n = dividir(10, c=1)
#print(n)

#el numero recibido se multiplica por 10
def multiplicar(a, b=0):
    return a * b

#x = int(input('Ingrese un numero: '))
#n = multiplicar(10, b=x)
#print(n)

def funcion_con_varios_tipos(a: int, b: float, c: str) -> str:
    if c == 'Suma':
        return str(a + b)
    elif c == 'Resta':
        return str(a - b)

    return str(a * b)

suma = funcion_con_varios_tipos(10, 5.5, 'Suma')
resta = funcion_con_varios_tipos(10, 5.5, 'Resta')
multiplicacion = funcion_con_varios_tipos(10, 5.5, 'Multiplicacion')

print('Suma:', suma)
print('Resta:', resta)
print('Multiplicacion:', multiplicacion)