import pandas as pd

df = pd.read_excel('ventas.xlsx')

# Lee el dato de la fila 5, columna 3
# print(df.iloc[5, 3])

# Lee de la fila 6, columnas 0, 1, y 2
# print(df.iloc[6, :3])

# # Lee de la fila 5, desde la columna 2 
# print(df.iloc[5, 2:])

# Lee hasta la fila 5, desde la columna 2 
print(df.iloc[:5, 2:])

# generar un nuevo excel, con sol odos columnas extraidas del set de datos.
# df_2 = df.iloc[:-1, 0:-1:3]
# df_2.to_excel("ventas_prb.xlsx")
