<<<<<<< HEAD
from sae import Controlo
from sae import Simulador

class ControloTeste(Controlo):
    def processar(self, percepcao):
        print("processar")

controlo = ControloTeste()
=======
from sae import Controlo
from sae import Simulador

class ControloTeste(Controlo):
    def processar(self, percepcao):
        print("processar")

controlo = ControloTeste()
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
Simulador(1, controlo).executar()