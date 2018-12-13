class Config:
    def __init__(self):

        ''' Configurações Gerais '''

        self.formatoRest = 'json'
        self.dominio = ''
        self.categoriaSemestre = ''
        self.categoriaPolos = ''
        self.categoriaMatrizesEsp = ''
        self.categoriaUnija = ''

        ''' Configuração das credenciais do método de criação de categorias '''

        self.categoriaToken = ''

        ''' Configuração das credenciais do método de duplicação de disciplinas '''

        self.duplicaToken = ''

        ''' Configuração das credenciais do método de alteração de links '''

        self.altLinkToken = ''

        ''' Configuração das credenciais do método alocação de grupos para alunos '''

        self.alocaGrupoToken = ''
