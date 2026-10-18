# Protocolo de pesquisa — UML e experimentação de objetos Java

Versão 0.1 — 17 de outubro de 2026, America/Fortaleza.
Status: proposta metodológica para revisão; sem implementação, coleta ou resultados empíricos.
Título provisório: **Conexões explícitas entre UML, código Java e estado de objetos: desenvolvimento e avaliação de uma ferramenta educacional**.

## 1. Finalidade e pressupostos

O projeto pretende construir e avaliar uma ferramenta que permita ao estudante relacionar uma classe em UML, sua implementação Java e o estado de suas instâncias durante chamadas de métodos. A unidade de valor do produto será essa experiência integrada. Componentes de edição, geração estrutural e execução servirão a essa experiência; não serão tratados como contribuições científicas independentes.

Pressupostos de trabalho: estudantes iniciantes de orientação a objetos; ensino superior como contexto candidato; Java como linguagem; avaliação educacional como foco principal; investigação comercial exploratória e separada. Instituição, disciplina, participantes, plataforma, infraestrutura e veículo de publicação ainda não foram definidos. Nenhum desses pressupostos representa decisão institucional.

## 2. Problema e lacuna provisória

Problema investigável: estudantes podem executar operações sobre instâncias sem conseguir explicar a correspondência entre a classe, o objeto, seus atributos e as mudanças de estado. Sua presença e frequência no contexto escolhido precisam ser diagnosticadas por tarefas e entrevistas; não se presume que todos os estudantes apresentem essa dificuldade.

Kölling et al. [1] fundamentam o ensino de orientação a objetos com ferramentas específicas; Ainsworth [3] mostra que múltiplas representações exigem desenho e tarefas adequados. A combinação sustenta investigar correspondências explícitas, mas não comprova a insuficiência dos ambientes existentes nem o benefício da nova ferramenta.

**Lacuna candidata:** verificar se evidenciar as correspondências entre elementos UML, trechos Java e mudanças de estado oferece benefício adicional a uma experiência equivalente sem esse recurso. A lacuna só será afirmada após comparação funcional e leitura aprofundada da literatura.

A documentação oficial do BlueJ confirma criação e inspeção de objetos e invocação de métodos [9]. Portanto, essas capacidades não são novidade da proposta. Não se afirmará que o produto é o primeiro, único ou superior sem evidências próprias.

## 3. Perguntas e objetivos

**Pergunta principal:** em atividades introdutórias de orientação a objetos em Java, qual é o efeito de correspondências visuais explícitas entre UML, código e estado de objetos sobre a compreensão de classes, instâncias e mudanças de estado?

**Perguntas secundárias:** quais dificuldades de uso surgem? Que utilidade professores e estudantes percebem? Professores identificam condições viáveis para adoção?

**Objetivo geral:** desenvolver e avaliar um artefato educacional que explicite essas correspondências.

Objetivos específicos:
1. Diagnosticar dificuldades do contexto e analisar ferramentas existentes.
2. Derivar requisitos da literatura e do diagnóstico, com rastreabilidade.
3. Implementar o fluxo mínimo e verificar sua correção funcional.
4. Avaliar compreensão conceitual, usabilidade e percepção de utilidade.
5. Caracterizar limites, condições de uso e implicações para desenvolvimento futuro.

**Hipótese direcional provisória:** a condição com correspondências explícitas apresenta melhor desempenho em tarefas conceituais de transferência do que a condição equivalente sem elas. Não se estabelece magnitude esperada sem dados ou estudos comparáveis. Resultado nulo ou desfavorável será relatado.

## 4. Mecanismo proposto

Problema → intervenção → consequência intermediária → evidência:

- Dificuldade de associar classe e instância → selecionar uma classe destaca seu código e suas instâncias → correspondências ficam observáveis → tarefas de identificação e explicação.
- Dificuldade de compreender estado por instância → chamada de método evidencia objeto receptor e valores antes/depois → torna-se observável qual objeto mudou → previsões e justificativas sobre duas instâncias.
- Observação passiva da execução → atividade pede prever, executar e explicar → estudante confronta previsão e comportamento → respostas conceituais e evidências qualitativas.

