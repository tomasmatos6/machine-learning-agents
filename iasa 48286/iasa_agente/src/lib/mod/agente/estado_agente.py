from lib.mod.estado import Estado

"""

"""
class EstadoAgente(Estado):
    @property
    def posicao(self):
        return self.__posicao
    
    """
    
    """
    def __init__(self, posicao):
        self.__posicao = posicao
        self.__id_valor = hash(self.__posicao)
        ""

    """
    
    """
    def id_valor(self):
        return self.__id_valor