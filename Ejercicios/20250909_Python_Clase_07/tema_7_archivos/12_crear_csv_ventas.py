import csv
from random import randint

_productos = ['Arroz', 'Azucar', 'Aceite vegetal', 'Harina de trigo', 'Leche', 'Pollo',
              'Carne de res', 'Huevos', 'Pasta', 'Pan', 'Papas', 'Platanos', 'Tomates', 'Cebollas',
              'Zanahorias', 'Cafe', 'Frijoles', 'Atun enlatado', 'Harina de maiz', 'Sal']

_regiones = ['Andina', 'Caribe', 'Pacifico', 'Amazonia', 'Insular', 'Orinoquia']

_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

try:
    archivo_csv = open('Ventas.csv', 'x')
except FileExistsError:
    archivo_csv = open('Ventas.csv', 'w')

campos = ['Producto', 'Region', 'Mes', 'Ventas']
writer = csv.DictWriter(archivo_csv, fieldnames=campos)
writer.writeheader()

# Generar los datos para llenar el csv de ventas
for mes in _meses:
    for reggion in _regiones:
        for producto in _productos:
            writer.writerow({'Producto': producto, 'Region': reggion, 'Mes': mes, 'Ventas': randint(10, 100) * 100000})

# Guardar el archivo CSV
archivo_csv.close()

print('El archivo CSV se ha creado correctamente.')
