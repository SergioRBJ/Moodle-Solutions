from src.criaCategoria import CriaCategoria
from src.duplicaDisciplina import Duplica
from src.alocaGrupo import Grupo
from datetime import datetime

class Acao:
    def categoriasCriadas(self):

        data = datetime.today()
        criaCat = CriaCategoria()
        categorias = criaCat.criacaoCat()
        updateRM = criaCat.populaCatCmoodle()

        if (len(categorias) > 0):

            print("##############################")
            print("Categorias Criadas")
            print("%s" % datetime.strftime(data, "%d/%m/%Y - %H:%M"))
            print("##############################")

            for nomePolos in categorias:
                print(nomePolos)

        else:
            print("Nenhuma categoria de polo criada!")

        if (len(updateRM) > 0):

            print("##############################")
            print("IDs populados na cmoodle2")
            print("##############################")

            for idCat in updateRM:
                print(idCat)

        else:
            print("Nenhum ID alterado na cmoodle 2!")

    def disciplinasImportadas(self):

        data = datetime.today()
        duplicaDisc = Duplica()
        disciplinas = duplicaDisc.duplicaDisc()

        if (len(disciplinas) > 0):

            print("##############################")
            print("Disciplinas Importadas")
            print("%s" % datetime.strftime(data, "%d/%m/%Y - %H:%M"))
            print("##############################")

            for disciplina in disciplinas:
                print(disciplina)

        else:
            print("Nenhuma disciplina importada!")

    def alunosAlocados(self):

        data = datetime.today()
        alocaAluno = Grupo()
        alunos = alocaAluno.alocaGrupo()

        if (len(alunos) > 0):

            print("##################################")
            print("Alunos Alocados em Grupos")
            print("%s" % datetime.strftime(data, "%d/%m/%Y - %H:%M"))
            print("##################################")

            for aluno in alunos:
                print(aluno[0]['nome'] + ' - ' + aluno[0]['grupo'] + ' - ', aluno[0]['disciplina'])

        else:
            print("Nenhum Aluno Alocado!")








