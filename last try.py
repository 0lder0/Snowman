# impordime vajalikud moodulid
from bs4 import BeautifulSoup
import requests
import json

# avame ja loeme sisse veebilehe andmed
url = 'http://192.168.22.172/menu-example/'
sisu = requests.get(url).text
tekst = BeautifulSoup(sisu, 'html.parser')
# filtreerime vajalikud koodijupid
fail = tekst.find_all('h2')
thing = tekst.find_all('ul')

# tühjad järjendid, sõnastik ja lugerid
elementide_arv = []
pealkirjad = []
final_list = []
json_list = []
json_dict = {}
food_dict ={}
indeks = 0
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
    for toit in tags:
        nimi = toit
        break
    # saame toidu lisainfo
    info = tags.small.string
    # kontrollime kas toidul on lisainfot
    if info == None:
        # kui toidul puudub lisainfo prindime 'Lisainfo puudub'
        info = 'Lisainfo puudub'
    else:
        info = tags.small.string
    #leiame hinna
    hind1 = tags.span.string
    hind = str(hind1).strip('€')
    # lisame andmed sõnastikku
    json_dict = {'nimetus': nimi, 'hind': hind, 'lisainfo': info}
    # lisame sõnastiku järjendisse
    json_list.append(json_dict)

# leiame elementide ala igas toitude kategoorias
for i in range(5):
    things = thing[i]
    luger1 = 0
    asi1 = '€'
    for asi1 in things:
        luger1 += 1
    indeks += 1
    if indeks == 5:
        # joogid on kahes osas ja need tuleb kokku liita
        elementide_arv[-1] = elementide_arv[-1] + luger1
    else:
        elementide_arv.append(luger1)
    
# vormistame jsoni faili
for i in range(len(pealkirjad)):
    food_dict = {'nimetus': pealkirjad[i], 'toidud': []}
    for x in elementide_arv:
        for l in range(x):
            food_dict['toidud'].append(json_list[0])
            json_list.pop(0)
        elementide_arv.pop(0)
        break
    final_list.append(food_dict)

# kirjutame andmed faili
print(final_list)
with open('json_fail.py', 'w') as j_fail:
    json.dump(final_list, j_fail, indent = 4)
j_fail.close()