from controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from controlo_react.reaccoes.evitar.resposta.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

"""
    Classe EvitarObst que representa um comportamento que permite ao agente evitar obstáculos, sendo estes as paredes do jogo.
    A colisão pode ser o agente estar em contacto com a parede ou tentar mover-se em contra a parede, sendo assim, o objetivo
    é que durante as exploração, o agente não colida com os obstáculos.
"""
class EvitarObst(Hierarquia):
    """
        Construtor da classe EvitarObst onde é criada a resposta apartir da classe RespostaEvitar() e depois, utilizando essa resposta
        são criadas 4 instâncias de EvitarDir(), uma para cada direção.
    """
    def __init__(self):
        self.__resposta = RespostaEvitar()
        super().__init__([EvitarDir(direccao, self.__resposta)
                          for direccao in Direccao])
        