from deposito.mod_prob.estado_volume import EstadoVolume
from deposito.mod_prob.operador_encher import OperadorEncher
from deposito.mod_prob.operador_vazar import OperadorVazar
from lib.mod.problema.problema import Problema

"""
    Classe ProblemaPlanDeposito que serve para criar o problema, com o estado inicial dado pelo volume inicial,
    e com os operadores existentes.
"""
class ProblemaPlanDeposito(Problema):
    def __init__(self, vol_inicial, vol_final):
        super().__init__(EstadoVolume(vol_inicial),
                         [OperadorEncher(2), 
                          OperadorEncher(3), 
                          OperadorVazar(2), 
                          OperadorVazar(3)])
        self.__volume_final = vol_final
        
    def objetivo(self, estado):
        return estado == self.__volume_final