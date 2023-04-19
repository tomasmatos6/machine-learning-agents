from ..mec_proc.fronteira.fronteira_prioridade import FronteiraPrioridade
from ..mec_proc.procura_grafo import ProcuraGrafo

"""
    Classe abstrata ProcuraMelhorPrim que representa um mecanismo de procura em que
        o critério de procura é feito através de uma função f, que devolve a prioridade dos nós.
        Esta avaliação é feita através de uma instância da classe Avaliador, que diz qual é o 
        critério para o "melhor" nó.
        
        Herda da classe ProcuraGrafo
"""
class ProcuraMelhorPrim(ProcuraGrafo):
    """
        Construtor da classe ProcuraMelhorPrim onde é inicializada a fronteira e criada a 
        instância da classe Avaliador.
    """
    def __init__(self, avaliador):
        super().__init__(FronteiraPrioridade())
        self._avaliador = avaliador
        
    """
        Método protegido manter() que verifica se o nó deve ou não ser mantido em memória.
        O nó será mantido se este não fizer parte dos explorados ou se o seu custo for menor
        que o custo do no anteriormente guardado.
    """
    def _manter(self, no):
        return super()._manter(no) or no < self._explorados[no.estado]