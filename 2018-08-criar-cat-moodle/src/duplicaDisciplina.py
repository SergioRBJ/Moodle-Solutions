import requests
from config.config import Config
from config.conexao import DbConnect

class Duplica:
    def duplicaDisc(self):
        config = Config()

        '''Resgata todos as disciplinas'''

        serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                    config.duplicaToken + "&wsfunction=" + "core_course_get_courses" + "&moodlewsrestformat=" + config.formatoRest

        response = requests.post(serverUrlDisc)
        disciplinasAva = response.json()

        for disciplinasMatriz in disciplinasAva:
            if disciplinasMatriz['categoryid'] == config.categoriaMatrizesEsp:
                getDisc = Duplica.getDisImp(disciplinasMatriz['idnumber'])
                for disciplinaReplica in getDisc:
                    if disciplinasMatriz['idnumber'] == disciplinaReplica['equivalencia']:
                        params = {'importfrom': disciplinasMatriz['id'],
                                  'importto': disciplinaReplica['id'],
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

                        return disciplinasMatriz['shortname'] + "/ " + disciplinaReplica['fullname'] + "/ " + disciplinaReplica['id']


    def getDisImp(self, equivalencia):

        discRM = []

        try:
            mssql = DbConnect().mssqlConnect()
            sql = """ DECLARE @CODPERLET	VARCHAR(7)
                        SET @CODPERLET = '2018-02'
                        SELECT shortname, CATEGORIA, CODCAMPUS, DISCMODELO
                        FROM polis_moodle_cmoodle2_temp AS PMCM2T (NOLOCK)
                        WHERE PMCM2T.CODCOLIGADA = 1
                        AND PMCM2T.CODTIPOCURSO IN (123, 124, 125)
                        AND PMCM2T.CODPERLET = @CODPERLET
                        AND PMCM2T.IMPORTADO = 'N' 
                        AND DISCMODELO = %s
                        """ % equivalencia

            mssql.execute(sql)
            resultado = mssql.fetchall()

        except Exception as e:
            print(e)

        for shortname, CATEGORIA, CODCAMPUS, DISCMODELO in resultado:

            config = Config()

            serverUrlDisc = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                            config.duplicaToken + "&wsfunction=" + "core_course_get_courses_by_field" + "&moodlewsrestformat=" + config.formatoRest

            params = {'field': 'shortname', 'value': shortname}

            response = requests.post(serverUrlDisc, params)
            disciplinasAva = response.json()

            discRM.append({'shortname': shortname, 'equivalencia': DISCMODELO, 'id': disciplinasAva['id']})

        return discRM



