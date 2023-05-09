from lib.pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur

"""
    Classe AvaliadorSof
"""
class AvaliadorSof(AvaliadorHeur):
    """
        Método prioridade()
    """
    def prioridade(self, no):
        return self._heuristica.h(no.estado)