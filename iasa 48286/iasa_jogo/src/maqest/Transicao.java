<<<<<<< HEAD
package jogo.maqest;

/**
 *  A classe Transicao representa a passagem entre dois estados da máquina de
 *  estados. Assim tem que ter conhecimento do estado a que passa e da ação a
 *  a realizar.
 */
public class Transicao<EV,AC> {
    /**
     *  Atributos privados da classe Transicao: estadoSucessor e accao;
     * 
     *  O atributo estadoSucessor refere o estado seguinte caso ocorra a transição.
     *  O atributo accao refere a ação a realizar nesta transição.
     */
    private Estado<EV,AC> estadoSucessor;
    private AC accao;

    /**
     *  Método construtor da classe.
     * 
     *  @param estadoSucessor estado a que se passa depois da transição.
     *  @param accao ação que deve ser realizada nesta transição, pode ser null.
     */
    public Transicao(Estado<EV,AC>estadoSucessor, AC accao) {
        this.accao = accao;
        this.estadoSucessor = estadoSucessor;
    }

    /**
     *  Método que retorna o estado seguinda.
     * 
     *  @return o estado seguinte.
     */
    public Estado<EV,AC> getEstadoSucessor() {
        return estadoSucessor;
    }

    /**
     *  Método que retorna a ação a ser executada nesta transição
     * 
     *  @return ação que deve ser realizada, pode ser null.
     */
    public AC getAccao() {
        return accao;
    }
}
=======
package jogo.maqest;

/**
 *  A classe Transicao representa a passagem entre dois estados da máquina de
 *  estados. Assim tem que ter conhecimento do estado a que passa e da ação a
 *  a realizar.
 */
public class Transicao<EV,AC> {
    /**
     *  Atributos privados da classe Transicao: estadoSucessor e accao;
     * 
     *  O atributo estadoSucessor refere o estado seguinte caso ocorra a transição.
     *  O atributo accao refere a ação a realizar nesta transição.
     */
    private Estado<EV,AC> estadoSucessor;
    private AC accao;

    /**
     *  Método construtor da classe.
     * 
     *  @param estadoSucessor estado a que se passa depois da transição.
     *  @param accao ação que deve ser realizada nesta transição, pode ser null.
     */
    public Transicao(Estado<EV,AC>estadoSucessor, AC accao) {
        this.accao = accao;
        this.estadoSucessor = estadoSucessor;
    }

    /**
     *  Método que retorna o estado seguinda.
     * 
     *  @return o estado seguinte.
     */
    public Estado<EV,AC> getEstadoSucessor() {
        return estadoSucessor;
    }

    /**
     *  Método que retorna a ação a ser executada nesta transição
     * 
     *  @return ação que deve ser realizada, pode ser null.
     */
    public AC getAccao() {
        return accao;
    }
}
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
