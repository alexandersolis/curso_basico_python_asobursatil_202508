# Leer contenido de un archivo e imprimirlo en pantalla
# archivo = open("archivo_de_prueba.txt")
# contenido = archivo.read()
# print(contenido)
# archivo.close()

# Leer archivo línea por línea
# archivo = open("archivo_de_prueba.txt")
# for linea in archivo:
#     print(linea.strip())  # .strip() elimina espacios en blanco y saltos de línea adicionales
# archivo.close()

# El uso de 'with' maneja automáticamente el cierre del archivo
with open("archivo_de_prueba.txt") as archivo:
    contenido = archivo.read()
    print(contenido)
