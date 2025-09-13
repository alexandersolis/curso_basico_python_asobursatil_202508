# Recuerda instalar pandas: pip install pandas
import pandas as pd
# Recuerda instalar matplotlib: pip install matplotlib
import matplotlib.pyplot as plt

# Cargar el archivo Excel
df = pd.read_excel('ventas.xlsx')

# Calcular las ventas totales por región y mes
ventas_totales = df.groupby(['Region', 'Mes'])['Ventas'].sum()

# Imprimir el resumen de ventas totales por región y mes
print("Resumen de ventas totales por región y mes:")
print(ventas_totales)

# VISUALIZACION DE DATOS Y ASIGNACION DE COLORES
# https://htmlcolorcodes.com/
# https://matplotlib.org/stable/gallery/color/named_colors.html
# colors = ['#FF0000', '#0000FF', '#FFFF00', '#008000', '#800080', '#00FFFF']
colors = ['red', 'blue', 'yellow', 'green', 'purple', 'aqua']

# Determinar los productos más vendidos en cada región
productos_mas_vendidos = df.groupby(['Region', 'Producto'])['Ventas'].sum().reset_index()
productos_mas_vendidos = productos_mas_vendidos.groupby('Region').apply(lambda x: x.nlargest(1, 'Ventas'))

# Imprimir los productos más vendidos en cada región
print("\nProductos más vendidos por región:")
print(productos_mas_vendidos)

# Identificar los 3 meses con mayores ventas
meses_mayores_ventas = df.groupby('Mes')['Ventas'].sum().nlargest(3)

# Imprimir los meses con mayores ventas
print("\nMeses con mayores ventas:")
print(meses_mayores_ventas)

# Comparar las ventas entre diferentes regiones utilizando gráficos
ventas_por_region = df.groupby('Region')['Ventas'].sum()
print(ventas_por_region)

# alpha: Have referencia la nivel de transparencia de los colores
# donde 0.0 es totalmente transparente, y 1.0 es sin transparencia.
plt.bar(ventas_por_region.index, ventas_por_region.values, color=colors, alpha=0.5)
plt.xlabel('Región')
plt.ylabel('Ventas')
plt.title('Ventas por Región')
plt.show()
#plt.savefig('Ventas.jpg')
