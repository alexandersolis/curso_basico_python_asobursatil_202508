class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.especie = None

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def dormir(self):
        print(f"{self.nombre} está durmiendo.")

class Perro(Animal):
    def __init__(self, nombre):
        # Aqui estoy llamando __init__ de la clase base Animal
        super().__init__(nombre)
        # Aqui estoy estableciendo la especie del perro
        self.especie = "Perro"

    def ladrar(self):
        print("¡Guau, guau!")

class Gato(Animal):
    def maullar(self):
        print("¡Miau, miau!")

    def dormir(self):
        #super().dormir()
        print(f"El gato {self.nombre} está durmiendo plácidamente.")

# Crear objetos de las clases derivadas
mi_perro = Perro("Firulais")
mi_gato = Gato("Michi")

# Acceder a los métodos de la clase base y las clases derivadas
mi_perro.comer()  # Salida: Firulais está comiendo.
mi_perro.dormir()  # Salida: Firulais está durmiendo.
mi_gato.dormir()  # Salida: El gato Michi está durmiendo plácidamente.
mi_perro.ladrar()  # Salida: ¡Guau, guau!
mi_gato.maullar()  # Salida: ¡Miau, miau!
print(mi_perro.especie)  # Salida: Perro
print(mi_gato.especie)   # Salida: None
