from src.criaCategoria import CriaCategoria
from src.duplicaDisciplina import Duplica
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







