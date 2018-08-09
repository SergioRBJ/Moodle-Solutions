import requests
from pprint import pprint

from config.config import Config

dadosRm = [{'name': 'Polo Itatiba', 'id': '01'},
            {'name': 'Polo Jaguariuna', 'id': '02'},
           {'name': 'Polo Itu', 'id': '03'}]

restformat = 'json'

criteria = {'criteria[0][key]': 'parent', 'criteria[0][value]': 20}

config = Config()

serverurl = config.credenciais['domainname'] + "/webservice/rest/server.php" + "?wstoken=" + \
            config.credenciais['token'] + "&wsfunction=" + config.credenciais['functionname'] + "&moodlewsrestformat=" + restformat

response = requests.post(serverurl, criteria)
categoriasAva = response.json()

'''pprint(categoriasAva)
pprint(categoriasAva[0]['name'])
pprint(dadosRm[0]['name'])'''

categoriasAvaNome = []

for nome in categoriasAva:
    categoriasAvaNome.append(nome['name'])

for categoriaRm in dadosRm:
    if categoriaRm['name'] not in categoriasAvaNome:
        categories = {'categories[0][name]': categoriaRm['name'],
                      'categories[0][parent]': 20}

        serverurl = config.credenciais['domainname'] + "/webservice/rest/server.php" + "?wstoken=" + \
                    config.credenciais['token'] + "&wsfunction=" + "core_course_create_categories" \
                    + "&moodlewsrestformat=" + restformat

        resp = requests.post(serverurl, categories)

        pprint(serverurl)
        pprint(resp.json())