from pee.mec_proc.fronteira.fronteira_fifo import FronteiraFIFO
from pee.mec_proc.procura_grafo import ProcuraGrafo

"""
    Classe ProcuraLargura 
"""
class ProcuraLargura(ProcuraGrafo):
    """
        Construtor da classe ProcuraLargura que chama o construtor da classe pai 
        com uma instância da classe FronteiraFIFO
    """
    def __init__(self):
        super().__init__(FronteiraFIFO())