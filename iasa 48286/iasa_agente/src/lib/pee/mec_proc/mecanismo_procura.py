from abc import ABC, abstractmethod
from mod.estado import Estado

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

"""
    Classe MecanismoProcura que permite procurar uma solução para um problema, para isso é utilizado uma fronteira de 
    exploração para memorizar e gerir os nós explorados.
    O algoritmo geral pode ser resumido em começar num estado inicial ao qual se aplicam todos os operadores que podem ser
    aplicados, e assim vai-se descobrindo assim novos estados representados pelos nós.
"""
class MecanismoProcura(ABC):
    """
        Atributos read-only:
        Pode ser visto como getters para as propriedades privadas.
    """
    # Número de nós explorados/expandidos
    @property
    def complexidade_temporal(self):
        return self.__complexidade_temporal
    
    # Número maixo de nós em memória
    @property
    def complexidade_espacial(self):
        return self.__complexidade_espacial
    
    @complexidade_espacial.setter
    def complexidade_espacial(self, value):
        self.__complexidade_espacial = value
        
    @complexidade_temporal.setter
    def complexidade_temporal(self, value):
        self.complexidade_temporal = value
    
    
    """
        Construtor da classe MecanismoProcura onde é declarada a fronteira.
        A complexidade temporal e a complexidade espacial são ambas iniciadas a 0.
    """
    def __init__(self, fronteira):
        self._fronteira = fronteira
        self.__complexidade_temporal = 0
        self.__complexidade_espacial = 0
    
    """
        Método protegido iniciar_memoria() onde é iniciada a fronteira.
    """
    def _iniciar_memoria(self):
        self._fronteira.iniciar()
    
    
    @abstractmethod
    def _memorizar(no):
        """
        Memoriza um nó de acordo com o tipo de procura, a complexidade espacial é dada 
        pelo o número de nós em memória.
        """
    
    """
        Método procurar() onde é implementado o algoritmo geral de resolução do problema.
        Esta parte do algoritmo segue o seguinte processo:
            - Iniciar a fronteira;
            - Criar o nó inicial;
            - Memorizar o nó de acordo com o tipo de procura;
            - Equanto a fronteira não está vazia:
                - Remover este nó da fronteira;
                - Se o estado deste nó for o objetivo do problema, retornar a solução;
                - Se o estado deste nó não for o objetivo do problema, memorizar todos os nós retornados
                    por expandir o nó currente;
                    
        Aumenta a complexidade temporal por cada nó explorado, ou seja, expandido.
    """
    def procurar(self, problema):
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not(self._fronteira.vazia == True):
            no = self._fronteira.remover()
            if(problema.objetivo(no.estado)):
                return Solucao(no)
            for no_sucessor in self._expandir(problema, no):
                self._memorizar(no_sucessor)
            self.__complexidade_temporal += 1 # Complexidade temporal representa o número de nós explorados
        
    """
        Método protegido expandir() onde é aplicado o algoritmo de expansão de um nó.
        A todos os operadores do problema é aplicado o estado do nó.

        Esta parte do algoritmo segue o seguinte processo:
            - Por cada operador do problema:
                - Criar o estado sucessor através do método aplicar() do operador;
                - Se houver estado sucessor libertar um novo No;
    """
    def _expandir(self, problema, no):
        for operador in problema.operadores:
            estado_sucessor = operador.aplicar(no.estado)
            if estado_sucessor: 
                # Se houver estado sucessor libertar um novo No
                yield No(estado_sucessor, operador, no)
        
    