from src.criaCategoria import CriaCategoria
from src.duplicaDisciplina import Duplica
from datetime import datetime

class Acao:
    def categoriasCriadas(self):

        data = datetime.today()
        criaCat = CriaCategoria()
        categorias = criaCat.criacaoCat()

        if (len(categorias) > 0):

            print("##############################")
            print("Categorias Criadas")
            print("%s" % datetime.strftime(data, "%d/%m/%Y - %H:%M"))
            print("##############################")

            print(criaCat)



