#funcion len()
mi_dato = "Buenos dias a todos"
#print(len(mi_dato))


#imprimir, primer, tres primeros, y 2 últimos caracteres
texto_a = "Python es un excelente leguaje de programacion" #tiene una longitud de 46 caracteres
primer_caracter = texto_a[0]
print(primer_caracter)

#Extraer trozos de una cadena
#cadena[start:end:step]
#end: Siempre es end-1
tres_primeros_chars = texto_a[0:3]
print(tres_primeros_chars)
longitud = len(texto_a)
#print(longitud)
#son 46 caracteres
ultimos_2_chars = texto_a[44:46]
print(ultimos_2_chars)
print(texto_a[44:])
print(texto_a[longitud-2:])
print(texto_a[len(texto_a)-2:])
print(texto_a[-2:-1])

#Invertir/Reversar una cadena
texto_a_invertido = texto_a[::-1]
print(texto_a_invertido)
#uso de step
print("Saltos de 2:", texto_a[::2])
print("Saltos de 5:", texto_a[::5])
