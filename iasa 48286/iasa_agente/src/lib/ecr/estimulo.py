from abc import abstractmethod

"""
    Interface Estimulo 
    Define informação activadora de uma reação


    Permite obter um estímulo através de uma percepção no ambiente.
"""
class Estimulo():

    @abstractmethod
    def detectar(self, percepcao):
        """Detetar um estímulo numa percepção"""