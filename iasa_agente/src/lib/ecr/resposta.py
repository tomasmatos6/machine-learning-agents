
"""
    Classe Resposta

    Esta classe permite gerar um resposta que o agente 
    irá desempenhar.
"""
class Resposta:

    """
        Construtor da classe que recebe uma accao

        Atributo da classe: accao

        O atributo accao representa a ação que vai ser feita nesta resposta.

        @param accao
    """
    def __init__(self, accao):
        self._accao = accao

    """
        Método que recebe como parâmetros um objeto da classe percepcao
        e a intensidade.
        Este método define a prioridade e permite gerar e retornar uma ação

        Activar resposta, definindo prioridade e verificando condições de ativação.

        @param percepcao, intensidade
        @return A ação a ser executada
    """
    def activar(self, percepcao, intensidade = 0):
        self._accao.prioridade = intensidade
        return self._accao