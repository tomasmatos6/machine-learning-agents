<<<<<<< HEAD
package jogo.personagem;

import jogo.ambiente.Evento;

/**
 *  A classe Percepcao é uma das classes quais a classe Controlo depende.
 *  Esta classe vai permitir armazenar o evento atual de forma a ser possível
 *  posteriormente ser interpretado pela personagem.
 */
public class Percepcao {
    /**
     * Atributo privado da classe Percepcao: Evento
     *
     * O atributo evento vai traduzir o evento que a personagem tem no momento.
     */
    private Evento evento;

    /**
     * Método construtor da classe.
     * @param evento, o evento que vai ser processado posteriormente.
     */
    public Percepcao(Evento evento) {
        this.evento = evento;
    }


    /**
     *  Método que retorna o atributo evento.
     * @return evento
     */
    public Evento getEvento() {
        return this.evento;
    }
}
=======
package jogo.personagem;

import jogo.ambiente.Evento;

/**
 *  A classe Percepcao é uma das classes quais a classe Controlo depende.
 *  Esta classe vai permitir armazenar o evento atual de forma a ser possível
 *  posteriormente ser interpretado pela personagem.
 */
public class Percepcao {
    /**
     * Atributo privado da classe Percepcao: Evento
     *
     * O atributo evento vai traduzir o evento que a personagem tem no momento.
     */
    private Evento evento;

    /**
     * Método construtor da classe.
     * @param evento, o evento que vai ser processado posteriormente.
     */
    public Percepcao(Evento evento) {
        this.evento = evento;
    }


    /**
     *  Método que retorna o atributo evento.
     * @return evento
     */
    public Evento getEvento() {
        return this.evento;
    }
}
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
