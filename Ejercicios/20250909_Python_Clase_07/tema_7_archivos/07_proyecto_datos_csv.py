import csv

with open('tema_7_archivos/ventas_libros.csv', 'r') as archivo:
    ventas_por_mes = {} #Declaramos un diccionario vacio
    reader_csv = csv.reader(archivo)
    next(reader_csv)  # Saltar los encabezados

    for linea in reader_csv:
        mes, libro, cantidad = linea

        # Validar que cantidad sea un entero
        #if isinstance(cantidad, int):

        if mes not in ventas_por_mes:
            ventas_por_mes[mes] = {}
        if libro not in ventas_por_mes[mes]:
            ventas_por_mes[mes][libro] = int(cantidad)
        else:
            #ventas_por_mes[mes][libro] = ventas_por_mes[mes][libro] + int(cantidad)
            ventas_por_mes[mes][libro] += int(cantidad)

#print(ventas_por_mes)

# Encontrar el libro más vendido por mes
for mes, libros in ventas_por_mes.items():
    # print(f"Mes: {mes}, Libros vendidos: {libros}")
    # Mes: enero, Libros vendidos: {'Libro1': 10, 'Libro2': 11}
    # Mes: febrero, Libros vendidos: {'Libro3': 15, 'Libro1': 12}

    libro_mas_vendido = max(libros, key=libros.get)
    print(f"El libro más vendido en {mes} fue: {libro_mas_vendido}")
