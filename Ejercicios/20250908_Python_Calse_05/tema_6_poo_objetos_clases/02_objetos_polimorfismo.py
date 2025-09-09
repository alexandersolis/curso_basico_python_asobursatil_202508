class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass
        # Es buena práctica gnerar un error si no se implementa en la clase hija
        #raise NotImplementedError("Subclase debe implementar este método")

class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau, guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau, miau!"
    
class Vaca(Animal):
    pass

# Función que hace sonar a un animal
# def hacer_sonar_un_animal(animal):
#     print(animal.hacer_sonido())

# Crear objetos de las clases derivadas
mi_perro = Perro("Firulais")
mi_gato = Gato("Michi")

# Llamar a la función con diferentes objetos
# hacer_sonar_un_animal(mi_perro)  # Salida: ¡Guau, guau!
# hacer_sonar_un_animal(mi_gato)  # Salida: ¡Miau, miau!

print(mi_perro.hacer_sonido())  # Salida: ¡Guau, guau!
print(mi_gato.hacer_sonido())  # Salida: ¡Miau, miau!

mi_vaca = Vaca("Mimosa")
print(mi_vaca.hacer_sonido())  # Esto generará un error NotImplemented
