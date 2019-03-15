import csv
import os

class GeradorCSV:

    def trataCSV(self):
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))

        with open(BASE_DIR + 'adi.csv', 'rb', newline='', encoding='utf_8_sig') as ficheiro:
            reader = csv.reader(ficheiro)

            for linha in reader:

                print(linha['CATEGORIA'])

   '''teste = trataCSV()
    print(teste)'''


