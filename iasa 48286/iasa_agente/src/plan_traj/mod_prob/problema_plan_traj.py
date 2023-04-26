from plan_traj.mod_prob.estado_localidade import EstadoLocalidade
from plan_traj.mod_prob.operador_ligacao import OperadorLigacao
from lib.mod.problema.problema import Problema

"""
    Classe ProblemaPlanTraj que representa o problema de apartir de uma localização chegar a outra, ou seja
    obter o plano do trajeto a ser feito para ir de uma localização a outra.
    
    Herda da classe Problema.
"""
class ProblemaPlanTraj(Problema):
    """
        Construtor da classe ProblemaPlanTraj recebe uma lista de ligacoes que é transformada numa lista de objetos
        da classe OperadorLigacao, cada ligação vai ter a informação da origem, do destino e do custo da ligação.
        É chamado o construtor da classe pai, que recebe além da lista, um EstadoLocalidade que representa o estado
        inicial.
        Guarda também o estado final como um EstadoLocalidade relativo á localização final.
    """
    def __init__(self, ligacoes, loc_inicial, loc_final):
        super().__init__(EstadoLocalidade(loc_inicial), 
                         [OperadorLigacao(ligacao.origem, ligacao.destino, ligacao.custo) for ligacao in ligacoes])
        self.__estado_final = EstadoLocalidade(loc_final)
        
    """
        Método objectivo() retorna se o estado recebido é igual ao estado final.
    """
    def objetivo(self, estado):
        return estado == self.__estado_final