"""
    Classe Solucao que representa um percurso correspondente a uma solução 
    de um problema. Esta classe:
        - Consegue guardar a sequência de nós
        - Permite acesso indexado e iteração sobre o percurso
        - Permite remover o primeiro nó do percurso
"""
class Solucao():
    """
        Atributos read-only:
        Pode ser visto como getters para as propriedades privadas.
    """
    @property
    def dimensao(self):
        return len(self.__percurso)
    
    @property
    def percurso(self):
        return self.__percurso
    
    """
        Construtor da classe Solucao onde é construído o percurso através do nó final recebido e dos seus antecessores.
    """
    def __init__(self, no_final):
        self.__percurso = []
        no = no_final
        while no:
            self.__percurso.insert(0, no)
            no = no.antecessor
    
    """
        Método remover() que remove o primeiro elemento do percurso e retorna-o.
    """
    def remover(self):
        if self.__percurso:
            return self.__percurso.pop(0)
    
    """
        Método iter() que retorna um iterador de nós da solução (para suporte de instruções do tipo for-each).
    """
    def __iter__(self):
        return iter(self.__percurso)
    
    """
        Método getitem() que retorna o elemento do percurso no index dado.
    """
    def __getitem__(self, index):
        return self.__percurso[index]