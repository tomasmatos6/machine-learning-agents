from dataclasses import dataclass

"""
    Dataclass Ligacao que representa as linhas da tabela que representão o problema, ou seja
    junta a informação da localidade origem para a localidade destino e o custo desta deslocação.
"""
@dataclass
class Ligacao:
    origem: str
    destino: str
    custo: int