import requests
from config.config import Config
from config.conexao import DbConnect

class Link:
    def alteraLink(self):
        config = Config()

        '''Resgata todos as disciplinas'''

        serverUrl = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                        config.altLinkToken + "&wsfunction=" + "core_course_get_courses" + "&moodlewsrestformat=" + config.formatoRest

        response = requests.post(serverUrl)
        disciplinasAva = response.json()

        '''Resgata todas as categorias'''

        criteria = {'criteria[0][key]': 'parent', 'criteria[0][value]': config.categoriaSemestrePolos}
        serverUrlCat = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                       config.altLinkToken + "&wsfunction=" + "core_course_get_categories" + "&moodlewsrestformat=" + config.formatoRest

        response = requests.post(serverUrlCat, criteria)
        categoriasAva = response.json()

        for discModelo in disciplinasAva:
            if (discModelo['categoryid'] == config.categoriaUnija):

                '''Retorna as disciplinas especificas levando em conta a modelo'''

                for discEspecifica in disciplinasAva:
                    for categoriaPolos in categoriasAva:
                        if (discEspecifica['categoryid'] == categoriaPolos['id']):
                            shortNameModelo = discModelo['shortname'].split("_")
                            shortNameEspecifica = discEspecifica['shortname'].split("_")
                            '''if (shortNameModelo[1] == shortNameEspecifica[1]):'''



                '''Resgata todos os grupos de determinada discplina'''

                param = {'courseid': discModelo['id']}
                serverUrl = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                            config.altLinkToken + "&wsfunction=" + "core_group_get_course_groups" + "&moodlewsrestformat=" + config.formatoRest

                response = requests.post(serverUrl, param)
                disciplinasGrupos = response.json()

                try:
                    mySql = DbConnect().mysqlConnect()
                    mysql = mySql.cursor()

                    sql = """SELECT id,instance FROM mdl_course_modules WHERE course = %s AND module = 20
                                """ % discModelo['id']

                    mysql.execute(sql)
                    resultado = mysql.fetchall()

                    print(resultado)

                except Exception as e:
                    print(e)

                finally:
                    if(mySql.is_connected()):
                        mySql.close()

                cont = len(disciplinasGrupos)

                for c in range(cont):
                    sqlModules = """ UPDATE mdl_course_modules 
                                SET availability = '{"op":"&","c":[{"type":"group","id": %s}],"showc":[false]}', visible = 1 
                                WHERE id = %s AND course = %s """
                    valModules = (disciplinasGrupos[c - 1]['id'], links, discModelo['id'])

                    sqlUrl = """ UPDATE mdl_url SET externalurl = %s,display = 5 WHERE id = %s AND course = %s """
                    externalurl = 'http://localhost/moodle/course/view.php?id='
                    valUrl = (disciplinasGrupos[c - 1]['id'], links, discModelo['id'])

                    links = resultado[c][0]
                    urlinstance = resultado[c][1]

                    try:
                        mySql = DbConnect().mysqlConnect()
                        mysql = mySql.cursor()

                        mysql.execute(sqlModules, valModules)
                        mysql.execute(sqlModules, valUrl)
                        mySql.commit()

                    except Exception as e:
                        print(e)

                    finally:
                        if(mySql.is_connected()):
                            mySql.close()













