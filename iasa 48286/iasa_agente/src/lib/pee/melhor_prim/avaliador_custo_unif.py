from lib.pee.mec_proc.fronteira.avaliador import Avaliador

"""
    Classe AvaliadorCustoUnif representa um tipo de avaliador de prioridade de nós, sendo que
    neste caso, a funcao f(n) que decide a prioridade do nó será baseada no custo da solução.
    
    Implementa a interface Avaliador.
"""
class AvaliadorCustoUnif(Avaliador):
    
    """
        Método prioridade() que neste caso depende de uma estimativa do custo da solução através do
        nó, retornando assim esse valor.
    """
    def prioridade(self, no):
        return no.custo