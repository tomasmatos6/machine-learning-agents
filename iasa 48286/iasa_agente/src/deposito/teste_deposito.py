from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from deposito.planeador.planeador import Planeador
from deposito.planeador.acoes_encher_vazar import AcoesEncherVazar


TAMANHO_INICIAL = 0
TAMANHO_FINAL = 9

MECANISMOS = [
    ProcuraCustoUnif(),
    ProcuraProfLim(),
    ProcuraProfIter(),
    ProcuraProfundidade(),
    ProcuraLargura()
]

def TesteDeposito():
    for mecanismo in MECANISMOS:
        print(mecanismo.__class__.__name__, "\n")
        planeador = Planeador(mecanismo)
        solucao = planeador.planear(TAMANHO_INICIAL, TAMANHO_FINAL)
        if(solucao):
            AcoesEncherVazar(solucao).mostrar()
        print("------------------------------------------")

TesteDeposito()