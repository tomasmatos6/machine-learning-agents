<<<<<<< HEAD
from ecr.comport_comp import ComportComp

"""
    Classe hierarquia que permite a seleção de uma ação de mode hierarquico,
    "Os comportamentos estão organizados numa hierarquia fixa de subsunção."
"""
class Hierarquia(ComportComp):

    """
        Método que permite selecionar uma ação através de um modo de hierarquia,
        este método recebe uma lista de ações e retorna a ação a ser executada.
        É retornado o primeiro elemento da lista por este ser o de maior prioridade.

        @param lista de ações que podem ser escolhidas
        @return ação selecionada
    """
    def selecionar_accao(self, accoes):
        if(accoes):
=======
from ecr.comport_comp import ComportComp

"""
    Classe hierarquia que permite a seleção de uma ação de mode hierarquico,
    "Os comportamentos estão organizados numa hierarquia fixa de subsunção."
"""
class Hierarquia(ComportComp):

    """
        Método que permite selecionar uma ação através de um modo de hierarquia,
        este método recebe uma lista de ações e retorna a ação a ser executada.
        É retornado o primeiro elemento da lista por este ser o de maior prioridade.

        @param lista de ações que podem ser escolhidas
        @return ação selecionada
    """
    def selecionar_accao(self, accoes):
        if(accoes):
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
            return accoes[0]