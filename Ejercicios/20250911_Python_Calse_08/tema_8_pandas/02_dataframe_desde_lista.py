# Recuerda instalar pandas: pip install pandas
import pandas as pd

datos = [["Carlos", "Abogado", 40],
         ["Pedro", "Contador", 35],
         ["Maria", "Ingeniera", 30],
         ["Rosa", "Arquitecta", 25]]

personas = pd.DataFrame(datos, columns=["Nombre", "Profesion", "Edad"])

print(personas)
