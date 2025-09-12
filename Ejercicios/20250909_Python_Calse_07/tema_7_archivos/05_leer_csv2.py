import csv

with open('datos.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo, delimiter=',', quotechar='"')
    encabezados = next(lector_csv)
    for fila in lector_csv:
        print(fila)