import mysql.connector

'''
    Conexão com o banco de dados
'''
class DbConnect():

    def mysqlConnect(self):
        server = ''
        database = ''
        username = ''
        password = ''

        config = {
            'host': server,
            'database': database,
            'user': username,
            'password': password
        }

        try:
            conn = mysql.connector.connect(**config)

        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            return conn