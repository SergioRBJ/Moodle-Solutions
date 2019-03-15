from datetime import datetime
from src.gera_shortname import GeradorCSV

class Acao:

    def gerarCsvShortname(self):

        data = datetime.today()
        shortname = GeradorCSV.trataCSV()
