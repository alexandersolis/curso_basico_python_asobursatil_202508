print("Para finalizar el programa ingrece un numero menor que uno como edad, o una letra")
while True:
    edad = input("Ingrese la edad de la persona: ")
    if not edad.isdigit():
        break

    edad = int(edad)

    if edad < 1:
        break

    if edad >= 18:
        print("La persona puede votar.")
    else:
        print("La persona no puede votar.")
