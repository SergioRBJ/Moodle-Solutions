class Disciplina:

    '''
    Get and Set
    '''

    def getCategoria(self):
        return self._categoria

    def setCategoria(self, categoria):
        self._categoria = categoria

    categoria = property(
        fget=getCategoria(),
        fset=setCategoria()
    )

    def getModalidade(self):
        return self._modalidade

    def setModalidade(self, modalidade):
        self._modalidade = modalidade

    modalidade = property(
        fget=getModalidade(),
        fset=setModalidade()
    )

    def getSiglaDisc(self):
        return self._siglaDisc

    def setSiglaDisc(self, siglaDisc):
        self._siglaDisc = siglaDisc

    siglaDisc = property(
        fget=getSiglaDisc(),
        fset=setSiglaDisc()
    )