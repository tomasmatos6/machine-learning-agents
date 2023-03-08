package jogo.ambiente;

import java.util.HashMap;
import java.util.Scanner;

public class Ambiente {
    /**
     * Atributos privados da classe Ambiente: eventos, evento e sc.
     *
     * O atributos eventos é um HashMap que associa as strings que podem
     * ser introduzidas pelo utilizador a um evento.
     *
     * O atributo evento indica o evento mais recente que aconteceu no
     * ambiente.
     *
     * O atributo sc é um scanner para permitir o utilizador interagir com
     * o jogo através da consola.
     */
    private HashMap<String, Evento> eventos;
    private Evento evento;
    private Scanner sc = new Scanner(System.in);

    /**
     * Método construtor da classe.
     *
     * Faz a criação de um HashMap com os vários comandos (Strings) que
     * o utilizador pode usar para escolher o evento (Evento).
     */
    public Ambiente() {
        /**
         * Utilização de um HashMap para não ser utilizado repetitivamente
         * if's e switch-cases, fazendo diretamente a ligação entre o input
         * e os eventos.
         */
        eventos = new HashMap<>();
        eventos.put("S", Evento.SILENCIO);
        eventos.put("R", Evento.RUIDO);
        eventos.put("A", Evento.ANIMAL);
        eventos.put("F", Evento.FUGA);
        eventos.put("O", Evento.FOTOGRAFIA);
        eventos.put("T", Evento.TERMINAR);
    }
    /**
     * Função que retorna o valor do atributo privado evento.
     *
     * @return Evento atual no ambiente.
     */
    public Evento getEvento() {
        return this.evento;
    }

    /**
     * Método encarregado da evolução do ambiente permitindo mudar o evento que está a decorrer,
     * chamando a seguir um método que permite a visualização disto ao utilizador.
     */
    public void evoluir() {
        evento = gerarEvento();
        mostrar();
    }

    /**
     * Método para fazer a criação do próximo evento.
     *
     * @return novo Evento criado.
     */
    private Evento gerarEvento() {
        System.out.println("Evento? ");
        String com = sc.next();
        return eventos.get(com);
    }

    /**
     * Método que permite a visualização do evento atual na consola, para permitir
     * uma melhor visibilidade dos acontecimentos do ambiente.
     */
    private void mostrar() {
        if(evento != null) System.out.printf("Evento: %s\n", evento);
    }
}
