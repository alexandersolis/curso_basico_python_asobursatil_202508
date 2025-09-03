#CREAR LAS TABLAS DE MULTIPLICAR HASTA EL 10
for w in range(1, 11):
    for j in range(1, 11):
        print(str(w)+"X"+str(j)+"="+str(w*j), end="\t")
    print("")
