from mod.estado import Estado


class EstadoPilha(Estado):
    @property
    def pilhas(self):
        return self.__blocos
    
    def __init__(self, blocos):
        self.__blocos = blocos
        self.__id_valor = hash(tuple(tuple(pilhas) for pilhas in self.__blocos))
        
        
    def id_valor(self):
        return self.__id_valor