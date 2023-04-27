from .procura_profundidade import ProcuraProfundidade


"""
    Classe ProcuraProfLim que representa uma procura em profundidade limitada, neste procura é aplicado
    o algoritmo de procura em profundidade até ao limite de profundidade dado. Este método não é ótimo, 
    nem completo, visto que a solução pode não estar no seu limite de profundidade ou que esta seja a 
    melhor solução, mesmo assim esta classe resolve o problema da profundidade infinita, quando utilizada
    em conjunto com uma pesquisa iterativa, é possível resolver os dois problemas referidos.
    
    Esta classe herda da classe ProcuraProfundidade
"""
class ProcuraProfLim(ProcuraProfundidade):
    """
        Atributo ReadWrite:
        Pode ser visto como um getter e um setter para a propriedade privada.
    """
    @property
    def prof_max(self):
        return self.__prof_max
    
    @prof_max.setter
    def prof_max(self, prof_max):
        self.__prof_max = prof_max
    
    """
        Construtor da classe ProcuraProfLim que recebe prof_max que representa a profundidade
        máxima desta procura, e é chamado o construtor da classe pai.
    """
    def __init__(self, prof_max=100):
        super().__init__()
        self.__prof_max = prof_max
    
    """
        Método protegido expandir() que expande um nó se a sua profundidade for inferior à
        profundidade máxima da procura.
    """  
    def _expandir(self, problema, no):
        if(no.profundidade < self.__prof_max):
            yield from super()._expandir(problema, no)
     
    """
        Método protegido memorizar() que memoriza um nó se não corresponder a um ciclo.
    """   
    def _memorizar(self, no):
        if not self._ciclo(no):
            super()._memorizar(no)
        
    """
        Método protegido ciclo() que verifica se o nó corresponde a um ciclo no ramo respectivo,
        para evitar a expansão de nós referentes a estados já explorados, sendo que, não evita
        ciclos em relação a outros ramos.
    """
    def _ciclo(self, no):
        """
        antecessor = no.antecessor
        while antecessor:
            if no.estado == antecessor.estado:
                return True
            antecessor = antecessor.antecessor
        return False
        """
        return no.estado in self.__estados_antecessores(no)
    
    """
        Método privado estados_antecessores que retorna através do yield todos os antecessores do
        dado nó.
        É utilizado o método yield para salvar recurso sendo que serão guardados os antecessores na
        memória interna do yield.
    """
    def __estados_antecessores(self, no):
        antecessor = no.antecessor
        while antecessor:
            yield antecessor.estado
            antecessor = antecessor.antecessor