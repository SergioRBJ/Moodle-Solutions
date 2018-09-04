from src.duplicaDisciplina import Duplica
from pprint import pprint
from src.criaCategoria import CriaCategoria
from src.acao import Acao
import requests
from config.config import Config
from config.conexao import DbConnect
from src.alteraLink import Link
from pprint import pprint

'''cricat = CriaCategoria()
retorno = cricat.getCategoriaAVA()
print(retorno)'''

'''duplica = Duplica()
retorno = duplica.getDisImp("NULL")
pprint(retorno)'''

'''acao = Acao()
retorno = acao.categoriasCriadas()
'''
'''config = Config()

param = {'courseid': '30'}

serverUrl = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
            config.altLinkToken + "&wsfunction=" + "core_group_get_course_groups" + "&moodlewsrestformat=" + config.formatoRest

response = requests.post(serverUrl, param)
disciplinasGrupos = response.json()

print(len(disciplinasGrupos))'''

'''link = Link()
retorno = link.alteraLink()
print(retorno)'''

'''valor = "jdhsdigsf_teste"
teste = valor.split("_")
print(teste[1])'''


config = Config()

serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
config.duplicaToken + "&wsfunction=" + "core_course_get_courses_by_field" + "&moodlewsrestformat=" + config.formatoRest

params = {'field': 'shortname', 'value': "MODELOMA"}

response = requests.post(serverUrlDisc, params)
disciplinasAva = response.json()

pprint(disciplinasAva)