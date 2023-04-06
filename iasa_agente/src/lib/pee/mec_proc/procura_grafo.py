from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
    Classe ProcuraGrafo
"""
class ProcuraGrafo(MecanismoProcura):
    """
        Método protegido iniciar_memoria() que inicia a memória incluindo memória de nós explorados.
    """
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {}
        
    """
        Método protegido memorizar() que memoriza um nó de acordo com o tipo de procura, concretiza 
        o método abstracto do mecanismo de procura
    """
    def _memorizar(self, no):
        if(self._manter):
            self._explorados[no.estado] = no
            self._fronteira.insert(no)
        
    """
        Método protegido manter() que verifica se nó deve ser mantido para exploração.
    """
    def _manter(self, no):
        return no.estado not in self._explorados