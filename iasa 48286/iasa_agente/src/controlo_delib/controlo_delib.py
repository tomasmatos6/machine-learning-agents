from controlo_delib.mec_delib import MecDelib
from controlo_delib.modelo.modelo_mundo import ModeloMundo
from sae import Controlo


class ControloDelib(Controlo):
    """
        Classe ControloDelib onde nesta implementação do controlo o agente tem acesso a uma memória do passado e a uma
        previsão do futuro, esta previsões são feitas através de simulações do passado.
    """
    def __init__(self, planeador):
        """
            Construtor da classe ControloDelib onde é recebido um planeador, que é guardado como atributo, é também guardado
            um objeto ModeloMundo, e um objeto MecDelib.
        """
        self.__planeador = planeador
        self.__modelo_mundo = ModeloMundo()
        self.__mec_delib = MecDelib(self.__modelo_mundo)
        self.__objetivos = None
        self.__plano = None

        ""


    def processar(self, percepcao):
        """
            Método processar() que segue a seguinte sequência:
                Assimilar a percepcao recebida
                Necessário reconsiderar?
                    Sim, deliberar, planear e executar
                    Não, apenas executar
                    
        """
        self.__assimilar(percepcao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        self.__mostrar()
        return self.__executar()

    def __assimilar(self, percepcao):
        """
            Método privado assimilar() que atualiza o seu modelo mundo com a sua percepcao 
            através do método, actualizar() da classe ModeloMundo.
        """
        self.__modelo_mundo.actualizar(percepcao)


    def __reconsiderar(self):
        """
            Método privado reconsiderar() que verifica se é necessário reconsiderar o modelo mundo, 
            isto acontece caso este tiver sido alterado ou se não existir plano.
        """
        return self.__modelo_mundo.alterado or not self.__plano


    def __planear(self):
        """
            Método privado planear()
        """
        if self.__objetivos:
            self.__plano = self.__planeador.planear(self.__modelo_mundo, self.__objetivos)
            
        else:
            self.__plano = None

    def __deliberar(self):
        """
            Método privado deliberar() que atualiza os objetivos com a lista de estado retornada pelo método deliberar() 
            do MecDelib
        """
        self.__objetivos = self.__mec_delib.deliberar()

    def __executar(self):
        "Plano foi gerado, por cada passo de processamento retorna a acao a ser executada pelo agente"
        if self.__plano:
            operador = self.__plano.obter_accao(self.__modelo_mundo.obter_estado())
            if operador:
                return operador.accao

    def __mostrar(self):
        "Mostra o modelo mundo e mostra o plano"
        self.vista.limpar()
        if self.__plano:
            self.__modelo_mundo.mostrar(self.vista)
            self.__plano.mostrar(self.vista)