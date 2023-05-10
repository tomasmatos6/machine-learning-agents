from deposito.mod_prob.estado_volume import EstadoVolume
from deposito.mod_prob.operador_transferir import OperadorTransferir
from lib.mod.operador import Operador


class OperadorVazar(OperadorTransferir):  
    def aplicar(self, estado):
        #return EstadoVolume(estado.volume - self._volume)
        novo_volume = estado.volume - self._volume
        
        # Utilizar a outra forma de retorno para seguir a métrica de 1 entrada e 1 saída
        #return EstadoVolume(novo_volume) if novo_volume >= 0 else EstadoVolume(0)
        
        if novo_volume < 0:
          novo_volume = 0
        return EstadoVolume(novo_volume)
    
    """
        Override do método str() para ser possível mostrar na consola o nome da ação e o seu valor,
        nesta solução é escolhido o repr visto que o str era necessário utilizar prints.
    """
    def __str__(self):
        return "Vazar(%s)" % self._volume
    """
        Override do método repr() para ser possível mostrar na consola o nome da ação e o seu valor.
    """
    def __repr__(self):
        return "Vazar(%s)" % self._volume