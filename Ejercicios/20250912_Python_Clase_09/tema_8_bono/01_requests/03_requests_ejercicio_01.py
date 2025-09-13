#  crear un script que obtenga datos de una API pública, procese los datos y los muestre en un formato legible
import requests
import pandas as pd

# URL de la API pública de Coindesk
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'

try:
    # Realizar una solicitud o peticion GET
    response = requests.get(url)
    response.raise_for_status()

    # Obtener los datos en formato JSON
    datos = response.json()
    #print(datos)

    # Procesar los datos
    precios = datos['bpi']
    lista_precios = []

    print(f"Precio actual del Bitcoin en USD, GBP y EUR")
    for moneda, info in precios.items():
        lista_precios.append({
            'Moneda': moneda,
            'Tasa': info['rate'],
            'Descripción': info['description']
        })

    # Crear un DataFrame con los datos
    df = pd.DataFrame(lista_precios)

    # Mostrar el DataFrame
    print(df)

except requests.exceptions.RequestException as err:
    print(f"Error en la solicitud: {err}")
