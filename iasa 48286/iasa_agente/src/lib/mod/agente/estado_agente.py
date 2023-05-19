from lib.mod.estado import Estado

"""
    Classe EstadoAgente que herda de estado e representa o estado do agente, que pode ser visto
    como a sua posição.
"""
class EstadoAgente(Estado):
    @property
    def posicao(self):
        return self.__posicao
    
    """
        Construtor da classe EstadoAgente onde é guardado o valor da posicao e criado o valor
        para o id_valor, que é o valor de identificação.
    """
    def __init__(self, posicao):
        self.__posicao = posicao
        self.__id_valor = hash(self.__posicao)
        ""

    """
        Método id_valor() que retorna a variavel id_valor.
    """
    def id_valor(self):
        return self.__id_valor