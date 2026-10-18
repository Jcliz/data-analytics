# Plano de tarefas — RA1 e RA2

> Divide o RA1 e o RA2 em tarefas, com responsáveis, arquivos, dependências e prazos. Os critérios (IDs `C`, `N`, `AP`, `S`, `X`, `K`) estão em [criterios-de-aceite.md](criterios-de-aceite.md); aqui só se citam os IDs.
> **Status:** proposta de 15/10/2026, a confirmar pelo grupo (responsáveis por área e datas).

---

## 1. Áreas e responsáveis

Decisão: [ADR-0008](../docs/adr/0008-divisao-em-quatro-areas.md). Nomes e responsáveis definidos pelo João em 15/10/2026: o João Correa fica com a área A, que inclui o documento do RA1 em `.docx` (T11), e o Eduardo Fabri fica com a área C, que é de código.

| Área | Escopo | Responsável (proposto) |
|---|---|---|
| **A** — Problema e síntese | Problema, recorte, perguntas; identificação; considerações do RA1; objetivo e considerações do RA2; **documento do RA1 em `.docx`** (referências, consolidação e PDF, que é a parte 1 do PDF único) | João Correa (`jvecodev`) |
| **B** — Fonte, ingestão e reprodutibilidade | Ficha da fonte, coleta pela API, retrato bruto, ambiente; reprodutibilidade; gerador de eventos e leitura em streaming | João Pedro Cardoso (`Jcliz`) |
| **C** — Compreensão e qualidade | Exploração inicial, dicionário, diagnóstico Q1…Qn; janela temporal e agregação | Eduardo Fabri (`eduardofabrii`) |
| **D** — Limpeza e conjunto resultante | Decisões D1…Dn, preparo, conjunto preparado; resultados e interpretação do RA2 | Rodrigo Alves (`rdsalvesPUC`) |

Tarefas **gerais** (marcadas "Geral") não têm dono fixo: quem puxar se atribui na issue.

## 2. Arquivos por área (cada área edita só os seus)

| Arquivo | Área |
|---|---|
| `notebook/secoes/00a-identificacao.py`, `01-contexto-e-objetivo.py`, `07-consideracoes-ra1.py`, `08-objetivo-streaming.py`, `12-consideracoes-ra2.py` | A |
| `documentacao/ra1/01-problema-e-perguntas.md`, `documentacao/ra1/00-capa.md`, `documentacao/ra1/07-referencias-e-anexos.md`, `output/ra1-documentacao.docx` e `.pdf` | A |
| `notebook/secoes/00b-ambiente.py`, `02-fonte-e-ingestao.py`, `09-fonte-e-processamento.py` | B |
| `documentacao/ra1/02-fontes-e-ingestao.md`, `documentacao/ra1/06-organizacao-e-reprodutibilidade.md`, `dados/brutos/`, `requirements.txt` | B |
| `notebook/secoes/03-exploracao-inicial.py`, `10-janelas-temporais.py` | C |
| `documentacao/ra1/03-compreensao-e-qualidade.md` | C |
| `notebook/secoes/04-limpeza-e-preparacao.py`, `05-transformacao.py`, `11-resultados.py` | D |
| `documentacao/ra1/04-limpeza-e-preparacao.md`, `documentacao/ra1/05-conjunto-resultante.md`, `dados/preparados/` | D |
| `output/projeto_data_analytics.pdf`, `output/entrega-ra1-ra2.pdf`, `notebook/projeto_data_analytics.ipynb` (gerado) | Geral |
| `README.md`, `CONTEXT.md`, `AGENTS.md`, `CLAUDE.md`, `docs/`, `base/`, `entregas/`, `scripts/` | Geral (mudança combinada no PR) |

## 3. Fluxo de trabalho

- **Branch por tarefa, com nome curto:** `tNN-palavra` (número da tarefa com dois dígitos e uma palavra), tudo em minúsculas, sem acento e sem barra. O nome de cada tarefa está na coluna "Branch" da seção 5. Ajuste fora de tarefa: `ajuste-palavra`.
- **Quadro (kanban):** GitHub Projects ligado ao repositório, colunas A fazer → Em andamento → Em revisão → Concluído. Quem pega a tarefa se atribui e move o card; PR aberto vai para Em revisão; merge fecha a issue e move para Concluído (README, "Quadro de tarefas").
- **Pull request para a `main`** com `Closes #<n>` e a evidência de cada critério. Outro integrante revisa. Todos têm permissão de push na `main` para correções pequenas (erro de digitação, link quebrado); conteúdo de tarefa entra por PR.
- **Commits sem coautoria de IA** ([ADR-0007](../docs/adr/0007-commits-sem-coautoria-de-ia.md)). Ative o hook uma vez: `git config core.hooksPath .githooks`.
- **Pendência entre áreas:** a seção de uma área depende de algo que outra ainda não fez (ex.: C precisa do `df_bruto` com uma coluna que B não trouxe). O trabalho não para: registre uma linha na issue com o rótulo `pendencia-cruzada` da área que precisa resolver (crie se não existir), com o arquivo e o trecho onde a suposição aparece. A linha fecha com o commit que resolve ou com a decisão de não fazer.

