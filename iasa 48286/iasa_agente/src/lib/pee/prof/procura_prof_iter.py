from .procura_prof_lim import ProcuraProfLim

"""
    Classe ProcuraProfIter que representa uma procura em profundidade iterativa, este mecanismo retorna uma
    solução ótima e é um mecanismo completo, visto que garante que, caso exista solução, esta será encontrada.
    Utilizando o mecanismo de procura em profundidade limitada, é aplicado o seu algoritmo a profundidades cada
    vez maiores até ser encontrada a solução ou se perceba que não existe solução.
    
    Esta classe herda da classe ProcuraProfLim
"""
class ProcuraProfIter(ProcuraProfLim):
    """
        Método procurar() onde é realizada a procura em profundidade iterativa, equanto não chegarmos 
        ao limite da profundidade vamos primeiro definir a profundidade máxima para a iteração currente,
        utilizamos o método procurar() da classe pai, que representa o algoritmo de procura em profundidade 
        limitado, se a solução não for None posso retorna-la, senão é necessário repetir para uma 
        profundidade máxima maior.
    """
    def procurar(self, problema, inc_prof = 1, limite_prof = 100):
        """
        profundidade = 0
        while profundidade < limite_prof:
            self.prof_max = profundidade
            solucao = super().procurar(problema)
            profundidade += inc_prof
            if solucao is not None:
                return solucao
        """
        " Resolução do professor que utiliza um for em vez de um while retirando 2 linhas de código"
        for profundidade in range(0, limite_prof + 1, inc_prof):
            self.prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao