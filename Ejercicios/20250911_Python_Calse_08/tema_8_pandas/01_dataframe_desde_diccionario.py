# Recuerda instalar pandas: pip install pandas
import pandas as pd

datos = {"Nombre": ["Carlos", "Pedro", "Maria", "Rosa"],
         "Profesion": ["Abogado", "Contador", "Ingeniera", "Arquitecta"],
         "Edad": [40, 35, 30, 25]}

personas = pd.DataFrame(datos)

print(personas)
