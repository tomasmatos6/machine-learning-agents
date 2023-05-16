from deposito.mod_prob.problema_plan_deposito import ProblemaPlanDeposito

"""
    Classe Planeador onde é criado o problema e feita a procura da solução
"""
class Planeador():
    def __init__(self, mecanismo):
        self.__mecanismo = mecanismo
        
    def planear(self, vol_inicial, vol_final):
        problema = ProblemaPlanDeposito(vol_inicial, vol_final)
        solucao = self.__mecanismo.procurar(problema)
        print('Complexidade Temporal: ' + str(self.__mecanismo.complexidade_temporal))
        print('Complexidade Espacial: ' + str(self.__mecanismo.complexidade_espacial))
        return solucao