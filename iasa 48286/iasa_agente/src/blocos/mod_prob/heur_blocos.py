from pee.melhor_prim.aval.heuristica import Heuristica


class HeurBlocos(Heuristica):
    """
        CLasse HeurBlocos que representa a heuristica para este problema.
    """
    def __init__(self,estado_final):
        self.estado_final = estado_final

    def h(self, estado):
        dif = 0.0
        for i in range(len(estado.pilhas[0])):
            if estado.pilhas[0][i] != self.estado_final[0][i]:
                dif += 1
        return dif