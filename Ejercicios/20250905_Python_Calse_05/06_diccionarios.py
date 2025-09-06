diccionario1 = {
    "Nombre": "Jimmy",
    "Profesion": "Ingeniero",
    "Edad": 25
}

diccionario2 = dict(Nombre="Jimmy", Profesion="Ingeniero", Edad=25)

print(diccionario1)
print(diccionario2)

persona_2 = {
    "Nombre": "Ana",
    "Profesion": "Arquitecta",
    "Edad": 30
}

personas = dict(persona_1=diccionario1, persona_2=persona_2)
print(personas)