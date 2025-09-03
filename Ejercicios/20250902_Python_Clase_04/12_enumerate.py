frutas = ["Manzana", "Pera", "Banano", "Mango"]
for indice, fruta in enumerate(frutas, start=1):
    print("La fruta", fruta, "esta en la posicion", indice)

print("")

for indice, fruta in enumerate(frutas[:2]):
    print("La fruta", fruta, "esta en la posicion", indice)