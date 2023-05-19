from plan.plano import Plano


class PlanoPee(Plano):
    def __init__(self, solucao):
        self.__solucao = solucao
        
    def obter_accao(self, estado):
        # Se calhar trocar por um for?
        if self.__solucao:
            passo = self.__solucao.remover()
            if passo.estado == estado:
                print(passo.operador)
                return passo.operador
    
    def mostrar(self, vista):
        vista.mostrar_solucao(self.__solucao)