## 4. Rótulos

| Rótulo | Uso |
|---|---|
| `ra1`, `ra2` | Entrega |
| `geral` | Tarefa sem área fixa |
| `area-a` … `area-d` | Área (seção 1) |
| `notebook`, `documento` | Onde a tarefa escreve |
| `pendencia-cruzada` | Amarração que uma área deixou dependendo de outra |
| `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix` | Triagem ([docs/agents/triage-labels.md](../docs/agents/triage-labels.md)) |

## 5. Tarefas

Convenção de título: `[RA1][Área X] Tnn — descrição`, `[RA2][Área X] Tnn — descrição` ou `[Geral] Tnn — descrição`.

| ID | Issue | Branch | Tarefa | Área | Arquivos | Critérios | Bloqueada por | Prazo |
|---|---|---|---|---|---|---|---|---|
| T00 | [#1](https://github.com/Jcliz/data-analytics/issues/1) | — | Estrutura do repositório, contexto e regras para agentes | Geral | todos os de base | — | — | 15/10 |
| T01 | [#2](https://github.com/Jcliz/data-analytics/issues/2) | `t01-problema` | Problema, recorte e perguntas analíticas | A | nb 00a, 01; doc 00, 01 | C1.1–C1.4, N.1, N.3–N.4 | T00 | 16/10 |
| T02 | [#3](https://github.com/Jcliz/data-analytics/issues/3) | `t02-coleta` | Coleta pela API, retrato bruto e ficha da fonte | B | nb 00b, 02; doc 02; `dados/brutos/` | C2.1–C2.5, N.3–N.4 | T00; T01 (só C2.2) | 16/10 |
| T03 | [#4](https://github.com/Jcliz/data-analytics/issues/4) | `t03-qualidade` | Exploração inicial e diagnóstico de qualidade | C | nb 03; doc 03 | C3.1–C3.5, C5.5, N.3–N.4 | T02 | 17/10 |
| T04 | [#5](https://github.com/Jcliz/data-analytics/issues/5) | `t04-limpeza` | Limpeza, preparo e conjunto resultante | D | nb 04, 05; doc 04, 05; `dados/preparados/` | C4.1–C4.5, C5.1–C5.5, N.3–N.4 | T03 | 19/10 |
| T05 | [#6](https://github.com/Jcliz/data-analytics/issues/6) | `t05-reproducao` | Organização e reprodutibilidade | B | doc 06; `requirements.txt`; README (seção "Como executar") | C6.1–C6.3 | T02, T04 | 19/10 |
| T06 | [#7](https://github.com/Jcliz/data-analytics/issues/7) | `t06-consideracoes` | Considerações do RA1 | A | nb 07 | C5.5, N.3–N.4 | T04 | 19/10 |
| T07 | [#8](https://github.com/Jcliz/data-analytics/issues/8) | `t07-objetivo` | Objetivo da análise em streaming e considerações do RA2 | A | nb 08, 12 | S8.1, S12.1, N.3–N.4 | T01 (seção 8); T10 (seção 12) | 19/10 (seção 8); 20/10 (seção 12) |
| T08 | [#9](https://github.com/Jcliz/data-analytics/issues/9) | `t08-eventos` | Gerador de eventos e leitura em streaming | B | nb 09 | S9.1–S9.3, N.3–N.4 | T00 (amostra), T04 (final) | 19/10 |
| T09 | [#10](https://github.com/Jcliz/data-analytics/issues/10) | `t09-janela` | Janela temporal e agregação | C | nb 10 | S10.1–S10.2, N.3–N.4 | T08; T07 (seção 8) | 19/10 |
| T10 | [#11](https://github.com/Jcliz/data-analytics/issues/11) | `t10-resultados` | Resultados e interpretação do RA2 | D | nb 11 | S11.1–S11.2, N.3–N.4 | T09 | 20/10 |
| T11 | [#12](https://github.com/Jcliz/data-analytics/issues/12) | `t11-docx` | Referências, consolidação do documento do RA1 (`.docx`) e PDF (parte 1 da entrega) | A | doc 07; `output/ra1-documentacao.*` | C7.1–C7.2, X.3–X.4, X.7, X.9 | T01–T06 | 20/10 |
| T12 | [#13](https://github.com/Jcliz/data-analytics/issues/13) | `t12-revisao` | Revisão cruzada RA1 e RA2 | Geral | relatório na issue | K.1–K.8, X.1, X.7, X.9 | T01–T11 | 20/10 |
| T13 | [#14](https://github.com/Jcliz/data-analytics/issues/14) | `t13-envio` | Execução final, PDF único e envio no RA1 e no RA2 | Geral | notebook gerado; doc 06 (só C6.4); `output/` | C6.4, N.2–N.3, X.2, X.5–X.8 | T12 | 21/10 |
| T14 | [#15](https://github.com/Jcliz/data-analytics/issues/15) | `t14-roteiro` | Roteiro da apresentação do RA1 e da demonstração do RA2 | Geral | `entregas/roteiro-apresentacao.md` | AP.1, S.D | T12 | 21/10 |

Prazo de entrega das duas tarefas no Canvas: **21/10/2026**. O mesmo PDF único vai nas duas: o arquivo no RA2 e o link dele no RA1 ([ADR-0009](../docs/adr/0009-entrega-unica-em-pdf.md)).

## 6. Corpo padrão de cada issue

```markdown
## Objetivo
<o que a tarefa entrega, em uma ou duas frases>

## Insumos obrigatórios
- Ler `CONTEXT.md` (seções 1, 6 e 9) antes de começar.
- Arquivos da base e decisões indicados para a tarefa: <links>

## Arquivos desta tarefa
- <caminhos que a área pode alterar>

## Critérios de aceite
Referência: `entregas/criterios-de-aceite.md`
- [ ] <ID> <texto resumido do critério>

## Dependências
- Bloqueada por: #<n>
- Bloqueia: #<n>

## Definição de pronto
- Branch própria e PR para a `main` com `Closes #<n>`.
- Notebook montado (`python scripts/montar_notebook.py`) e executado sem erro até a seção desta tarefa.
- `python scripts/verificar_entrega.py` sem pendência nos arquivos desta tarefa.
- Cada critério marcado com evidência (seção e célula do notebook, contagem).
- Commits sem coautoria de IA.
```

## 7. Instruções para agentes (criação das issues)

1. Ler este arquivo e `criterios-de-aceite.md` por inteiro.
2. Criar os rótulos da seção 4 que ainda não existirem.
3. Criar uma issue por linha da seção 5, com título, corpo no formato da seção 6, rótulos de entrega, área e destino (`notebook`/`documento`) e o critério copiado com o texto resumido.
4. Atribuir ao responsável da área **só depois** que ele for colaborador do repositório; antes disso, citar o login entre crases no corpo, sem `@`.
5. Preencher "Bloqueada por" e "Bloqueia" com os números reais.
6. Conferir por contagem: 15 issues (T00–T14), cada uma com rótulo de entrega ou `geral`.

As 15 issues foram criadas em 15/10/2026 (T00 = #1 … T14 = #15). Em 16/10/2026, com os quatro integrantes já colaboradores, cada issue de área foi atribuída ao seu responsável (Eduardo: #4 e #10; Rodrigo: #5 e #11).

## 8. Dúvidas do grupo

**Nenhuma dúvida em aberto.** Dúvida nova entra aqui como uma linha: a dúvida, onde surgiu e o padrão que o repositório segue até a resposta.

Respondidas pelo João em 15/10/2026:

| Dúvida | Decisão |
|---|---|
| Nomes da equipe | Eduardo Fabri, João Correa, Rodrigo Alves e João Pedro Cardoso, exatamente assim; sem RA. |
| Professora e turma | Professora Marina de Lara; a turma não entra na capa nem no notebook. |
| Divisão das áreas | A João Correa (inclui o `.docx`, T11), B João Pedro Cardoso, C Eduardo Fabri, D Rodrigo Alves. |
| Envio do RA1 e do RA2 | **Um PDF só**: o documento do RA1 (com a URL do repositório na capa) e depois o notebook executado. No RA2 vai o arquivo; no RA1, cujo formulário só aceita URL, o link do mesmo PDF no repositório, na tag `entrega` ([ADR-0009](../docs/adr/0009-entrega-unica-em-pdf.md)). |
| Prazo | 21/10/2026 para o RA1 e o RA2. |
| Seção 5 "Transformação" do notebook | Só transformações de preparo (tipos, colunas derivadas simples, nomes em português), sem agregação. |
| Declaração de uso de IA | **Não incluir** em nenhuma entrega (critério X.7). |
| Organização interna (área, tarefa, issue, PR, branch) | **Não citar** no texto entregue (critério X.9). |
| Templates do professor no repositório público | Ficam em `modelos/`, porque os scripts precisam deles. |
| Grafo de conhecimento (Graphify) | Não será montado. |
