# Plano de tarefas — RA3

> Divide o RA3 em tarefas, com responsáveis, arquivos, dependências e prazos. Continua a numeração do [plano do RA1 e do RA2](plano-de-tarefas.md) (T00 a T14), que segue valendo para as regras de fluxo, rótulos e corpo das issues. Os critérios (IDs `R`, `RD`, `RAP` do enunciado, `RN` do repositório, recomendações `RC` e revisão `RK`) estão em [criterios-de-aceite-ra3.md](criterios-de-aceite-ra3.md).
> **Status:** proposta de 05/11/2026, a confirmar pelo João (divisão por pessoa e datas). Prazo do RA3 no Canvas e apresentação: **18/11/2026**.

---

## 1. Áreas e responsáveis

As quatro áreas do RA1 e do RA2 continuam ([ADR-0008](../docs/adr/0008-divisao-em-quatro-areas.md)), cada uma com uma parte do RA3 ligada ao que já fez. O RA3 tem um notebook próprio, com uma seção por requisito do enunciado ([ADR-0012](../docs/adr/0012-ra3-no-notebook-e-entrega-por-url.md)).

| Área | RA3 | Por que essa área | Responsável (proposto) |
|---|---|---|---|
| **A** — Problema e síntese | Conclusões (seção 5); documentação das técnicas, dos resultados e das instruções de execução (`documentacao/ra3/README.md`) | Escreveu o problema, as perguntas, as considerações e o documento do RA1 | João Correa (`jvecodev`) |
| **B** — Fonte, ingestão e reprodutibilidade | Amostragem e representatividade (seção 3); Machine Learning (seção 4) | Conhece a origem e os limites da coleta; o modelo depende de separação reproduzível (semente) | João Pedro Cardoso (`Jcliz`) |
| **C** — Compreensão e qualidade | Análise estatística descritiva (seção 1) | Fez a exploração inicial e as estatísticas do diagnóstico do RA1 | Eduardo Fabri (`eduardofabrii`) |
| **D** — Limpeza e conjunto resultante | Visualizações e interpretação (seção 2) | Preparou o conjunto e interpretou os resultados do RA2 | Rodrigo Alves (`rdsalvesPUC`) |

Tarefas **gerais** (marcadas "Geral") não têm dono fixo: quem puxar se atribui na issue. Alternativa em aberto: o Machine Learning (T19) pode ir para o Eduardo (área C, de código), se o grupo preferir.

## 2. Arquivos por área (cada área edita só os seus)

| Arquivo | Área |
|---|---|
| `notebook/secoes-ra3/05-conclusoes.py`, `documentacao/ra3/README.md` | A |
| `notebook/secoes-ra3/03-representatividade.py`, `04-machine-learning.py`, `requirements.txt` (bibliotecas do modelo) | B |
| `notebook/secoes-ra3/01-estatistica-descritiva.py` (as duas primeiras células de código, ambiente e `df_analise`, vêm prontas) | C |
| `notebook/secoes-ra3/02-visualizacoes.py` | D |
| `notebook/secoes-ra3/00-identificacao.py`, `notebook/ra3-deezer.ipynb` (gerado), `requirements-ra3.txt`, cópia para o `machine-learning-ra3`, `entregas/roteiro-apresentacao-ra3.md` | Geral |
| `README.md`, `CONTEXT.md`, `AGENTS.md`, `CLAUDE.md`, `docs/`, `base/`, `entregas/`, `scripts/` | Geral (mudança combinada no PR) |

O notebook do RA1 e do RA2 (`notebook/secoes/`) e o documento do RA1 (`documentacao/ra1/`) não mudam no RA3. Se um número do RA1 precisar de correção, registre na issue e combine com o grupo antes.

## 3. Fluxo de trabalho

O mesmo do [plano do RA1 e do RA2](plano-de-tarefas.md), seção 3: branch `tNN-palavra` por tarefa (coluna "Branch" abaixo), PR para a `main` com `Closes #<n>` e evidência de cada critério, revisão de outro integrante, commits sem coautoria de IA e pendência entre áreas registrada na issue `pendencia-cruzada` da área dona.

Ordem: a T15 entrega a estrutura, com as duas primeiras células de código da seção 1 prontas (ambiente e `df_analise`). Por isso as seções 1 a 4 podem começar no mesmo dia.

## 4. Rótulos

Os da seção 4 do [plano do RA1 e do RA2](plano-de-tarefas.md), mais `ra3` (entrega). As issues do RA3 levam `ra3` (ou `geral`), a área e o destino (`notebook` ou `documento`).

## 5. Tarefas

Convenção de título: `[RA3][Área X] Tnn — descrição` ou `[Geral] Tnn — descrição`.

