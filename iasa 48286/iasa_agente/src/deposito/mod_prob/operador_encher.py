from deposito.mod_prob.estado_volume import EstadoVolume
from lib.mod.operador import Operador


class OperadorEncher(Operador):
    def __init__(self, volume):
        self.__custo = volume**2
        self.__volume = volume
        
    def aplicar(self, estado):
        return EstadoVolume(estado.volume + self.__volume)
        
    def custo(self, estado, estado_suc):
        return self.__custo