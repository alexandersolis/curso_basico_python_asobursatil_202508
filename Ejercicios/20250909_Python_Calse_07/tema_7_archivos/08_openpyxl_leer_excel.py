#Recuerda instalar openpyxl: pip install openpyxl
import openpyxl

# Abrir el archivo Excel
libro = openpyxl.load_workbook('Ventas.xlsx')

# Seleccionar una hoja
hoja = libro.active  # o libro['Sheet']

# Leer datos de celdas
valor_celda = hoja['A1'].value
print(valor_celda)

hoja['D2'].value = 10000000 

# Guardar los cambios
libro.save('Ventas.xlsx')

# Iterar sobre filas
for fila in hoja.iter_rows(min_row=2, values_only=True):
    print(fila)

