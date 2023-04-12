<<<<<<< HEAD
package jogo;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;
import jogo.personagem.Personagem;

/**
 * A classe Jogo utiliza um objeto da classe Ambiente e um da classe Personagem.
 * Esta classe serve como base para a execução do jogo, sendo assim necessário inicializar
 * as instâncias das classes referidas, Ambiente e Personagem, que irão permitir o funcionamento
 * do jogo.
 */
public class Jogo {
    /**
     * Atributos privados da classe Jogo: ambiente e personagem
     *
     * Ambos os atributos representam diretamente o que o nome indica,
     * sendo o personagem o Personagem de jogo e o ambiente o Ambiente de jogo.
     */
    private static Ambiente ambiente;
    private static Personagem personagem;

    /**
     * O método main é responsável por iniciar os atributos personagem e ambiente.
     *
     * @param args não é utilizado.
     */
    public static void main(String[] args) {
        ambiente = new Ambiente();
        personagem = new Personagem(ambiente);
        executar();
    }

    /**
     * Método que permite cumprir o comportamento de Jogo.
     * Enquanto não receber o evento que marca o final da sua execução,
     * este irá invocar o método executar() do personagem e evoluir() do
     * ambiente.
     */
    private static void executar() {
        do {
            personagem.executar();
            ambiente.evoluir();
        } while(ambiente.getEvento() != Evento.TERMINAR);
    }
}
=======
package jogo;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;
import jogo.personagem.Personagem;

/**
 * A classe Jogo utiliza um objeto da classe Ambiente e um da classe Personagem.
 * Esta classe serve como base para a execução do jogo, sendo assim necessário inicializar
 * as instâncias das classes referidas, Ambiente e Personagem, que irão permitir o funcionamento
 * do jogo.
 */
public class Jogo {
    /**
     * Atributos privados da classe Jogo: ambiente e personagem
     *
     * Ambos os atributos representam diretamente o que o nome indica,
     * sendo o personagem o Personagem de jogo e o ambiente o Ambiente de jogo.
     */
    private static Ambiente ambiente;
    private static Personagem personagem;

    /**
     * O método main é responsável por iniciar os atributos personagem e ambiente.
     *
     * @param args não é utilizado.
     */
    public static void main(String[] args) {
        ambiente = new Ambiente();
        personagem = new Personagem(ambiente);
        executar();
    }

    /**
     * Método que permite cumprir o comportamento de Jogo.
     * Enquanto não receber o evento que marca o final da sua execução,
     * este irá invocar o método executar() do personagem e evoluir() do
     * ambiente.
     */
    private static void executar() {
        do {
            personagem.executar();
            ambiente.evoluir();
        } while(ambiente.getEvento() != Evento.TERMINAR);
    }
}
>>>>>>> 3976a3f6da1b734f3b7d4dc5030b32391c3adfcb
