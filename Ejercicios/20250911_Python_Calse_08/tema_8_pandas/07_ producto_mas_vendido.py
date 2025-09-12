import pandas as pd
                 
# Cargar el archivo CSV
df = pd.read_csv('ventas.csv')

# Calcular el total de ventas por producto
ventas_por_producto = df.groupby('Producto')['Ventas'].sum()

# Encontrar el producto con el mayor total de ventas
producto_mas_vendido = ventas_por_producto.idxmax()

# Obtener el valor de ventas del producto más vendido
ventas_mas_vendido = ventas_por_producto.loc[producto_mas_vendido]

# Imprimir el resultado
print(f"El producto más vendido es: {producto_mas_vendido}")
print("Total de ventas: {:,.2f}".format(ventas_mas_vendido))

