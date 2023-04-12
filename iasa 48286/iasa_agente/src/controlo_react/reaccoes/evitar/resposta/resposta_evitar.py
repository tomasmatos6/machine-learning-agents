import random
from controlo_react.reaccoes.resposta.resposta_mover import RespostaMover
from sae import Direccao

"""
    Classe RespostaEvitar que permite ao agente evitar obstáculos
    
    Segue uma lógica simples de, existe obstáculo?:
        - Se não, podemos continuar na direção atual.
        - Se sim, verifica-se a existência de uma direção livre:
            - Se existir, altera-se a direção para uma direção livre aleatória
            - Se não, continuamos com um obstáculo em frente

"""
class RespostaEvitar(RespostaMover):
    """
        Construtor da classe RespostaEvitar que recebe uma direção inicial, com valor por omissão de "ESTE".
        Também é chamado o construtor da classe pai RespostaMover passando a direção inicial como parametro,
        é também criada uma lista privada com todas as direções.
    """
    def __init__(self, dir_inicial = Direccao.ESTE):
        super().__init__(dir_inicial)
        self.__direccoes = list(Direccao)

    """
        Método activar:
            Existe obstáculo?
                - Se não, Ativar resposta na direção atual
                - Se sim, Existe direção livre?
                    - Se sim, Alterar direção para uma direção livre aleatória
                    - Se não, Continua a existir obstáculo
                    
        É verificado se existe contacto com obstáculo caso exista é chamado o método
        privado alterar_direccao() e alterado o valor da variavél local contacto_obst
        utilizada para saber se estamos em contacto com um objecto, se depois disto ainda
        existir contacto com um obtáculo é chamado o método activar() outra vez.            
    """
    def activar(self, percepcao, intensidade):
        contacto_obst = percepcao.contacto_obst(self._accao.direccao)
        if contacto_obst:
            contacto_obst = not self.__alterar_direccao(percepcao)
        if not contacto_obst:
            return super().activar(percepcao, intensidade)

    """
        Método privado direccao_livre que permite verificar se existem direções livres, ou seja alguma direção 
        sem obstáculo. É criada uma lista com todas as direções que não tenham obstáculos e depois de verificar 
        se a lista contém algum elemento é escolhido uma direção ao calhas.
    """
    def __direccao_livre(self, percepcao):
        dir_livres = [direccao for direccao in self.__direccoes     # Elemento -> Ciclo
                        if not percepcao.contacto_obst(direccao)]   # -> Condição
        if dir_livres:
            return random.choice(dir_livres)

    """
        Método privado alterar_direcao que permite alterar a direção atual, chama o método privado direccao_livre()
        e caso existe muda a direção atual e retorna o valor para poder se utilizado como verificação da existência
        da mundança de direção
    """
    def __alterar_direccao(self, percepcao):
        if self.__direccao_livre(percepcao):
            self._accao.direccao = self.__direccao_livre(percepcao)
            return self._accao.direccao