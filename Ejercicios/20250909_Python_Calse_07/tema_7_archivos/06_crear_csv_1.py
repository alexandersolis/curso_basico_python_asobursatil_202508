import csv

datos = [
    ['Nombre', 'Edad', 'Ciudad'],
    ['Ana', 28, 'Madrid'],
    ['Luis', 34, 'Barcelona'],
    ['Marta', 22, 'Valencia']
]

with open('tema_7_archivos/06_crear_csv_1.csv', 'w', newline='') as archivo:
    escritor_csv = csv.writer(archivo, delimiter=',')
    
    #Escribir todos los datos que estan en la lista "datos" 
    escritor_csv.writerows(datos)

    #Escribir una a una las filas
    escritor_csv.writerow(['Marta', 22, 'Valencia'])
    escritor_csv.writerow(['Carlos', 30, 'Sevilla'])
    escritor_csv.writerow(['Lucia', 25, 'Granada'])

    escritor_csv.writerow(['Lucia', 25, 'Granada', "Extra"])  # Esto agregará una columna extra
