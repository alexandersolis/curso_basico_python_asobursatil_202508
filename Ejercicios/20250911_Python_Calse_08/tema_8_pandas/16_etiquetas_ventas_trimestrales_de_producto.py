import pandas as pd
import matplotlib.pyplot as plt

# función para agregar las etiquetas a las barras
def addlabels(x,y):
    for i in range(len(x)):
        #plt.text(i, y[i], y[i], ha = 'center')

        # Mostrar las etiquetas en millones
        #plt.text(i, y[i], (y[i]/1000000), ha = 'center')
 
        # Mostrar las etiquetas en millones, redondeados a 2 decimales
        plt.text(i, y[i], (y[i]/1000000).round(2), ha = 'center')

# Cargar el archivo de Excel en un DataFrame
df = pd.read_excel('ventas.xlsx')

colors = ['red', 'blue', 'yellow', 'green', 'purple', 'aqua']

trimestres = [
    ['Enero', 'Febrero', 'Marzo'],
    ['Abril', 'Mayo', 'Junio'],
    ['Julio', 'Agosto', 'Septiembre'],
    ['Octubre', 'Noviembre', 'Diciembre']
    ]

nombres_trimestres = ["Perimer", "Segundo", "Tercero", "Cuarto"]

producto = input("Ingrese un producto: ")
trimestre = int(input("Ingrese un trimestre (Valor numerico entre 1 y 4): "))

# Filtrar los datos para los primeros tres meses del año y el producto específico
df_filtrado = df[(df['Mes'].isin(trimestres[trimestre-1])) & (df['Producto'] == producto)]

# Agrupar los datos por región y calcular la suma de las ventas
ventas_por_region = df_filtrado.groupby('Region')['Ventas'].sum()

# Crear el gráfico de barras agrupado
#ventas_por_region.plot(kind='bar')
ventas_por_region.plot(kind='bar', color=colors)
#ventas_por_region.plot(kind='bar', alpha=0.5, color=colors)
#plt.bar(ventas_por_region.index, ventas_por_region.values)

# Llamar la funcion que agrega las etiquetas a las barras
addlabels(ventas_por_region.index, ventas_por_region.values)

# Configurar los ejes y el título
plt.xlabel('Región')
plt.ylabel('Ventas')
plt.title(f'Ventas de {producto} por Región en el {nombres_trimestres[trimestre-1]} Trimestre')

# Mostrar el gráfico
plt.show()