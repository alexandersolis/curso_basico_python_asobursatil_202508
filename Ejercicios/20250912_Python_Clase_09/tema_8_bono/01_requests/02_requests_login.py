import requests

respuestas = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
print(f"Codigo de estado o respuesta: {respuestas.status_code}")
print(f"Tipo de contenido {respuestas.headers['content-type']}")
print(f"Encoding: {respuestas.encoding}")
print(f"Texto: {respuestas.text}")
print(f"JSON: {respuestas.json()}")
