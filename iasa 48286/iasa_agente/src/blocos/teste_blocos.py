from blocos.planeador.mostrarAcoes import MostrarAcoes
from blocos.planeador.planeador import Planeador
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from plan.plan_pee.planeador_pee import PlaneadorPee


SEQ_INICIAL = [[2, 3, 1],[],[]]
SEQ_FINAL = [[1, 2, 3],[],[]]


planeador = Planeador()
solucao = planeador.planear(SEQ_INICIAL, SEQ_FINAL)
if(solucao):
    MostrarAcoes(solucao).mostrar()