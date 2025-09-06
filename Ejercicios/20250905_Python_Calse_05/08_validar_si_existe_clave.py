diccionario1 = {
    "Nombre": "Jimmy",
    "Profesion": "Ingeniero",
    "Edad": 25,
    "Direccion": {
        "pais": "Colombia",
        "Direccion": "Calle 2 # 45-01",
    }
}

if "Direccion" in diccionario1:
    direccion = diccionario1.get("Direccion")
    print(direccion)
    # if direccion.get("Ciudad", 0) > 0:
    if "Ciudad" in direccion:
        print("La ciudad de la direccion es:", direccion.get("Ciudad"))
    else:
        print("La direccion no tiene ciudad")
else:
    print("La direccion no existe en el diccionario")
