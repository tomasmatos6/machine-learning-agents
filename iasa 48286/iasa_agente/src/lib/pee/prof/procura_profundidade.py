from abc import abstractproperty
from pee.mec_proc.fronteira.fronteira_lifo import FronteiraLIFO
from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
    Classe ProcuraProfundidade que representa um mecanismo de procura em profundidade.
    Este algoritmo inicia no nó inicial e explora até ao fim cada ramo seguinte antes de voltar para o ramo anterior.
    Sendo que este método não garante que a solução encontrada seja a melhor, ou que encontre um solução sequer.

    É utilizada uma fronteira LIFO.
    Herda da classe MecanismoProcura.
"""
class ProcuraProfundidade(MecanismoProcura):
    @property
    def complexidade_espacial(self):
        return self.__complexidade_espacial
    """
        Construtor da classe ProcuraLargura que chama o construtor da classe pai 
        com uma instância da classe FronteiraLIFO.
    """
    def __init__(self):
        super().__init__(FronteiraLIFO())
        self.__complexidade_espacial = 0;
        
    """
        Método protegido memorizar() que memoriza um nó de acordo com o tipo de procura, 
        concretiza o método abstracto do mecanismo de procura.
        
        Aumenta a complexidade espacial se esta for maior que a anterior, sendo a complexidade
        espacial o número de nós memorizados.
    """
    def _memorizar(self, no):
        self._fronteira.inserir(no)
        #self.complexidade_espacial = max(len(self._fronteira._nos), self.complexidade_espacial)
        
        if self._fronteira.dimensao > self.complexidade_espacial:
            self.__complexidade_espacial = self._fronteira.dimensao
    