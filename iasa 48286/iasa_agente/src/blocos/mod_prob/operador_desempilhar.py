from copy import deepcopy

from blocos.mod_prob.estado_pilha import EstadoPilha

class OperadorDesempilhar():
    def __init__(self, destino):
        self.__destino = destino
        
    def aplicar(self, estado):
        novaPilha = deepcopy(estado.blocos)
        bloco = estado.blocos[0][0]
        novaPilha[self.__destino].insert(0, bloco)
        novaPilha[0].remove(bloco)
        return EstadoPilha(novaPilha)
        
    def custo(self):
        return self.__destino
    
    def __repr(self):
        return "Desempilhar(%s)" % self.__destino