from deposito.mod_prob.estado_volume import EstadoVolume
from deposito.mod_prob.operador_ligacao import OperadorLigacao
from lib.mod.problema.problema import Problema


class ProblemaPlanTraj(Problema):
    def __init__(self, ligacoes, vol_inicial, vol_final):
        super().__init__(EstadoVolume(vol_inicial),
                         [OperadorLigacao(ligacao.volume, ligacao.operador, ligacao.custo) for ligacao in ligacoes])
        self.__estado_final = EstadoVolume(vol_final)
        
        def objetivo(self, estado):
            return estado == self.__estado_final