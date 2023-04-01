from controlo_react.reaccoes.evitar.evitar_dir import EvitarDir
from controlo_react.reaccoes.evitar.resposta.resposta_evitar import RespostaEvitar
from ecr.hierarquia import Hierarquia
from sae.ambiente.direccao import Direccao

"""
    Classe EvitarObst que permite ao agente evitar obstáculos
"""
class EvitarObst(Hierarquia):
    """
        Construtor da classe EvitarObst
    """
    def __init__(self):
        self.__resposta = RespostaEvitar()
        super().__init__([EvitarDir(direccao, self.__resposta)
                          for direccao in Direccao])
        