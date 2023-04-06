from abc import ABC, abstractmethod

"""
    Classe Fronteira que permite inserir e remover nós de forma ordenada, existe tamém
    a possibilidade de saber se esta se encontra vazia.
"""
class Fronteira(ABC):
    """
        Propriedade
    """
    @property
    def vazia(self):
        return len(self._nos == 0)
    
    """
        Construtor da classe Fronteira onde é chamado o método iniciar().
    """
    def __init__(self):
        self.iniciar()
    
    """
        Método iniciar() que cria um array de nós vazio.
    """
    def iniciar(self):
        self._nos = []
    
    
    @abstractmethod
    def inserir(no):
        """
            Insere um nó na fronteira, dependendo do tipo de fronteira será inserido
            de maneira diferente.
        """
        
    """
        Método remover() que remove o primeiro nó da fronteira, que representa o próximo a ser explorado
    """    
    def remover(self):
        return self._nos.pop(0)