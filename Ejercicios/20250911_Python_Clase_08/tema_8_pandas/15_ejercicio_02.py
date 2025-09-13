# Recuerda instalar pandas: pip install pandas
import pandas as pd
# Recuerda instalar matplotlib: pip install matplotlib
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('ventas.csv')

# Exploración inicial de los datos
print("Primeras filas del DataFrame:")
print(df.head())

print("\nInformación básica del DataFrame:")
print(df.info())

# Ventas totales por región
ventas_por_region = df.groupby('Region')['Ventas'].sum()

# Gráfico de barras de ventas totales por región
ventas_por_region.plot(kind='bar')
plt.xlabel('Región')
plt.ylabel('Ventas Totales')
plt.title('Ventas Totales por Región')
plt.show()

# Distribución de las ventas mensuales
ventas_por_mes = df.groupby('Mes')['Ventas'].sum()

# Gráfico de líneas de las ventas mensuales
ventas_por_mes.plot(kind='line')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.title('Distribución de las Ventas Mensuales')
plt.show()

# Productos más vendidos
productos_mas_vendidos = df.groupby('Producto')['Ventas'].sum().nlargest(5)

# Gráfico de barras de los productos más vendidos
productos_mas_vendidos.plot(kind='bar')
plt.xlabel('Producto')
plt.ylabel('Ventas Totales')
plt.title('Productos Más Vendidos')
plt.show()

# # Correlación entre ventas y edad de los clientes
# df.plot.scatter(x='Edad', y='Ventas')
# plt.xlabel('Edad')
# plt.ylabel('Ventas')
# plt.title('Correlación entre Ventas y Edad')
# plt.show()

# Análisis de tendencias de ventas a lo largo de los meses
ventas_por_mes.plot(kind='line')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.title('Tendencias de Ventas Mensuales')
plt.xticks(rotation=45)
plt.show()
