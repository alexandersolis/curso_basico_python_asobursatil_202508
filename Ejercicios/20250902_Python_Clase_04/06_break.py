texto = "Buenos dias Curso"
for caracter in texto:
    if caracter == "o":
        break

    print(caracter)

indice = 0
caracter = texto[indice] # B
while caracter != " ":
    print(caracter)

    #indice += 1
    indice = indice + 1
    caracter = texto[indice]

    if caracter == "o":
        break
