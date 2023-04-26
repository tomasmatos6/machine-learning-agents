from lib.mod.estado import Estado

"""
    Classe EstadoLocalidade que pode ser visto como um tipo de estado relativo ao planeador de trajetos, 
    esta classe representa uma localidade no trajeto.
    
    Herda da classe Estado.
"""
class EstadoLocalidade(Estado):
    """
        Atributo read-only:
        Pode ser visto como um getter para a propriedade privada.
    """
    @property
    def localidade(self):
        return self.__localidade
    """
        Construtor da classe EstadoLocalidade que guarda a localizacao recebida.
    """
    def __init__(self, localidade):
        self.__localidade = localidade
        
    """
        Método id_valor() que retorna um valor inteiro que identifica o valor do identificador
        do estado.
    """
    def id_valor(self):
        return int(self.__localidade[-1])