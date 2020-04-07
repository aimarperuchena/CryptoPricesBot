import urllib.request
import time
import urlopen
import request
import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
cont = 1


def leerDatos(ranking, simbol, name, price):
    url = 'https://aimarcrypto.herokuapp.com/api/currency'
    objeto = {'ranking': ranking, 'simbol': simbol,
              'name': name, 'price': price}
    x = requests.post(url, data=objeto)
    if x.text!="":
        print(x.text)


def readLine(linea):
    tds = linea.findAll("div")
    leerDatos(str(tds[0].text), str(tds[1].text),
              str(tds[2].text), str(tds[3].text))


def leerHtml(soup2):

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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    reg_url = 'https://cryptowat.ch/es-es/assets'
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html)
    leerHtml(soup2)


a = 0
while a == 0:
    abrirPagina()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    time.sleep(42)
