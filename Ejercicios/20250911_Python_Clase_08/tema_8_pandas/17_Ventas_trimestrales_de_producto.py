import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo de Excel en un DataFrame
df = pd.read_excel('ventas.xlsx')

# Filtrar los datos para el producto específico
producto = input('Ingrese un producto:')
df_filtrado = df[df['Producto'] == producto]

# Crear un diccionario para mapear los nombres de los meses a números
meses = {
    'Enero': 1,
    'Febrero': 2,
    'Marzo': 3,
    'Abril': 4,
    'Mayo': 5,
    'Junio': 6,
    'Julio': 7,
    'Agosto': 8,
    'Septiembre': 9,
    'Octubre': 10,
    'Noviembre': 11,
    'Diciembre': 12
}

# Convertir los nombres de los meses a números
df_filtrado['Mes'] = df_filtrado['Mes'].map(meses)

# Agrupar los datos por región y trimestre, y calcular la suma de las ventas
trimestres = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]
df_filtrado['Trimestre'] = pd.cut(df_filtrado['Mes'], bins=[0, 3, 6, 9, 12], labels=['T1', 'T2', 'T3', 'T4'])
ventas_por_region_trimestre = df_filtrado.groupby(['Region', 'Trimestre'])['Ventas'].sum()

# Reformatear los datos para tener los trimestres como columnas
ventas_por_region_trimestre = ventas_por_region_trimestre.unstack(level=1)

# Crear el gráfico de barras agrupado para los cuatro trimestres
ventas_por_region_trimestre.plot(kind='bar')

# Configurar los ejes y el título
plt.xlabel('Región')
plt.ylabel('Ventas')
plt.title(f'Ventas de {producto} por Región en los Cuatro Trimestres')

# Mostrar el gráfico
plt.show()
