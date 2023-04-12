<<<<<<< HEAD
from abc import ABC, abstractmethod


"""
    Interface Operador que representa uma transição entre estados, quando for
    aplicado um operador a um estado é criado outro estado.
"""
class Operador(ABC):
    
    @abstractmethod
    def aplicar(self, estado):
        """
            Método aplicar() que permite aplicar o operador a um estado para criar 
            um novo estado.
        """
    
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        """
            Método custo() que permite avaliar o custo da transição entre dois estados.
=======
from abc import ABC, abstractmethod


"""
    Interface Operador que representa uma transição entre estados, quando for
    aplicado um operador a um estado é criado outro estado.
"""
class Operador(ABC):
    
    @abstractmethod
    def aplicar(self, estado):
        """
            Método aplicar() que permite aplicar o operador a um estado para criar 
            um novo estado.
        """
    
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        """
            Método custo() que permite avaliar o custo da transição entre dois estados.
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
        """