| ID | Issue | Branch | Tarefa | Área | Arquivos | Critérios | Bloqueada por | Prazo |
|---|---|---|---|---|---|---|---|---|
| T15 | — | `t15-estrutura` | Estrutura do RA3: enunciado, critérios, plano, contexto e esqueleto do notebook do RA3 | Geral | os de base; notebook do RA3 (esqueleto) | — | — | 06/11 |
| T16 | — | `t16-estatistica` | Análise estatística descritiva | C | nb RA3 §1 | R1.1–R1.5, RN.2–RN.3 | T15 | 11/11 |
| T17 | — | `t17-graficos` | Visualizações e interpretação | D | nb RA3 §2 | R2.1–R2.4, RN.2–RN.3 | T15; T16 (números citados) | 12/11 |
| T18 | — | `t18-representatividade` | Amostragem e representatividade | B | nb RA3 §3 | R3.1–R3.4, RN.2–RN.3 | T15 | 10/11 |
| T19 | — | `t19-modelo` | Aplicação de Machine Learning | B | nb RA3 §4; `requirements.txt` | R4.1–R4.6, RN.2–RN.3 | T15 | 12/11 |
| T20 | — | `t20-conclusoes` | Conclusões do RA3 | A | nb RA3 §5 | R5.1–R5.4, RN.2–RN.3 | T16–T19 | 14/11 |
| T21 | — | `t21-documentacao` | Documentação e instruções de execução do RA3 | A | `documentacao/ra3/README.md` | RD.2–RD.3 | T16–T19 (técnicas); T20 (conclusões) | 14/11 |
| T22 | — | `t22-revisao` | Revisão cruzada do RA3 | Geral | relatório na issue | RK.1–RK.6, RN.4, RN.6 | T16–T21 | 15/11 |
| T23 | — | `t23-envio` | Execução final, cópia para o `machine-learning-ra3` e envio da URL | Geral | `notebook/ra3-deezer.ipynb`; `machine-learning-ra3` | RN.1, RN.5, RD.1, RD.4, X.2, X.6 | T22 | 17/11 |
| T24 | — | `t24-roteiro` | Roteiro da apresentação do RA3 | Geral | `entregas/roteiro-apresentacao-ra3.md` | RAP.1–RAP.2 | T22 | 17/11 |

Entrega no Canvas: **18/11/2026**, só a URL do `Jcliz/machine-learning-ra3`, que tem só o que é entregue ([ADR-0012](../docs/adr/0012-ra3-no-notebook-e-entrega-por-url.md)).

## 6. Corpo padrão de cada issue

O da seção 6 do [plano do RA1 e do RA2](plano-de-tarefas.md), com estas trocas: em "Insumos obrigatórios", ler `CONTEXT.md` (seções 1, 6 e 9), [enunciados/ra3.md](../enunciados/ra3.md) e [base/analise-e-ml.md](../base/analise-e-ml.md); em "Critérios de aceite", a referência é `entregas/criterios-de-aceite-ra3.md`; na "Definição de pronto", o notebook do RA3 (`python scripts/montar_notebook.py --ra3`) é executado sem erro até a seção da tarefa.

## 7. Instruções para agentes (criação das issues)

1. Ler este arquivo e `criterios-de-aceite-ra3.md` por inteiro.
2. Criar o rótulo `ra3`, se ainda não existir.
3. Criar uma issue por linha da seção 5, a partir da T16 (a T15 é o PR da estrutura), com título, corpo no formato da seção 6, rótulos e os critérios copiados com o texto resumido.
4. Atribuir cada issue de área ao responsável da seção 1, depois que o João confirmar a divisão.
5. Preencher "Bloqueada por" e "Bloqueia" com os números reais e a coluna "Issue" da seção 5.
6. Conferir por contagem: 9 issues (T16–T24), cada uma com `ra3` ou `geral`.

## 8. Dúvidas do grupo

| Dúvida | Onde surgiu | Padrão até a resposta |
|---|---|---|
| Pesos da rubrica do RA3 (a tabela de pontos não veio no PDF da tarefa) | [enunciado](../enunciados/ra3.md), seção 6 | Critérios seguem os requisitos do enunciado, sem peso |
| Quem fica com o Machine Learning: João Pedro (B) ou Eduardo (C) | Seção 1 | João Pedro (B) |
| Abordagem do modelo: regressão do `rank` | [ADR-0013](../docs/adr/0013-ra3-regressao-do-rank.md) | Regressão do `rank`, com classificação de lançamento recente como plano B |

Respondida pelo João em 05/11/2026: o RA3 vai num notebook próprio, e não no notebook do RA1 e do RA2 ([ADR-0012](../docs/adr/0012-ra3-no-notebook-e-entrega-por-url.md)). Também em 05/11: o RA3 é entregue num repositório novo, `Jcliz/machine-learning-ra3`, só com o que é entregue; o desenvolvimento e as issues ficam aqui.
