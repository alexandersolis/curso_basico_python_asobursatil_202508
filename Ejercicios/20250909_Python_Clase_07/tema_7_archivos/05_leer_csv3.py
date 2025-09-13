import csv

archivos = ["ventas_libros_enero.csv", 
            "ventas_libros_febrero.csv", 
            "ventas_libros_marzo.csv"]

encabezado_guardados = False

#recomendacion, verificar que el archivo ventas_libros_final2.csv no exista.
try:
    archivo_final = open('ventas_libros_final2.csv', 'x')
except FileExistsError:
    archivo_final = open('ventas_libros_final2.csv', 'w')

csv_writer = csv.writer(archivo_final)

for nombre_archivo in archivos:
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)

        encabezados = next(lector_csv)
        if not encabezado_guardados:
            csv_writer.writerow(encabezados)
            encabezado_guardados = True

        for fila in lector_csv:
            csv_writer.writerow(fila)

archivo_final.close()