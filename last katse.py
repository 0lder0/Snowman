from bs4 import BeautifulSoup
import requests

url = 'http://192.168.22.172/menu-example/'
sisu = requests.get(url).text
tekst = BeautifulSoup(sisu, 'html.parser')
fail = tekst.find_all('h2')

thing = tekst.find_all('ul')
elementide_arv = []

indeks = 0
for i in range(5):
    things = thing[i]
    luger = 0
    asi = '€'
    for asi in things:
        luger += 1
    indeks += 1
    if indeks == 5:
        elementide_arv[-1] = elementide_arv[-1] + luger
    else:
        elementide_arv.append(luger)
print(elementide_arv)
