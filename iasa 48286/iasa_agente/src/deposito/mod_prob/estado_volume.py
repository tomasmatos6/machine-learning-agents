from lib.mod.estado import Estado


class EstadoVolume(Estado):
    
    @property
    def volume(self):
        return self.__volume
    
    def __init(self, volume):
        self.__volume = volume
        
    def id_valor(self):
        return self.__volume