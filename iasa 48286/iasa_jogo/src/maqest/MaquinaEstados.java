package jogo.maqest;

/**
 *  A classe MaquinaEstados trata do processamento das transições entre estados,
 *  mantendo sempre conhecimente do estado atual e permitindo a transição deste
 *  dependendo dos eventos que acontecem no Ambiente, decidindo assim quais as 
 *  ações a serem tomadas pelo personagem.
 * 
 *  A biblioteca da Maquina de Estados, MaquinaEstados, permite a utilização das 
 *  classes relacionadas noutros contextos, sem necessitar da utilização das classes
 *  Evento e Accao. Para este efeito é necessário a utilizar tipos genéricos que são,
 *  EV e AC.
 * 
 *  No contexto deste jogo:
 *  EV -> O Evento que aconteceu
 *  AC -> A Ação de resposta
 */
public class MaquinaEstados<EV,AC> {
    /**
     *  Atributo privado da classe MaquinaEstados: estado.
     * 
     *  Este atributo representa o estado atual com que a 
     *  máquina de estados vai ser iniciada.
     */
    private Estado<EV,AC> estado;

    /**
     *  Método construtor da classe.
     * 
     *  @param estado estado inicial.
     */
    public MaquinaEstados(Estado<EV,AC> estado) {
        this.estado = estado;
    }

    /**
     *  Método que retorna a variavél privada estado representante
     *  do estado inicial da máquina de estados.
     * 
     *  @return Estado atual do ambiente.
     */
    public Estado<EV,AC> getEstado() {
        return this.estado;
    }

    /**
     * Método que recebe um evento que aconteceu no Ambiente, interpretando
     * tendo em conta o estado atual, atualizando a seguir o estado para o seu
     * estado sucessor, retornando no fim a ação.
     * 
     * @param evento Evento que ocurreu no Ambiente, para ser processado.
     * @return Acção que a Personagem deve executar, no caso de não ocurrer transição
     *         entre estados retorna null.
     */
    public AC processar(EV evento) {
        Transicao<EV,AC> transicao = estado.processar(evento);
        
        if(transicao != null) {
            estado = transicao.getEstadoSucessor();
            return transicao.getAccao();
        }
        return null;
    }
}
