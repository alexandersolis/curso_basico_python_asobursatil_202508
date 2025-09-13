palabra_buscada = input("Ingresa la palabra que deseas buscar: ")

contador = 0

with open("01_operaciones_archivos.txt", "r") as archivo:
    for linea in archivo:
        linea_strip = linea.strip()
        print(linea_strip)
        palabras = linea.strip().split()
        contador += palabras.count(palabra_buscada)

print(f"La palabra '{palabra_buscada}' aparece {contador} veces en el archivo.")
