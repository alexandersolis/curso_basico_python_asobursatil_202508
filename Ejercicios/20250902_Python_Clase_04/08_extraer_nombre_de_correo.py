#CAPTURE UN CORREO ELECTRONICO POR PANTALLA
#EXTRAR EL NOMBRE DE USUARIO Y EL DOMINIO

correo = input("Ingresa un correo:")
nombre = ""
dominio = ""

arroba_encontrada = False
for letra in correo:
    if letra == "@":
        arroba_encontrada = True
        continue

    if arroba_encontrada:
        dominio = dominio + letra
    else:
        nombre += letra

print(nombre)
print(dominio)
