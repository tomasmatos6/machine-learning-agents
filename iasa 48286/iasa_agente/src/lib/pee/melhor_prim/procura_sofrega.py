from lib.pee.melhor_prim.aval.avaliador_sof import AvaliadorSof
from lib.pee.melhor_prim.procura_informada import ProcuraInformada

"""
    Classe ProcuraSofrega
"""
class ProcuraSofrega(ProcuraInformada):
    """
        Construtor da classe ProcuraSofrega
    """
    def __init__(self):
        super().__init__(AvaliadorSof())