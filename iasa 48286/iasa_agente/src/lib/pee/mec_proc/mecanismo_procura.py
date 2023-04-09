from abc import ABC, abstractmethod
from mod.estado import Estado

from pee.mec_proc.no import No
from pee.mec_proc.solucao import Solucao

"""
    Classe MecanismoProcura que permite procurar uma solução para um problema, para isso
    é utilizado uma fronteira de exploração para memorizar e gerir os nós explorados.
"""
class MecanismoProcura(ABC):
    """
        Construtor da classe MecanismoProcura onde é declarada a fronteira.
    """
    def __init__(self, fronteira):
        self._fronteira = fronteira
    
    """
        Método protegido iniciar_memoria() onde é iniciada a fronteira.
    """
    def _iniciar_memoria(self):
        self._fronteira.iniciar()
    
    
    @abstractmethod
    def _memorizar(no):
        "Memoriza um nó de acordo com o tipo de procura"
    
    """
        Método procurar() onde é implementado o algoritmo geral de resolução do problema.
    """
    def procurar(self, problema):
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        while not(self._fronteira.vazia()):
            self._fronteira.remover()
            if(problema.objetivo(no.estado)):
                return Solucao(no)
            for no_sucessor in self._expandir(problema.no):
                self._memorizar(no_sucessor)
        
    """
        Método protegido expandir() onde é aplicado o algoritmo de expansão de um nó.
        A todos os operadores do problema é aplicado o estado do nó.
    """
    def _expandir(problema, no):
        for operador in problema.operadores:
            estado_sucessor = operador.aplicar(no.estado)
            if(estado_sucessor): 
                # Se houver estado sucessor libertar um novo No
                yield No(estado_sucessor, operador, no)
        
    