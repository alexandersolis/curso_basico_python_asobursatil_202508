# pip install schedule
import schedule
import time

def tarea():
    print("Ejecutando tarea programada...")

# Programar la tarea para que se ejecute cada hora
schedule.every().hour.do(tarea)

# Programar la tarea para que se ejecute diariamente a una hora específica
schedule.every().day.at("22:30").do(tarea)

# Programar la tarea para que se ejecute todos los lunes a las 8:00 AM
schedule.every().monday.at("08:00").do(tarea)

while True:
    schedule.run_pending()
    time.sleep(1)