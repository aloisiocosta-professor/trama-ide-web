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
| Introdução | Relações entre classe e objetos motivam o demonstrador; BlueJ e DeFT fundamentam o recorte | Distinguir descrição da conta, conta criada e saldo; formular pergunta técnica sem prometer ganho educacional |
| Metodologia | Levantamento, análise documental e construção com testes; aproximação com Hevner et al. | Explicar o que foi construído, qual valor era esperado e qual foi observado; delimitar o alcance dos testes |
| Referencial teórico | Conceitos, múltiplas representações e antecedentes documentados | Relacionar cada fundamento ao exemplo e às escolhas de implementação; separar inspiração de resultado próprio |
| Considerações finais | Resultados das execuções e antecedente BlueJ | Responder à pergunta técnica, explicar o exemplo 100 mais 25 e declarar etapas futuras necessárias |

## Evidências e citações indiretas

Paráfrases atribuem ideias aos autores sem reproduzir suas frases. Os exemplos de implementação são identificados como resultados do projeto, sem atribuí-los a esses autores. A literatura consultada não é apresentada como experimento realizado pelo projeto.

| Fonte | Uso delimitado nesta revisão | Evidência consultada |
|---|---|---|
| Kölling et al. 2003 | Antecedente de classes, criação e interação com objetos; limite à novidade ampla | Texto original, seções 3.1–3.3: https://www.cs.kent.ac.uk/pubs/2003/2190/content.pdf |
| Ainsworth 2006 | Desenho, funções e tarefas no uso de múltiplas representações | Resumo e partes conceituais do original: https://www.inf.ufpr.br/alexd/REPRESENTACOES_EXTERNAS/Ainsworth_2006.pdf ; DOI 10.1016/j.learninstruc.2006.03.001 |
| Hundhausen Douglas e Stasko 2002 | Importância das atividades com visualização; sem extrapolar efeito para esta ferramenta | Resumo e discussão 6.1 consultados: https://faculty.cc.gatech.edu/~stasko/papers/jvlc02.pdf ; DOI 10.1006/jvlc.2002.0237 |
| Hevner et al. 2004 | Construção e avaliação de artefatos; sem alegar ciclo educacional completo | Resumo e registro original: https://aisel.aisnet.org/misq/vol28/iss1/6/ ; DOI 10.2307/25148625 |
| Moreno et al. 2004 e Gestwicki e Jayaraman 2004 | Antecedentes de visualização, com alcance documental | Registros originais já conferidos na matriz do projeto; DOI 10.1145/989863.989928 e 10.1145/1028664.1028762 |
| Evidência própria | 28 verificações Java, cinco testes Python e nove verificações gráficas nas versões indicadas | docs/research/evidence/ci-5cf946/ e ci-89a84a/; participantes iguais a zero |

Foram reconferidas em 18/10/2026 as fontes primárias acima indicadas como consultadas nesta revisão. Isso não é declaração de leitura integral de todos os artigos nem auditoria completa de retratações. As limitações bibliográficas anteriores continuam válidas.

## Critérios de revisão e estado

As quatro seções foram reescritas, com definições simples, exemplos e delimitação das evidências. O texto continua sendo uma versão de revisão. Persistem identificação da escola, curso, autores, professor e cidade, revisão humana das fontes e exigências complementares. O prazo permanece 31/10/2026. Não foram fabricados resultados nem encerradas issues científicas por uma melhoria editorial.

A conferência estrutural verifica presença de seções, citações, estilos e coerência do sumário com a renderização. A inspeção das páginas verifica legibilidade e diagramação; nenhuma delas substitui avaliação acadêmica do conteúdo.
