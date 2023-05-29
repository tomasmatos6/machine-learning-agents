from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPee
from sae import Simulador


controlo = ControloDelib(PlaneadorPee())


Simulador(4, controlo).executar()