from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
    Classe ProcuraProfundidade
"""
class ProcuraProfundidade(MecanismoProcura):
    """
        Construtor da classe ProcuraLargura que chama o construtor da classe pai 
        com uma instância da classe FronteiraLIFO.
    """
    def __init__(self):
        super().__init__(FronteiraLIFO())
        
    """
        Método protegido memorizar() que memoriza um nó de acordo com o tipo de procura, 
        concretiza o método abstracto do mecanismo de procura.
    """
    def _memorizar(self, no):
        self._fronteira.inserir(no)