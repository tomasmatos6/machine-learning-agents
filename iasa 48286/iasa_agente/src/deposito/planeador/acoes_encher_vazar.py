class AcoesEncherVazar:
    def __init__(self, solucao):
        # Utilização do método __str__()
        #self.__volumes = [print(no.operador) for no in solucao if no.operador != None]
        # Utilização do método __repr__()
        self.__operadores = [no.operador for no in solucao if no.operador != None]
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.percurso[-1].custo
        
    def mostrar(self):
        print('Solução: ', self.__operadores, '\n')
        print('Dimensão: ', self.__dimensao, '\n')
        print('Custo: ', self.__custo, '\n')