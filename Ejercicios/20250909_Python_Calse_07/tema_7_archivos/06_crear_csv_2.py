import csv
with open('ejemplo_05.csv', 'w') as csvfile:
    campos = ['Nombre', 'Apellido', 'Grado']
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    writer.writerows([{'Grado': 'B', 'Nombre': 'Juan', 'Apellido': 'Aldana'},
                      {'Grado': 'A', 'Nombre': 'Ricardo', 'Apellido': 'Rodriguez'},
                      {'Grado': 'C', 'Nombre': 'Tom', 'Apellido': 'Cruz'},
                      {'Grado': 'B', 'Nombre': 'Jaime', 'Apellido': 'Gonzalez'},
                      {'Grado': 'A', 'Nombre': 'Pedro', 'Apellido': 'Perez'}])

print("Escritura completa")