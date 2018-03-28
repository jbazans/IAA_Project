#
# Codigo que permite obtener informacion de algunas fuentes de internet
#--------------------------------
# Se tiene que ver la estructura primero de cada pagina para poder
# agregar a nuestra base de datos
#

from bs4 import BeautifulSoup
import requests
import re

buscar=input('Producto a buscar: ')
#buscar="taza"

print(" ")
print("Producto                                |Precio             |URL")
print("-------------------------------------------------------------")
url="http://jyldigital.com/productos.php?producto="+buscar
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
productos=soup.find_all('div', class_='producto-contenido')
for producto in productos:
	linea=producto.find_all('div',class_='descripcion-texto-producto')[0].get_text()
	while(len(linea)<40):
		linea=linea+" "
	if len(producto.find_all('div',class_='descripcion-precio'))!=0:
		precio=producto.find_all('div',class_='descripcion-precio')[0].get_text()
		precio=re.sub(r'\s', '', precio)
		linea=linea+"|"+precio
	else:
		linea=linea+"|-----"
	while(len(linea)<60):
		linea=linea+" "
	linea+="|"+url
	print(linea)


#Pagina 2 // Mercado libre
# Estrucuta compleja por que no utiliza codificacion UTF-8
"""
buscar2=buscar
while buscar2.find(" ")>0:
	buscar2=buscar2.replace(" ","-")
url="https://listado.mercadolibre.com.pe/"+buscar2+"#D[A:"+buscar2+"]"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser').encode("ascii")
productos=soup.find_all('div', class_='rowItem item item--stack new')
print(productos)
for producto in productos:
	linea=producto.find_all('span',class_='main-title')[0].get_text()
	while(len(linea)<40):
		linea=linea+" "
	if len(producto.find_all('span',class_='price__fraction'))!=0:
		linea=linea+"|"+producto.find_all('div',class_='descripcion-precio')[0].get_text()
	else:
		linea=linea+"|-----"
	print(linea)
	"""

#Pagina 3 // Kregalos
buscar3=buscar
while buscar3.find(" ")>0:
	buscar3=buscar3.replace(" ","+")
url="http://www.kregalos.com/shopping/buscar?controller=search&orderby=position&orderway=desc&search_query="+buscar3
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
productos=soup.find_all('div', class_='product-container')
for producto in productos:
	linea=producto.find_all('a',class_='product-name')[0].get_text()
	nombre=""
	vacios=[]
	for x in range(0,len(linea)):
		if linea[x]==' ':
			vacios.append(x)
	linea=re.sub(r'\s', '', linea)
	lugar=8
	i=0
	for pos in vacios:
		condi=False
		while condi==False:
			if i==pos-lugar:
				nombre+=" "+linea[i]
				condi=True
			else:
				nombre+=linea[i]
			i+=1
		lugar+=1
	for x in range(i,len(linea)):
		nombre+=linea[x]
	linea=nombre
	while(len(linea)<40):
		linea=linea+" "	
	precio=producto.find_all('span',class_='price product-price')[0].get_text()
	precio=re.sub(r'\s', '', precio)
	linea=linea+"|"+precio
	while(len(linea)<60):
		linea=linea+" "
	linea+="|"+"http://www.kregalos.com/shopping/buscar?controller...."
	print(linea)

#Pagina 4 // Don Regalo
buscar4=buscar
while buscar4.find(" ")>0:
	buscar4=buscar4.replace(" ","+")
url="http://www.donregalo.pe/?q="+buscar4
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
productos=soup.find_all('li', class_='liCat')
for producto in productos:
	linea=producto.find_all('div',class_='nameProd')[0].get_text()
	while(len(linea)<40):
		linea=linea+" "	
	precio=producto.find_all('span',class_='soles')[0].get_text()
	precio=re.sub(r'\s', '', precio)
	precio=precio.replace('(','')
	precio=precio.replace(')','')
	linea=linea+"|"+precio
	while(len(linea)<60):
		linea=linea+" "
	linea+="|"+url
	print(linea)