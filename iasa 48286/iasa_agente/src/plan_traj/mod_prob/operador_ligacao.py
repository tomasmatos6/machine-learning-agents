from lib.mod.operador import Operador
from plan_traj.mod_prob.estado_localidade import EstadoLocalidade

"""
    Classe OperadorLigacao que representa a transição entre duas localidades do cenário em teste,
    tendo também a informção do custo associada.
    
    Herda da classe Operador, e é composto por 2 objetos da classe EstadoLocalidade.
"""
class OperadorLigacao(Operador):
    """
        Construtor da classe OperadorLigacao onde é guardado o valor do custo, e criado dois objetos da
        classe EstadoLocalidade, em que um representa o estado da origem e outro o estado do destino.
    """
    def __init__(self, origem, destino, custo):
        self.__custo = custo
        self.__estado_origem = EstadoLocalidade(origem)
        self.__estado_destino = EstadoLocalidade(destino)
        
    """
        Método aplicar() que verificar se o estado recebido é igual ao estado origem, se sim, retorna o
        estado destino.
    """
    def aplicar(self, estado):
        if(estado == self.__estado_origem):
            return self.__estado_destino
        
    """
        Método custo() que retorna o atributos custo guardado.
        

        Independentemente dos estados o custo é fixo, mas para ser possível extender a classe operador a
        problemas mais complexos é incluído o estado e o estado sucessor.
    """
    def custo(self, estado, estado_suc):
        return self.__custo