# impordime vajalikud moodulid
from bs4 import BeautifulSoup
import requests

# avame ja loeme sisse veebilehe andmed
url = 'https://siseveeb.voco.ee/veebivormid/sookla_menuu'
sisu = requests.get(url).text
tekst = BeautifulSoup(sisu, 'html.parser')
# filtreerime vajaliku koodijupi
fail = tekst.find_all('h2')


lug = 0
pealkirjad = []
json_list = []
json_dict = {}

# leiame toitude liigid
something = tekst.find_all('strong')
# saame tag'ide vahelt  
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
    for i in tags:
        nimi = i
        break
    info = tags.small.string
    if info == None:
        info = 'Lisainfo puudub'
    else:
        info = tags.small.string
    hind = tags.span.string
    json_dict = {'Nimi': nimi, 'Lisainfo': info, 'Hind': hind}
    json_list.append(json_dict)
print(json_list)