Essas são explicações hipotéticas. Cliques, permanência na tela ou satisfação não demonstram que o mecanismo produziu aprendizagem. Se perguntas guiadas, conteúdo e interface mudarem juntos, o efeito será atribuído ao conjunto, sem isolar artificialmente a visualização.

## 5. Revisão e análise de alternativas

Será realizada revisão estruturada, inicialmente exploratória, com clássicos fundacionais e busca de publicações recentes. Não será chamada de revisão sistemática sem protocolo, cobertura e procedimentos compatíveis.

Fontes a consultar: ACM Digital Library, IEEE Xplore e editoras/repositórios institucionais; outras bases dependerão do acesso. Google Scholar poderá apoiar descoberta e encadeamento de citações. Essas consultas futuras ainda não foram executadas.

Consultas planejadas:
- ("object-oriented programming" OR "Java") AND ("program visualization" OR "object visualization") AND (learning OR teaching)
- ("UML" OR "class diagram") AND ("multiple representations" OR "runtime" OR "object interaction") AND education
- ("educational software" OR "programming tools") AND ("technology acceptance" OR adoption OR "willingness to pay")

Registrar, para cada execução: data e fuso, base, consulta exata adaptada, campos/filtros, quantidade retornada, exportação e exclusões justificadas. Deduplicar por DOI e, depois, título/autoria. Incluir fontes com contribuição direta a requisitos, mecanismos ou avaliação. Excluir materiais sem identificação verificável, divulgação comercial usada como prova de eficácia e duplicatas; documentação oficial será mantida apenas como evidência técnica.

Extrair autoria, ano, DOI, tipo de publicação, contexto, participantes quando disponíveis, método, comparação, medidas, resultados, limitações, acesso ao texto e situação de correções/retratações. Ausência de alerta em uma página não equivale a verificação completa de integridade.

Comparar BlueJ, Umbrello e candidatos encontrados, registrando versão, tarefa reproduzível e evidência de cada capacidade. Campos mínimos: modelo de classes, fidelidade de relações UML, geração estrutural Java, criação de instâncias, inspeção, chamadas de métodos e correspondências visuais. Distinguir capacidade documentada de comportamento testado.

**Porta de decisão:** se uma ferramenta existente atender ao mecanismo, avaliar extensão ou estudo sobre ela antes de justificar um novo ambiente.

## 6. Artefato mínimo e critérios funcionais

| ID | Requisito | Verificação de aceite |
|---|---|---|
| R1 | Representar classe, atributos e métodos em um subconjunto UML declarado | Modelo de exemplo corresponde às declarações Java |
| R2 | Gerar estrutura Java editável | Projeto de exemplo compila após implementação dos corpos necessários |
| R3 | Criar duas instâncias da mesma classe | Identidades e estados permanecem distinguíveis |
| R4 | Invocar método com parâmetros e apresentar retorno ou erro | Resultado coincide com execução Java de referência |
| R5 | Inspecionar estado antes/depois | Valores exibidos correspondem aos objetos reais |
| R6 | Evidenciar correspondências entre representações | Seleção aponta aos elementos corretos, sem associações falsas |
| R7 | Aplicar a sequência prever–executar–explicar | Respostas podem ser registradas conforme protocolo de dados |

A geração de estrutura não significa geração automática do comportamento completo. O subconjunto UML e as restrições de Java devem ser documentados. Não se promete sincronização bidirecional geral entre código arbitrário e UML.

Fora do primeiro escopo: todos os diagramas UML, colaboração simultânea, IA generativa, marketplace, sistema completo de gestão de turmas e implantação comercial. Plataforma e mecanismo de execução serão definidos após análise técnica. Execução de código exige política de isolamento, tempo e recursos compatível com o ambiente escolhido, a validar antes de disponibilização a participantes.

Exemplo condutor: duas instâncias de ContaBancaria, chamada de depositar em apenas uma e explicação do estado de ambas. Usar outro domínio no pós-teste para verificar transferência, e não memorização do exemplo.

## 7. Método e desenho de avaliação

