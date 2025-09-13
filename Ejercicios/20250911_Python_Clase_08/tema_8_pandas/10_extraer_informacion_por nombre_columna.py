import pandas as pd

df = pd.read_excel('ventas.xlsx')

# Recordar que en un excel con Encabezados, la primera fila de datos es la posición 0.
# Por lo tanto, la fila 24 es la fila 26 en el excel.

# Lee el dato de la fila 10, columna Region
print(df.loc[10, "Region"])

# Lee el dato de la fila 24, columna Ventas
print(df.loc[24, "Ventas"])

# Lee el dato de la fila 24, columnas Region y Ventas
print(df.loc[24, ["Region", "Ventas"]])
