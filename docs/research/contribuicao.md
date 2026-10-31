# Delimitacao da contribuicao — v0.2

Contexto-alvo: ensino introdutorio de orientacao a objetos com Java, especialmente em cursos superiores. Instituicao e turma nao foram identificadas; nao existe diagnostico local nem amostra recrutada.

Problema investigavel: estudantes podem ter dificuldade de relacionar declaracoes de classes, referencias para instancias e mudancas de estado ao executar metodos. O artigo de Kolling e colaboradores discute essas abstracoes e apresenta interacao direta com classes e objetos; isso fundamenta o problema pedagogico geral, nao sua incidencia em uma turma especifica [1, secoes 3.1–3.3 e 5.1].

**Contribuicao principal delimitada:** um instrumento experimental aberto, com executor Java compartilhado entre duas condicoes visuais, para investigar o efeito adicional de correspondencias explicitas entre UML, fonte e snapshots de objetos. A entrega tecnica e sua verificacao sao diferentes da hipotese de aprendizagem.

Nao se reivindica a invencao de diagramas ligados a execucao. BlueJ ja possui diagrama de classes e interacao com objetos. JIVE usa representacoes de execucao baseadas em UML. Portanto, novidade e vantagem educacional permanecem questoes a avaliar; a existencia de um prototipo nao as demonstra.

Mecanismo delimitado: destaque de membro UML e regiao correspondente do fonte, ligado ao receptor e aos estados antes/depois da chamada. A condicao plain apresenta o mesmo exemplo, executor e tarefas, sem os destaques e mensagens extras de correspondencia. Isso favorece controle experimental, mas nao elimina possiveis efeitos de atencao ou familiaridade.

Escopo inicial: BankAccount, saldo decimal, criar duas instancias, depositar, retirar, consultar e demonstrar alias. Fora do escopo: Java arbitrario, IDE completa, todos os diagramas UML, eventos internos de cada instrucao, sincronizacao bidirecional ou eficacia comprovada.

Decisao de engenharia: construir um demonstrador independente pequeno, em vez de recriar BlueJ/Umbrello ou presumir que um plugin existente seja insuficiente. Esta escolha atende a verificabilidade do experimento; migrar para extensao continua possivel apos avaliar contexto e alternativas. Nao e argumento de superioridade comercial.

## Criterio de aceite da delimitacao

Publico, contexto-alvo, dificuldade, mecanismo, contribuicao e limites definidos. Ainda sao necessarios diagnostico local, revisao aprofundada e revisao do autor. A especificacao nao implica que o estudo possa recrutar participantes.

[1] Kolling et al. (2003). DOI: https://doi.org/10.1076/csed.13.4.249.17496 . Secoes consultadas na copia de autor: https://www.cs.kent.ac.uk/pubs/2003/2190/content.pdf .
