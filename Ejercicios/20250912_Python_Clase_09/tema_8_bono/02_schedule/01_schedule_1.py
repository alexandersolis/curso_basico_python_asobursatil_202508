# pip install schedule
import schedule
#Time viene incorporado en Python
import time

def tarea():
    print(f"{time.ctime()}: Ejecutando tarea programada...")

# Programar la tarea para que se ejecute cada minuto
schedule.every(2).seconds.do(tarea)

while True:
    schedule.run_pending()
    time.sleep(1)

# Para detener el Script utilizamos CTRL+C