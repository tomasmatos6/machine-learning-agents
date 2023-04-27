import sys
from planeador.ligacao import Ligacao
from planeador.planeador_trajeto import PlaneadorTrajeto
from planeador.trajeto import Trajeto

#print(sys.path)

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

def TestePlanTraj():
    planeador = PlaneadorTrajeto
    solucao = planeador.planear(LIGACOES, LOC_INICIAL, LOC_FINAL)
    if(solucao):
        Trajeto(solucao).mostrar()
    
        
TestePlanTraj()