import requests
from config.config import Config
from requests.packages.urllib3.exceptions import InsecureRequestWarning

'''remover warning por não verificar o SSL'''
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Duplica:
    def duplicaDisc(self):
        config = Config()

        '''Resgata todas as disciplinas'''

        serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                    config.duplicaToken + "&wsfunction=" + "core_course_get_courses" + "&moodlewsrestformat=" + config.formatoRest

        response = requests.get(serverUrlDisc, verify=False)
        disciplinasAva = response.json()

        discMatriz = []
        discModelo = []

        listaImportadas = []

        for disciplinasMatriz in disciplinasAva:

            if str(disciplinasMatriz['categoryid']) == str(config.categoriaMatrizesEsp):
                discMatriz.append([{'id': disciplinasMatriz['id'], 'idnumber': disciplinasMatriz['idnumber'],
                                    'fullname': disciplinasMatriz['fullname']}])

            if str(disciplinasMatriz['categoryid']) == str(config.categoriaUnija):
                discModelo.append([{'id': disciplinasMatriz['id'], 'idnumber': disciplinasMatriz['idnumber'],
                                    'fullname': disciplinasMatriz['fullname']}])

        for discMatrizReg in discMatriz:
            for discModeloReg in discModelo:

                i = len(discModeloReg[0]['idnumber'])

                if discMatrizReg[0]['idnumber'] == discModeloReg[0]['idnumber'][4:i-3] and discMatrizReg[0]['idnumber'] != '':

                    params = {'importfrom': discMatrizReg[0]['id'],
                              'importto': discModeloReg[0]['id'],
                              'deletecontent': '1',
                              'options[0][name]': 'activities',
                              'options[0][value]': '1',
                              'options[1][name]': 'blocks',
                              'options[1][value]': '0',
                              'options[2][name]': 'filters',
                              'options[2][value]': '0'
                              }

                    serverUrlImp = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                                   config.duplicaToken + "&wsfunction=" + "core_course_import_course" + "&moodlewsrestformat=" \
                                   + config.formatoRest + "&importfrom=" + str(discMatrizReg[0]['id']) + "&importto=" + str(discModeloReg[0]['id']) \
                                   + "&deletecontent=1" + "&options[0][name]=activities&options[0][value]=1" + "&options[1][name]=blocks&options[1][value]=0" \
                                   + "&options[2][name]=filters&options[2][value]=0"

                    requests.get(serverUrlImp, verify='/cert-file/certs.pem')
                    listaImportadas.append(discModeloReg[0]['fullname'])

        return listaImportadas




