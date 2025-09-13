diccionario1 = {
    "Nombre": "Jimmy",
    "Profesion": "Ingeniero",
    "Edad": 25,
    "Direccion": {
        "pais": "Colombia",
        "Direccion": "Calle 2 # 45-01",
        "Ciudad": "Bogota"
    }
}

print(diccionario1["Profesion"])
print(diccionario1.get("Edad"))
print(diccionario1.get("edad")) #Devuelve None, por que edad no existe, existe Edad
print(diccionario1.get("edad", 0)) #Devuelve 0, por que edad no existe, existe Edad

diccionario1["Profesion"] = "Medico"
diccionario1["Genero"] = "Masculino"
diccionario1["Direccion"]["Ciudad"] = "Medellin"

print(diccionario1)