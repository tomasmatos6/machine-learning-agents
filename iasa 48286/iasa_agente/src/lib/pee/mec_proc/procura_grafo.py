from pee.mec_proc.mecanismo_procura import MecanismoProcura

"""
    Classe abstrata ProcuraGrafo que representa um mecanismo de procura em grafo.
    Este tipo de procura mantém a informação dis nós já explorados, sendo assim é necessário implementar se memória.
    Visto que existe memória é possível optimizar os resultados e garantir que se existe uma solução, esta vai ser encontrada,
    sendo que é garantido que o agente não repete os mesmos erros, impedindo loops infinitos de exploração.
    
    Herda da classe MecanismoProcura.
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
        
        Aumenta a complexidade espacial se esta for maior que a anterior, sendo a complexidade
        espacial o número de nós memorizados.
    """
    def _memorizar(self, no):
        if(self._manter):
            self._explorados[no.estado] = no
            self._fronteira.insert(no)
            self.complexidade_espacial = max(len(self._explorados), self.complexidade_espacial)
        
    """
        Método protegido manter() que verifica se nó deve ser mantido para exploração.
    """
    def _manter(self, no):
        return no.estado not in self._explorados