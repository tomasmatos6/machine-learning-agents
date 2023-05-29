from blocos.mod_prob.estado_pilha import EstadoPilha
from copy import deepcopy

class OperadorEmpilhar():
    def __init__(self, origem):
        self.__origem = origem
    
    def aplicar(self, estado):
        "Pilha onde vou colucar o meu bloco"
        novaPilha = deepcopy(estado.blocos)
        bloco = estado.blocos[self.__origem][0]
        novaPilha[0].insert(0, bloco)
        novaPilha[self.__origem].remove(bloco)
        return EstadoPilha(novaPilha)
        
    
    def custo(self, estado, estado_suc):
        return self.__origem
    
    def __repr(self):
        return "Empilhar(%s)" % self.__origem