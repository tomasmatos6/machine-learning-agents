from abc import ABC, abstractmethod


"""
    Classe Problema
"""
class Problema(ABC):
    """
        Construtor da classe Problema
    """
    def __init__(self, estado_inicial, operadores):
        
        self.estado_inicial = estado_inicial
        self.operadores = operadores

    """

    """
    @property
    def estado_inicial(self):
        return self.estado_inicial

    """

    """
    @property
    def operadores(self):
        return self.operadores

    """

    """
    @abstractmethod
    def objetivo(self, estado):
        raise NotImplementedError