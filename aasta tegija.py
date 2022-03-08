import json

nimed = ['Peeter', 'Jaak','Malle', 'Karin']
vanus = [7, 15, 47, 28]
haigused = ['Jah', 'Ei', 'Ei', 'Jah']

json_list = []

i = 0
for nimi in nimed:
    midagi = {'nimi': nimi, 'vanus': vanus[i], 'haige': haigused[i]}
    json_list.append(midagi)

print(json_list)