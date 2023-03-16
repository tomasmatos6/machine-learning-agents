from abc import abstractmethod

"""
    Interface Comportamento

    Esta classe permite modularizar o conjunto de reações.
"""
class Comportamento():
    
    @abstractmethod
    def activar(self, percepcao):
        """ Ativar um dado comportamento"""