from lib.pee.larg.procura_largura import ProcuraLargura
from lib.pee.mec_proc.solucao import Solucao
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from lib.pee.prof.procura_prof_iter import ProcuraProfIter
from lib.pee.prof.procura_prof_lim import ProcuraProfLim
from lib.pee.prof.procura_profundidade import ProcuraProfundidade
from plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj


class PlaneadorTrajeto():
    def planear(ligacoes, loc_inicial, loc_final):
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        procura_custo_uniforme = ProcuraCustoUnif()
        procura_profundidade_iterativa = ProcuraProfIter()
        procura_profundidade_limitada = ProcuraProfLim()
        procura_profundidade = ProcuraProfundidade()
        procura_largura = ProcuraLargura()
        solucao = procura_custo_uniforme.procurar(problema)
        print('Complexidade Temporal: ' + str(procura_custo_uniforme.complexidade_temporal))
        print('Complexidade Espacial: ' + str(procura_custo_uniforme.complexidade_espacial))
        return solucao