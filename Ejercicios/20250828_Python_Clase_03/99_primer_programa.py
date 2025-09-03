# Programa de cálculo de descuento en una tienda.
# Capturamos el precio del producto y su descuento.
# Calculamos el precio final a partir de los datos ingresados.

# Función para calcular el descuento
def calcular_descuento(precio, porcentaje_descuento):
    descuento = precio * (porcentaje_descuento / 100)
    precio_final = precio - descuento
    return precio_final

# Función para mostrar el resultado
def mostrar_resultado(precio_inicial, porcentaje_descuento, precio_final):
    print("Precio inicial: $", precio_inicial)
    print("Porcentaje de descuento: ", porcentaje_descuento, "%")
    print("Precio final: $", precio_final)

# Solicitar el precio del producto al usuario
precio_producto = float(input("Ingrese el precio del producto: "))

# Solicitar el porcentaje de descuento al usuario
porcentaje_descuento = int(input("Ingrese el porcentaje de descuento: "))

# Calcular el precio final llamando a la función calcular_descuento
precio_final = calcular_descuento(precio_producto, porcentaje_descuento)

# Mostrar el resultado llamando a la función mostrar_resultado
mostrar_resultado(precio_producto, porcentaje_descuento, precio_final)
