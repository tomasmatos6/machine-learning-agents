from plan.modelo.modelo_plan import ModeloPlan

"""
    Gerar um modelo para os blocos
"""
class ModeloBlocos(ModeloPlan):
    # Falta definir um construtor para ser possivel retornar valores
    def obter_estado(self):
        raise NotImplementedError
    
    def obter_estados(self):
        raise NotImplementedError
    
    def obter_operadores(self):
        raise NotImplementedError