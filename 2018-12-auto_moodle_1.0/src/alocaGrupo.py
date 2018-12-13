import requests
from config.config import Config
from requests.packages.urllib3.exceptions import InsecureRequestWarning

'''remover warning por não verificar o SSL'''
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class Grupo:

    '''Resgata todas as disciplinas modelo'''
    def alocaGrupo(self):

        config = Config()

        serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                        config.alocaGrupoToken + "&wsfunction=" + "core_course_get_courses_by_field" \
                        + "&moodlewsrestformat=" + config.formatoRest + '&field=category&value=' + str(config.categoriaUnija)

        params = {'field': 'category', 'value': config.categoriaUnija}

        response = requests.get(serverUrlDisc, verify=False)
        disciplinasAva = response.json()

        listaAlunosGrupo = []

        for disMod in disciplinasAva['courses']:

            '''Resgata alunos matriculados na disciplina'''
            params = {'courseid': disMod['id'],
                      'options[0][name]': 'userfields',
                      'options[0][value]': 'institution',
                      'options[1][name]': 'userfields',
                      'options[1][value]': 'username'
                      }

            serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                            config.alocaGrupoToken + "&wsfunction=" + "core_enrol_get_enrolled_users" + "&moodlewsrestformat=" \
                            + config.formatoRest + "&courseid=" + str(disMod['id']) + "&options[0][name]=userfields&options[0][value]=institution" \
                            + "&options[1][name]=userfields&options[1][value]=username" + "&options[2][name]=onlyactive&options[2][value]=1"

            response = requests.get(serverUrlDisc, verify=False)
            alunosAva = response.json()

            alunoLista=[]

            '''Inserindo valores relevantes do json em lista '''
            for aluno in alunosAva:
                if len(aluno)>3:
                    alunoLista.append(
                        {'id': aluno['id'], 'institution': aluno['institution'], 'username': aluno['username']})

            '''Resgata grupos já existentes na disciplina'''
            params = {'courseid': disMod['id']}

            serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                            config.alocaGrupoToken + "&wsfunction=" + "core_group_get_course_groups" \
                            + "&moodlewsrestformat=" + config.formatoRest + "&courseid=" + str(disMod['id'])

            response = requests.get(serverUrlDisc, verify=False)

            gruposAva = response.json()

            '''Inserindo valores relevantes do json em lista '''
            gruposLista = []

            for grupos in gruposAva:
                gruposLista.append({'id': grupos['id'], 'name': grupos['name'], 'disciplina': grupos['courseid']})

            for grupo in gruposLista:
                for aluno in alunoLista:
                    if str(grupo['name']) == str(aluno['institution']):
                        params = {'members[0][groupid]': grupo['id'],
                                'members[0][userid]': aluno['id'],
                                }

                        serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                                        config.alocaGrupoToken + "&wsfunction=" + "core_group_add_group_members" + "&moodlewsrestformat=" \
                                        + config.formatoRest + "&members[0][groupid]=" \
                                        + str(grupo['id']) + "&members[0][userid]=" + str(aluno['id'])

                        response = requests.get(serverUrlDisc, verify=False)
                        response.json()

                        listaAlunosGrupo.append([{'nome': aluno['username'], 'grupo': grupo['name'], 'disciplina': grupo['disciplina']}])

        return listaAlunosGrupo






































