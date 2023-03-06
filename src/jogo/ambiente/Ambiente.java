package jogo.ambiente;

import java.util.HashMap;

public class Ambiente {
    /**
     * HashMap criado para guardar a relação entre uma String e um Evento
     * para facilitar a criação de eventos
     */
    private HashMap<String, Evento> eventos = new HashMap<>();
    private Evento evento;

    /**
     * Função que retorna o valor do atributo privado evento
     * @return Evento
     */
    public Evento getEvento() {
        return this.evento;
    }

    public void evoluir() {
        evento = gerarEvento();
        mostrar();
    }

    private Evento gerarEvento() {
        eventos.put("S", Evento.SILENCIO);
        eventos.put("R", Evento.RUIDO);
        eventos.put("A", Evento.ANIMAL);
        eventos.put("FU", Evento.FUGA);
        eventos.put("FO", Evento.FOTOGRAFIA);
        eventos.put("T", Evento.TERMINAR);
        return null;
    }

    private void mostrar() {

    }
}
