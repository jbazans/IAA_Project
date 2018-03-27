from bs4 import BeautifulSoup
import requests

buscar=input('Producto a buscar: ')
#buscar="taza"

print(" ")
print("Producto                                |Precio")
print("-------------------------------------------------------------")
page = requests.get("http://jyldigital.com/productos.php?producto="+buscar)
soup = BeautifulSoup(page.content, 'html.parser')
productos=soup.find_all('div', class_='producto-contenido')
for producto in productos:
	linea=producto.find_all('div',class_='descripcion-texto-producto')[0].get_text()
	while(len(linea)<40):
		linea=linea+" "
	if len(producto.find_all('div',class_='descripcion-precio'))!=0:
		linea=linea+"|"+producto.find_all('div',class_='descripcion-precio')[0].get_text()
	else:
		linea=linea+"|-----"
	print(linea)


#Pagina 2 // Mercado libre
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
	for x in range(0,len(linea)):
		if linea[x]!=' ':
			nombre+=linea[x]
	print(nombre)
	"""
	while(len(linea)<40):
		linea=linea+" "	
	precio=producto.find_all('span',class_='price product-price')[0].get_text()
	linea=linea+"|"+precio
	print(linea)"""