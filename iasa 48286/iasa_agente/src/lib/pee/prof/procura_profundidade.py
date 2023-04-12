<<<<<<< HEAD
from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
    Classe ProcuraProfundidade que representa um mecanismo de procura em profundidade.
    Este algoritmo inicia no nó inicial e explora até ao fim cada ramo seguinte antes de voltar para o ramo anterior.
    Sendo que este método não garante que a solução encontrada seja a melhor.

    É utilizada uma fronteira LIFO.
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
=======
from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
    Classe ProcuraProfundidade que representa um mecanismo de procura em profundidade.
    Este algoritmo inicia no nó inicial e explora até ao fim cada ramo seguinte antes de voltar para o ramo anterior.
    Sendo que este método não garante que a solução encontrada seja a melhor.

    É utilizada uma fronteira LIFO.
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
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
        self._fronteira.inserir(no)