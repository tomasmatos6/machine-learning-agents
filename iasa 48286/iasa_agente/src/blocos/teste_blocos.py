from blocos.planeador.mostrarAcoes import MostrarAcoes
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from plan.plan_pee.planeador_pee import PlaneadorPee


SEQ_INICIAL = [[2, 3, 1],[],[]]
SEQ_FINAL = [[1],[2],[3]]

MECANISMOS = [
    ProcuraCustoUnif(),
    ProcuraAA()
]

def TesteBlocos():
    for mecanismo in MECANISMOS:
        print(mecanismo.__class__.__name__, "\n")
        planeador = PlaneadorPee() 
        solucao = "Solucao"
        if(solucao):
            MostrarAcoes(solucao).mostrar()
            print("------------------------------------------")
        
TesteBlocos()