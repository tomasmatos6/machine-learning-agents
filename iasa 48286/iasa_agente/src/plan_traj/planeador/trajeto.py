from lib.pee.mec_proc.solucao import Solucao


"""
    Trajeto representado como uma lista de nomes de localidades, guarda informação sobre a dimensão
    da solução e o custo do percurso.
"""
class Trajeto:
    """
        Construtor da classe Trajeto, é guardado uma lista com o nome das localidades, a dimensão da solução
        e o custo do percurso.
    """
    def __init__(self, solucao):
        self.__localidades = [no.estado.localidade for no in solucao]
        self.__dimensao = solucao.dimensao
        self.__custo = solucao.percurso[-1].custo
        
    """
        Método mostrar() que mostra na consola a solução, a dimensão e o custo.
    """
    def mostrar(self):
        """
            Solução: [...]
            Dimensão: 10
            Custo: 50
        """
        print('Solução: ', self.__localidades, '\n')
        print('Dimensão: ', self.__dimensao, '\n')
        print('Custo: ', self.__custo, '\n')
        