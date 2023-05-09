from lib.pee.melhor_prim.aval.avaliador_custo_unif import AvaliadorCustoUnif
from lib.pee.melhor_prim.procura_melhor_prim import ProcuraMelhorPrim

"""
    Classe ProcuraCustoUnif que representa um mecanismo de procura por melhor primeiro,
    sendo que o melhor aqui será o de menor custo.
    A função f(n) da classe pai será por base do custo da solução através da solução
    do no.
    
    Herda de ProcuraMelhorPrim
"""
class ProcuraCustoUnif(ProcuraMelhorPrim):
    
    """
        Construtor da Classe ProcuraCustoUnif que chama o construtor da classe pai, passando
        o AvaliadorCustoUnif como avaliador.
    """
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())