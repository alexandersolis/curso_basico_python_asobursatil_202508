import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('Ventas.csv')

while True:
    producto = input("Ingrese un producto (0 pasa salir):")
    if producto == '0':
        break

    df_producto = df['Producto'] == producto

    # Hasta aqui, tenemos un nuevo Dataframe filtrado por el producto.
    df_filtro_producto = df[df_producto]

    # Obtener ventas totales por región y mes
    ventas_totales = df_filtro_producto.groupby(['Region'])['Ventas'].sum().reset_index(name='Ventas Totales')
    print(ventas_totales.sort_values('Ventas Totales'))
    #print(ventas_totales)

    # Mostrar los datos ordenados por ventas totales en orden descendente
    #print(ventas_totales.sort_values('Ventas Totales', ascending=False))
