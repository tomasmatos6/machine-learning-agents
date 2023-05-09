from deposito.mod_prob.problema_plan_traj import ProblemaPlanTraj


class Planeador():
    def __init__(self, mecanismo):
        self.__mecanismo = mecanismo
        
    def planear(self, ligacoes, vol_inicial, vol_final):
        problema = ProblemaPlanTraj(ligacoes, vol_inicial, vol_final)
        solucao = self.__mecanismo.procurar(problema)
        print('Complexidade Temporal: ' + str(self.__mecanismo.complexidade_temporal))
        print('Complexidade Espacial: ' + str(self.__mecanismo.complexidade_espacial))
        return solucao