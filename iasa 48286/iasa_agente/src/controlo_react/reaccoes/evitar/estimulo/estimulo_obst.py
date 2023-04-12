from ecr.estimulo import Estimulo

"""
    Classe EstimuloObst que tem como objetivo detetar o contacto com obstáculos em cada direção.
    Implementa a Interface Estimulo e recebe no construtor uma direção aonde vai detetar os obstáculos, 
    esta deteção é feita através do método detectar() que recebe uma percepcao.
"""
class EstimuloObst(Estimulo):
    """
        Construtor da classe EstimuloObst recebe um objeto do enumerado Direccao, direccao, e uma intensidade,
        com valor por omissão de 1.0
    """
    def __init__(self, direccao, intensidade=1.0):
        self.__direccao = direccao
        self.__intensidade = intensidade

        """
            Método detectar onde se existir contacto com o obstáculo retorna a intensidade, senão retorna 0.
        """
    def detectar(self, percepcao):
        if(percepcao.contacto_obst(self.__direccao)):
            return self.__intensidade
        return 0.0