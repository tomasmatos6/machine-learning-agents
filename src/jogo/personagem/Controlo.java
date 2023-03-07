package jogo.personagem;

/**
 *  A classe Controlo vai permitir ao personagem reagir ao ambiente em que este se encontra,
 *  com base na ideia que a personagem tem do ambiente.
 */
public class Controlo {

    /**
     *  Atributo privado da classe Controlo: accao.
     */
    private Accao accao;

    /**
     * Método que permite à personagem, face à sua percepção do ambiente, saber
     * como reagir, ou seja, quais as ações que tem que executar.
     *
     * @param percepcao noção que a personagem tem do ambiente.
     * @return Uma ação
     */
    public Accao processar(Percepcao percepcao) {
        return this.accao;
    }
}
