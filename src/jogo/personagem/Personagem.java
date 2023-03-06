package jogo.personagem;

import jogo.ambiente.Ambiente;

public class Personagem {
    private Controlo controlo;
    private Ambiente ambiente;
    public Personagem(Ambiente ambiente) {
        controlo = new Controlo();
        this.ambiente = ambiente;
    }
    public void executar() {
        actuar(controlo.processar(percepcionar()));
    }

    private Percepcao percepcionar() {
        return new Percepcao(ambiente.getEvento());
    }

    private void actuar(Accao accao) {
        if(accao != null)
            System.out.println("Açâo realizada:" + accao);
    }
}
