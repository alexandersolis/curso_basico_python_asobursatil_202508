# Definición de la función para agregar una tarea
def agregar_tarea(lista_tareas, tarea):
    lista_tareas.append(tarea)
    print("Tarea agregada con éxito.")


# Definición de la función para ver todas las tareas
def ver_tareas(lista_tareas):
    if len(lista_tareas) == 0:
        print("No hay tareas en la lista.")
    else:
        print("Lista de tareas:")
        for i, tarea in enumerate(lista_tareas, start=1):
            print(f"{i}. {tarea}")


# Definición de la función para marcar una tarea como completada
def marcar_completada(lista_tareas, numero_tarea):
    if numero_tarea >= 1 and numero_tarea <= len(lista_tareas):
        lista_tareas[numero_tarea - 1] += " (Completada)"
        print("Tarea marcada como completada.")
    else:
        print("Número de tarea inválido.")


# Definición de la función para eliminar una tarea
def eliminar_tarea(lista_tareas, numero_tarea):
    if numero_tarea >= 1 and numero_tarea <= len(lista_tareas):
        tarea_eliminada = lista_tareas.pop(numero_tarea - 1)
        print(f"Tarea '{tarea_eliminada}' eliminada.")
    else:
        print("Número de tarea inválido.")


# Lista para almacenar las tareas
tareas = []


# Ciclo principal del programa
while True:
    print("---- Administrador de Tareas ----")
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        tarea_nueva = input("Ingrese la nueva tarea: ")
        agregar_tarea(tareas, tarea_nueva)
    elif opcion == "2":
        ver_tareas(tareas)
    elif opcion == "3":
        num_tarea = int(input("Ingrese el número de la tarea a marcar como completada: "))
        marcar_completada(tareas, num_tarea)
    elif opcion == "4":
        num_tarea = int(input("Ingrese el número de la tarea a eliminar: "))
        eliminar_tarea(tareas, num_tarea)
    elif opcion == "5":
        print("Gracias por usar el Administrador de Tareas. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

