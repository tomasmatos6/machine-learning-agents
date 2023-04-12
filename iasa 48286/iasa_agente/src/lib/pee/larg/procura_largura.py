from pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO
from pee.mec_proc.procura_grafo import ProcuraGrafo

"""
    Classe ProcuraLargura que representa o mecanismo de procura em largura. Este implmenta uma estratégia em que seram explorados primeiro
    os nós mais antigos. É um mecanismo de procura similar à procura em grafos, onde é efetuada a travessia pela árvpre de nós, começa no nó
    inicial e explora primeiro os nós diretamente vizinhos, seguindo assim o resto da árvore fazendo uma procura exaustiva de cada nível.

    É utilizada uma fronteira FIFO.
"""
class ProcuraLargura(ProcuraGrafo):
    """
        Construtor da classe ProcuraLargura que chama o construtor da classe pai 
        com uma instância da classe FronteiraFIFO
    """
    def __init__(self):
        super().__init__(FronteiraFIFO())