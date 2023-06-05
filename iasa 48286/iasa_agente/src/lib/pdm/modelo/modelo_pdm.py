from abc import ABC, abstractmethod


class ModeloPDM(ABC):
    """
        Interface ModeloPDM que representa um mundo sobre a forma de um PDM (Processo de Decisão de Markov).
    """
    @abstractmethod
    def S(self):
        """
            Conjunto de estados do Mundo.
        """
    
    @abstractmethod
    def A(self, s):
        """
            Conjunto de acções possíveis no estado pertencente a S.
        """
    
    @abstractmethod
    def T(self, s,a,sn):
        """
            Probabilidade de transição do estado currente para o estado sucessor através da ação a.
        """
    
    @abstractmethod
    def R(self, s,a,sn):
        """
            Recompensa esperada na transição do estado currente para o estado sucessor através da ação a.
        """
    
    @abstractmethod
    def Sucessores(self, s,a):
        ""