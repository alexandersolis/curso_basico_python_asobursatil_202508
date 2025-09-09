class Animal:
    def __init__(self, nombre):
        self._nombre = nombre
        # self._historial_nombres = []

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nuevo_nombre):
        # self._historial_nombres.append(self._nombre)
        self._nombre = nuevo_nombre

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau, guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau, miau!"

# Crear objetos de las clases derivadas
mi_perro = Perro("Firulais")
mi_gato = Gato("Michi")

# Acceder al nombre del perro
print(mi_perro.get_nombre())  # Salida: Firulais

# Cambiar el nombre del perro
mi_perro.set_nombre("Max")

# Acceder al nombre actualizado del perro
print(mi_perro.get_nombre())  # Salida: Max
