import pandas as pd

df = pd.read_excel('ventas.xlsx')

# Agregamos la columna Cantidad
# Para agregar una nueva columna, la asignamos al dataFrame con el nombre de la columna.
df['Cantidad'] = pd.Series([])
print(df)

# Eliminar una columna, utilizamos el método pop, indicando el nombre de la columna.
mes = df.pop('Mes')
print(df)
