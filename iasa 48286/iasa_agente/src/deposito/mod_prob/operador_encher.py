from deposito.mod_prob.estado_volume import EstadoVolume
from deposito.mod_prob.operador_transferir import OperadorTransferir
from lib.mod.operador import Operador

"""
    Classe OperadorEncher que representa um operador, implementa o método abstrato aplicar da classe pai.
"""
class OperadorEncher(OperadorTransferir):
    """
        Método aplicar() que aplicar este operador, neste caso aumentar o volume.
    """ 
    def aplicar(self, estado):
        return EstadoVolume(estado.volume + self._volume)

    """
        Override do método str() para ser possível mostrar na consola o nome da ação e o seu valor,
        nesta solução é escolhido o repr visto que o str era necessário utilizar prints.
    """
    def __str__(self):
        return "Encher(%s)" % self._volume
    """
        Override do método repr() para ser possível mostrar na consola o nome da ação e o seu valor.
    """
    def __repr__(self):
        return "Encher(%s)" % self._volume