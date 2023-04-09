package jogo.personagem;

import jogo.ambiente.Ambiente;

/**
 * Esta classe é o que vai permitir a simulação do comportamento de uma personagem
 * tendo em conta o ambiente em que se encontra. Utiliza um objeto da classe Controlo e
 * um da classe Ambiente.
 */
public class Personagem {
    /**
     * Atributos privados da classe Personagem: controlo e ambiente.
     *
     * O atributo controlo vai ser utilizado para processar as reações da personagem
     * tendo em conta o ambiente onde se encontra. Para ter conhecimente desses acontecimentos
     * tem que ter conhecimento do ambiente, sendo esta a utilização do atributo ambiente.
     */
    private Controlo controlo;
    private Ambiente ambiente;

    /**
     * Método construtor da classe.
     * @param ambiente o ambiente em que a personagem se encontra.
     */
    public Personagem(Ambiente ambiente) {
        controlo = new Controlo();
        this.ambiente = ambiente;
    }

    /**
     * Método chamado pela classe Jogo, que permite que a personagem execute as suas funções.
     * Para este efeito, é necessário começar por percecionar o ambiente e posteriormente processar
     * esta informação obtida de moda a obter a ação que deverá ser executada.
     */
    public void executar() {
        actuar(controlo.processar(percepcionar()));
    }

    /**
     * Método que permite à personagem adquirir noção do que a rodeia.
     *
     * @return Percepcao, perceção do ambiente onde se encontra, obtida através do evento atual.
     */
    private Percepcao percepcionar() {
        return new Percepcao(ambiente.getEvento());
    }

    /**
     * Método que, recebendo uma ação, permite à personagem executá-la.
     * Sendo que o jogo funciona apenas através de texto, é preciso fazer
     * um print desta ação para a consola.
     *
     * @param accao ação a ser desepenhada pelo personagem e a ser mostrada ao utilizador.
     */
    private void actuar(Accao accao) {
        if(accao != null)
            System.out.println("Açâo:" + accao + "\n");
    }
}
