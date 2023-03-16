from abc import abstractmethod
from ecr.comportamento import Comportamento

"""
    Classe ComportComp que representa um comportamento composto por
    1 ou mais comportamentos.
"""
class ComportComp(Comportamento):
    """
        Construtor da classe que recebe uma lista de comportamentos.

        @param comportamentos
    """
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos
    
    """
        Método que ativa um comportamento baseado na percepcao recebida.

        @param percepcao
    """
    def activar(self, percepcao):
        raise NotImplementedError

    @abstractmethod
    def selecionar_accao(self, accoes):
        """
        Método que vai permitir selecionar uma ação que depende do mecanismo 
        de reação escolhido 
        """