dados1 = [{'name': 'Polo Pedreira', 'id': '02'},
            {'name': 'Polo Jaguariuna', 'id': '03'},
            {'name': 'Polo Itu', 'id': '01'}]

dados2 = [{'name': 'Polo Jaguariuna', 'id': '03'},
           {'name': 'Polo Itu', 'id': '04'}]


listaNomes=[]
for nome in dados2:
    listaNomes.append(nome['name'])

for dadosT1 in dados1:
    if dadosT1['name'] not in listaNomes:
        print(dadosT1)