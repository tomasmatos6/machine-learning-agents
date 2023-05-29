from blocos.mod_prob.heur_blocos import HeurBlocos
from blocos.mod_prob.problema_plan_blocos import ProblemaPlanBlocos
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif


class Planeador():
    def __init__(self):
        self.__mecanismo = ProcuraCustoUnif()

    def planear(self, seq_inicial, seq_final):
        problema = ProblemaPlanBlocos(seq_inicial, seq_final)
        heuristica = HeurBlocos(seq_final)
        solucao = self.__mecanismo.procurar(problema)
        print('Complexidade Temporal: ' + str(self.__mecanismo.complexidade_temporal))
        print('Complexidade Espacial: ' + str(self.__mecanismo.complexidade_espacial))
        return solucao