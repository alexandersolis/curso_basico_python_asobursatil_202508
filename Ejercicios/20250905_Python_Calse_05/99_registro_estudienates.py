# Proyecto: Registro de estudiantes

# Crear un diccionario vacío para almacenar los registros de estudiantes
registros = {}

# Función para agregar un registro de estudiante
def agregar_registro(codigo, nombre, edad, curso):
    if codigo not in registros:
        registros[codigo] = {'nombre': nombre, 'edad': edad, 'curso': curso}
        print("Registro agregado con éxito.")
    else:
        print("El código de estudiante ya existe en los registros.")

# Función para mostrar los detalles de un registro de estudiante
def mostrar_registro(codigo):
    if codigo in registros:
        registro = registros[codigo]
        print("Detalles del estudiante:")
        print("Código:", codigo)
        print("Nombre:", registro['nombre'])
        print("Edad:", registro['edad'])
        print("Curso:", registro['curso'])
    else:
        print("El código de estudiante no existe en los registros.")

# Función para mostrar todos los registros de estudiantes
def mostrar_registros():
    if len(registros) == 0:
        print("No hay registros de estudiantes.")
    else:
        print("Lista de registros de estudiantes:")
        for codigo, registro in registros.items():
            print("Código:", codigo)
            print("Nombre:", registro['nombre'])
            print("Edad:", registro['edad'])
            print("Curso:", registro['curso'])
            print("--------------------")

# Función para cambiar el curso de un estudiante
def cambiar_curso(codigo, nuevo_curso):
    if codigo in registros:
        registros[codigo]['curso'] = nuevo_curso
        print("Curso cambiado con éxito.")
    else:
        print("El código de estudiante no existe en los registros.")

# Función para eliminar un registro de estudiante
def eliminar_registro(codigo):
    if codigo in registros:
        del registros[codigo]
        print("Registro de estudiante eliminado.")
    else:
        print("El código de estudiante no existe en los registros.")

# Función principal del programa
def main():
    print("Bienvenido al Registro de Estudiantes!")

    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar registro de estudiante")
        print("2. Mostrar registro de estudiante")
        print("3. Mostrar registros de estudiantes")
        print("4. Eliminar registro de estudiante")
        print("5. Cambiar de curso a un estudiante")
        print("6. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            codigo = input("Ingrese el código de estudiante: ")
            nombre = input("Ingrese el nombre del estudiante: ")
            edad = input("Ingrese la edad del estudiante: ")
            curso = input("Ingrese el curso del estudiante: ")
            agregar_registro(codigo, nombre, edad, curso)
        elif opcion == "2":
            codigo = input("Ingrese el código de estudiante: ")
            mostrar_registro(codigo)
        elif opcion == "3":
            mostrar_registros()
        elif opcion == "4":
            codigo = input("Ingrese el código de estudiante a eliminar: ")
            eliminar_registro(codigo)
        elif opcion == "5":
            codigo = input("Ingrese el código de estudiante: ")
            nuevo_curso = input("Ingrese el nuevo curso del estudiante: ")
            cambiar_curso(codigo, nuevo_curso)
        elif opcion == "6":
            print("Gracias por usar el Registro de Estudiantes. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Ejecutar el programa principal
main()