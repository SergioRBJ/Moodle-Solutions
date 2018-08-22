class Config:
    def __init__(self):

        ''' Configurações Gerais '''

        self.formatoRest = 'json'
        self.dominio = 'http://localhost/moodle'

        ''' Configuração das credenciais do método de criação de categorias '''

        self.categoriaToken = ''
        self.categoriaSemestre = ''

        ''' Configuração das credenciais do método de duplicação de disciplinas '''

        self.duplicaToken = ''
