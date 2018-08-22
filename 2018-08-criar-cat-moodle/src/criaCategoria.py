import requests
from pprint import pprint

from config.config import Config

class CriaCategoria:
    def criacaoCat(self):

        dadosRm = [{'name': 'Polo Itatiba', 'id': '01'},
                   {'name': 'Polo Jaguariuna', 'id': '02'},
                   {'name': 'Polo Itu', 'id': '03'},
                   {'name': 'Polo Bebedouro', 'id': '04'},
                   {'name': 'Polo Bambui', 'id': '05'}]

        config = Config()
        criteria = {'criteria[0][key]': 'parent', 'criteria[0][value]': config.categoriaSemestre}

        serverurl = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                    config.categoriaToken + "&wsfunction=" + "core_course_get_categories" + "&moodlewsrestformat=" + config.formatoRest

        response = requests.post(serverurl, criteria)
        categoriasAva = response.json()

        categoriasAvaNome = []
        polos = []
        for nome in categoriasAva:
            categoriasAvaNome.append(nome['name'])

        for categoriaRm in dadosRm:
            if categoriaRm['name'] not in categoriasAvaNome:
                categories = {'categories[0][name]': categoriaRm['name'],
                              'categories[0][parent]': config.categoriaSemestre}

                serverurl = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                            config.categoriaToken + "&wsfunction=" + "core_course_create_categories" \
                            + "&moodlewsrestformat=" + config.formatoRest

                resp = requests.post(serverurl, categories)
                polo = resp.json()

                polos.append(polo[0]['name'])

        return polos

