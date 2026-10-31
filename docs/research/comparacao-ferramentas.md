# Comparacao documental de alternativas — v0.2

Consulta: 17/10/2026, America/Fortaleza. Nao e benchmark, teste de usabilidade ou auditoria exaustiva. "Nao verificado" nao significa que o recurso nao existe. Capacidades historicas nao sao garantia de compatibilidade de uma versao atual.

| Ferramenta | Capacidade sustentada pela fonte | Relacao com a proposta | Limite da verificacao |
|---|---|---|---|
| BlueJ | Classes UML, criacao de objetos, chamadas de metodos e inspecao de campos | Antecedente direto; invalida novidade por simples integracao | Artigo e documentacao; sem instalacao/ensaio nesta sessao |
| Umbrello | Modelagem e geracao de declaracoes de classes, atributos e metodos | Fundamenta passagem de modelo para estrutura do codigo | Manual oficial; nao se conclui ausencia de recursos fora das paginas consultadas |
| Jeliot 3 | Visualizacao automatica/semi-automatica de dados e controle para iniciantes | Antecedente de visualizacao da execucao | Resumo original, nao texto integral |
| JIVE | Visualizacoes de estrutura de objetos, historico, consultas e navegacao na execucao | Antecedente forte de UML relacionada a comportamento dinamico | Artigo curto, site e secoes de relatorio tecnico; sem teste instalado |
| Trama IDE Web | Edicao UML e de fontes; execucao completa e anunciada para Linux, nao para web/APK | Produto ja existente no repositorio; mecanismo experimental nao presumido | README publico lido; sem ensaio funcional |
| Demonstrador deste projeto | Duas condicoes do mesmo executor, snapshots por chamada e mapeamento de regioes de fonte | Instrumento de pesquisa delimitado; uma classe/exemplo | Codigo produzido; resultados dependem da execucao tecnica registrada |

## Consequencia para o argumento cientifico

A proposta precisa ser avaliada como desenho de um mecanismo e de seu estudo, sem afirmar que e a primeira ferramenta desse tipo. A comparacao funcional instalada e a revisao mais ampla permanecem pendentes. O recorte de uma classe simplifica a analise, mas limita generalizacao para heranca, colecoes, concorrencia e sistemas reais.

## Fontes originais

- BlueJ: https://www.cs.kent.ac.uk/pubs/2003/2190/content.pdf ; https://www.bluej.org/about.html .
- Umbrello: https://docs.kde.org/stable_kf6/en/umbrello/umbrello/code-import-generation.html .
- Moreno et al. (2004), Visualizing programs with Jeliot 3: https://doi.org/10.1145/989863.989928 ; registro institucional https://weizmann.elsevierpure.com/en/publications/visualizing-programs-with-jeliot-3/ .
- Gestwicki e Jayaraman (2004), JIVE: https://doi.org/10.1145/1028664.1028762 ; https://cse.buffalo.edu/jive/ .
- Lessa, Czyz e Jayaraman, JIVE: A Pedagogic Tool for Visualizing the Execution of Java Programs: relatorio tecnico 2010-13, copia com cabecalho de submissao SIGCSE 2011; nao tratado como artigo aceito: https://www.cse.buffalo.edu/tech-reports/2010-13.pdf .
- Trama IDE Web: https://github.com/aloisiocosta-professor/trama-ide-web/blob/main/README.md .
