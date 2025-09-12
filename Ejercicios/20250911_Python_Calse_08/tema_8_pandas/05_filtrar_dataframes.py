import pandas as pd

# Cargar el archivo Excel
df = pd.read_excel('Ventas.xlsx')

# Cargar el archivo CSV
# df = pd.read_csv('Ventas.csv')

# Filtrar por la región Andina (Columna B del Excel)
# andina = df['Region'] == 'Andina'
# print(andina)

# Filtrar por la región Andina y el mes de Enero
andina = (df['Region'] == 'Andina') & (df["Mes"] == "Enero")
#print(andina.head(30))
#print(andina.tail(12))

df_filtro_andina = df[andina]
print(df_filtro_andina.tail())
