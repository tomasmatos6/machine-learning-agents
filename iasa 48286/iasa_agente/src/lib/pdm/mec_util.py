class MecUtil():
    """
        Classe MecUtil() que server para calcular a utilidade dos estados e ações a serem realizadas.
    """
    def __init__(self, modelo, gama, delta_max):
        """
            Constructor da classe MecUtil que guarda o modelo, o gama e o delta_max.
            O gama representa a taxa de desconto para recompensas diferidas no tempo e o delta_max representa
            qual a variação de utilidade mais baixa entre duas ações.
        """
        self.__modelo = modelo
        self.__gama = gama
        self.__delta_max = delta_max
    
    
    def utilidade(self):
        """
            Método utilidade() que calcula a utilidade de todos os estados.
            Funcionamento do algoritmo:
                - Iniciar a Utilidade, um dicionário de estados - utilidade, com utilidade a zero
                - Iterar o dicionário para obter a ação com maior utilidade
                - Realizar esta iteração até que a formula retorne a forma ótima, a condição é aceite
                quando o delta, que representa a variação entre duas iterações, for menor que o delta_max
        """
        
        S, A = self.__modelo.S, self.__modelo.A
        U = {s:0.0 for s in S()}
        while True:
            Uant = U.copy() # Tem que se usar o copy senão seriam só duas variaveis a apontar para o mesmo objeto
            delta = 0
            for s in S():
                U[s] = max([self.util_accao(s, a, Uant) for a in A(s)], default=0) # valor por omissão 0 caso não haja ação
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta <= self.__delta_max:
                break
        return U
        
    
    def util_accao(self, s, a, U):
        """
            Método util_acao() que retorna a utilidade de um estado fazer uma ação
        """
        """
            utilidade = 0.0
            T, R, sn = self.__modelo.T, self.__modelo.R, a.aplicar(s)
            
            if sn:
                utilidade += (T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn]))
            return utilidade
        """
        T = self.__modelo.T
        R = self.__modelo.R
        Sucessores = self.__modelo.Sucessores
        return sum(T(s,a,sn) * R(s,a,sn) +   self.__gama * U[sn] for sn in Sucessores(s,a))
        