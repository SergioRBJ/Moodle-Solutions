import requests
from pprint import pprint

from config.config import Config

dadosRm = [{'name': 'Polo Itatiba', 'id': '01'},
            {'name': 'Polo Jaguariuna', 'id': '02'},
           {'name': 'Polo Itu', 'id': '03'}]

categoriaSemestre = 20

criteria = {'criteria[0][key]': 'parent', 'criteria[0][value]': categoriaSemestre}

config = Config()

serverurl = config.credenciais['domainname'] + "/webservice/rest/server.php" + "?wstoken=" + \
            config.credenciais['token'] + "&wsfunction=" + "core_course_get_categories" + "&moodlewsrestformat=" + config.formatoRest

response = requests.post(serverurl, criteria)
categoriasAva = response.json()

categoriasAvaNome = []

for nome in categoriasAva:
    categoriasAvaNome.append(nome['name'])

for categoriaRm in dadosRm:
    if categoriaRm['name'] not in categoriasAvaNome:
        categories = {'categories[0][name]': categoriaRm['name'],
                      'categories[0][parent]': categoriaSemestre}

        serverurl = config.credenciais['domainname'] + "/webservice/rest/server.php" + "?wstoken=" + \
                    config.credenciais['token'] + "&wsfunction=" + "core_course_create_categories" \
                    + "&moodlewsrestformat=" + config.formatoRest

        resp = requests.post(serverurl, categories)

        pprint(serverurl)
        pprint(resp.json())
