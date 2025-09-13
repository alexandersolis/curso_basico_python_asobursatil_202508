
import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('Ventas.csv')

# Obtener ventas totales por región y mes
ventas_totales = df.groupby(['Region', 'Mes'])['Ventas'].sum()

# Imprimir el resumen de ventas totales por región y mes
print("Resumen de ventas totales por region y mes:")
print(ventas_totales)

# Obtener ventas totales y promedio por producto
ventas_productos = df.groupby('Producto')['Ventas'].agg(['sum', 'mean'])

# Dar formato de dos decimales al promedio
ventas_productos['mean'] = ventas_productos['mean'].round(2)

# Imprimir el resumen de ventas totales y promedio por producto
print("\nResumen de ventas totales y promedio por producto:")
print(ventas_productos)
