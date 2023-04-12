<<<<<<< HEAD
from abc import abstractmethod

"""
    Interface Estimulo 
    Define informação activadora de uma reação


    Permite obter um estímulo através de uma percepção no ambiente.
"""
class Estimulo():

    @abstractmethod
    def detectar(self, percepcao):
=======
from abc import abstractmethod

"""
    Interface Estimulo 
    Define informação activadora de uma reação


    Permite obter um estímulo através de uma percepção no ambiente.
"""
class Estimulo():

    @abstractmethod
    def detectar(self, percepcao):
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
        """Detetar um estímulo numa percepção"""