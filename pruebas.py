# 
# En esta parte solo prueba como almacenar los datos cada vez que encuentro una nueva pagina
#

# Aun no pude agregar este contenido a la web
from bs4 import BeautifulSoup
import requests
import re

buscar=input('Producto a buscar: ')
#buscar="taza"

print(" ")
print("Producto                                |Precio             |URL")
print("----------------------------------------------------------------------------------------------")

#Pagina 5 // NComunica
buscar4=buscar
while buscar4.find(" ")>0:
	buscar4=buscar4.replace(" ","+")
url="http://www.ncomunica.com/ventasblog/tienda/articulos-de-sublimacion/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
productos=soup.find_all('div', class_='ProductName')
print(soup.prettify())
"""
for producto in productos:
	linea=producto.find_all('div',class_='ProductName')[0].get_text()
	linea=re.sub(r'\s', '', linea)
	while(len(linea)<40):
		linea=linea+" "	
	precio=producto.find_all('div',class_='ProductPrice')[0].get_text()
	precio=re.sub(r'\s', '', precio)
	linea=linea+"|"+precio
	while(len(linea)<60):
		linea=linea+" "
	linea+="|"+url
	print(linea)
"""