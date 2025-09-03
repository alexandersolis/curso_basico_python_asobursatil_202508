def convertir_texto(cadena, a_mayusculas=True):
    #if a_mayusculas == True:
    if a_mayusculas:
        return cadena.upper()
    else:
        return cadena.lower()


minusculas = convertir_texto("Hola buenos Dias", False)
mayusculas = convertir_texto("Hola buenos Dias")

print("Mayusculas:", mayusculas)
print("Minusculas:", minusculas)
