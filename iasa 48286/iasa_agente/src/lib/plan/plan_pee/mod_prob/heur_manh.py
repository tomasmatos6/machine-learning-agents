from pee.melhor_prim.aval.heuristica import Heuristica
import math

class HeurManh(Heuristica):
    def __init__(self, estado_final):
        self.__estado_final = estado_final
        
    def h(self, estado):
        x, y = estado.posicao
        x2, y2 = self.__estado_final.posicao
        return abs(x - x2) + abs(y - y2)