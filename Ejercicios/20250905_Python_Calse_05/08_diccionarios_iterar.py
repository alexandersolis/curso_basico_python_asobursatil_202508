diccionario1 = {
    "Nombre": "Jimmy",
    "Profesion": "Ingeniero",
    "Edad": 25,
    "Direccion": {
        "pais": "Colombia",
        "Direccion": "Calle 2 # 45-01",
    }
}

#iterar un diccionario pro cada una de sus llaves
for llave in diccionario1:
    print(llave, ":", diccionario1[llave])

#iterar un diccionario pro cada una de sus llaves
for llave in diccionario1.keys():
    print(llave)

#iterar un diccionario pro cada una de sus llaves y valores
for llave, valor in diccionario1.items():
    print(llave, ":", valor)

#iterar un diccionario pro cada uno de sus valores
for valor in diccionario1.values():
    print(valor)
