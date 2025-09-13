import csv
import pathlib

#Abrir el archivo con asignacion de variable
# archivo = open('ventas_libros.csv', 'r')
# lector_csv = csv.reader(archivo)
# encabezados = next(lector_csv)
# for fila in lector_csv:
#     print(fila)
# archivo.close()

#Abrir el archivo con with
with open('tema_7_archivos/ventas_libros.csv', 'r') as archivo:
    lector_csv = csv.reader(archivo)

    #Esta linea de codigo (next) hace que saltemos la primera fila (los encabezados)
    encabezados = next(lector_csv)
    for fila in lector_csv:
        print(fila)

print("fin del programa")
