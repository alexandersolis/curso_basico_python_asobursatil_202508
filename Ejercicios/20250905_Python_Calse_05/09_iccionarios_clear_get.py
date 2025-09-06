diccionario = {}
diccionario["Cindy"] = {"Edad": 20, "Profesion": "Ingeniera"}
diccionario["Andrea"] = {"Edad": 22, "Profesion": "Economista"}
print(diccionario)

edad = diccionario["Cindy"].get("Edad")
direccion = diccionario["Cindy"].get("Direccion", "Sin direccion")
print(edad, direccion)

diccionario.clear()
print(diccionario)
