#Instalando bibliotecas
#Scraper
#pip install selenium
from selenium import webdriver
#Para pegar os elementos
from selenium.webdriver.common.by import By
from Credenciais import usuario, senha

driver = webdriver.Chrome()
driver.get('https://moodle.imd.ufrn.br/')
usuario = driver.find_element(by=By.XPATH, value='//*[@id="username"]').send_keys(usuario)
senha = driver.find_element(by=By.XPATH, value='//*[@id="password"]').send_keys(senha)
senha = driver.find_element(by=By.XPATH, value='//*[@id="loginbtn"]').click()