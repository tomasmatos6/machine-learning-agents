from abc import abstractmethod
from lib.mod.operador import Operador


class OperadorTransferir(Operador):
	def __init__(self, volume):
		self._volume = volume

	@abstractmethod
	def aplicar(self, estado):
		"""Aplicar operador ao estado"""
	
	def custo(self, estado, estado_suc):
		return abs(estado_suc.volume - estado.volume)**2