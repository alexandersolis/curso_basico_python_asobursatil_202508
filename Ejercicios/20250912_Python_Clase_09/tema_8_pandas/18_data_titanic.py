import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic-Dataset.csv')

#cual es la dimension (filas, columnas) de mi dataframe?
print(data.shape)

# Tengo datos completos para todos los registros?
# el metodo count cuanto cada registro(fila) que tenga datos
# podemos ver que por ejemplo para la columna Cabin tengo algunos registros sin datos
print(f'Datos completos por columna:\n{data.count()}')

# Pero tener datos, no significa tener datos "limpios"
# Podemos ver en la previsualizacion que para la columna Cabin tengo algunos NaN, el cual en python 
# es interpretado como un valor nulo o Null, lo cual me podria traer problemas cuando analice la data
# contemos cuantos datos nulos tenemos

# 1. Obtener los nombres de las columnas como una lista
#col_nombres = ["PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"]
col_names = data.columns.tolist()
# 2. Iterar sobre la lista
for column in col_names:
    print("Valores nulos en <{0}>: {1}".format(column, data[column].isnull().sum()))

# Imagina que para fines de simplicidad quieres reemplazar el female, male por F, M

# 1. Creamos un diccionario con los valores originales y los valores de reemplazo
d = {'male' : 'M', 'female' : 'F'}

# Esta funcion de reemplazo, es el equivalente la lambda x: d[x]
# def replace_sex(x):
#     return d[x]
# 2. Utilizamos un lambda para el reemplazo, en una sola linea n.n
data['Sex'] = data['Sex'].apply(lambda x: d[x])

#checa el cambio
print(f"Listar los primeros 5 valores de la columna 'Sex':")
print(data['Sex'].head())

# Agrupemos por Sobrevivencia y Sexo
print(f"Tabla de contingencia entre Sobrevivencia y Sexo:\n{pd.crosstab(data.Survived, data.Sex)}")

#Como fue la sobreviviencia por clase, sexo
pclass_gender_survival_count_df = data.groupby(['Pclass', 'Sex'] )['Survived'].sum()
print(f"Sobrevivencia por Clase y Sexo:\n{pclass_gender_survival_count_df}")

# VISUALIZACION DE DATOS
colors = ['#FF0000', '#0000FF', '#BBBB00', '#00FF00']

# Cuantos sobrevivieron  
fig = plt.figure(figsize=(30,10)) #creamos un canvas o figura de 30x10 pixeles

# queremos ver un plot al costado del otro, para esto pensemos en una grilla (celdas)
plt.subplot2grid((2,3),(0,0))
data.Survived.value_counts().plot(kind='bar', alpha=1.0, color=colors)
plt.title('Sobrevivieron - cuenta total -')
#plt.show()
plt.savefig("data/Sobrevivieron - cuenta total.jpg")

# Hay manera un poco mas amigable de interpretar datos....con porcentajes!
plt.subplot2grid((2,3),(0,1))
data.Survived.value_counts(normalize = True).plot(kind='bar', alpha=0.5, color=colors)
plt.title('Sobrevivieron - porcentaje total -')
#plt.show()
plt.savefig("data/Sobrevivieron - porcentaje total.jpg")

#Sobrevivieron mas hombres o mas mujeres?
fig = plt.figure(figsize=(30,10))
data.Sex[data.Survived == 1].value_counts(normalize = True).plot(kind='barh', alpha=0.5, color=colors)
plt.title('Sobrevivieron - Male vs Female -')
#plt.show()
plt.savefig("data/Sobrevivieron - Male vs Female.jpg")

# Que relacion hay entre sobrevivencia y edad de los sobrevivientes
fig = plt.figure(figsize=(6,8))
plt.scatter(data.Survived, data.Age, alpha=0.5, color='#808000')
#plt.show()
plt.savefig("data/Relacion sobrevivencia y edad.jpg")

# La clase del ticket fue un factor de sobrevivencia (si viste Titanic, ya lo sabes!)
fig = plt.figure(figsize=(10,5))

#colors bgrcmykw
data.Pclass[data.Survived == 1 ].value_counts(normalize = True).plot(kind='bar', alpha=0.5, color=colors)
plt.title('Sobrevivientes por Clase de Ticket')
#plt.show()
plt.savefig("data/Sobrevivientes por Clase de Ticket.jpg")

# Habra alguna relacion entre tipo de ticket y edad? (Poder Adquisitivo)
fig = plt.figure(figsize=(20,10))

for t_class in [1,2,3]:
    data.Age[data.Pclass == t_class].plot(kind='line')
    
plt.legend(("1ra. Clase", "2da. Clase", "3ra.Clase"))  
#plt.show()
plt.savefig("data/Relacion entre tipo de ticket y edad.jpg")

# La linea de la 1ra clase, nos muestra que el promedio de edad del comprador es de 40 annios
# La linea de la 3ra clase, tiene un promedio mucho mas joven

# Podriamos hacer una inferencia temprana y decir que los hombres que salvaron fueron 
# en su mayoria ricos y > 30 annios
print(data[data.Age < 1])
