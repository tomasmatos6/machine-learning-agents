from controlo_react.reaccoes.evitar.evitar_obst import EvitarObst
from ecr.hierarquia import Hierarquia
from controlo_react.reaccoes.aproximar.aproximar_alvo import AproximarAlvo
from controlo_react.reaccoes.explorar.explorar import Explorar

"""
    Classe Recolher que tem instâncias das classes AproximarAlvo, EvitarObst e Explorar.
    Esta classe herda da classe Hierarquia, sendo este o mecanismo de seleção usado para escolher
    o comportamento que deve ser executado
"""
class Recolher(Hierarquia):
    """
        Construtor da classe Recolher que utiliza o construtor da classe pai Hierarquia, criando uma lista
        com as 3 instâncias dos comportamentos necessários para o comportamento do agente
    """
    def __init__(self):
        super().__init__([AproximarAlvo(),EvitarObst(),Explorar()])