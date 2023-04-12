from abc import ABC, abstractmethod

"""
    Classe abstrata Fronteira que permite inserir e remover nós de forma ordenada, existe também a possibilidade de saber 
    se esta se encontra vazia. Um mecanismo de procura pode terminar o seu funcionamento quando chegar ao objetivo ou tiver
    explorado toda a sua fronteira.

    Esta classe guarda uma lista de nós ainda não explorados durante a procura. Os nós são inseridos de maneira diferente,
    dependendo do tipo de fronteira, podendo ser do tipo FIFO(first in first out) ou LIFO(last in first out).
"""
class Fronteira(ABC):
    """
        Atributos read-only:
        Pode ser visto como getters para as propriedades privadas.
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