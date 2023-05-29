from blocos.mod_prob.estado_pilha import EstadoPilha
from blocos.mod_prob.operador_desempilhar import OperadorDesempilhar
from blocos.mod_prob.operador_empilhar import OperadorEmpilhar
from mod.problema.problema import Problema

class ProblemaPlanBlocos(Problema):
    def __init__(self, seq_inicial, seq_final):
        super().__init__(EstadoPilha(seq_inicial),
                       [OperadorEmpilhar(2),
                        OperadorEmpilhar(3),
                        OperadorDesempilhar(2),
                        OperadorDesempilhar(3)])
        self.__seq_final = seq_final
        
    def objetivo(self, estado):
        return estado.pilhas[0] == self.__seq_final[0]