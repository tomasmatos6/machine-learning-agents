from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPee
from sae import Simulador

planeador = PlaneadorPee()
planeador.definir_heuristica("Manh")
controlo = ControloDelib(planeador)


Simulador(4, controlo).executar()

"""
    Heurística: Distância de Manhattan
    Complexidade temporal: 202
    Complexidade espacial: 226
    
    Heurística: Distância de Manhattan
    Complexidade temporal: 420
    Complexidade espacial: 233
    
    Heurística: Distância de Manhattan
    Complexidade temporal: 807
    Complexidade espacial: 426
    
    -----------------------------------
    Heurística: Distância Euclidiana
    Complexidade temporal: 230
    Complexidade espacial: 247
    
    Heurística: Distância Euclidiana
    Complexidade temporal: 463
    Complexidade espacial: 246
    
    Heurística: Distância Euclidiana
    Complexidade temporal: 882
    Complexidade espacial: 438
"""