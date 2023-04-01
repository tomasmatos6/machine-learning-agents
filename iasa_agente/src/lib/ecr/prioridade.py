from ecr.comport_comp import ComportComp

"""
    Classe Prioridade que permite a seleção de uma ação através de uma prioridade,
    "As resposta são selecionadas de acordo com uma prioridade associada que varia
    ao longo da execução."
"""
class Prioridade(ComportComp):
    """
        Método que permite selecionar uma ação através de uma prioridade,
        este método recebe uma lista de ações e retorna a ação a ser executada.

        O elemento da lista a ser retornado é o que apresentar maior prioridade variável.
    """
    def selecionar_accao(self, accoes):
        if(accoes):
            return max(accoes, key= lambda accao: accao.prioridade)