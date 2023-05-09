from lib.pee.melhor_prim.aval.avaliador_heur import AvaliadorHeur
from lib.pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

"""
    Classe ProcuraInformada
"""
class ProcuraInformada(ProcuraMelhorPrim):
    # protected heuristica
    
    """
        Método procurar() onde é definida a heuristica e utilizado o método procurar da 
        classe pai, visto que isto é uma procura informada é garantido que o o avaliador
        é um avaliador heuristico, logo existe o método definir_heuristica().
    """
    def procurar(self, problema, heuristica):
        self._heuristica = heuristica
        self._avaliador.definir_heuristica(heuristica)
        return super().procurar(problema)