# Validacao tecnica do demonstrador

Execucao real: https://github.com/aloisiocosta-professor/trama-ide-web/actions/runs/39083293325 . Commit avaliado: 5cf946e5a77439c3c41759536c006d6d8a2e3810 . Data UTC: 18/10/2026 00:35. JDK Temurin 17.0.20.1, Ubuntu runner.

Resultado observado: 28 verificacoes Java e cinco testes Python passaram. Zero participantes. Estados de instancias independentes, alias, valores decimais, rejeicao de chamadas invalidas, snapshots, mapeamento, igualdade semantica A/B, diferenca de destaque, cronologia de respostas e renderizacao fora da tela foram verificados. Esqueleto gerado e exemplo implementado foram compilados separadamente.

Arquivos originais da execucao estao em evidence/ci-5cf946/. ZIP original conferido por SHA-256 d35acf54ef7ef5d16dc045689df120d18c1737239e3d3e46eddcfce0bb3ca1f9 . Fontes e seus hashes estao no resultado JSON.

| Requisito do protocolo | Evidencia | Alcance |
|---|---|---|
| R1 | Cartao UML e modelo de BankAccount | Uma classe/exemplo; sem editor UML geral |
| R2 | Geracao e compilacao de esqueleto | Corpos precisam ser implementados; sem sincronizacao bidirecional |
| R3 | Testes distinct instances e alias identity | Objetos reais JVM |
| R4 | Deposito, retirada, getter e rejeicoes | Subconjunto fixo |
| R5 | Snapshots imutaveis e saldo independente | Fronteiras de chamadas, sem rastrear instrucao a instrucao |
| R6 | Mapeamento deposit e marcadores obrigatorios | Regioes declaradas de fonte, nao debugger |
| R7 | Registro local com cronologia de eventos | Sem piloto humano; exportacao manual ainda requer ensaio interativo |

As duas imagens foram produzidas pelo painel Swing fora da tela. A imagem linked foi inspecionada visualmente nesta sessao; o conteudo principal estava visivel com rolagem para linhas extensas. Isso nao equivale a teste de usabilidade ou acessibilidade com participantes.

Conclusao permitida: o demonstrador executou os cenarios tecnicos previstos. Nao se conclui eficacia educacional, novidade, aptidao comercial ou validade dos instrumentos. A issue #8 permanece em revisao ate completar os requisitos de aceitacao pertinentes, inclusive ensaio interativo de registro/exportacao.

## Atualizacao de aceite tecnico — 18/10/2026

O commit 89a84aa3132eb6c369a2dfe7ff2057716fe4b0df passou em 28 verificacoes Java, cinco testes do gerador e nove verificacoes graficas em display virtual. O ensaio criou contas por botoes, chamou metodo, registrou respostas e exportou TSV pelo seletor real. Corrigida a abertura da visualizacao de estado no fim da linha e o recorte de rotulo UML; as regressões passaram. Execucao: https://github.com/aloisiocosta-professor/trama-ide-web/actions/runs/39104951676 . Evidencias originais adicionais em evidence/ci-89a84a/.

A issue #8 foi fechada como completed para o prototipo minimo desse escopo. A pendencia de ensaio funcional de exportacao foi resolvida por teste grafico automatizado e inspecao visual da captura; nao se substitui avaliacao de usabilidade com pessoas. A evidencia inicial acima permanece historica.
