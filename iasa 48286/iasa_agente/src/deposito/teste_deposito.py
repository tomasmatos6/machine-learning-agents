from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from deposito.planeador.planeador import Planeador
from deposito.planeador.acoes_encher_vazar import AcoesEncherVazar


"""
Problema do deposito de agua:
Dado um deposito de agua com um determinado volume inicial
de agua e dois recipientes de 2 e 3 litros, com quais é
possível encher e vazar o deposito, determinar qual a
sequencia de acoes de encher e vazar que deve ser feita
para o deposito ter um determinado volume final de agua.
O custo de cada accao é proporcional ao quadrado do volume 
de agua transferido.
"""

TAMANHO_INICIAL = 0
TAMANHO_FINAL = 9

MECANISMOS = [
    ProcuraCustoUnif(),
    ProcuraProfLim(4),
    ProcuraProfIter(),
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


"""
ProcuraCustoUnif 

Complexidade Temporal: 13
Complexidade Espacial: 14
Solução:  [Encher(2), Encher(2), Encher(2), Encher(3)]

Dimensão:  4

Custo:  21

------------------------------------------
ProcuraProfLim - Com 4 de profundidade máxima

Complexidade Temporal: 13
Complexidade Espacial: 7
Solução:  [Encher(3), Encher(3), Encher(3)]

Dimensão:  3

Custo:  27

------------------------------------------
ProcuraProfIter

Complexidade Temporal: 19
Complexidade Espacial: 5
Solução:  [Encher(3), Encher(3), Encher(3)]

Dimensão:  3

Custo:  27 

------------------------------------------
ProcuraLargura

Complexidade Temporal: 11
Complexidade Espacial: 12
Solução:  [Encher(3), Encher(3), Encher(3)]

Dimensão:  3

Custo:  27

------------------------------------------
"""