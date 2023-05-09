from lib.pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

"""
    Classe AvaliadorAA
"""
class AvaliadorAA(AvaliadorHeur):
    """
        Método prioridade()
    """
    def prioridade(self, no):
        return no.custo + self._heuristica.h(no.estado)