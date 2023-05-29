import math
from lib.mod.operador import Operador
from mod.agente.estado_agente import EstadoAgente
from sae import Accao


class OperadorMover(Operador):
    """
        Classe OperadorMover que é um operador que representa um movimento do agente, este movimento é representado por um
        ângulo e um passo. Utiliza também um objeto do tipo ModeloMundo para verificar se o estado obtido é um estado existente.
    """
    @property
    def ang(self):
        return self.__ang
    
    @property
    def accao(self):
        return self.__accao
        
    
    def __init__(self, modelo_mundo, direccao):
        """
            Construtor da classe OperadorMover, onde são guardado os valores de 
            modelo_mundo, o angulo que é o valor da direccao e a accao que é um objeto da classe
            Accao passando a direccao.
        """
        self.__modelo_mundo = modelo_mundo
        self.__ang = direccao.value
        self.__accao = Accao(direccao)
        

    
    def aplicar(self, estado):
        """
        Método aplicar() que aplica o incremento dx e dy aos valores x e y, 
        criando um novo EstadoAgente com a nova posição obtida, se este estado
        for um estado existente é retornado.
        """
        
        x, y = estado.posicao
        # cálculo do incremento em x e y
        dx = round(self.__accao.passo * math.cos(self.__ang))
        dy = round(-self.__accao.passo * math.sin(self.__ang))
        
        nova_posicao = x + dx, y + dy
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo.obter_estados():
            return novo_estado

    
    def custo(self, estado, estado_suc):
        """
        Método custo() que retorna o custo entre 2 posições sendo o custo mínimo 1.
        """
        print("Estado_suc ", estado_suc)
        print("ESTADO ", estado)
        distancia = math.dist(estado.posicao, estado_suc.posicao)
        return max(distancia, 1)
        