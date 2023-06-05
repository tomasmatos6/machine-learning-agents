from pdm.pdm import PDM
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador


class PlaneadorPDM(Planeador):
    """
        Classe PlaneadorPDM que tem como função para criar um plano.
    """
    def __init__(self, gama = 0.85, delta_max = 1):
        self.__gama = gama
        self.__delta_max = delta_max
    
    def planear(self, modelo_plan, objectivos):
        """
            Método planear() que cria um modelo através do modelo_plan e dos objetivos recebidos,
            através da utilidade e politica recebida de PDM é criado um Plano.
        """
        modelo = ModeloPDMPlan(modelo_plan, objectivos)
        pdm = PDM(modelo, self.__gama, self.__delta_max)
        U, pol = pdm.resolver()
        return PlanoPDM(U, pol)