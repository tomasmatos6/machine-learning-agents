package jogo.ambiente;

import java.util.HashMap;

public class Ambiente {
    HashMap<String, Evento> eventos = new HashMap<>();
    private Evento evento;
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
