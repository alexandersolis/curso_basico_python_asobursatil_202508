# Escribe un programa que tome dos diccionarios y los combine en uno solo, 
# manteniendo las claves y sumando los valores si hay claves repetidas

def combinar_diccionarios(diccionario1, diccionario2):
    resultado = {}

    # Combinar los diccionarios
    for clave, valor in diccionario1.items():
        resultado[clave] = valor

    for clave, valor in diccionario2.items():
        if clave in resultado:
            resultado[clave] += valor
        else:
            resultado[clave] = valor

    return resultado

# Ejemplo de uso
diccionario1 = {'a': 10, 'b': 20, 'c': 30}
diccionario2 = {'b': 5, 'c': 15, 'd': 25}

resultado = combinar_diccionarios(diccionario1, diccionario2)
print(resultado)