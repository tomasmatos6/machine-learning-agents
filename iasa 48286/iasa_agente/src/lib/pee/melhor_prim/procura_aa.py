from lib.pee.melhor_prim.aval.avaliador_aa import AvaliadorAA
from lib.pee.melhor_prim.procura_informada import ProcuraInformada

"""
    Classe ProcuraAA
"""
class ProcuraAA(ProcuraInformada):
    """
        Construtor da classe ProcuraAA
    """
    def __init__(self):
        super().__init__(AvaliadorAA())