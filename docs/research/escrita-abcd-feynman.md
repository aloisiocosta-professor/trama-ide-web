# Aplicação de ABCD e Feynman à escrita do Projeto Integrador

## Decisão de escrita

O autor pediu ABCD, técnica Feynman e preferência por citações indiretas nas quatro seções do trabalho. Como a sigla não foi definida na conversa, adota-se provisoriamente **A de Afirmação, B de Base em evidências, C de Conexão com o projeto e D de Desdobramento**. Essa é uma convenção editorial explícita para esta revisão, não uma norma científica universal nem uma definição atribuída a um autor sem fonte.

ABCD organiza a argumentação; Feynman orienta a clareza. Nenhuma das duas práticas é apresentada como desenho experimental, garantia de aprendizagem ou demonstração de eficácia do software. Não foi realizado um teste de compreensão com o autor ou com estudantes nesta revisão.

## Como a combinação foi aplicada

| Passo | Pergunta usada na revisão | Aplicação concreta |
|---|---|---|
| A Afirmação | Qual ideia este trecho sustenta? | As vistas mostram estrutura, implementação e estado do mesmo exemplo |
| B Base | Qual fonte ou observação sustenta essa ideia? | Literatura para fundamentos; logs e fontes do projeto para comportamentos implementados |
| C Conexão | Como explicar a relação em um caso simples? | Conta com saldo 100 recebe 25 e passa a 125; outra conta mantém 20 |
| D Desdobramento | O que isso permite concluir e o que falta verificar? | Cenário funcional verificado; aprendizagem ainda não examinada |

O roteiro foi usado para orientar os parágrafos e a progressão entre eles, sem inserir letras A B C D artificialmente no corpo acadêmico. Os objetivos permanecem no formato exigido pelo modelo: um geral e dois específicos no infinitivo.

Para aplicar Feynman, foram substituídas ou explicadas expressões técnicas, usados exemplos pequenos, procuradas lacunas de explicação e retomadas as evidências para corrigir simplificações. Por exemplo: em lugar de apenas mencionar snapshots, a metodologia explica que o executor conserva os estados de antes e de depois da operação. A referência é explicada como meio de acesso ao objeto; dois nomes para a mesma conta não são tratados como dois objetos. O exemplo de conta é um recurso de explicação, não uma afirmação sobre sistemas bancários reais.

## Mapa das quatro seções

| Seção | Afirmação e base | Conexão simples e desdobramento |
|---|---|---|
| Introdução | Relações entre classe e objetos motivam o demonstrador; Lu e Alexandru 2023 e Rexigel et al. 2024 fundamentam o recorte | Distinguir descrição da conta, conta criada e saldo; formular pergunta técnica sem prometer ganho educacional |
| Metodologia | Levantamento, análise documental e construção com testes; aproximação com Johannesson e Perjons 2021 | Explicar o que foi construído, qual valor era esperado e qual foi observado; delimitar o alcance dos testes |
| Referencial teórico | Conceitos, múltiplas representações e antecedentes documentados | Relacionar cada fundamento ao exemplo e às escolhas de implementação; separar inspiração de resultado próprio |
| Considerações finais | Resultados das execuções e antecedente BlueJ | Responder à pergunta técnica, explicar o exemplo 100 mais 25 e declarar etapas futuras necessárias |

## Evidências e citações indiretas após a atualização temporal

Em 18/10/2026, o autor restringiu a base a publicações de 2016–2026, preferindo 2021–2026. A fundamentação ativa do DOCX passou a usar cinco fontes de 2021–2026, incluindo uma publicação de agosto de 2026. As fontes antigas continuam no histórico e nos materiais anteriores; não sustentam a redação atual da entrega.

As paráfrases atribuem aos autores apenas as ideias consultadas. Os resultados da ferramenta permanecem evidências próprias. A matriz em matriz-fontes-2016-2026.csv registra fonte, desenho, acesso real, uso e limites. A pesquisa é exploratória; não se declara cobertura exaustiva de 2016–2026. O recorte se refere ao ano da publicação usada, sem afirmar que todos os estudos reunidos pelas revisões sejam recentes.

A linguagem foi adaptada a leitores sem formação em computação: Java é apresentado como linguagem de instruções; objeto, como uma conta criada no exemplo; saldo, como um dado guardado; UML, como notação de desenho. Termos como JVM, alias, traces, snapshots e nomes linked/plain foram retirados do corpo principal. Detalhes de reprodução continuam no apêndice técnico.

O mapa anterior de ABCD continua a orientar a escrita, com nova base: Johannesson e Perjons 2021 no método, Lu e Alexandru 2023 nas ferramentas, Rexigel et al. 2024 na combinação de formas de apresentação, Sibia et al. 2026 nas diferenças de uso e Yusuf e Noor 2023 nos limites da literatura. ABCD e Feynman permanecem escolhas editoriais, sem alegação de validação experimental.

## Critérios de revisão e estado

As quatro seções foram reescritas, com definições simples, exemplos e delimitação das evidências. O texto continua sendo uma versão de revisão. Persistem identificação da escola, curso, autores, professor e cidade, revisão humana das fontes e exigências complementares. O prazo permanece 31/10/2026. Não foram fabricados resultados nem encerradas issues científicas por uma melhoria editorial.

A conferência estrutural verifica presença de seções, citações, estilos e coerência do sumário com a renderização. A inspeção das páginas verifica legibilidade e diagramação; nenhuma delas substitui avaliação acadêmica do conteúdo.
