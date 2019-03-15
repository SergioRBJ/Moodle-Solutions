import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

with open(BASE_DIR + '/arquive/adi.csv', 'rt', encoding='utf_8_sig') as ficheiro:
    reader = csv.DictReader(ficheiro)

    for linha in reader:
        print(linha[])
