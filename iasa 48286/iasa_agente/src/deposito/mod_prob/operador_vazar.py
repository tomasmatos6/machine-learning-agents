from deposito.mod_prob.estado_volume import EstadoVolume
from lib.mod.operador import Operador


class OperadorVazar(Operador):
    def __init__(self, volume):
        self.__custo = volume**2
        self.__volume = volume
        
    def aplicar(self, estado):
        return EstadoVolume(estado.volume - self.__volume)
        
    def custo(self, estado, estado_suc):
        return self.__custo
    
    def __str__(self):
        return "Vazar(%s)" % self.__volume

    def __repr__(self):
        return "Vazar(%s)" % self.__volume