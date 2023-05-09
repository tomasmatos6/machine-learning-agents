from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.mec_proc.solucao import Solucao
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj

"""
   Classe PlaneadorTrajeto onde o objetivo é criar um planeador de trajetos entre 2 localidades, para os testes
   são utilizados todos os métodos de procura. 
"""
class PlaneadorTrajeto():
    def __init__(self, mecanismo):
        self.__mecanismo = mecanismo
    """
        Método planear() quee cria um ProblemaPlanTraj, depois é utilizado o método procurar() do mecanismo de 
        procura selecionado. No  final é retornada a solução e mostrada a complexidade temporal e espacial.
    """
    def planear(self, ligacoes, loc_inicial, loc_final):
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        """
            Teste Procura Custo Uniforme, onde o é necessário verificar se o trajeto escolhido é o mais económico.
        """
        procura_custo_uniforme = ProcuraCustoUnif()
        """
            Teste Procura Profundidade Limitativa, onde visto que é posto um limite podem existir situações onde não
            existe solução, nesta situações o tempo que o método demora é bastante elevado.
        """
        procura_profundidade_limitada = ProcuraProfLim()
        """
            Teste Procura Profundidade Iterativa, onde é utilizado a procura em profundidade limitativa iterativamente,
            para ser possível resolver ambos os problemas da procura anteriormente referida.
        """
        procura_profundidade_iterativa = ProcuraProfIter()
        """
            Teste Procura Profundidade, neste caso o resultado é a solução ideal mas este mecanismo não garante sempre
            uma solução ideal.
        """
        procura_profundidade = ProcuraProfundidade()
        """
            Teste Procura Largura, este mecanismo em procura maiores ocupa uma grande capacidade de memória, sendo que
            neste caso não apresenta problemas devido à complexidade do problema.
        """
        procura_largura = ProcuraLargura()
        solucao = self.__mecanismo.procurar(problema)
        print('Complexidade Temporal: ' + str(self.__mecanismo.complexidade_temporal))
        print('Complexidade Espacial: ' + str(self.__mecanismo.complexidade_espacial))
        return solucao