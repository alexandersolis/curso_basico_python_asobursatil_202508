diccionario = {
    "Nombre": "Jimmy",
    "Profesion": "Ingeniero",
    "Edad": 25,
    "Direccion": {
        "pais": "Colombia",
        "Direccion": "Calle 2 # 45-01",
    }
}

while len(diccionario) > 0:
    elemento = diccionario.popitem()
    print(elemento)

print(diccionario)