Enquadramento proposto: Design Science Research [8], articulando problema, requisitos, construção e avaliação. O estudo educacional será um componente de avaliação do artefato; a publicação deverá descrever o que foi efetivamente realizado.

### 7.1 Diagnóstico e piloto

Entrevistas com docentes e tarefas iniciais com estudantes, quando autorizadas, investigarão dificuldades e adequação curricular. O piloto verificará instruções, duração, legibilidade, acessibilidade, funcionamento e critérios da rubrica. Sua finalidade principal não é estimar eficácia.

Quantidade de participantes do piloto: a definir pela diversidade de perfis e viabilidade. Alterações serão registradas. Dados do piloto não serão automaticamente incorporados à análise confirmatória após mudanças nos instrumentos.

### 7.2 Comparação preferencial

Condição A: protótipo com correspondências explícitas.
Condição B: o mesmo protótipo com essas correspondências desativadas.

Manter iguais: conteúdo, exemplos, tempo, perguntas guiadas, instrução, recursos de execução e, quando possível, professor. Essa comparação permite investigar o incremento do recurso. Uma comparação adicional com BlueJ poderá avaliar o produto completo, mas não isola o mecanismo.

Aplicar pré-teste de conhecimento, intervenção com atividades equivalentes e pós-teste de transferência. Priorizar grupos paralelos com alocação aleatória quando viável. Se a alocação ocorrer por turma, considerar dependência entre estudantes e diferenças de contexto na análise. Caso só seja possível uma turma sem comparação, reformular o objetivo para viabilidade e compreensão exploratória; não manter uma alegação causal de superioridade.

### 7.3 Participantes e tamanho amostral

Definir instituição, disciplina, critérios de inclusão, experiência prévia, recrutamento e perdas antes da coleta. A amostra principal será planejada a partir do desfecho, do menor efeito educacional relevante, da precisão ou poder desejado e da estrutura de grupos. Não fixar número sem esse planejamento.

Se o recrutamento não permitir inferência adequada, tratar o estudo como exploratório e explicitar a imprecisão. Não interpretar ausência de significância como equivalência.

### 7.4 Medidas

**Desfecho primário proposto:** pontuação no pós-teste de transferência, considerando conhecimento inicial. Rubrica abordará classe/instância, estado por objeto, receptor da chamada e explicação de mudanças. Escala, itens, regras e análise serão fixados antes da coleta principal.

Medidas secundárias: desempenho por conceito, tempo e erros em tarefas, necessidade de ajuda, facilidade de uso e utilidade percebida. Questionários inspirados em Davis [5] exigem adaptação documentada; a validade original não se transfere automaticamente para uma tradução ou instrumento novo.

A rubrica será revisada quanto ao conteúdo. Quando houver respostas abertas, prever correção sem identificação da condição, dois avaliadores quando viável, acordo entre avaliadores e adjudicação. Se só houver um avaliador, declarar a limitação.

### 7.5 Análise

Publicar regras de exclusão, tratamento de ausências e análise antes de examinar resultados por condição. Para o desfecho primário, considerar modelo do pós-teste ajustado ao pré-teste e à estrutura da alocação, desde que compatível com os dados. Relatar estimativas, intervalos de confiança e relevância educacional, além de testes quando pertinentes.

Desfechos secundários serão identificados como tais; evitar selecionar apenas resultados favoráveis. Análises qualitativas registrarão categorias, processo de codificação e casos discrepantes. Mudanças pós-coleta serão rotuladas como exploratórias.

## 8. Ética, dados e rastreabilidade

Antes do recrutamento, confirmar com a instituição o enquadramento ético e os procedimentos exigidos. O protocolo não pressupõe aprovação, dispensa ou número de parecer. Se houver participantes menores, o plano deverá ser revisto com a instituição.

Prever participação voluntária, possibilidade de recusa sem prejuízo acadêmico, separação entre avaliação da disciplina e pesquisa, minimização de dados e medidas para reduzir coerção quando o pesquisador também for professor. Definir responsáveis, acesso, retenção, descarte e condições de compartilhamento.

