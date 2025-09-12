
import pandas as pd

df = pd.read_excel('Ventas.xlsx')

convertido = df.to_csv('convertido_a_csv.csv', sep=';', header=True, index=10)