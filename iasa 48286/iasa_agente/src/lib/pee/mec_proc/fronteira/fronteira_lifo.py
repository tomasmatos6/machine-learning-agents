from pee.mec_proc.fronteira.fronteira import Fronteira

"""
    Classe FronteiraLIFO que representa um tipo de fronteira.

    Implementa a estratégia de "last in first out", funcionando como uma pilha ou stack, sendo assim os nós adicionados 
    em último têm maior prioridade de saída. A inserção de nós na lista é feita no ínicio da mesma.
    Herda da classe Fronteira.
"""
class FronteiraLIFO(Fronteira):
    """
        Método inserir() que insere um nó no inicio da lista de nós.
    """
    def inserir(self, no):
        self._nos.insert(0, no)