# Extraer Información de una Página Web:
# Extraer información específica de una página web, como los títulos de los artículos y sus enlaces.
import requests
from bs4 import BeautifulSoup

# Realizar una petición GET a la página web
url = 'https://news.ycombinator.com/'
response = requests.get(url)

# Crear un objeto BeautifulSoup para analizar el contenido HTML
soup = BeautifulSoup(response.content, 'lxml')

# Extraer los títulos de los artículos y sus enlaces
# article = soup.find('span', class_='titleline')
# print(f'Título: {article.a.get_text()}')
# print(f'Enlace: {article.a['href']}')

articles = soup.find_all('span', class_='titleline')
for article in articles:
    title = article.a.get_text()
    link = article.a['href']
    print(f'Título: {title}')
    print(f'Enlace: {link}')
