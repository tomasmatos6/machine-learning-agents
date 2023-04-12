from controlo_react.reaccoes.aproximar.aproximar_dir import AproximarDir
from ecr.prioridade import Prioridade
from sae import Direccao

"""
    Classe AproximarAlvo que permite ao agente aproximar-se de um alvo.

    Para simplificação da complexidade do projeto são criados comportamentos
    de aproximar para cada direção, ou seja, 4 instâncias. Sendo que a prioridade de
    cada uma dessas instância é dada pela distância do alvo.
    Este comportamento trate-se de um comportamentos composto, recebendo as instâncias
    de AproximarDir. O método de seleção para este comportamentos é o mecanismo de prioridade,
    assim sendo esta classe tem que herdar da classe Prioridade.
"""
class AproximarAlvo(Prioridade):
    """
        Construtor da classe AproximarAlvo que utiliza o construtor da classe pai, para criar uma
        lista com as 4 instâncias de AproximarDir, cada uma representando uma direção.
    """
    def __init__(self):
        super().__init__([AproximarDir(Direccao.ESTE),
                          AproximarDir(Direccao.OESTE),
                          AproximarDir(Direccao.NORTE),
                          AproximarDir(Direccao.SUL)])

