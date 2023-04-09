from abc import ABC, abstractmethod


"""
    Interface Operador que representa uma transição entre estados, quando for
    aplicado um operador a um estado é criado outro estado.
"""
class Operador(ABC):
    """
        Método aplicar() que permite aplicar o operador a um estado para criar 
        um novo estado.
    """
    @abstractmethod
    def aplicar(self, estado):
        raise NotImplementedError
    
    """
        Método custo() que permite avaliar o custo da transição entre dois estados.
    """
    @abstractmethod
    def custo(self, estado, estado_suc):
        raise NotImplementedError