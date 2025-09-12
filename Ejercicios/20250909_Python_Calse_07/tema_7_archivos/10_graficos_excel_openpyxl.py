#Recuerda instalar openpyxl: pip install openpyxl
from openpyxl import Workbook  
from openpyxl.chart import BarChart, Reference  
  
wb = Workbook()  
hoja = wb.active  
  
# Datos de ejemplo  
filas = [  
    ["Serial_no", "Roll no", "Marks"],  
    [1, "0090011", 75],  
    [2, "0090012", 60],  
    [3, "0090013", 43],  
    [4, "0090014", 97],  
    [5, "0090015", 63],  
    [6, "0090016", 54],  
    [7, "0090017", 86],  
]  
  
for i in filas:  
    hoja.append(i)  

# Grafico de Barras BarChart()
# Grafico de lineas: LineChart() 
# Dcumentacion oficial openpyxl: Graficos
# https://openpyxl.readthedocs.io/en/stable/charts/introduction.html
grafico = BarChart()
 
valores = Reference(worksheet=hoja,  
                 min_row=1,  
                 max_row=8,  
                 min_col=2,  
                 max_col=3)  
  

grafico.add_data(valores, titles_from_data=True)  

#Celda en la que vamos a ubicar el grafico
hoja.add_chart(grafico, "E2")  
  
wb.save("10_grafico_estudiantes.xlsx")  
