# Trama IDE — Web, Android e Linux

Editor de diagramas UML com classes, métodos, interfaces e herança. Interface para telas pequenas, editor de código Java/TypeScript e galeria de 19 exemplos.

- [Abrir a plataforma web](https://aloisiocosta-professor.github.io/trama-ide-web/)
- [Baixar APK Android, aplicativo Linux e pacote web](https://github.com/aloisiocosta-professor/trama-ide-web/releases/latest)

A web/PWA e o APK editam diagramas e fontes, salvam localmente e exportam JSON, SVG e ZIP. O APK inclui interface e galeria offline, requer Android 8.0+ com WebView atualizado e usa o seletor de documentos para importar/exportar. A PWA fica disponível offline após a primeira visita completa.

Compilação, execução de aplicações Java/TypeScript, gráficos e servidores de protocolo estão na versão Linux. Exporte um projeto ZIP na web, extraia e execute `sh run.sh` no Linux com as dependências instaladas.

O pacote Linux contém os fontes completos do aplicativo GTK atual e um instalador para Arch Linux/ARM (`sh install.sh`). O histórico de desenvolvimento permanece no repositório privado original; esta é a distribuição pública autorizada. O código da interface estática está neste repositório.

Não há sincronização em nuvem. Exporte seus projetos antes de limpar dados do aplicativo ou do navegador. Diagramas e código são editados separadamente.

A publicação do Pages usa a raiz da branch main. Para hospedar o ZIP web em outro servidor, extraia seus arquivos e sirva a pasta por HTTPS (ou localhost durante o desenvolvimento).
