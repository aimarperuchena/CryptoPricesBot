
import time


import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from datetime import datetime
cont = 1
volume_msg = ''
capital_msg = ''
offer_msg = ''
demand_msg = ''


def limpiarVolume(dato):
    txt = ''
    if "B" in dato:
        dato = dato.replace("B", "")
        txt = ' Billion '

    if "M" in dato:
        dato = dato.replace("M", "")
        txt = ' Million '

    if "k" in dato:
        dato = dato.replace("k", "")
        txt = ' Thousands '

    return [dato, txt]


def limpiarCapital(dato):
    txt = ''
    if "B" in dato:
        dato = dato.replace("B", "")
        txt = ' Billion '
    if "M" in dato:
        dato = dato.replace("M", "")
        txt = ' Million '
    if "k" in dato:
        dato = dato.replace("k", "")
        txt = ' Thousands '
    return [dato, txt]


def limpiarOffer(dato):
    txt = ''
    if "B" in dato:
        dato = dato.replace("B", "")
        txt = ' Billion '
    if "M" in dato:
        dato = dato.replace("M", "")
        txt = ' Million '
    if "k" in dato:
        dato = dato.replace("k", "")
        txt = ' Thousands '
    return [dato, txt]


def limpiarDemand(dato):
    txt = ''
    if "B" in dato:
        dato = dato.replace("B", "")
        txt = ' Billion '
    if "M" in dato:
        dato = dato.replace("M", "")
        txt = ' Million '
    if "k" in dato:
        dato = dato.replace("k", "")
        txt = ' Thousands '
    return [dato, txt]


def limpiar(dato):
    if "B" in dato:
        dato = dato.replace("B", "")

    if "M" in dato:
        dato = dato.replace("M", "")

    if "k" in dato:
        dato = dato.replace("k", "")

    if "%" in dato:
        dato = dato.replace("%", "")
    if "+" in dato:
        dato = dato.replace("+", "")

    return dato


def generarPeticion(ranking, simbol, name, price, volume, capital, change24h, change7d, change1m, change6m, change1a, offer, demand, ratio, volume_msg, capital_msg, offer_msg, demand_msg):
    url = 'http://localhost:3000/api/crypto/prices'
    objeto = {'simbol': simbol, 'name': name, 'ranking': ranking, 'price': price, 'volume': volume, 'capital': capital, 'change24h': change24h,
              'change7d': change7d, 'change1m': change1m, 'change6m': change6m, 'change1a': change1a, 'offer': offer, 'demand': demand, 'ratio': ratio,
              'volume_msg': volume_msg, 'capital_msg': capital_msg, 'offer_msg': offer_msg, 'demand_msg': demand_msg}
    x = requests.post(url, data=objeto)


def leerDatos(ranking, simbol, name, price, volume, capital, change24h, change7d, change1m, change6m, change1a, offer, demand, ratio):
    dvolume = limpiarVolume(volume)
    volume = dvolume[0]
    volume_msg = dvolume[1]
    capitald = limpiarCapital(capital)
    capital = capitald[0]
    capital_msg = capitald[1]
    change24h = limpiar(change24h)
    change7d = limpiar(change7d)
    change1m = limpiar(change1m)
    change6m = limpiar(change6m)
    change1a = limpiar(change1a)
    offerd = limpiarOffer(offer)
    offer = offerd[0]
    offer_msg = offerd[1]
    demandd = limpiarDemand(demand)
    demand = demandd[0]
    demand_msg = demandd[1]
    ratio = limpiar(ratio)

    generarPeticion(ranking, simbol, name, price, volume, capital, change24h,
                    change7d, change1m, change6m, change1a, offer, demand, ratio, volume_msg, capital_msg, offer_msg, demand_msg)


def readLine(linea):
    tds = linea.findAll("div")
    ranking = tds[0].text
    td_simbolo = tds[1]
    if tds[1].text == "BTC" or tds[1].text == "ETH" or tds[1].text == "LTC" or tds[1].text == "XRP" or tds[1].text == "BCH" or tds[1].text == "EOS":
        leerDatos(str(tds[0].text), str(tds[1].text), str(tds[2].text), str(tds[3].text), str(tds[4].text), str(tds[5].text), str(tds[6].text),
                  str(tds[7].text), str(tds[8].text), str(tds[9].text), str(tds[10].text), str(tds[11].text), str(tds[12].text), str(tds[13].text))


def leerHtml():

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3', }

    reg_url = 'https://cryptowat.ch/es-es/assets'
    req = Request(url=reg_url, headers=headers)
    html = urlopen(req).read()
    soup2 = BeautifulSoup(html, features="html.parser")

    body = soup2.find("div", {"id": "__next"})
    content = body.find("div", {"class": "my-10"})
    mx_auto = content.find("div", {"class": "mx-auto"})
    my_5 = mx_auto.find("div", {"class": "-my-5"})
    overflow_x_auto = my_5.find("div", {"class": "overflow-x-auto"})
    tabla = overflow_x_auto.find("div", {"class": "_2eV8NnSAuzZ4ULshmhbQV0"})
    lineas = tabla.findAll("a", {"class": "_1roDdymkPS2zplXEDcBm0L"})
    for linea in lineas:
        readLine(linea)


a = True
while a == True:
    leerHtml()
    time.sleep(300)
