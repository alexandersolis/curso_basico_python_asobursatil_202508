#Recuerda instalar openpyxl: pip install openpyxl
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font
from openpyxl.styles import colors, borders, fills

from random import randint

# Crear un nuevo archivo de Excel
wb = Workbook()

# Obtener la hoja activa del archivo
hoja = wb.active

_productos = ['Arroz', 'Azucar', 'Aceite vegetal', 'Harina de trigo', 'Leche', 'Pollo',
              'Carne de res', 'Huevos', 'Pasta', 'Pan', 'Papas', 'Platanos', 'Tomates', 'Cebollas',
              'Zanahorias', 'Cafe', 'Frijoles', 'Atun enlatado', 'Harina de maiz', 'Sal']

_regiones = ['Andina', 'Caribe', 'Pacifico', 'Amazonia', 'Insular', 'Orinoquia']

_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

border = Border(
    left=Side(border_style=borders.BORDER_THIN),
    right=Side(border_style=borders.BORDER_THIN),
    top=Side(border_style=borders.BORDER_THIN),
    bottom=Side(border_style=borders.BORDER_THIN)
)

# Definir los encabezados de las columnas
hoja['A1'] = 'Producto'
hoja['B1'] = 'Region'
hoja['C1'] = 'Mes'
hoja['D1'] = 'Ventas'

hoja['A1'].border = border
hoja['B1'].border = border
hoja['C1'].border = border
hoja['D1'].border = border

hoja['A1'].font = Font(bold=True)
hoja['B1'].font = Font(bold=True)
hoja['C1'].font = Font(bold=True)
hoja['D1'].font = Font(bold=True)

hoja['A1'].alignment = Alignment(horizontal='center')  
hoja['B1'].alignment = Alignment(horizontal='center')  
hoja['C1'].alignment = Alignment(horizontal='center')  
hoja['D1'].alignment = Alignment(horizontal='center')  

ancho_col_a = 0
ancho_col_b = 0
ancho_col_c = 0
ancho_col_d = 10.0

# Generar los datos para llenar el excel de ventas
fila = 1
for mes in _meses:
    for reggion in _regiones:
        for producto in _productos:
            try:
                if len(producto) > ancho_col_a:
                    ancho_col_a = len(producto)

                if len(reggion) > ancho_col_b:
                    ancho_col_b = len(reggion)

                if len(mes) > ancho_col_c:
                    ancho_col_c = len(mes)
            except:
                pass

            fila += 1
            hoja[f'A{fila}'] = producto
            hoja[f'B{fila}'] = reggion
            hoja[f'C{fila}'] = mes
            hoja[f'D{fila}'] = randint(10, 100) * 100000

            hoja[f'A{fila}'].border = border
            hoja[f'B{fila}'].border = border
            hoja[f'C{fila}'].border = border
            hoja[f'D{fila}'].border = border

hoja.column_dimensions['A'].width = (ancho_col_a + 2) * 1.2
hoja.column_dimensions['B'].width = (ancho_col_b + 2) * 1.2
hoja.column_dimensions['C'].width = (ancho_col_c + 2) * 1.2
hoja.column_dimensions['D'].width = (ancho_col_d + 2) * 1.2

# Guardar el archivo de Excel
wb.save('Ventas.xlsx')

print('El archivo de Excel se ha creado correctamente.')
