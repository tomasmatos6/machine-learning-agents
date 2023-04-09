from controlo_react.reaccoes.aproximar.estimulo.estimulo_alvo import EstimuloAlvo
from ecr.reaccao import Reaccao
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

"""
    Classe AproximarDir que representa a deteção e aproximação de um alvo numa certa
    direção. Para simplificação da complexidade do projeto são criados comportamentos
    de aproximar para cada direção, ou seja, 4 instâncias. Sendo que a prioridade de
    cada uma dessas instância é dada pela distância do alvo.
"""
class AproximarDir(Reaccao):
    """
        Construtor da classe AproximarDir que chama o construtor da classe pai Reaccao,
        que recebe um Estimulo e uma Resposta.
    """
    def __init__(self, direccao):
        super().__init__(EstimuloAlvo(direccao), RespostaMover(direccao))
