package jogo;

import jogo.ambiente.Ambiente;
import jogo.ambiente.Evento;
import jogo.personagem.Personagem;

public class Jogo {
    private static Ambiente ambiente;
    private static Personagem personagem;
    public static void main(String[] args) {
        ambiente = new Ambiente();
        personagem = new Personagem(ambiente);
        executar();
    }

    private static void executar() {
        do {
            personagem.executar();
            ambiente.evoluir();
        } while(ambiente.getEvento() != Evento.TERMINAR);
    }
}
