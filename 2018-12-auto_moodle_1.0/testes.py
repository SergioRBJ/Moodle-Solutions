from pprint import pprint
from src.acao import Acao
import requests
from config.config import Config
from pprint import pprint
from src.alocaGrupo import Grupo
from requests.packages.urllib3.exceptions import InsecureRequestWarning

'''remover warning por não verificar o SSL'''
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

'''dados1 = [{'name': 'Polo Pedreira', 'id': '02'},
            {'name': 'Polo Jaguariuna', 'id': '03'},
            {'name': 'Polo Itu', 'id': '01'}]

dados2 = [{'name': 'Polo Jaguariuna', 'id': '03'},
           {'name': 'Polo Itu', 'id': '04'}]


listaNomes=[]
for nome in dados2:
    listaNomes.append(nome['name'])

for dadosT1 in dados1:
    if dadosT1['name'] not in listaNomes:
        print(dadosT1)'''

var = '2019U1230074JAN'

var2 = 'U1230074'

if (var[4:12] == var2):
    print('ok')

class Duplica:
    def duplicaDisc(self):
        config = Config()

        '''Resgata todas as disciplinas'''

        serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                    config.duplicaToken + "&wsfunction=" + "core_course_get_courses" + "&moodlewsrestformat=" + config.formatoRest

        response = requests.post(serverUrlDisc)
        disciplinasAva = response.json()

        discMatriz = []
        discModelo = []

        for disciplinasMatriz in disciplinasAva:
            if str(disciplinasMatriz['categoryid']) == str(config.categoriaMatrizesEsp):
                discMatriz.append([{'id': disciplinasMatriz['id'], 'idnumber': disciplinasMatriz['idnumber'],
                                    'fullname': disciplinasMatriz['fullname']}])
            if str(disciplinasMatriz['categoryid']) == str(config.categoriaUnija):
                discModelo.append([{'id': disciplinasMatriz['id'], 'idnumber': disciplinasMatriz['idnumber'],
                                    'fullname': disciplinasMatriz['fullname']}])
        for discMatrizReg in discMatriz:
            for discModeloReg in discModelo:
                if discMatrizReg[0]['idnumber'] == discModeloReg[0]['idnumber'][4:12]:

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
                                   config.duplicaToken + "&wsfunction=" + "core_course_import_course" + "&moodlewsrestformat=" + config.formatoRest

                    response = requests.post(serverUrlImp, params)

        return response


aloca = Duplica()
retorno = aloca.duplicaDisc()
pprint(retorno)
