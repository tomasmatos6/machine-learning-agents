from lib.mod.estado import Estado


class EstadoVolume(Estado):
    """
        Classe EstadoVolume que representa o volume como um estado.
    """
    @property
    def volume(self):
        return self.__volume
    
    
    def __init__(self, volume):
        """
            Construtor da classe EstadoVolume onde é guardado o valor do volume e criado o valor de identificação.
        """
        self.__volume = volume
        # Otimização para não chamar o método hash() muitas vezes visto que isto é um objeto imutável
        self.__id_valor = hash(self.__volume)
        
    
    def id_valor(self):
        """
            Método id_valor() que retorna o valor de identificação.    
        """
        # Neste problema poderia ser usado apenas o volume como identificador.
        #return self.__volume
        
        # Otimização para não chamar o método hash() muitas vezes visto que isto é um objeto imutável
        return self.__id_valor