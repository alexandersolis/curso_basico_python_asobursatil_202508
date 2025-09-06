#Dado un diccionario de nombres y sus calificaciones, 
#crea una función que devuelva el nombre del estudiante con la calificación más alta

def obtener_estudiante_calificacion_mas_alta(diccionario):
    calificacion_mas_alta = 0
    estudiante_mas_alto = "" #el estudiante con la calificacion mas alta

    for estudiante, calificacion in diccionario.items():
        if calificacion > calificacion_mas_alta:
            calificacion_mas_alta = calificacion
            estudiante_mas_alto = estudiante

    return estudiante_mas_alto, calificacion_mas_alta

# Ejemplos de diccionarios de calificaciones
calificaciones1 = {
    "Juan": 95,
    "María": 87,
    "Carlos": 92,
    "Luisa": 98
}

calificaciones2 = {
    "Pedro": 76,
    "Ana": 82,
    "Elena": 91,
    "Miguel": 88
}

# Obtener el estudiante con la calificación más alta
estudiante_mas_alto1 = obtener_estudiante_calificacion_mas_alta(calificaciones1)
estudiante_mas_alto2 = obtener_estudiante_calificacion_mas_alta(calificaciones2)

print(f"El estudiante con la calificación más alta en el primer diccionario es: {estudiante_mas_alto1}")
print(f"El estudiante con la calificación más alta en el segundo diccionario es: {estudiante_mas_alto2}")