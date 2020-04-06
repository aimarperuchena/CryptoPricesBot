import urllib.request
import time
import urlopen
import request
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
cont = 1


def leerDatos(ranking, simbol, name, price):
    url = 'http://192.168.0.12:1234/api/currency'
    objeto = {'ranking': ranking, 'simbol': simbol, 'name':name,'price':price}
    x = requests.post(url, data=objeto)


def readLine(linea):
    tds = linea.findAll("div")
    leerDatos(str(tds[0].text), str(tds[1].text), str(tds[2].text), str(tds[3].text))


def leerHtml(html):
    soup2 = BeautifulSoup(html)
    body = soup2.find("div", {"id": "__next"})
    content = body.find("div", {"class": "my-10"})
    mx_auto = content.find("div", {"class": "mx-auto"})
    my_5 = mx_auto.find("div", {"class": "-my-5"})
    overflow_x_auto = my_5.find("div", {"class": "overflow-x-auto"})
    tabla = overflow_x_auto.find("div", {"class": "_2eV8NnSAuzZ4ULshmhbQV0"})
    lineas = tabla.findAll("a", {"class": "_1roDdymkPS2zplXEDcBm0L"})
    for linea in lineas:
        readLine(linea)


def abrirPagina():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.maximize_window()
    driver.get("https://cryptowat.ch/es-es/assets")
    btnEuro = driver.find_element_by_xpath("//button[@id='eur']")
    btnEuro.click()
    html = driver.page_source
    leerHtml(html)      
    driver.close
abrirPagina()
