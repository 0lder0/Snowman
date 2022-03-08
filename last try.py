# impordime vajalikud moodulid
from bs4 import BeautifulSoup
import requests

# avame ja loeme sisse veebilehe andmed
url = 'https://siseveeb.voco.ee/veebivormid/sookla_menuu'
sisu = requests.get(url).text
tekst = BeautifulSoup(sisu, 'html.parser')
# filtreerime vajaliku koodijupi
fail = tekst.find_all('h2')

# tühjad järjendid ja sõnastik
pealkirjad = []
json_list = []
json_dict = {}
lug = 0

# leiame veebilehelt toitude liigid
something = tekst.find_all('strong')
# võtame tag'ide vahelt toitude liigid
for asi in something:
    sõna = str(asi).strip('[<strong>')
    sõne = sõna.strip('</strong>')
    # lisame puhastatud sõne järjendisse
    pealkirjad.append(sõne)

# teeme lugeri, et teada mitu elementi (toitu) on
for a in fail:
    lug += 1
# lugerist läheb 1 maha, kuna see arvestab ka koolilõunatoetuse (lehe all)
luger = lug - 1

# luger piirab tsükli toimumise kordi elementide arvuga
for luger in range(luger):
    # luger võtab ükshaaval elementide (toitude) koode
    tags = tekst.find_all('h2')[luger]
    # saame toidu nimetuse
    for i in tags:
        nimi = i
        break
    # saame toidu lisainfo
    info = tags.small.string
    # kontrollime kas toidul on lisainfot
    if info == None:
        # kui toidul puudub lisainfo prindime 'Lisainfo puudub'
        info = 'Lisainfo puudub'
    else:
        info = tags.small.string
    # leiame hinna
    hind = tags.span.string
    # lisame andmed sõnastikku
    json_dict = {'Nimi': nimi, 'Lisainfo': info, 'Hind': hind}
    # lisame sõnastiku järjendisse
    json_list.append(json_dict)