from copy import deepcopy

from blocos.mod_prob.estado_pilha import EstadoPilha


class OperadorDesempilhar():
    """
        Classe OperadorDesempilhar que representa o operador que desempilha um bloco da pilha.
    """
    def __init__(self, destino):
        self.__destino = destino-1
        
    def aplicar(self, estado):
        """
            Método aplicar() que remove um bloco da primeira pilha para a pilha escolhida.
        """
        novaPilha = deepcopy(estado.pilhas)
        if len(estado.pilhas[0]) != 0:
            bloco = estado.pilhas[0][0]
            novaPilha[self.__destino].insert(0, bloco)
            novaPilha[0].remove(bloco)
        return EstadoPilha(novaPilha)
        
    def custo(self, estado, estado_suc):
        return self.__destino
    
    def __repr__(self):
        return "Desempilhar(%s)" % (self.__destino+1)