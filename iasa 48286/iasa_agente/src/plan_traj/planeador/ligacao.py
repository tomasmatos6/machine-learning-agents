from dataclasses import dataclass

"""
    Dataclass Ligacao
"""
@dataclass
class Ligacao:
    origem: str
    destino: str
    custo: int