Logs devem evitar nomes, senhas e conteúdo pessoal desnecessário. Materiais abertos serão anonimizados quando aplicável e compartilhados apenas conforme permissões. Dados individuais não serão publicados por padrão.

Identificar versão do software, ambiente, instrumentos e scripts usados. Controle de versão é recomendado; repositório remoto e visibilidade não estão definidos por este protocolo.

## 9. Validação comercial exploratória

Não confundir eficácia educacional, utilidade percebida e disposição real a pagar. Entrevistar docentes e responsáveis por compras separadamente; investigar problemas recentes, alternativas usadas, restrições e processo decisório.

Hipóteses candidatas:
- Professores percebem utilidade no fluxo durante aulas introdutórias.
- O esforço de preparação é aceitável no contexto.
- Um comprador considera uma oferta concreta de licença por turma ou semestre.

Registrar formato e preço de cada oferta, denominador de contatos, demonstrações, pilotos, propostas e conversões. Não cobrar nem fazer publicidade antes de existir oferta funcional descrita com clareza. O teste comercial demandará decisão própria de execução; este documento apenas o planeja.

Schmidt e Bijmolt [6] fundamentam cautela com respostas hipotéticas, mas tratam de bens de consumo. Camuffo et al. [7] fundamentam testes de hipóteses empreendedoras, sem garantir retorno deste produto.

Alegações descritivas verificáveis podem ser usadas quando implementadas: permite criar instâncias, executar métodos e inspecionar atributos. Alegações de ganho de aprendizagem ou economia de tempo exigem estudos próprios. Curtidas e intenção de compra não serão apresentadas como vendas.

## 10. Matriz de alegações

| Alegação | Situação atual | Evidência necessária |
|---|---|---|
| O mecanismo tem fundamentação teórica | Apoio inicial na literatura selecionada | Leitura integral e síntese crítica |
| A solução é tecnicamente funcional | Não demonstrado | Implementação e verificação dos requisitos |
| A proposta é inédita | Não demonstrado | Revisão e comparação de alternativas |
| A ferramenta melhora compreensão | Hipótese | Avaliação educacional adequada |
| Professores desejam utilizá-la | Hipótese | Estudo de adoção no contexto |
| Existe demanda pagante | Hipótese | Decisões reais de compra |
| Os resultados se aplicam a outras instituições | Não demonstrado | Replicação e diversidade contextual |

## 11. Plano de execução e critérios de conclusão

1. Consolidar revisão, diagnóstico e análise de alternativas. Aceite: problema contextualizado e contribuição reformulada conforme evidências.
2. Fixar protocolo, instrumentos, contexto e exigências institucionais. Aceite: plano exequível e condições para recrutamento atendidas.
3. Implementar e verificar o protótipo. Aceite: R1–R7 verificados e versão preservada.
4. Realizar piloto e revisar o protocolo. Aceite: instruções e instrumentos utilizáveis.
5. Executar estudo, analisar e documentar desvios. Aceite: resultados rastreáveis, incluindo perdas e incertezas.
6. Concluir e auditar o artigo. Aceite: pergunta respondida dentro do alcance dos dados; referências verificadas; limitações e materiais identificados.

Não há prazo absoluto proposto: calendário depende de acesso institucional, tamanho amostral, exigências éticas e desenvolvimento. Resultado nulo não impede conclusão; ausência de estudo impede alegar eficácia.

## 12. Estrutura de escrita

Introdução: problema contextual, alternativas, lacuna confirmada, objetivo e contribuição.
Referencial: ensino de objetos; múltiplas representações; interação ativa; ferramentas relacionadas. Adoção e preço serão incluídos conforme o escopo executado.
Método: DSR, requisitos, contexto, participantes, condições, instrumentos, ética e análise.
Artefato: arquitetura, mecanismo, limites e rastreabilidade dos requisitos.
Resultados: funcionamento, avaliação e incertezas sem discussão antecipada.
Discussão: resposta à pergunta, relação com literatura, explicações alternativas e ameaças à validade.
Conclusão: contribuição demonstrada e limites, sem extrapolação comercial.
Resumo e título definitivos: redigidos após resultados.

