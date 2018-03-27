from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("chromedriver.exe")
url = "http://jyldigital.com/productos.php"
driver.get(url)
driver.find_element_by_id("buscar").send_keys("taza")
driver.find_element_by_id("buscar").send_keys(Keys.ENTER)
productos = driver.find_elements_by_class_name('producto-contenido')
for producto in productos:
    print (producto.find_element_by_class_name('descripcion-texto-producto').text)