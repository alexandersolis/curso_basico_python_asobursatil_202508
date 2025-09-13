import pandas as pd

datos = [["Carlos", "Abogado", 40],
         ["Pedro", "Doctor", 35],
         ["Maria", "Ingeniera", 30],
         ["Rosa", "Doctor", 25],
         ["Luis", "Doctor", 45],
         ["Ana", "Enfermera", 28]]

df = pd.DataFrame(datos, columns=["Nombre", "Profesion", "Edad"])

# Filtrar las personas que sean Doctor y tengan mas de 27 años
df_filtrado = df[(df["Profesion"] == 'Doctor') & (df['Edad'] >= 28)]
print(df_filtrado)
