from pee.mec_proc.fronteira.fronteira import Fronteira

"""
    Classe FronteiraFIFO
"""
class FronteiraFIFO(Fronteira):
    """
        Método inserir() que insere um nó no final da lista de nós.
    """
    def inserir(self, no):
        self._nos.append(no)