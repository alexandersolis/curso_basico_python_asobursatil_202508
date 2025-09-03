texto = "Bienvenidos al curso de Python"
curso_existe = "curso" in texto

posicion_curso = texto.index("curso")
posicion_curso_2 = texto.find("curso")

print(curso_existe)
print(posicion_curso)
print(posicion_curso_2)

import math

coordenadas = [(1, 2), (3, 4), (5, 6)]
distancias = [math.sqrt((x2 - x1)**2 + (y2 - y1)**2) for (x1, y1), (x2, y2) in zip(coordenadas, coordenadas[1:])]
print(distancias)
