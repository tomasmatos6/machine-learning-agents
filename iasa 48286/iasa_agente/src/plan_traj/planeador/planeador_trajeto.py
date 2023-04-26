from lib.pee.mec_proc.solucao import Solucao
from lib.pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from plan_traj.mod_prob.problema_plan_traj import ProblemaPlanTraj


class PlaneadorTrajeto():
    def planear(ligacoes, loc_inicial, loc_final):
        problema = ProblemaPlanTraj(ligacoes, loc_inicial, loc_final)
        mecanismo_procura = ProcuraCustoUnif()
        solucao = mecanismo_procura.procurar(problema)
        return solucao