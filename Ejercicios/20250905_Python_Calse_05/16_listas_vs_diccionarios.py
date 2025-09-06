"""
En el código siguiente se implementa el glosario utilizando dos listas: 
en la primera se almacenarían los conceptos a definir (siguiendo un orden lexicográfico, 
aunque en este caso el orden podría ser arbitrario) y en la segunda lista 
aparecen las definiciones correspondientes: aquí el orden tiene que ser consecuente
 con el orden elegido para la primera lista, cualquiera que este sea.
"""
conceptos = ['hashable', 'inmutable', 'interactivo', 'interpretado', 'iterable']
definiciones = ['Si su valor "hash" nunca cambia. Pueden actuar como "clave de diccionarios".',
                'Objeto con valor fijo.',
                'Python posee un intérprete interactivo.',
                'Python es un lenguaje interpretado.',
                'Objeto capaz de devolver sus elementos, uno cada vez.']

concepto = input('Diga concepto a buscar en lista: ')

indice = conceptos.index(concepto)
definicion = definiciones[indice]

print(definicion)

# Glosario de Python implementado con un diccionario
# La tarea es realizable utilizando listas, pero resulta más compacta e intuitiva 
# si se utilizan los diccionarios de Python

glosario = {'hashable': 'Si su valor "hash" nunca cambia. Pueden actuar como "clave de diccionarios".',
            'inmutable': 'Objeto con valor fijo.',
            'interactivo': 'Python posee un intérprete interactivo.',
            'interpretado': 'Python es un lenguaje interpretado.',
            'iterable': 'Objeto capaz de devolver sus miembros, uno cada vez.'}

concepto = input('Diga concepto a buscar en diccionario: ')
definicion = glosario[concepto]
print(definicion)