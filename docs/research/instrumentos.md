# Instrumentos de avaliacao — rascunho para revisao e piloto

18/10/2026. Uso futuro condicionado ao contexto e aos procedimentos institucionais pertinentes. Instrumentos criados para este projeto; nao foram validados, aplicados ou respondidos por participantes. Este arquivo contem perguntas e gabaritos, nao resultados.

## A. Teste conceitual: seis itens, 0–12 pontos

Orientacao: mostrar o codigo e os valores iniciais, pedir previsao e justificativa sem executar. Tempo-alvo e dificuldade serao aferidos no piloto, nao impostos como medida validada. Usar formas paralelas A/B em ordem contrabalancada, se o piloto confirmar viabilidade. Elas nao sao presumidas psicometricamente equivalentes.

### Forma A — deposito/contadores

Considere que cada objeto Contador inicia com o numero recebido e que adicionar(x) soma x apenas ao atributo valor do receptor; ler() retorna valor sem modifica-lo.

```java
Contador a = new Contador(20);
Contador b = new Contador(5);
Contador c = a;
a.adicionar(7);
```

1. Quantas classes/tipos de dominio e quantos objetos foram apresentados? Diferencie referencia e objeto. **Gabarito:** um tipo Contador; dois objetos; tres referencias, c e a designam a mesma instancia.
2. Qual e o valor de b apos a chamada? Por que? **Gabarito:** 5; b referencia outro objeto.
3. Qual e o valor acessivel por a e qual objeto recebeu a chamada? **Gabarito:** 27; a instancia referenciada por a, nao a classe inteira.
4. Se c.adicionar(3) ocorrer em seguida, quais valores sao acessiveis por a, b e c? **Gabarito:** 30, 5, 30; a e c compartilham identidade.
5. Uma chamada a.ler() muda o estado? Diferencie retorno de alteracao. **Gabarito:** nao neste contrato; retorna o valor atual.
6. O atributo valor declarado na classe corresponde a um unico numero compartilhado por todos? Relacione declaracao e instancias. **Gabarito:** nao; neste exemplo e atributo de instancia, com estado por objeto; duas referencias ao mesmo objeto observam o mesmo estado.

### Forma B — transferencia proxima para estoque

Considere que cada Estoque inicia com a quantidade recebida; receber(x) soma x a quantidade do receptor e consultar() retorna quantidade sem altera-la.

```java
Estoque x = new Estoque(30);
Estoque y = new Estoque(8);
Estoque z = x;
x.receber(4);
```

Aplicar os mesmos seis tipos de pergunta substituindo nomes/metodos. Gabaritos: um tipo, dois objetos, tres referencias; y=8; x=34; apos z.receber(2), x=36, y=8, z=36; consultar nao modifica; atributo de instancia nao e uma variavel estatica compartilhada. Essa mudanca de dominio mede transferencia proxima, nao transferencia distante.

### Rubrica por item

- **2 pontos:** resposta correta com justificativa compativel com classe, identidade e estado conforme o item.
- **1 ponto:** resposta parcialmente correta ou numero correto sem justificativa conceitual suficiente; registrar a razao.
- **0 pontos:** resposta incorreta, contraditoria ou em branco. Branco tambem deve ser distinguido como ausencia de resposta na base.

Revisar ambiguidades com docentes antes do piloto. Recomenda-se que dois avaliadores corrijam respostas abertas sem conhecer a condicao do estudante. Divergencias, acordo e adjudicacao devem ser registrados. Nao calcular confiabilidade sem respostas reais.

## B. Atividade guiada em ambas as condicoes

1. Criar duas contas independentes com saldos definidos na tarefa.
2. Registrar uma previsao antes de depositar em uma delas.
3. Executar e inspecionar os dois estados.
4. Registrar explicacao apos a chamada.
5. Criar alias e prever uma nova mudanca.
6. Exportar a sessao local em local acordado no protocolo de dados.

Identificar tarefa, evento anterior/posterior, previsao e explicacao. Os registros do prototipo incluem contagem de eventos, mas nao impedem registro tardio. O observador deve registrar violacoes de sequencia; regra de tratamento sera fixada antes da analise.

## C. Observacao de uso

Campos previstos: pseudonimo, versao, condicao, tarefa, inicio/fim, sucesso, erro, ajuda, observacao e falha tecnica. Categorias iniciais: selecao do receptor errado, confusao entre classe e instancia, confusao entre alias e copia, entrada invalida, dificuldade de navegar no fonte, exportacao e erro do sistema. Revisar categorias a partir do piloto.

Exito operacional nao equivale a compreensao. Tempos e erros nao devem substituir o teste conceitual.

## D. Entrevista curta com estudante/docente

- Em qual momento foi dificil relacionar o diagrama ao codigo ou ao objeto?
- Como voce explica a diferenca entre criar outro objeto e criar outra referencia?
- O que a ferramenta ajudou a perceber? O que ela dificultou?
- Que atividade de aula faria sentido com esse recurso? Que alternativa voce usa hoje?

Perguntas abertas sem pressupor beneficio. Evitar perguntar apenas se a ferramenta e boa. Consentimento e registro seguem o plano institucional pertinente.

## E. Adocao comercial, em estudo separado

Perguntar ao comprador sobre a ultima decisao real de compra/adocao de ferramenta, quem participa, restricoes, alternativas e processo. Depois apresentar oferta concreta com escopo e preco ainda a decidir. Registrar recusa, aceite e razoes; intencao hipotetica nao e venda.
