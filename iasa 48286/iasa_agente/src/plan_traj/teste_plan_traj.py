from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from planeador.ligacao import Ligacao
from planeador.planeador_trajeto import PlaneadorTrajeto
from planeador.trajeto import Trajeto

"""
    Teste ao planeador de trajetos
"""

LOC_INICIAL = 'loc-0'
LOC_FINAL = 'loc-4'

LIGACOES = [
    Ligacao('loc-0', 'loc-1', 5),
    Ligacao('loc-0', 'loc-2', 25),
    Ligacao('loc-1', 'loc-3', 12),
    Ligacao('loc-1', 'loc-6', 5),
    Ligacao('loc-2', 'loc-4', 30),
    Ligacao('loc-3', 'loc-2', 10),
    Ligacao('loc-3', 'loc-5', 5),
    Ligacao('loc-4', 'loc-3', 2),
    Ligacao('loc-5', 'loc-6', 8),
    Ligacao('loc-5', 'loc-4', 10),
    Ligacao('loc-6', 'loc-3', 15),
]

MECANISMOS = [
    ProcuraCustoUnif(),
    ProcuraProfLim(),
    ProcuraProfIter(),
    ProcuraProfundidade(),
    ProcuraLargura()
]

def TestePlanTraj():
    for mecanismo in MECANISMOS:
        print(mecanismo.__class__.__name__, "\n")
        planeador = PlaneadorTrajeto(mecanismo)
        solucao = planeador.planear(LIGACOES, LOC_INICIAL, LOC_FINAL)
        if(solucao):
            Trajeto(solucao).mostrar()
        print("------------------------------------------")
    
        
TestePlanTraj()