from pprint import pprint
from src.acao import Acao
import requests
from config.conexao import DbConnect
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
listaTeste = []
db = DbConnect().mysqlConnect()
cursor = db.cursor()

query = """ SELECT u.username AS RA, u.institution AS POLO, c.fullname AS CURSO  FROM moodle.mdl_user u
            INNER JOIN mdl_role_assignments ra ON ra.userid = u.id
            INNER JOIN mdl_context cx ON cx.id = ra.contextid AND cx.contextlevel =50
            INNER JOIN mdl_course c ON c.id = cx.instanceid
            WHERE c.category = '1'
            AND c.visible = '1' """

cursor.execute(query)
'''resultado = cursor.fetchall()'''

for (RA, POLO, DISC) in cursor:
    listaTeste.append({'RA':RA, 'POLO':POLO, 'DISC': DISC})

cursor.close()
db.close()

pprint(listaTeste)




