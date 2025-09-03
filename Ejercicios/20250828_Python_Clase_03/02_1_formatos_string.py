nombre = "Ana"

print("Hola", nombre, "¿Cómo estás?")
print("Hola " + nombre + " ¿Cómo estás?")

# Elaborando una cadena de texto con formato a variables
print(f"Hola {nombre} ¿Cómo estás?")

def sumar(a, b):
    return a + b

# Llamando a la función y mostrando el resultado a la vez que se da formato
print(f"El resultado de la suma es: {sumar(5, 10)}")


#Uso de la funcion str.format
print("Hola {} ¿Cómo estás?".format(nombre))
print("El resultado de la suma es: {}".format(sumar(5, 10)))

a = 5
b = 10
c = sumar(a, b)
print("El resultado de la suma entre {} y {} es: {}".format(a, b, c))
print(f"El resultado de la suma entre {a} y {b} es: {c}")

#formaterar un flotante con tres posiciones decimales
pi = 3.141592653589793
print(f"El valor de pi es: {pi:.3f}")
