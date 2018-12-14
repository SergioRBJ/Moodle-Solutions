import requests
from config.config import Config
from config.conexao import DbConnect
from requests.packages.urllib3.exceptions import InsecureRequestWarning

'''remover warning por não verificar o SSL'''
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Grupo:

    def alocaGrupo(self):

        config = Config()
        db = DbConnect().mysqlConnect()
        cursor = db.cursor()

        query = """ 
                SELECT u.id AS ID_ALUNO, u.username as RA_ALUNO, u.institution AS POLO, c.fullname AS DISCIPLINA,
                (SELECT gs.id FROM mdl_groups gs
                LEFT JOIN mdl_groups_members gms ON gms.groupid = gs.id
                WHERE gs.courseid = c.id AND gs.name = u.institution) AS GRUPO_ESPERADO_ID
                
                FROM moodle.mdl_user u
                INNER JOIN mdl_role_assignments ra ON ra.userid = u.id
                INNER JOIN mdl_context cx ON cx.id = ra.contextid AND cx.contextlevel =50
                INNER JOIN mdl_course c ON c.id = cx.instanceid
                INNER JOIN mdl_groups g ON g.courseid = c.id
                LEFT JOIN mdl_groups_members gm ON gm.groupid = g.id AND gm.userid = u.id
                
                WHERE c.category = %s
                AND c.visible = '1'
                AND gm.id IS NULL
                AND u.institution != '';
         
                """ % config.categoriaUnija
        cursor.execute(query)

        listaAlunos = []

        for (ID_ALUNO, RA_ALUNO, POLO, DISCIPLINA, GRUPO_ESPERADO_ID) in cursor:

            serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                            config.alocaGrupoToken + "&wsfunction=" + "core_group_add_group_members" + "&moodlewsrestformat=" \
                            + config.formatoRest + "&members[0][groupid]=" \
                            + str(GRUPO_ESPERADO_ID) + "&members[0][userid]=" + str(ID_ALUNO)

            response = requests.get(serverUrlDisc, verify=False)
            response.json()

            listaAlunos.append(
                [{'nome': RA_ALUNO, 'grupo': POLO, 'disciplina': DISCIPLINA}])

        return listaAlunos






































