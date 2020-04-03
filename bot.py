import urllib.request
import time
import urlopen
import request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
cont = 1


def leerDatos(ranking, simbolo, nombre, precio, volumen, capitalizacion, cambio24h, cambio7d, cambio1m, cambio6m, cambio1a, oferta, demanda, ratio):
    print("Ranking: "+str(ranking))
    print("Simbolo: "+str(simbolo))
    print("Nombre: "+str(nombre))
    print("Precio: "+str(precio))
    print("Volumen: "+str(volumen))
    print("Capital: "+str(capitalizacion))
    print("24H: " + str(cambio24h))
    print("Cambio 7D: "+str(cambio7d))
    print("Cambio 1M: "+str(cambio1m))
    print("Cambio 6M: "+str(cambio6m))
    print("Cambio 1A:"+str(cambio1a))
    print("Oferta: "+str(oferta))
    print("Demanda: "+str(demanda))
    print("Ratio: "+str(ratio))
    print("-------------------------------------")


def readLine(linea):
    tds = linea.findAll("div")
    ranking = tds[0].text
    td_simbolo = tds[1]
    leerDatos(tds[0].text, tds[1].text, tds[2].text, tds[3].text, tds[4].text, tds[5].text, tds[6].text,
              tds[7].text, tds[8].text, tds[9].text, tds[10].text, tds[11].text, tds[12].text, tds[13].text)


def leerHtml(html):
    print("LEER HTML")
    """ headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = 'https://cryptowat.ch/es-es/assets'
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read() """
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
    for x in range(1, 13):
        html = driver.page_source
        leerHtml(html)
        if x<12:
            link="https://cryptowat.ch/es-es/assets?page="+str(x+1)
            btnSiguiente=None
            while btnSiguiente==None: 
                try:
                    btnSiguiente=driver.find_element_by_xpath("//*[contains(text(), 'siguiente')]")
                except:
                    print("An exception occurred"+ str(x+1))
            btnSiguiente.click()        
    driver.close
abrirPagina()
