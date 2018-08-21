import requests
from pprint import pprint

from config.config import Config

class Duplica:
    def duplicaDisc(self):
        config = Config()

        '''Resgata todos as disciplinas'''

        serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                    config.duplicaToken + "&wsfunction=" + "core_course_get_courses" + "&moodlewsrestformat=" + config.formatoRest

        response = requests.post(serverUrlDisc)
        disciplinasAva = response.json()

        '''Resgata todas as categorias'''

        criteria = {'criteria[0][key]': 'parent', 'criteria[0][value]': 20}
        serverUrlCat = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                        config.duplicaToken + "&wsfunction=" + "core_course_get_categories" + "&moodlewsrestformat=" + config.formatoRest

        response = requests.post(serverUrlCat, criteria)
        categoriasAva = response.json()

        for disciplinasMatriz in disciplinasAva:
            if (disciplinasMatriz['categoryid'] == 52):
                for disciplinasReplica in disciplinasAva:
                    for categoriasPolo in categoriasAva:
                        if (disciplinasReplica['categoryid'] == categoriasPolo['id']):
                            if (disciplinasMatriz['fullname'] == disciplinasReplica['fullname']):
                                params = {'importfrom': disciplinasMatriz['id'],
                                          'importto': disciplinasReplica['id'],
                                          'deletecontent': '1',
                                          'options[0][name]': 'activities',
                                          'options[0][value]': '1',
                                          'options[1][name]': 'blocks',
                                          'options[1][value]': '0',
                                          'options[2][name]': 'filters',
                                          'options[2][value]': '0'
                                          }

                                serverUrlImp = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                                               config.duplicaToken + "&wsfunction=" + "core_course_import_course" + "&moodlewsrestformat=" + config.formatoRest

                                response = requests.post(serverUrlImp, params)

                                print(categoriasPolo['name'] + "/ " + disciplinasReplica['fullname'])

