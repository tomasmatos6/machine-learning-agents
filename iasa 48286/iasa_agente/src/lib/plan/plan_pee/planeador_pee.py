from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.heur_manh import HeurManh
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPee
from plan.planeador import Planeador
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
from pee.melhor_prim.procura_aa import ProcuraAA


class PlaneadorPee(Planeador):
    def __init__(self):
        self.__mecanismo = ProcuraAA()
        self.__heuristica = HeurDist
        
    def planear(self, modelo_plan, objetivos):
        problema = ProblemaPlan(modelo_plan, objetivos[0])
        heuristica = self.__heuristica(objetivos[0])
        solucao = self.__mecanismo.procurar(problema, heuristica)
        self.__mostrar_heuristica()
        return PlanoPee(solucao)
        
    def definir_heuristica(self, heur):
        if heur == "Manh":
            self.__heuristica = HeurManh
        elif heur == "Dist":
            self.__heuristica = HeurDist
            
    def __mostrar_heuristica(self):
        if self.__heuristica == HeurManh:
            print("Heurística: Distância de Manhattan")
        elif self.__heuristica == HeurDist:
            print("Heurística: Distância Euclidiana")
        print("Complexidade temporal: ",self.__mecanismo.complexidade_temporal)
        print("Complexidade espacial: ",self.__mecanismo.complexidade_espacial)
        print()