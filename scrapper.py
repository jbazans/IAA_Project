from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--kiosk")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome("chromedriver.exe")
url = "http://apps2.mef.gob.pe/consulta-vfp-webapp/consultaExpediente.jspx"
driver.get(url)