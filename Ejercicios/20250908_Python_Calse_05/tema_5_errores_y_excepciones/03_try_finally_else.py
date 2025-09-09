while True:
    try:
        numero1 = int(input("Ingrese un numero:"))
        if numero1 == 9999:
            break

        numero2 = int(input("Ingrese otro numero:"))

        resultado = numero1 / numero2

        print("El resultdo de la division es:", resultado)
    except ValueError:
        print("Error: Debe ingresar un numero válido")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    except Exception as e:
        print("Error:", str(e))
    else:
        print("La division se realizó correctamente")
    finally:
        print("Fin del programa")
