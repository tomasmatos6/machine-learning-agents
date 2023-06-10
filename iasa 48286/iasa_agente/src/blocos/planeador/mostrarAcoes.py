class MostrarAcoes():
    """
        Classe MostrarAcoes para ser possível a visualização dos resultados das procuras realizadas.
    """
    def __init__(self, solucao):
        self.__operadores = [no.operador for no in solucao if no.operador != None]
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.percurso[-1].custo
        
    def mostrar(self):
        print('Solução:')
        for operador in self.__operadores:
            print('     ', operador)
        print('Dimensão: ', self.__dimensao, '\n')
        print('Custo: ', self.__custo, '\n')