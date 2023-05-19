from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPee
from plan.planeador import Planeador
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.melhor_prim.procura_aa import ProcuraAA


class PlaneadorPee(Planeador):
    def __init__(self):
        self.__mecanismo = ProcuraAA()
        
    def planear(self, modelo_plan, objetivos):
        problema = ProblemaPlan(modelo_plan, objetivos[0])
        heuristica = HeurDist(objetivos[0])
        solucao = self.__mecanismo.procurar(problema, heuristica)
        return PlanoPee(solucao)
        