from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau, guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau, miau!"

# No se puede crear un objeto de la clase Animal directamente
# animal = Animal("Animal")  # Generaría un error

# Crear objetos de las clases derivadas
perro = Perro("Firulais")
gato = Gato("Michi")

# Llamar al método hacer_sonido de cada objeto
print(perro.hacer_sonido())  # Salida: ¡Guau, guau!
print(gato.hacer_sonido())  # Salida: ¡Miau, miau!
