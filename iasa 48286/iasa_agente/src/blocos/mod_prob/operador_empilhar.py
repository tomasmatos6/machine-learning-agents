from blocos.mod_prob.estado_pilha import EstadoPilha
from copy import deepcopy

class OperadorEmpilhar():
    """
        Classe OperadorEmpilhar que representa o operador que Empilha um bloco da pilha.
    """
    def __init__(self, origem):
        self.__origem = origem-1
    
    def aplicar(self, estado):
        """
            Método aplicar() que adiciona um bloco na primeira pilha da pilha escolhida.
        """
        novaPilha = deepcopy(estado.pilhas)
        if len(estado.pilhas[self.__origem]) != 0:
            bloco = estado.pilhas[self.__origem][0]
            novaPilha[0].insert(0, bloco)
            novaPilha[self.__origem].remove(bloco)
        return EstadoPilha(novaPilha)
        
    
    def custo(self, estado, estado_suc):
        return self.__origem
    
    def __repr__(self):
        return "Empilhar(%s)" % (self.__origem+1)