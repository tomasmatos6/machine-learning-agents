from pdm.mec_util import MecUtil


class PDM():
    """
        Classe PDM que representa a classe principal da biblioteca do Processo de Decisão de Marlov.
        Este processo procura uma solução tendo em conta casos e estados futuros mais distantes, para isto
        a solução define um conceito de utilidade para cada ação, para estas ações pode estar ligada uma incerteza.
    """
    def __init__(self, modelo, gama, delta_max):
        """
            Constructor da classe PDM que guarda o modelo e uma instancia de MecUtil que recebe o modelo,
            o gama e o delta_max.
        """
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)
        

    def politica(self, U):
        """
            Método politica() que retorna o critério de seleção de ação.
        """

        # Variáveis explicativas que permitem explicar de uma forma mais clara o código
        S, A = self.__modelo.S, self.__modelo.A
        
        # Politica é um dicionario que liga a cada estado uma ação
        pol = {}
        for s in S():
            if A(s):
                # Escolher a ação que leva ao estado seguinte com maior utilidade
                pol[s] = max(A(s), key=lambda a : self.__mec_util.util_accao(s, a, U))
        return pol
    
    
    def resolver(self):
        """
            Método resolver() através do Processo de Decisão de Marlov.
            Calcula-se a utilidade e a politica através dessa utilidade.
        """
        
        U = self.__mec_util.utilidade()
        pol = self.politica(U)
        return U, pol