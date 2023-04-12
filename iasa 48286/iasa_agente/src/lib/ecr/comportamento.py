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
        """ Ativar um dado comportamento"""