# Sprint 6 — Modo Claro / Escuro (Dark/Light)

Esta pasta contém **cópias** das telas do MoodFlow com um botão de alternância
entre **modo claro** e **modo escuro**.

## Importante
- Os arquivos do aplicativo (em `MoodFlow/`) **não foram alterados**. Estas são
  versões independentes, feitas só para demonstração do tema claro/escuro.
- Cada arquivo aqui é **autossuficiente**: pode abrir direto no navegador (duplo
  clique), sem precisar rodar o servidor. O CSS foi embutido em cada página e as
  tags do Django foram removidas para que funcionem isoladamente.

## Como usar
Abra qualquer `.html` da pasta `HTML Dark-Light/` no navegador e clique no botão
🌙 / ☀️ no canto superior direito para alternar o tema.

## Telas incluídas
home, login, registro, editar perfil, listar usuário, remover usuário, humor e
calendário.

## Como funciona (resumo)
O modo escuro é aplicado invertendo as cores da página e girando o matiz de volta,
o que escurece os fundos mas mantém os tons de azul da identidade do MoodFlow.
Um pequeno script JavaScript guarda qual tema está ativo e troca o ícone do botão.
