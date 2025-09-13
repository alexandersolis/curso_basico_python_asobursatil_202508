# pip install schedule
# pip install requests
import requests
import schedule
import time
import os
 
def cambair_extension(ruta_archivo, nnueva_extension):
    base_name, _ = os.path.splitext(ruta_archivo)
    new_file_path = base_name + "." + nnueva_extension
    return new_file_path


def obtener_trm():
    """Obtiene la TRM desde el diario La Republica y la imprime."""

    try:
        #url = "https://www.superfinanciera.gov.co/publicaciones/60819/informes-y-cifrascifrasestablecimientos-de-creditoinformacion-periodicadiariatasa-de-cambio-representativa-del-mercado-trm-60819/"
        #url = 'https://www.banrep.gov.co/es/estadisticas/trm'
        #url = 'https://www.datos.gov.co/Econom-a-y-Finanzas/Tasa-de-Cambio-Representativa-del-Mercado-TRM/32sa-8pi3/data'
        #url = 'https://www.superfinanciera.gov.co/'
        url = 'https://www.larepublica.co/indicadores-economicos/mercado-cambiario/dolar'
        headers = {'User-Agent': 'Mozilla/5.0'}

        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levantar una excepción si la solicitud falla
        print(response)
        #print(response.text)

        # Crear archivo HTML
        texto_html = response.text
        # archivo_html = cambair_extension(os.path.abspath(__file__), 'HTML')
        # print(archivo_html)

        # with open(archivo_html, 'w') as f:
        #     f.write(texto_html)

        #<span class="price">$ 3.903,18</span>
        texto_clave = '<span class="price">'
        posicion_trm = texto_html.find(texto_clave)+len(texto_clave)
        trm = texto_html[posicion_trm:posicion_trm+10]
        print(f"La TRM al día de hoy es: {trm}")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener la TRM: {e}")
        return None


# Ejecutar la función a las 5:00 PM todos los días
# schedule.every().day.at("17:00").do(obtener_trm)

# while True:
#   schedule.run_pending()
#   time.sleep(1)

obtener_trm()
