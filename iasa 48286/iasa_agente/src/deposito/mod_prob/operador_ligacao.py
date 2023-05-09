from deposito.mod_prob.estado_volume import EstadoVolume
from lib.mod.operador import Operador


class OperadorLigacao(Operador):
    def __init__(self, origem, operador, custo):
        self.__custo = custo
        self.__estado_origem = EstadoVolume(origem)
        self.__operador = operador
        
    def aplicar(self, estado):
        if(estado == self.__estado_origem):
            return self.__estado_origem + self.__operador
        
    def custo(self, estado, estado_suc):
        return self.__custo