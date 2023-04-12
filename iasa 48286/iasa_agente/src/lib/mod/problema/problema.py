<<<<<<< HEAD
from abc import ABC, abstractmethod


"""
    Classe Problema que representa um problema que deve ser solucionado pelo agente.

    Um problema pode ser modelado da seguinte forma:
        Estado, referencia à classe Estado:
            - Representa uma situação na resolução de um problema.
            - Identifcação única.

        Operador, referencia à classe Operador:
            - Representa uma ação, ou seja uma transição de estado.
"""
class Problema(ABC):
    """
        Atributos read-only:
        Pode ser visto como getters para as propriedades privadas.
    """
    @property
    def estado_inicial(self):
        return self.estado_inicial
    
    @property
    def operadores(self):
        return self.operadores
    
    """
        Construtor da classe Problema, onde é guardado o estado inicial e a lista de operadores.
    """
    def __init__(self, estado_inicial, operadores):
        
        self.estado_inicial = estado_inicial
        self.operadores = operadores

    @abstractmethod
    def objetivo(self, estado):
=======
from abc import ABC, abstractmethod


"""
    Classe Problema que representa um problema que deve ser solucionado pelo agente.

    Um problema pode ser modelado da seguinte forma:
        Estado, referencia à classe Estado:
            - Representa uma situação na resolução de um problema.
            - Identifcação única.

        Operador, referencia à classe Operador:
            - Representa uma ação, ou seja uma transição de estado.
"""
class Problema(ABC):
    """
        Atributos read-only:
        Pode ser visto como getters para as propriedades privadas.
    """
    @property
    def estado_inicial(self):
        return self.estado_inicial
    
    @property
    def operadores(self):
        return self.operadores
    
    """
        Construtor da classe Problema, onde é guardado o estado inicial e a lista de operadores.
    """
    def __init__(self, estado_inicial, operadores):
        
        self.estado_inicial = estado_inicial
        self.operadores = operadores

    @abstractmethod
    def objetivo(self, estado):
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
        "Método abstrato que retorna se o estado é objetivo."