#ESCRIBA UN PROGRAMA QUE PIDA UNA CONTRASEÑA, 
#Y VALIDE SI ESTA CUMPRE CON LOS SIGUIENTES REQUISITOS
#1. Debe tener mínimo 8 caracteres de largo.
#2. Debe tener maximo 32 caracteres de largo.
#3. Debe tener al menos un digito numerico.
#4. Debe tener al menos una letra mayuscula.
#5. Debe tener al menos una letra minuscula.
#6. Debe tener al menos uno de los siguientes caracteres especiales: ~¡@#$%^*()_-+={ }[ ]|:;",.¿

contrasena = input("Ingrese una contraseña:")

largo_minimo = len(contrasena) >= 8
"""
largo_minimo Tambien se puede expresar con un if, asi:
if len(contrasena) >= 8:
    largo_minimo = True
else:
    largo_minimo = False

Pero le estamos asignando el resultado de evaluar si el largo de la variable 
contrasena es mayor o igual que 8
"""

largo_maximo = len(contrasena) <= 32
"""
largo_maximo Tambien se puede expresar con un if, asi:
if len(contrasena) <= 32:
    largo_maximo = True
else:
    largo_maximo = False

Pero le estamos asignando el resultado de evaluar si el largo de la variable 
contrasena es menos o igual que 32
"""

caracteres_especiales = '~¡@#$%^*()_-+={ }[ ]|:;",.¿'

#CREAMOS UNA VARIABLE PARA CADA UNA DE LAS VALIDACIONES
#INICIALMENTE ASUMINOS COMO FALSE CADA UNA DE LAS VALIDACIONES.
tiene_numero = False
tiene_mayuscula = False
tiene_minuscula = False
tiene_caracter_especial = False

#LUEGO RECORREMOS LA CONTRASEÑA DIGITO POR DIGITO
#Y VALIDAMOS CADA CONDICION
for caracter in contrasena:
    #ESTE TIPO DE ASIGNACION SIGNIFICA QUE:
    # tiene_numero ES IGUAL AL VALOR QUE TIEN ACTUALMENTE LA VARIABLE (tiene_numero)
    # O A LA VALIDACION DE SI EL CARACTER ES UN NUMERO.
    # ESTO PERMITE QUE SI EN ALGUN MOMENTO LA VARIABLE tiene_numero ES VERDADEDA, SIGA SIENDO VERDADERA. 
    tiene_numero = tiene_numero or caracter.isnumeric() #isnumeric() DEVUELVE TRUE SI UNA CADENA ES NUMERICA (TODOS LOS CARACRTERES SON NUMEROS)
    tiene_mayuscula = tiene_mayuscula or caracter.isupper() #isupper() DEVUELVE TRUE SI TODOS LOS CARACRTERES SON LETRAS MAYUSCULAS
    tiene_minuscula = tiene_minuscula or caracter.islower() #islower() DEVUELVE TRUE SI TODOS LOS CARACRTERES SON LETRAS  INUSCULAS
    tiene_caracter_especial = tiene_caracter_especial or (caracter in caracteres_especiales) #DEVUELVE TRUE SI caracter ESTÁ EN LA VARIABLE caracteres_especiales

contrasena_valida = True

if not largo_minimo:
    contrasena_valida = False
    print("La contraseña debe tener mínimo 8 caracteres de largo.")

if not largo_maximo:
    contrasena_valida = False
    print("La contraseña debe tener maximo 32 caracteres de largo.")

if not tiene_numero:
    contrasena_valida = False
    print("La contraseña debe tener al menos un digito numerico.")

if not tiene_mayuscula:
    contrasena_valida = False
    print("La contraseña debe tener al menos una letra mayuscula.")

if not tiene_minuscula:
    contrasena_valida = False
    print("La contraseña debe tener al menos una letra minuscula.")

if not tiene_caracter_especial:
    contrasena_valida = False
    print('La contraseña debe tener al menos o de los siguientes caracteres especiales: ~¡@#$%^*()_-+={ }[ ]|:;",.¿')


if contrasena_valida:
    print("La contraseña ingresada cumple con la validación")
else:
    print("La contraseña ingresada no es válida")
