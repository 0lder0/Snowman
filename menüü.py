from bs4 import BeautifulSoup
import requests

url = 'http://192.168.22.172/menu-example/'
sisu = requests.get(url).text
tekst = BeautifulSoup(sisu, 'html.parser')
fail = tekst.find_all('h2')

lug = 0
pealkirjad = []
something = tekst.find_all('strong')

for asi in something:
    sõna = str(asi).strip('[<strong>')
    sõne = sõna.strip('</strong>')
    pealkirjad.append(sõne)

for a in fail:
    lug += 1
#lugerist läheb 1 maha, kuna see arvestab ka koolilõunatoetuse lehe all
luger = lug - 1

for luger in range(luger):
    tags = tekst.find_all('h2')[luger]
    try:
        for i in tags:
            print(i)
            break
        print('Lisainfo: ' + tags.small.string)
        print('Hind: ' + tags.span.string + '\n')
    except:
        print('Lisainfo puudub')
        print('Hind: ' + tags.span.string + '\n')
    