<<<<<<< HEAD
from abc import abstractmethod

"""
    Interface Comportamento
    Um comportamento é um conjunto de reacções relacionadas entre si no sentido 
    de produzirem um resultado específico, por exemplo, evitar um obstáculo

    
    Esta classe permite modularizar o conjunto de reações.
"""
class Comportamento():
    
    @abstractmethod
    def activar(self, percepcao):
=======
from abc import abstractmethod

"""
    Interface Comportamento
    Um comportamento é um conjunto de reacções relacionadas entre si no sentido 
    de produzirem um resultado específico, por exemplo, evitar um obstáculo

    
    Esta classe permite modularizar o conjunto de reações.
"""
class Comportamento():
    
    @abstractmethod
    def activar(self, percepcao):
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
        """ Ativar um dado comportamento"""