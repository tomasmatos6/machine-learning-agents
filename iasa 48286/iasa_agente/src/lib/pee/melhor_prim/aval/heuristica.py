from abc import ABC, abstractmethod

"""
    Classe Heuristica 
"""
class Heuristica(ABC):
    """
        O método h() implementa a função heurística e representa uma estimativa do custo do percurso 
        desde o nó n até ao nó objetivo.
    """
    @abstractmethod
    def h(self, estado):
        """"""