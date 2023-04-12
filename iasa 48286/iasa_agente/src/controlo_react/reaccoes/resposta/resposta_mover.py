<<<<<<< HEAD
from ecr.resposta import Resposta
from sae import Accao

"""
    Classe RespostaMover é uma extensão da classe Resposta que permite ao
    agente mover-se.

    Os movimentos do agente podem ser descritos por uma direção, assim cada instância desta
    classe está ligada a um elemento do enumerado Direccao, que representa os sentidos de
    movimento possíveis: Norte, Sul, Este e Oeste.
"""
class RespostaMover(Resposta):
    """
        Construtor da classe RespostaMover
        Este construtor chama o construtor da classe Resposta, enviando uma ação 
        baseada na direccao para onde se pertende o agente ir.
    """
    def __init__(self, direccao):
=======
from ecr.resposta import Resposta
from sae import Accao

"""
    Classe RespostaMover é uma extensão da classe Resposta que permite ao
    agente mover-se.

    Os movimentos do agente podem ser descritos por uma direção, assim cada instância desta
    classe está ligada a um elemento do enumerado Direccao, que representa os sentidos de
    movimento possíveis: Norte, Sul, Este e Oeste.
"""
class RespostaMover(Resposta):
    """
        Construtor da classe RespostaMover
        Este construtor chama o construtor da classe Resposta, enviando uma ação 
        baseada na direccao para onde se pertende o agente ir.
    """
    def __init__(self, direccao):
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
        super().__init__(Accao(direccao))