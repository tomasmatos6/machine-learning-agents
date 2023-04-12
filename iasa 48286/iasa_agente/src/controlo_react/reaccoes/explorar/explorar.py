<<<<<<< HEAD
from random import choice
from ecr.comportamento import Comportamento
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

from sae import Direccao

"""
    Classe Explorar é um comportamento simples que tem como objetivo
    permitir movimentar o agente numa direção aleatória.

    Este comportamento faz parte de uma hierarquia de comportamentos:
        Objetivo: Recolher alvos.
        Sub-Objetivos: Aproximar do alvo, Evitar obstáculos, Explorar.

    Assim consegue-se observar que este é o sub-objetivo com menor prioridade.
    Sendo que este comportamento não tem de reagir a nada herda de Comportamento
    em vez de Reaccao.
"""
class Explorar(Comportamento):
    """
        Método que permite através da percepcao recebida obter a ação que deve ser realizada.
        É necessário obter um direção aleatória, onde depois esta é usada na criação de uma
        instância de RespostaMover e por fim retornando uma ação através do método activar
        da resposta.
    """
    def activar(self, percepcao):
        direcao = choice(list(Direccao))
        resposta = RespostaMover(direcao)
=======
from random import choice
from ecr.comportamento import Comportamento
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover

from sae import Direccao

"""
    Classe Explorar é um comportamento simples que tem como objetivo
    permitir movimentar o agente numa direção aleatória.

    Este comportamento faz parte de uma hierarquia de comportamentos:
        Objetivo: Recolher alvos.
        Sub-Objetivos: Aproximar do alvo, Evitar obstáculos, Explorar.

    Assim consegue-se observar que este é o sub-objetivo com menor prioridade.
    Sendo que este comportamento não tem de reagir a nada herda de Comportamento
    em vez de Reaccao.
"""
class Explorar(Comportamento):
    """
        Método que permite através da percepcao recebida obter a ação que deve ser realizada.
        É necessário obter um direção aleatória, onde depois esta é usada na criação de uma
        instância de RespostaMover e por fim retornando uma ação através do método activar
        da resposta.
    """
    def activar(self, percepcao):
        direcao = choice(list(Direccao))
        resposta = RespostaMover(direcao)
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
        return resposta.activar(percepcao)