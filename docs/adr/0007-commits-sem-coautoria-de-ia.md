---
id: adr-0007
titulo: "ADR-0007 — Nenhum commit com IA como coautora"
tipo: decisao
decisao: "0007"
status: aceita
data: 2026-10-15
decisor: João Pedro Cardoso
entregas: [RA1, RA2]
areas: [A, B, C, D]
fontes: []
relacionados: []
---
# ADR-0007 — Nenhum commit com IA como coautora

- **Status:** aceita · **Data:** 15/10/2026 · **Decisor:** João Pedro Cardoso

## Contexto

- O grupo usa assistentes de IA (Claude Code e outros) para escrever código e texto. Algumas ferramentas acrescentam por padrão linhas como `Co-Authored-By: Claude …` e `Claude-Session: …` ao commit, e às vezes o próprio autor fica configurado como a IA.
- O grupo quer que o histórico mostre só os integrantes como autores. O uso de IA é declarado no documento, não no histórico de commits.

## Decisão

1. Nenhum commit pode ter IA como coautora (`Co-Authored-By` de Claude, Anthropic, Copilot, OpenAI, Codex, ChatGPT, Cursor, Gemini), nem `Claude-Session`, nem "Generated with Claude Code".
2. Autor e committer são sempre o integrante que pediu o trabalho.
3. Um agente que perceber, no meio da ação, que ia commitar com coautoria **para, remove as linhas e commita só com o autor real**.
4. A regra é garantida em quatro camadas: configuração do Claude Code (`attribution` vazio), hook do Claude Code que bloqueia o comando, hook `commit-msg` do git e verificação no GitHub Actions.

## Consequências

- Cada integrante ativa o hook uma vez por clone: `git config core.hooksPath .githooks`. O Claude Code ativa sozinho ao iniciar a sessão.
- PRs com commit fora da regra ficam reprovados na verificação "Verificar commits" até serem refeitos.
- Corpo de PR também não leva assinatura de IA.

---

## Ligações

- **Regras para agentes:** [CLAUDE.md](../../CLAUDE.md), [AGENTS.md](../../AGENTS.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
