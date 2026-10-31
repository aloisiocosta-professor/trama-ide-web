# Laboratorio de correspondencias UML–Java–estado

Prototipo de referencia para investigacao, separado da distribuicao web Trama IDE. Implementacao propria em Java/Swing; usa objetos Java reais, nao uma simulacao em JavaScript. Nao e plugin oficial de BlueJ, Umbrello ou JIVE.

## Executar

Requer JDK 17 ou posterior e ambiente grafico desktop compativel com Swing. A compilacao sempre deve acompanhar o fonte exibido:

```sh
mkdir -p prototype/out
javac --release 17 -encoding UTF-8 -d prototype/out prototype/src/*.java
java -cp prototype/out LabApp prototype/src/BankAccount.java linked
```

Para a condicao de comparacao, substitua `linked` por `plain`. O executor, as operacoes, as perguntas e os valores sao os mesmos; mudam os destaques e as mensagens de correspondencia. Nao e aplicativo web, APK nem solucao testada em Omalauncher.

## Experimentar

1. Crie `contaAna` com saldo `100.00`.
2. Crie `contaBruno` com saldo `20.00`.
3. Selecione contaAna, escreva e guarde uma previsao antes da chamada.
4. Informe `25.00` e execute deposit.
5. Compare identidade/saldo das duas contas e os estados antes/depois.
6. Escreva e guarde uma explicacao; exporte a sessao local se desejar.
7. Para um alias, selecione uma referencia existente, informe um nome novo e use Criar alias. Isso nao cria um novo objeto.

Respostas sao armazenadas em memoria ate exportacao explicita para um TSV local. A cronologia registra o numero de eventos bem-sucedidos existente no momento da resposta; nao impede respostas fora da sequencia planejada. O protocolo deve conferir a aderencia. Nada e enviado para a rede.

## Geracao estrutural e edicao

```sh
python3 prototype/generate.py prototype/model.json generated/BankAccount.java
```

O arquivo de saida deve ser novo; o gerador nao sobrescreve. E um subconjunto estrutural de classe, atributos, construtor e metodos. Corpos lancam UnsupportedOperationException ate implementacao pelo programador. O exemplo em src/BankAccount.java ja tem corpos implementados separadamente e marcadores de mapeamento; gerar o esqueleto nao recria esses corpos ou marcadores. O gerador nao e um parser geral de UML/Java nem oferece sincronizacao bidirecional.

## Verificar

```sh
python3 tools/build_research.py
```

Executa verificacoes do gerador, compila esqueleto e exemplo implementado, roda testes sem participantes e renderiza ambas as condicoes fora da tela e exercita criacao, chamadas, respostas e exportacao em display virtual com xvfb-run. O script exige javac/java no PATH. Testes de interface fora da tela verificam componentes e renderizacao; nao equivalem a estudo de usabilidade ou validacao manual de todos os controles.

## Limites

Um exemplo, uma classe, um atributo e um conjunto restrito de operacoes; sem relacoes entre classes, edicao UML interativa ou interpretacao de Java arbitrario. O fonte pode ser editado externamente e recompilado. Os destaques apontam para regioes de metodo declaradas por marcadores, nao para cada instrucao executada pela JVM. O snapshot captura estados nas fronteiras da chamada. Falhas preservam o estado e sao exibidas, mas nao entram no historico de chamadas bem-sucedidas. Nao ha time travel, debugger geral, persistencia automatica ou resultados educacionais.

O mecanismo e um demonstrador experimental, nao uma afirmacao de novidade frente a BlueJ/JIVE. Antes de uso com estudantes, resolver revisao de instrumentos, acessibilidade, contexto e procedimentos institucionais pertinentes.