Cada parágrafo argumentativo deverá apresentar ideia, evidência, análise e implicação. Não inserir resultados simulados como se fossem observados. Se o estudo com participantes não puder ocorrer, alterar título e contribuição para desenvolvimento/viabilidade e declarar a avaliação educacional pendente.

## 13. Bibliografia inicial

As referências abaixo foram identificadas e discutidas em busca exploratória nesta conversa. Não se declara leitura integral de todas, revisão sistemática, checagem exaustiva de correções/retratações ou avaliação Qualis/JIF. Há artigos de periódicos, um trabalho de conferência e documentação técnica; não são equivalentes em finalidade.

[1] KÖLLING, M.; QUIG, B.; PATTERSON, A.; ROSENBERG, J. The BlueJ system and its pedagogy. Computer Science Education, v. 13, n. 4, p. 249–268, 2003. https://doi.org/10.1076/csed.13.4.249.17496

[2] LU, Y.; ALEXANDRU, C. Systematic Review of UML Diagramming Software Tools for Higher Education Software Engineering Courses. UKICER ’23, artigo 4, p. 1–7, 2023. https://doi.org/10.1145/3610969.3611123

[3] AINSWORTH, S. DeFT: A conceptual framework for considering learning with multiple representations. Learning and Instruction, v. 16, n. 3, p. 183–198, 2006. https://doi.org/10.1016/j.learninstruc.2006.03.001

[4] HUNDHAUSEN, C. D.; DOUGLAS, S. A.; STASKO, J. T. A Meta-Study of Algorithm Visualization Effectiveness. Journal of Visual Languages & Computing, v. 13, n. 3, p. 259–290, 2002. https://doi.org/10.1006/jvlc.2002.0237

[5] DAVIS, F. D. Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology. MIS Quarterly, v. 13, n. 3, p. 319–340, 1989. https://doi.org/10.2307/249008

[6] SCHMIDT, J.; BIJMOLT, T. H. A. Accurately measuring willingness to pay for consumer goods: a meta-analysis of the hypothetical bias. Journal of the Academy of Marketing Science, v. 48, p. 499–518, 2020. https://doi.org/10.1007/s11747-019-00666-6

[7] CAMUFFO, A.; GAMBARDELLA, A.; MESSINESE, D.; NOVELLI, E.; PAOLUCCI, E.; SPINA, C. A scientific approach to entrepreneurial decision-making: Large-scale replication and extension. Strategic Management Journal, v. 45, n. 6, p. 1209–1237, 2024. https://doi.org/10.1002/smj.3580

[8] HEVNER, A. R.; MARCH, S. T.; PARK, J.; RAM, S. Design Science in Information Systems Research. MIS Quarterly, v. 28, n. 1, p. 75–106, 2004. https://doi.org/10.2307/25148625

[9] BLUEJ. About BlueJ. Documentação oficial. https://www.bluej.org/about.html. Consulta: 17 out. 2026, America/Fortaleza. Capacidade documentada, não teste executado nesta tarefa.

## 14. Registro de busca e decisões pendentes

Busca anterior, 17 out. 2026: mecanismo de busca web; conferência em editoras e repositórios. Consultas registradas nesta conversa incluem:
- Kolling Quig Patterson Rosenberg 2003 BlueJ system environment teaching Java objects first
- "UML" "education" "systematic" "2023" review
- Ainsworth 2006 DeFT conceptual framework learning multiple representations
- Schmidt Bijmolt 2020 accurately measuring willingness to pay meta analysis hypothetical bias DOI
- site.misq.umn.edu "Design Science in Information Systems Research" Hevner 2004

Na elaboração deste protocolo foi consultada a página inicial do BlueJ e sua página About para conferir as capacidades documentadas. Não foi realizada nova revisão integral dos oito trabalhos nem teste funcional do BlueJ.

Pendências materiais: instituição/disciplina e acesso; contribuição após comparação; plataforma; plano amostral; instrumentos; enquadramento ético; veículo de publicação. Ausência dessas definições não impede esta versão de planejamento, mas impede congelar o estudo principal ou declarar o artigo concluído.

