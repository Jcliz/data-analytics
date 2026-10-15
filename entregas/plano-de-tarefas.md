# Plano de tarefas — RA1 e RA2

> Divide o RA1 e o RA2 em tarefas, com responsáveis, arquivos, dependências e prazos. Os critérios (IDs `C`, `N`, `S`, `X`, `K`) estão em [criterios-de-aceite.md](criterios-de-aceite.md); aqui só se citam os IDs.
> **Status:** proposta de 15/10/2026, a confirmar pelo grupo (responsáveis por área e datas).

---

## 1. Áreas e responsáveis

Decisão: [ADR-0008](../docs/adr/0008-divisao-em-quatro-areas.md). A atribuição de pessoas segue a do projeto de Especificação de Software e **precisa ser confirmada**.

| Área | Escopo | Responsável (proposto) |
|---|---|---|
| **A** — Problema e síntese | Problema, recorte, perguntas; identificação; considerações do RA1; objetivo e considerações do RA2 | Eduardo Fabri (`eduardofabrii`) |
| **B** — Fonte, ingestão e reprodutibilidade | Ficha da fonte, coleta pela API, retrato bruto, ambiente; reprodutibilidade; gerador de eventos e leitura em streaming | João Pedro Cardoso de Liz (`Jcliz`) |
| **C** — Compreensão e qualidade | Exploração inicial, dicionário, diagnóstico Q1…Qn; janela temporal e agregação | João Vitor Correa Oliveira (`jvecodev`) |
| **D** — Limpeza e conjunto resultante | Decisões D1…Dn, preparo, conjunto preparado; resultados e interpretação do RA2 | Rodrigo Alves (`rdsalvesPUC`) |

Tarefas **gerais** (marcadas "Geral") não têm dono fixo: quem puxar se atribui na issue.

## 2. Arquivos por área (cada área edita só os seus)

| Arquivo | Área |
|---|---|
| `notebook/secoes/00a-identificacao.py`, `01-contexto-e-objetivo.py`, `07-consideracoes-ra1.py`, `08-objetivo-streaming.py`, `12-consideracoes-ra2.py` | A |
| `documentacao/ra1/01-problema-e-perguntas.md`, `documentacao/ra1/00-capa.md` | A |
| `notebook/secoes/00b-ambiente.py`, `02-fonte-e-ingestao.py`, `09-fonte-e-processamento.py` | B |
| `documentacao/ra1/02-fontes-e-ingestao.md`, `documentacao/ra1/06-organizacao-e-reprodutibilidade.md`, `dados/brutos/`, `requirements.txt` | B |
| `notebook/secoes/03-exploracao-inicial.py`, `10-janelas-temporais.py` | C |
| `documentacao/ra1/03-compreensao-e-qualidade.md` | C |
| `notebook/secoes/04-limpeza-e-preparacao.py`, `05-transformacao.py`, `11-resultados.py` | D |
| `documentacao/ra1/04-limpeza-e-preparacao.md`, `documentacao/ra1/05-conjunto-resultante.md`, `dados/preparados/` | D |
| `documentacao/ra1/07-referencias-e-anexos.md`, `output/`, `notebook/projeto_data_analytics.ipynb` (gerado) | Geral |
| `README.md`, `CONTEXT.md`, `AGENTS.md`, `CLAUDE.md`, `docs/`, `base/`, `entregas/`, `scripts/` | Geral (mudança combinada no PR) |

## 3. Fluxo de trabalho

- **Branch por tarefa:** `ra1/<area>-<descricao>` ou `ra2/<area>-<descricao>`, minúsculas, sem acento. Ex.: `ra1/b-ingestao`.
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

Convenção de título: `[RA1][Área X] descrição`, `[RA2][Área X] descrição` ou `[Geral] descrição`.

| ID | Tarefa | Área | Arquivos | Critérios | Bloqueada por | Prazo |
|---|---|---|---|---|---|---|
| T00 | Estrutura do repositório, contexto e regras para agentes | Geral | todos os de base | — | — | 15/10 |
| T01 | Problema, recorte e perguntas analíticas | A | nb 00a, 01; doc 00, 01 | C1.1–C1.4, N.1 | T00 | 16/10 |
| T02 | Coleta pela API, retrato bruto e ficha da fonte | B | nb 00b, 02; doc 02; `dados/brutos/` | C2.1–C2.5 | T00 | 16/10 |
| T03 | Exploração inicial e diagnóstico de qualidade | C | nb 03; doc 03 | C3.1–C3.5 | T02 | 17/10 |
| T04 | Limpeza, preparo e conjunto resultante | D | nb 04, 05; doc 04, 05; `dados/preparados/` | C4.1–C4.5, C5.1–C5.5 | T03 | 19/10 |
| T05 | Organização e reprodutibilidade | B | doc 06; `requirements.txt`; README (seção "Como executar") | C6.1–C6.4 | T02, T04 | 19/10 |
| T06 | Considerações do RA1 | A | nb 07 | N.4 | T04 | 19/10 |
| T07 | Objetivo da análise em streaming e considerações do RA2 | A | nb 08, 12 | S8.1, S12.1 | T01 | 19/10 |
| T08 | Gerador de eventos e leitura em streaming | B | nb 09 | S9.1–S9.3 | T00 (amostra), T04 (final) | 19/10 |
| T09 | Janela temporal e agregação | C | nb 10 | S10.1–S10.2 | T08 | 19/10 |
| T10 | Resultados e interpretação do RA2 | D | nb 11 | S11.1–S11.2 | T09 | 20/10 |
| T11 | Referências, consolidação do documento do RA1 e PDF | Geral | doc 07; `output/` | C7.1–C7.2, X.3–X.4 | T01–T06 | 20/10 |
| T12 | Revisão cruzada RA1 e RA2 | Geral | relatório na issue | K.1–K.8 | T01–T11 | 20/10 |
| T13 | Execução final, tag e envio do RA1 (URL) | Geral | notebook gerado | N.2–N.3, X.2, X.6 | T12 | 21/10 |
| T14 | PDF do notebook, roteiro da demonstração e envio do RA2 | Geral | `output/` | X.5, S.D | T12 | 21/10 |

Prazo de entrega das duas tarefas no Canvas: **21/10/2026**.

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
