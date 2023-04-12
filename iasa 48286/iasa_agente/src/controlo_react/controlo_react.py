from sae import Controlo

"""
    Classe ControloReact que se responsabiliza pelo Controlo Reativo do agente.

    Esta recebe um comportamento(Simples ou COmposto) e utilizando o método processar
    obtém e retorna uma ação.
"""
class ControloReact(Controlo):
    """
        Construtor da classe ControloReact
        Recebe um comportamento, este comportamento será ativado por uma percepcao quando
        o método processar for ativado.
    """
    def __init__(self, comportamento):
        self.__comportamento = comportamento
    """
        Método processar que recebe uma percepcao e depois ativa o comportamento através
        dessa percepcao recebida
    """
    def processar(self, percepcao):
        return self.__comportamento.activar(percepcao)  