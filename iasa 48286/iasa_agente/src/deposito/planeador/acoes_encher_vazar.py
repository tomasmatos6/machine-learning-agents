class AcoesEncherVazar:
    def __init__(self, solucao):
        self.__volumes = [no.estado.volume for no in solucao]
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.percurso[-1].custo
        
    def mostrar(self):
        print('Solução: ', self.__volumes, '\n')
        print('Dimensão: ', self.__dimensao, '\n')
        print('Custo: ', self.__custo, '\n')