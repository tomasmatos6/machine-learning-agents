from ecr.comportamento import Comportamento

"""
    Classe Reaccao que representa uma ligação entre um estímulo
    e a sua resposta.
"""
class Reaccao(Comportamento):
    """
        Construtor da classe Reaccao que recebe um estimulo e uma resposta

        Atributos da classe: _estimulo, _resposta

        O atributo _estimulo representa o estímulo recebido para esta reaccao

        O atributo _resposta representa a resposta que deve ser executada nesta reaccao

        @param estimulo, resposta
    """
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta
    
    """
        Método que permite ativar esta reação

        @param percepcao
        @return A ação a ser executada
    """
    def activar(self, percepcao):
        intensidade = self.__estimulo.detectar(percepcao)
        if(intensidade > 0):
            return self.__resposta.activar(percepcao, intensidade)