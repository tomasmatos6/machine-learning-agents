from controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae import Simulador


controlo = ControloDelib(PlaneadorPDM(0.95))


Simulador(4, controlo).executar()