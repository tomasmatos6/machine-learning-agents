from pee.mec_proc.fronteira.fronteira import Fronteira

"""
    Classe FronteiraFIFO que representa um tipo de fronteira.

    Implementa a estratégia de "first in first out", funcionando como uma fila, sendo assim os nós adicionados primeiro
    têm maior prioridade de saída. A inserção de nós na lista é feita no fim da mesma.
    Herda da classe Fronteira.
"""
class FronteiraFIFO(Fronteira):
    """
        Método inserir() que insere um nó no final da lista de nós.
    """
    def inserir(self, no):
        self._nos.append(no)