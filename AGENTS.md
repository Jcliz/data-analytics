# AGENTS.md

Regras para assistentes de IA (Claude Code, Codex, Copilot, Cursor e outros) que trabalham neste repositório. O Claude Code lê também o [CLAUDE.md](CLAUDE.md), que traz as mesmas regras com o passo a passo de desenvolvimento.

## Base de conhecimento (leia antes de qualquer tarefa)

1. Leia [`CONTEXT.md`](CONTEXT.md). Ele resume entregas, fonte de dados, decisões, o contrato entre as seções do notebook e o que ler para cada tarefa (seção 9).
2. Leia a **issue da tarefa**. Ela traz os critérios de aceite (IDs de [`entregas/criterios-de-aceite.md`](entregas/criterios-de-aceite.md)) e os arquivos que você pode alterar.
3. Abra só os arquivos indicados para a tarefa. Não leia a base inteira.
4. **Precedência:** enunciados (`enunciados/`) > decisões (`docs/adr/`) > base (`base/`) > rascunhos. Não contradiga uma decisão; se algo pedir mudança, registre a dúvida em vez de mudar o texto.

## Escrita

5. **Tudo em português do Brasil**: texto, células Markdown, comentários de código, nomes novos de variáveis e colunas, mensagens de commit, títulos de branch, issues e PRs.
6. **Evidência para toda afirmação sobre os dados**: a seção do notebook (ex.: "célula 3.2") ou o arquivo, com a contagem e o denominador. Separe [Fato] de [Inferência] e cite fontes por número de [`base/fontes.md`](base/fontes.md).
7. **O RA1 não tem análise**: nada de agregações analíticas, indicadores, gráficos de resultado ou conclusões sobre as perguntas. Isso é RA2/RA3.
8. **Respeite o contrato do notebook** (`CONTEXT.md`, seção 6). Não renomeie variáveis compartilhadas nem caminhos de dados.
9. **Cada área edita só os seus arquivos** (tabela de responsabilidade em [`entregas/plano-de-tarefas.md`](entregas/plano-de-tarefas.md)). Precisa de algo de outra área? Não invente: registre a suposição como uma linha na issue `pendencia-cruzada` da área dona, ou avise quem pediu a tarefa.
10. **Não edite** o arquivo gerado `notebook/projeto_data_analytics.ipynb` à mão nem os retratos em `dados/brutos/`. O notebook sai de `python scripts/montar_notebook.py`; o retrato sai da execução da seção 02 com `BAIXAR_DA_API = True`.
11. **Sem segredos**: a API da Deezer não usa chave. Não grave tokens, senhas nem caminhos pessoais da sua máquina.
12. **Nenhuma declaração de uso de IA nas entregas.** O documento do RA1, o notebook e os PDFs não têm seção, nota ou frase sobre o uso de assistentes de IA. É decisão do grupo e vale mesmo que um template ou o repositório do aircraft tenham essa seção.

## Commits (regra do grupo, sem exceção)

13. **Nenhum commit pode ter Claude, ou qualquer IA, como coautor.** Não escreva `Co-Authored-By: Claude …`, `Co-Authored-By: … <noreply@anthropic.com>`, `Claude-Session: …`, nem linhas equivalentes de outras ferramentas (Copilot, Codex, Cursor). O autor e o committer são a pessoa do grupo que pediu o trabalho. Se a sua ferramenta acrescenta essas linhas por padrão, **pare antes de commitar, remova as linhas e refaça o commit só com o autor real**. O hook [`.githooks/commit-msg`](.githooks/commit-msg) e a verificação do GitHub Actions recusam commits fora dessa regra ([ADR-0007](docs/adr/0007-commits-sem-coautoria-de-ia.md)).
14. Mensagem de commit em português, no imperativo, citando a tarefa: `ra1(qualidade): adiciona verificação de bpm igual a zero (#7)`.

## Agent skills

### Issue tracker

As issues ficam no GitHub Issues deste repositório. Ver [`docs/agents/issue-tracker.md`](docs/agents/issue-tracker.md).

### Triage labels

Vocabulário padrão: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. Ver [`docs/agents/triage-labels.md`](docs/agents/triage-labels.md).

### Domain docs

Contexto único: `CONTEXT.md` + `docs/adr/` na raiz. Ver [`docs/agents/domain.md`](docs/agents/domain.md).
