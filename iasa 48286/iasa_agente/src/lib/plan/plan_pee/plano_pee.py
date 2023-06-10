from plan.plano import Plano


class PlanoPee(Plano):
    def __init__(self, solucao):
        self.__solucao = solucao
        
    def obter_accao(self, estado):
        # Se calhar trocar por um for?
        """
            if self.__solucao:
            passo = self.__solucao.remover()
            prox_no = self.__solucao[0]
            if passo.estado == estado:
                return prox_no.operador
        """
        if self.__solucao.dimensao > 1:
            if estado == self.__solucao[0].estado:
                operador = self.__solucao[1].operador
                self.__solucao.remover()
                return operador
    
    def mostrar(self, vista):
        vista.mostrar_solucao(self.__solucao)