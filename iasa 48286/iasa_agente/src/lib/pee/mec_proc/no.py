"""
    Classe No que representa um elemento da árvore de procura, este mantém informação de:
        - Estado, a que corresponde o nó
        - Operador, que gerou o estado a que corresponde o nó
        - Antecessor, nó antecessor na árvore de procura
        - Profundidade do nó, na árvore de procura
        - Custo do percurso correspondente ao nó
        
    Sendo também possível comparar o seu custo com outros nós. 
"""
class No():
    """
        Atributos read-only:
        Pode ser visto como getters para as propriedades privadas.
    """
    @property
    def profundidade(self):
        return self.__profundidade
        
    @property
    def custo(self):
        return self.__custo
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor
        
    """
        Construtor da classe No
    """
    def __init__(self, estado, operador=None, antecessor=None):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        
        if antecessor:
            self.__profundidade = antecessor.profundidade + 1
            self.__custo = antecessor.custo + operador.custo(antecessor.estado, estado)
        else:
            self.__profundidade = 0
            self.__custo = 0
            
    """
        Método It() que define relação “menor” (“less than”) de comparação entre nós.
    """
    def __It__(self, no):
        return self.custo < no.custo