import requests
from config.config import Config
from config.conexao import DbConnect

class CriaCategoria:
    def criacaoCat(self, categoriasAva):

        try:
            mssql = DbConnect().mssqlConnect()
            sql = """
                SELECT SCA.CODCAMPUS AS COD_POLO, SCA.DESCRICAO AS NOME_POLO, SCA.DESCRICAO + ' (' + SCA.CODCAMPUS + ')' AS NOME_PADRAO

                FROM SCAMPUS AS SCA (NOLOCK)

                WHERE SCA.ATIVO = 'S'
                AND SCA.DESCRICAO LIKE 'Polo %'
                AND SCA.DESCRICAO NOT LIKE '%INATIV%'

                ORDER BY SCA.DESCRICAO
                """
            mssql.execute(sql)
            resultado = mssql.fetchall()

            polosRM = []

            for COD_POLO, NOME_POLO, NOME_PADRAO in resultado:
                polosRM.append({'name': NOME_PADRAO, 'id': COD_POLO, 'descricao': NOME_POLO})

        except Exception as e:
            print(e)

        dadosRm = [{'name': 'Polo Itatiba', 'id': '01'},
                   {'name': 'Polo Jaguariuna', 'id': '02'},
                   {'name': 'Polo Itu', 'id': '03'},
                   {'name': 'Polo Bebedouro', 'id': '04'},
                   {'name': 'Polo Bambui', 'id': '05'}]

        config = Config()
        polos = []

        categoriasAvaIDN = []

        for nome in categoriasAva:
            categoriasAvaIDN.append(nome['idnumber'])

        for categoriaRm in polosRM:
            if categoriaRm['id'] not in categoriasAvaIDN:
                categories = {'categories[0][name]': categoriaRm['name'],
                              'categories[0][parent]': config.categoriaPolos,
                              'categories[0][idnumber]': categoriaRm['id'],
                              'categories[0][description]': categoriaRm['descricao']}

                serverurl = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                            config.categoriaToken + "&wsfunction=" + "core_course_create_categories" \
                            + "&moodlewsrestformat=" + config.formatoRest

                resp = requests.post(serverurl, categories)
                polo = resp.json()

                polos.append(polo[0]['name'])

        return polos

    def populaCatCmoodle(self, categoriasAva):

        for params in categoriasAva:
            try:
                msSql = DbConnect().mssqlConnect()
                mssql = msSql.cursor()

                sql = """ UPDATE polis_moodle_cmoodle2_temp SET CATEGORIA = %s WHERE CODCAMPUS = %s """
                var = (params['id'], params['idnumber'])

                mssql.execute(sql, var)
                msSql.commit()

            except Exception as e:
                print(e)

        categoriasUpdate = categoriasAva['name']

        return categoriasUpdate

    def getCategoriaAVA(self):
        config = Config()
        criteria = {'criteria[0][key]': 'parent', 'criteria[0][value]': config.categoriaPolos}

        serverurl = config.dominio + "/webservice/rest/server.php" + "?wstoken=" + \
                    config.categoriaToken + "&wsfunction=" + "core_course_get_categories" + "&moodlewsrestformat=" + config.formatoRest

        response = requests.post(serverurl, criteria)
        categoriasAva = response.json()

        return categoriasAva









