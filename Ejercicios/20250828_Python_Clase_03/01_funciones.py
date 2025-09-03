def saludar():
    print("Hola bienvenido")


def saludo_de_buenos_dias(saludo, nombre):
    print("Buen", saludo, nombre)


#saludar()
nombre = "Eliana"
#saludo_de_buenos_dias(nombre, "dia") #PAERAMETROS POR POSICION (ERROR DE POSICION)
#saludo_de_buenos_dias(nombre=nombre, saludo="dia") #PARAMETROS POR NOMBRE


def sumar(a, b, c):
    """_summary_

    Args:
        a (_type_): _description_
        b (_type_): _description_
        c (_type_): _description_

    Returns:
        _type_: _description_
    """
    return a+b+c
    #ESTO NO SE EJECUTA
    print("No se ejecuta:", a+b+c)


print(sumar(5, 8, 3))

def restar(a, b, c=0):
    return a-b-c

#PARA SALIR DE LA DOCUMENTACION DE UNA FUNCION, UTULIZAMOS :q
#help(restar)

print("Resta A:", restar(8, 6, 4))
print("Resta B:", restar(b=8, a=3))