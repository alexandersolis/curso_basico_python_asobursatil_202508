import requests
import schedule
import datetime
import time
import os


def guardar_pagina(url, nombre_archivo):
    """Descarga el contenido HTML de una URL y lo guarda en un archivo.

    Args:
        url (str): La URL de la página web.
        nombre_archivo (str): El nombre del archivo donde se guardará el contenido.
    """

    #capturamos la hora de inincio del proceso
    inicio = time.time()
    print(f"{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}: Iniciando proceso")

    # Crear nombre de archivo con marca de tiempo
    # tiempo_actual = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # nombre_final = f'{tiempo_actual}_{nombre_archivo}'

    # Obtener la fecha y hora actual
    ahora = datetime.datetime.now()

    # Formatear la fecha y hora
    year = ahora.year
    month = ahora.month
    day = ahora.day
    hour = ahora.hour
    minute = ahora.minute
    second = ahora.second

    formatted_date = f"{year:04d}/{month:02d}/{day:02d}"
    formatted_datetime = f"{year:04d}{month:02d}{day:02d}_{hour:02d}{minute:02d}{second:02d}"

    # Construir la ruta completa
    nombre_final = os.path.join(formatted_date, f"{formatted_datetime}_{nombre_archivo}")

    # Crear el directorio si no existe
    os.makedirs(os.path.dirname(nombre_final), exist_ok=True)

    try:
        print(f"{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}: Iniciando peticion")
        response = requests.get(url)
        response.raise_for_status()  # Levanta una excepción si la solicitud falla

        print(f"{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}: Peticion completada")
        with open(nombre_final, 'wb') as f:
            f.write(response.content)
        print(f"{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}: Página guardada en {nombre_final}")

    except requests.exceptions.RequestException as e:
        print(f"{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}: Error al descargar la página: {e}")

    # Calcular la duracion del proceso
    duracion = time.time() - inicio
    print(f"{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}: El proceso ha finallizado, duración: {duracion}")


# Ejemplo de uso:
url = "https://www.python.org/"
nombre_archivo = "python.html"

# response = requests.get(url)
# print(response.content.decode('utf-8'))

#Ejecutar la funcion de inmediato
guardar_pagina(url, nombre_archivo)

# Programar la tarea para que se ejecute cada hora
# schedule.every().hour.do(guardar_pagina, url, nombre_archivo)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
