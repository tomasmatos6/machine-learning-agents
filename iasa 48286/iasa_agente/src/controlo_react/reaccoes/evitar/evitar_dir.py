
from controlo_react.reaccoes.evitar.estimulo.estimulo_obst import EstimuloObst
from ecr.reaccao import Reaccao

"""
    Classe EvitarDir é um comportamento que quando deteta um obstáculo numa determinada direção,
    realiza um movimento noutra direção que não tenha obstáculo.
    
    De forma a simplificar a complexidade do código são criados comportamentos evitar para cada direção,
    ou seja 4 instâncias. Esta classe herda da classe Reaccao.
"""
class EvitarDir(Reaccao):
    """
        Construtor da classe EvitarDir que chama o método da classe pai Reaccao, que recebe um Estimulo e
        uma Resposta. É importante para o estímulo que este trate da deteção de obstáculos na direção atual,
        para isso instância-se um objeto da classe EstimuloObst.
    """
    def __init__(self, direccao, resposta):
        super().__init__(EstimuloObst(direccao), resposta)