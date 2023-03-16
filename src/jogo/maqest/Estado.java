package jogo.maqest;

import java.util.HashMap;
import java.util.Map;

/**
 *  A classe Estado representa um dos possíveis estados da maquina de estados.
 *  
 *  Para o funcionamento da máquina de estados é necessário esta classe possuir 
 *  conhecimento das transições que podem ocurrer a partir deste estado, com isto
 *  foi criado um HashMap para ligar um Evento a uma Transicao, assim como um nome
 *  para cada estado que irá facilitar os prints necessários para o jogo.
 */
public class Estado<EV,AC> {
    /**
     * Atributos privados da classe Estado: transicoes e nome.
     * 
     *  O atributo transicoes é um HashMap onde todos os eventos que podem ocorrer 
     *  no ambiente estão ligados a uma resposta da Máquina de Estados, ou seja a
     *  resposta é constituída por, a transição que deve ser efetuada, o estado seguinte
     *  e a ação que o personagem deve executar.
     * 
     *  O atributo nome é a forma de referir o estado.
     */
    private Map<EV, Transicao<EV,AC>> transicoes;
    private String nome;

    /**
     *  Método construtor da classe.
     *  
     *  Faz a criação do HashMap que associa cada evento a uma transição.
     *  @param nome referente ao estado.
     */
    public Estado(String nome) {
        transicoes = new HashMap<>();
        this.nome = nome;
    }

    /**
     *  Método que retorna o nome do estado.
     * 
     *  @return nome do estado.
     */
    public String getNome() {
        return nome;
    }

    /**
     *  Método que dependendo do Evento que está a ser Percepcionado pela personagem,
     *  o processa tendo como retorno a transição que foi efetuada pela máquina de estados.
     *  Isto é feito através da verificação da entrada do HashMap referente à chave com o 
     *  evento, recebendo assim a transição necessária.
     * 
     * @param evento evento percepcionado pelo Personagem no Ambiente.
     * @return transição a ser efetuada.
     */
    public Transicao<EV,AC> processar(EV evento) {
        return transicoes.get(evento);
    }

    /**
     *  Método que adiciona ao HashMap da qual a classe é composta uma entrada na chave do
     *  Evento recebido, associando-lhe uma transição.
     * 
     *  Nesta função é feita a adição de uma transição onde o Personagem não tem de realizar
     *  qualquer ação. Isto é feito através da chamada de outro método da classe com o mesmo nome
     *  mas que recebe também uma Accao que á a ação que deve ser desempenhada.
     * 
     *  @param evento entrada do HashMap, evento que indica a transição que será guardada.
     *  @param estadoSucessor estado seguinte quando ocurre o evento recebido.
     *  @return instância do próprio de si mesmo.
     */
    public Estado<EV,AC> transicao(EV evento, Estado<EV, AC> estadoSucessor){
        return transicao(evento, estadoSucessor, null);
    }

    /**
     *  Método que adiciona ao HashMap da qual a classe é composta uma entrada na chave do
     *  Evento recebido, associando-lhe uma transição.
     * 
     *  Nesta função é guardada na entrada do evento recebido um objeto da classe Transicao
     *  que foi criado nesta função com os pârametros recebidos.
     * 
     *  @param evento entrada do HashMap, evento que indica a transição que será guardada.
     *  @param estadoSucessor estado seguinte quando ocurre o evento recebido.
     *  @param accao ação a realizar pela personagem na ocurrência do evento recebido.
     *  @return instância do próprio de si mesmo.
     */
    public Estado<EV,AC> transicao(EV evento, Estado<EV,AC> estadoSucessor, AC accao) {
        transicoes.put(evento, new Transicao<EV,AC>(estadoSucessor, accao));
        return this;
    }
}
