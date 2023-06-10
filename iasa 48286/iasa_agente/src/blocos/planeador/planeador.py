from blocos.mod_prob.heur_blocos import HeurBlocos
from blocos.mod_prob.problema_plan_blocos import ProblemaPlanBlocos
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif


class Planeador():
    """
        Classe Planeador que serve para planear o nosso problema.
    """
    def __init__(self, mecanismo = ProcuraCustoUnif()):
        self.__mecanismo = mecanismo

    def planear(self, seq_inicial, seq_final):
        problema = ProblemaPlanBlocos(seq_inicial, seq_final)
        if(self.__mecanismo.__class__ == ProcuraAA):
            heuristica = HeurBlocos(seq_final)
            solucao = self.__mecanismo.procurar(problema, heuristica)
        else:
            solucao = self.__mecanismo.procurar(problema)
        print('Complexidade Temporal: ' + str(self.__mecanismo.complexidade_temporal))
        print('Complexidade Espacial: ' + str(self.__mecanismo.complexidade_espacial))
        return solucao