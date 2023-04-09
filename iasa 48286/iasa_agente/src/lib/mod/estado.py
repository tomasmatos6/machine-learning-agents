from abc import ABC, abstractmethod


"""
    Classe Estado que representa uma situação (configuração) na 
    resolução de um problema. Apresenta uma identificação única.
"""
class Estado(ABC):
    """
        Método abstrato id_valor() que define identificação única do estado 
        em função da sua informação (valor de estado).
    """
    @abstractmethod
    def id_valor(self):
        raise NotImplementedError
    
    """
        Método hash() que define identificação única de um objecto.
    """
    def __hash__(self):
        return self.id_valor()
    
    """
        Método eq() que define relação de igualdade consistente com definição de identificação.
    """
    def __eq__(self, other):
        return self.__hash__() == other.__hash__()
        
        
