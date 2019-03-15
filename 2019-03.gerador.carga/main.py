from src.acao import Acao
import sys

'''
    Metodo Principal
'''
if __name__ == "__main__":
    if len(sys.argv) > 1:

        acao = Acao()
        paramAcao = sys.argv[1]

        if paramAcao == 'geracsvshortname':
            acao.geraShortname()

        else:
            print("Ação inválida!")

    else:
        print("Indique a ação que deseja executar.")
