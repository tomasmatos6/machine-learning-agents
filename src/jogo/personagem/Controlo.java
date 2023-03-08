package jogo.personagem;

import jogo.ambiente.Evento;
import jogo.maqest.Estado;
import jogo.maqest.MaquinaEstados;

/**
 *  A classe Controlo vai permitir ao personagem reagir ao ambiente em que este se encontra,
 *  com base na ideia que a personagem tem do ambiente.
 */
public class Controlo {

    /**
     *  Atributo privado da classe Controlo: maqEst.
     * 
     *  Este atributo representa a classe MaquinaEstados, fazendo a ligação entre os tipos genéricos
     *  EV e AC e as classes Evento e Accao. As mudanças de estados são feitas através desta classe.
     */
    private MaquinaEstados<Evento,Accao> maqEst;

    public Controlo() {
        // Definir estados
        Estado<Evento, Accao> procura = new Estado<>("Procura");
        Estado<Evento, Accao> inspeccao = new Estado<>("Inspeção");
        Estado<Evento, Accao> observacao = new Estado<>("Observação");
        Estado<Evento, Accao> registo = new Estado<>("Registo");

        /**
         * Definir as transições
         * 
         *  A arquitetura utlizada permite a definição simultanea da tabela de transições de estado e
         *  da tabela de ações de saída.
         */

        procura
            .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
            .transicao(Evento.RUIDO, inspeccao, Accao.APROXIMAR)
            .transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

        inspeccao
            .transicao(Evento.ANIMAL, observacao, Accao.APROXIMAR)
            .transicao(Evento.SILENCIO, procura, Accao.PROCURAR)
            .transicao(Evento.SILENCIO, procura, Accao.PROCURAR);

        observacao
            .transicao(Evento.ANIMAL, registo, Accao.OBSERVAR)
            .transicao(Evento.FUGA, inspeccao);

        registo
            .transicao(Evento.ANIMAL, registo, Accao.FOTOGRAFAR)
            .transicao(Evento.FOTOGRAFIA, procura)
            .transicao(Evento.FUGA, procura);

        // Inicialização da Maquina de Estados com estado inicial "PROCURA".
        maqEst = new MaquinaEstados<>(procura);
    }


    /**
     * Função que retorna o valor privado, evento, da classe MaquinaEstados.
     * 
     * @return o Estado em que a Maquina de Estados se encontra
     */
    public Estado<Evento,Accao> getEstado() {
        return maqEst.getEstado();
    }

    /**
     * Método que permite à personagem, face à sua percepção do ambiente, saber
     * como reagir, ou seja, quais as ações que tem que executar.
     *
     * @param percepcao noção que a personagem tem do ambiente.
     * @return Uma ação
     */
    public Accao processar(Percepcao percepcao) {
        Accao a = maqEst.processar(percepcao.getEvento());
        mostrar();
        return a;
    }

    /**
     * Método que permite ao utilizador observar na consola a ação atual, dando
     * assim uma melhor visibilidade dos acontecimentos no ambiente.
     */
    private void mostrar() {
        System.out.println("Estado: " + getEstado().getNome().toUpperCase());
    }
}
