# Governança da pesquisa e da sessão

Autorização: solicitação pública do usuário registrada no histórico, item 08.
Destino: https://github.com/aloisiocosta-professor/trama-ide-web
Branch inicial: docs/research-bootstrap
Issue principal: #1. Etapas: #2–#13. Governança: #14.

## Regra por interação
1. Ler mensagem e estado atual; recuperar pendências sem repetir perguntas.
2. Identificar issue(s) e critério(s) pertinente(s).
3. Registrar pergunta e resposta/pergunta final planejada em docs/session, junto das decisões.
4. Atualizar artefatos produzidos; distinguir fonte, inferência e proposta.
5. Atualizar inventario.json com hashes dos arquivos pertinentes, excluindo o próprio inventário. Verificar o necessário; criar commit convencional com referências a issues.
6. Sincronizar a branch e abrir/atualizar PR vinculado.
7. Conferir resultado remoto e comunicar links reais.
8. Se houver falha, preservá-la e informar o que não foi sincronizado.

Comentários de andamento são consolidados no registro da interação. O registro desta conversa foi reproduzido editorialmente a partir de mensagens disponíveis; não é exportação bruta. Outras sessões não são recuperadas automaticamente.

## PR e critérios
PR contém problema, mudança, issues, resultado esperado, critérios atendidos, verificações e pendências. Não encerrar etapas científicas por geração de documento preliminar. Merge não é automático. Enquanto o PR estiver aberto, os arquivos existem publicamente na branch e no diff, mesmo sem integrar main.

## Sub-issues nativas
O workflow research-governance configura relações de #2–#14 como filhos de #1, com permissão limitada a issues:write. Executa somente no repositório autorizado e em PR da branch de bootstrap do mesmo repositório. Relações nativas verificadas no workflow 39081842411 e em consulta independente à API. Ver relatório verificacao-publicacao.md.

## Limite das verificações
Verificação de hash demonstra preservação do protocolo; não valida cientificamente seu conteúdo. Workflow de hierarquia demonstra vínculos; não aprova pesquisa, ética ou manuscrito.

## Correcao de verificacoes — 18/10/2026

Os hashes do inventario medem consistencia interna do head. A preservacao historica do protocolo e uma verificacao separada contra o commit fixo 9d6b36ad85abbaf190ac7f49fd3b850ed820ea2c. O workflow passa a conferir completude do conjunto governado, inclui templates e codigo nos gatilhos, reexecuta em edited e verifica PRs do mesmo repositorio em outras branches. Apenas a mutacao de relacoes de issues fica limitada a branch bootstrap.

Aceite final: issue principal e descendentes fechados como completed, com evidencia; ver GOAL.md. Checks estruturais nao provam esse fechamento nem aprovacao cientifica.
