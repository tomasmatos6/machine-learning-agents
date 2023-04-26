from lib.pee.mec_proc.no import No
from .fronteira import Fronteira
from heapq import heappush, heappop

"""
    Classe FronteiraPrioridade que server para a procura por melhor primeiro
    A inserção de nós na lista é feita tendo em conta a prioridade de cada nó, para
    isto é utilizada a biblioteca heapq do python, que organiza automáticamente os
    valores por ordem crescente.
    
    Herda de Fronteira
"""
class FronteiraPrioridade(Fronteira):
    """
        Construtor da classe FronteiraPrioridade onde é chamada o construtor da classe pai e
        é guardado uma instância da classe Avaliador que permite avaliar a prioridade dos nos
    """
    def __init__(self, avaliador):
        super().__init__()
        self._avaliador = avaliador
        
    """
        Método inserir() onde é inserido um nó baseado na prioridade desse nó, sendo assim são 
        inseridos tuplos quem tem (prioridade, no), em vez de ser só um nó.
        
    """
    def inserir(self, no):
        prioridade = self._avaliador.prioridade(no)
        heappush(self._nos, (prioridade, no))
        
    """
        Método remover() onde é removido um tuplo que tem (prioridade, no), mas retornado apenas 
        o valor no.
    """
    def remover(self):
        _, no = heappop(self._nos)
        return no