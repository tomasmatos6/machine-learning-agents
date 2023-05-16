from abc import abstractmethod
from lib.mod.operador import Operador

"""
	Classe OperadorTransferir que representa um operador, com um método abstrato aplicar para ser implementado, 
	dependendo no tipo de transferencia que é feita.
"""
class OperadorTransferir(Operador):
	def __init__(self, volume):
		self._volume = volume

	@abstractmethod
	def aplicar(self, estado):
		"""Aplicar operador ao estado"""
	
	"""
		Método custo() que devolve o custo da transferencia feita.
	"""
	def custo(self, estado, estado_suc):
		return abs(estado_suc.volume - estado.volume)**2