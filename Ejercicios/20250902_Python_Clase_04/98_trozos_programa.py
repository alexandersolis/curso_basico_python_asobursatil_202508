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

    if opcion == "5":
        print("Gracias por usar el Administrador de Tareas. ¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
