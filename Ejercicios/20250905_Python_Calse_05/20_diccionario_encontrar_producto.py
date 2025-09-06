# Dado un diccionario de productos y sus precios, 
# crea una función que encuentre el producto más caro y devuelva su nombre y precio.

def encontrar_producto_mas_caro(diccionario):
    producto_mas_caro = ""
    precio_mas_alto = 0

    for producto, precio in diccionario.items():
        if precio > precio_mas_alto:
            precio_mas_alto = precio
            producto_mas_caro = producto

    return producto_mas_caro, precio_mas_alto

# Ejemplo de diccionario de productos y precios
productos = {
    "Manzanas": 2.50,
    "Plátanos": 1.75,
    "Fresas": 3.20,
    "Naranjas": 2.80
}

# Obtener el producto más caro
producto_mas_caro, precio_mas_alto = encontrar_producto_mas_caro(productos)

print(f"El producto más caro es: {producto_mas_caro} (${precio_mas_alto})")

