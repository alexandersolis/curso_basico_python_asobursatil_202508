# Respaldo Automático de Archivos
# crear un script que respalde un directorio especificado diariamente a las 11:00 PM 
# y almacene la copia de seguridad con una marca de tiempo en el nombre del archivo comprimido.

# pip install schedule
import os
import shutil
import datetime
import schedule
import time

# Paso 1: Definir la Función de Respaldo
def respaldo_directorio():
    origen = '20240729'
    destino = 'respaldos'
    
    if not os.path.exists(destino):
        os.makedirs(destino)
    
    # Crear nombre de archivo con marca de tiempo
    tiempo_actual = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_respaldo = f'respaldo_{tiempo_actual}.tar.gz'
    ruta_respaldo = os.path.join(destino, nombre_respaldo)
    
    # Comprimir el directorio de respaldo
    shutil.make_archive(ruta_respaldo.replace('.tar.gz', ''), 'gztar', origen)
    print(f'Respaldo completado: {ruta_respaldo}')


# Paso 2: Programar la tarea para que se ejecute diariamente a las 11:00 PM
schedule.every().day.at("23:00").do(respaldo_directorio)

while True:
    schedule.run_pending()
    time.sleep(1)

#respaldo_directorio()