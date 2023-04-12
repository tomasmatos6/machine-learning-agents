<<<<<<< HEAD
"""
Modelo de simulação
@author: Luís Morgado
"""

#_______________________________________________________________________________

class ModeloSimul:
    """
    Modelo de simulação
    Representa o ambiente e o agente
    """
    def __init__(self, ambiente, agente, reiniciar=False):
        self.__ambiente = ambiente
        self.__agente = agente
        self.__reiniciar = reiniciar

    @property
    def ambiente(self):
        return self.__ambiente

    @property
    def agente(self):
        return self.__agente

    def iniciar(self):
        """
        Iniciar modelo
        """
        self.__ambiente.iniciar()

    def executar_passo(self):
        """
        Executar passo de simulação
        """
        self.__agente.executar()
        # Reinício automático
        if self.__reiniciar and self.__ambiente.recolha:
            self.iniciar()
=======
"""
Modelo de simulação
@author: Luís Morgado
"""

#_______________________________________________________________________________

class ModeloSimul:
    """
    Modelo de simulação
    Representa o ambiente e o agente
    """
    def __init__(self, ambiente, agente, reiniciar=False):
        self.__ambiente = ambiente
        self.__agente = agente
        self.__reiniciar = reiniciar

    @property
    def ambiente(self):
        return self.__ambiente

    @property
    def agente(self):
        return self.__agente

    def iniciar(self):
        """
        Iniciar modelo
        """
        self.__ambiente.iniciar()

    def executar_passo(self):
        """
        Executar passo de simulação
        """
        self.__agente.executar()
        # Reinício automático
        if self.__reiniciar and self.__ambiente.recolha:
            self.iniciar()
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
