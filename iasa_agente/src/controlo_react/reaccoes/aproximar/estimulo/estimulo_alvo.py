from ecr.estimulo import Estimulo
from sae import Elemento

"""
    Classe EstimuloAlvo tem como objetivo detetar um alvo numa direção

    Esta classe implementa a classe Estimulo e recebe no construtor uma direção.
    Para detetar o alvo é utilizado o método detectar().
"""
class EstimuloAlvo(Estimulo):
    """
        Construtor da class EstimuloAlvo, recebe uma direccao que é um objeto do enumerado Direccao
        e um valor gama que representa uma redução exponencial do estímulo relativamente á distância.
    """
    def __init__(self, direccao, gama = 0.9):
        self.__direccao = direccao
        self.__gama = gama

    """
        Método detectar que através de uma percepcão do ambiente em que o agente se encontra, detetar
        a instensidade de uma caracteristica.

        É necessário aceder à percepção direcional para obter o elemento e a distancia sendo retornado 
        o valor de gama elevado à distância.
    """
    def detectar(self, percepcao):
        elem, dist, _ = percepcao.per_dir[self.__direccao]
        return self.__gama ** dist if(elem == Elemento.ALVO) else 0
