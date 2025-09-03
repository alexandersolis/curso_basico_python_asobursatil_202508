#validar longitud de un texto, maximo 29 caracteres
texto = input("Ingrese un texto (max 20 caracteres):")

if len(texto) > 20:
    print("El texto no puede superar 20 caracteres")
elif len(texto) < 5:
    print("El texto no puede ser menor de 5 caracteres")
else:
    print("Validacion exitosa!!")