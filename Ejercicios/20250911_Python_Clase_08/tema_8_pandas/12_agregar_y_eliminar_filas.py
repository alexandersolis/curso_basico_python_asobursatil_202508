import pandas as pd

datos = [["Carlos", "Abogado", 40],
         ["Pedro", "Contador", 35],
         ["Maria", "Ingeniera", 30],
         ["Rosa", "Arquitecta", 25]]

df = pd.DataFrame(datos, columns=["Nombre", "Profesion", "Edad"])
# print(df)

# # Agregar más filas al DataFrame
# nuevas_filas = [["Luis", "Doctor", 45],
#                 ["Ana", "Enfermera", 28]]

# nuevo_df = pd.DataFrame(nuevas_filas, columns=df.columns)
# #print(nuevo_df)
# df = pd.concat([df, nuevo_df], ignore_index=True)

# Imprimir el DataFrame actualizado
print(df)

# Eliminar filas
df = df.drop([1])
print(df)

# Eliminar múltiples filas, pero indice 4 no existe (Genera error)
df = df.drop([2,4])
print(df)
