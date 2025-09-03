def saludar_numero(n):
    print(f"Hola, {n}")

for i in range(3, 14, 2):
    if i == 0:
        continue
    elif i < 10:
        print("Menor que diez")
        if i == 5:
            print("Cinco encontrado")
        elif i == 7:
            print("Siete encontrado")
        else:
            print("Menor que diez")
    elif i == 12:
        print("Doce encontrado")
    else:
        saludar_numero(i)

    print("Vamos aqui")
