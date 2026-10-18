# Correcao dos cinco achados de revisao

18/10/2026. Issue #21; PR #15.

| Achado | Correcao |
|---|---|
| Templates nao acionavam checks | Gatilho .github/** |
| Inventario mutavel confundido com preservacao | Comparacao adicional com protocolo no commit historico fixo |
| Corpo editado nao revalidava referencias | Evento pull_request.edited |
| Branch diferente omitida | Verificacao em PRs do mesmo repositorio; mutacao de hierarquia limitada |
| Arquivo novo nao inventariado passava | Comparacao entre arvore Git governada e entradas do inventario |

11 testes de regressao locais passaram. O aceite da issue exige tambem execucao remota do novo head. Nao se declara essa execucao antes de observa-la.
