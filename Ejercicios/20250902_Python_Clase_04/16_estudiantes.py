##estudiantes = [["Juan", 4.5], ["María", 5.0], ["Pedro", 4.0], ["Ana", 3.5], ["Luis", 4.8]]
estudiantes = ["Juan", "María", "Pedro", "Ana", "Luis"]
notas = [4.5, 5.0, 4.0, 7.5, 4.8]

maxima_nota = max(notas)
maxima_nota_indice = notas.index(maxima_nota)

# nota = 0
# nota_indice = 0
# for i in range(len(estudiantes)):
#     print(f"Estudiante: {estudiantes[i]}, Nota: {notas[i]}")
#     if notas[i] > nota:
#         nota = notas[i]
#         nota_indice = i

print(f"La mejor nota es: {maxima_nota}")
print(f"El estudiante con la mejor nota es: {estudiantes[maxima_nota_indice]}")
