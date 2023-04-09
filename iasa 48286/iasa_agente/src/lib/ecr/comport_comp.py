from abc import abstractmethod
from ecr.comportamento import Comportamento

"""
    Classe ComportComp que representa um agregamento de um conjunto de comportamentos,
    para o funcionamento disto é necessário ainda a implementação de um mecanismo de 
    seleção de ação para determinar a ação a realizar em função das respostas dos vários 
    comportamentos internos.


    Baseado na informação obtida na aula pode ser separada a escolha em três formas:
        Hierarquia, onde os comportamentos estão organizados numa hierarquia fixa
                    de subsunção (supressão e substituição).

        Prioridade, as respostas são selecionadas de acordo com uma prioridade 
                    associada que varia ao longo da execução.

        Fusão, as respostas são combinadas numa única resposta por composição
                (por ex. soma vetorial).

    Para isso esta classe utiliza a classe Comportamento.
"""
class ComportComp(Comportamento):
    """
        Construtor da classe que recebe uma lista de comportamentos.

        @param comportamentos
    """
    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos
    
    """
        Método que ativa um comportamento baseado na percepcao recebida.
        Utilizando a percepcao recebida cada comportamento do comportamento composto
        vai ser ativado, que pode ou não devolver uma ação, de seguida é preciso
        utlizar um método de seleção para fazer a escolha da ação a ser realizada.

        @param percepcao
    """
    def activar(self, percepcao):
        accoes = []
        for comp in self.__comportamentos:
            accao = comp.activar(percepcao)
            if (accao):
                accoes.append(accao)
        if (accoes):
            return self.selecionar_accao(accoes)

    @abstractmethod
    def selecionar_accao(self, accoes):
        """
        Método que vai permitir selecionar uma ação que depende do mecanismo 
        de reação escolhido 
        """