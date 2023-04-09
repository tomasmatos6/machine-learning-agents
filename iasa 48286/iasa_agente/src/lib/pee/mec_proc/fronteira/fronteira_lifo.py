from pee.mec_proc.fronteira.fronteira import Fronteira

"""
    Classe FronteiraLIFO
"""
class FronteiraLIFO(Fronteira):
    """
        Método inserir() que insere um nó no inicio da lista de nós.
    """
    def inserir(self, no):
        self._nos.insert(0, no)