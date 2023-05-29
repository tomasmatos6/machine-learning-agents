import math
from controlo_delib.modelo.operador_mover import OperadorMover
from mod.agente.estado_agente import EstadoAgente
from plan.modelo.modelo_plan import ModeloPlan
from sae import Direccao



class ModeloMundo(ModeloPlan):
    """
        Classe ModeloMundo que mantém a informação necessária sobre o mundo para o agente tomar uma decisão.
    """
    @property
    def alterado(self):
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos
    
    def __init__(self):
        """
            Construtor da classe ModeloMundo onde são guardados os valores para o estado, a lista de estados, o dicionario dos elementos,
            a lista de operadores e uma variavél para saber se o modelo foi alterado.
        """
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        self.__operadores = [OperadorMover(self, direccao) 
                             for direccao in Direccao]
        self.__alterado = False
    
    """
        Métodos para obter os valores privados desta classe
    """
    def obter_estado(self):
        return self.__estado

    def obter_estados(self):
        return self.__estados

    def obter_operadores(self):
        return self.__operadores

    def obter_elemento(self, estado):
        return self.__elementos.get(estado.posicao)
    "---------------------------------------------------------"

    """
        Método para calcular a distância entre a posição de dois estados
    """
    def distancia(self, estado):
        return math.dist(self.__estado.posicao, estado.posicao)

    """
        Método actualizar() que recebe uma perceção e atualiza se necessário o modelo.
    """
    def actualizar(self, percepcao):
        self.__estado = EstadoAgente(percepcao.posicao)
        if self.__elementos != percepcao.elementos:
            self.__elementos = percepcao.elementos
            self.__estados = [EstadoAgente(posicao) 
                              for posicao in percepcao.posicoes]
            self.__alterado = True
        else:
            self.__alterado = False

    """
        Método mostrar() para mostrar os alvos e a posicao do agente
    """
    def mostrar(self, vista):
        vista.limpar()
        vista.mostrar_alvos_obst(self.__elementos)
        vista.marcar_posicao(self.__estado.posicao)