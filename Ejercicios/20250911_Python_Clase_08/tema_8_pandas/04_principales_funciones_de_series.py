# Recuerda instalar pandas: pip install pandas
import pandas as pd

serie = pd.Series([2, 4, 5, 6, 7, 8, 9, 10])

print("Cantiad de elementos en la serie:", serie.size)
print("Valor minimo de la serie:", serie.min())
print("Valor maximo de la serie:", serie.max())
print("Promedio de la serie:", serie.mean())
print("Suma de los elementos de la serie:", serie.sum())
print("Desviacion estandar de la serie:", serie.std())
# Imprmie 100 veces el caracter =
print("="*100)
print("Elementos Pultiplicados por 5:", serie * 5)
# Imprmie 100 veces el caracter =
print("="*100)
print("Elementos > 6:", serie[serie > 6])
# Imprmie 100 veces el caracter =
print("="*100)
print(serie.describe())
