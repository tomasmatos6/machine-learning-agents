
"""
    Trajeto representado como uma lista de nomes de localidades.
"""
from lib.pee.mec_proc.solucao import Solucao


class Trajeto:
    def __init__(self, solucao: Solucao):
        self.__localidades = [no.estado.localidade for no in solucao]
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.percurso[-1].custo
        
    def mostrar(self):
        """
            Solução: [...]
            Dimensão: 10
            Custo: 50
        """
        print('Solução: ', self.__localidades, '\n')
        print('Dimensão: ', self.__dimensao, '\n')
        print('Custo: ', self.__custo, '\n')
        