from sae import Elemento


class MecDelib():
    """
        Classe MecDelib que representa o mecanismo de deliberação do agente
    """
    def __init__(self, modelo_mundo):
        """
        Construtor da class MecDelib que guarda o modelo mundo.
        """
        self.__modelo_mundo = modelo_mundo

    
    def deliberar(self):
        """
            Método deliberar() que tem como objetivo gerar os objetivos do agente, que podem
            ser dados como uma lista de estados que se pretendem atingir.
        """
        "retornar uma lista de objetivos ordenada pela distancia ao agente"
        objetivos = [estado for estado in self.__modelo_mundo.obter_estados() 
                     if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]
        if objetivos:
            objetivos.sort(key=self.__modelo_mundo.distancia)
            return objetivos

    