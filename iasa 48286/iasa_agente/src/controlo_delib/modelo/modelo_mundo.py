import math
from controlo_delib.modelo.operador_mover import OperadorMover
from mod.agente.estado_agente import EstadoAgente
from sae import Direccao



class ModeloMundo():
    """
        Mantém a informação necessária para tomar uma decisão
    """
    @property
    def alterado(self):
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos
    
    """
    
    """
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        self.__operadores = [OperadorMover(self, direccao) 
                             for direccao in Direccao]
        self.__alterado = False
    

    def obter_estado(self):
        return self.__estado

    def obter_estados(self):
        return self.__estados

    def obter_operadores(self):
        return self.__operadores

    def obter_elemento(self, estado):
        return self.__elementos(estado.posicao)

    def distancia(self, estado):
        return math.dist(self.__estado.posicao, estado.posicao)

    def actualizar(self, percepcao):
        self.__estado = EstadoAgente(percepcao.posicao)
        if self.__elementos != percepcao.elementos:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) 
                              for posicao in percepcao.posicoes]
            self.__alterado = True
        else:
            self.__alterado = False

    def mostrar(self, vista):
        vista.mostrar_alvos_obst(self.__elementos)
        vista.marcar_posicao(self.__estado.posicao)