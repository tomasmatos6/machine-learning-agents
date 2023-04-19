from abc import ABC, abstractmethod

"""
    Interface Avaliador que define a avaliação da prioridade do nós.
    Possui apenas um método para a avaliação da prioridade de um nó.
"""
class Avaliador(ABC):
    
    @abstractmethod
    def prioridade(no):
        "Retorna a prioridade de um nó, ou seja o valor de f(n)"