from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan


class ModeloPDMPlan(ModeloPlan, ModeloPDM):
    """
        Classe ModeloPDMPlan que representa o plano do processo de decisão de markov,
        esta classe implementa a classe ModeloPlan e ModeloPDM.
    """
    def __init__(self, modelo_plan, objetivos, rmax = 1000.0):
        self.__modelo_plan = modelo_plan
        self.__rmax = rmax
        self.__objetivos = objetivos
        self.__transicoes = {}
        for s in self.S():
            for a in self.A(s):
                # Modelo determinista retorna apenas 1 estado sucessor
                sn = a.aplicar(s)
                if sn:
                    self.__transicoes[(s, a)] = sn
        
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
    
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()
    
    def S(self):
        return self.obter_estados()
    
    def A(self, s):
        return self.obter_operadores()
    
    def T(self, s, a, sn):
        sn_trans = self.__transicoes.get((s, a))
        return 1.0 if sn == sn_trans else 0.0
        
    def R(self, s, a, sn):
        r = -a.custo(s, sn)
        if sn in self.__objetivos:
            r += self.__rmax
        return r
    
    def Sucessores(self, s, a):
        """
            Método Sucessores que retorna o estado seguinte depois de aplicar a ação 'a' ao estado 's'.
        """
        sn = self.__transicoes.get((s, a))
        ret = []
        if sn:
            ret = [sn]
        return ret
    