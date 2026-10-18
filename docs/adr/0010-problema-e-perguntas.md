---
id: adr-0010
titulo: "ADR-0010 — Problema e perguntas analíticas: perfil das faixas populares por gênero"
tipo: decisao
decisao: "0010"
status: proposta
data: 2026-10-16
decisor: João Correa
entregas: [RA1, RA2]
areas: [A, B, C, D]
fontes: [1, 2, 3]
relacionados: [adr-0001, adr-0004, adr-0005, sugestoes-de-perguntas]
---
# ADR-0010 — Problema e perguntas analíticas: perfil das faixas populares por gênero

- **Status:** proposta · **Data:** 16/10/2026 · **Decisor:** João Correa

## Contexto

- O RA1 pede o problema e perguntas analíticas "suficientemente específicas para orientar as próximas etapas" [Fato, fonte 3].
- Até aqui as áreas trabalhavam com um recorte provisório (faixas dos charts, geral e por gênero) e duas ideias em [sugestoes-de-perguntas](../../base/sugestoes-de-perguntas.md).
- A API dá, para cada item de chart, `duration`, `rank`, `position` e o artista; `/track/{id}` dá `release_date` e `bpm`; `/artist/{id}` dá `nb_fan` [Fato para `/chart` e `/track`, fonte 2; `/artist`, `/genre` e os campos são Inferência a confirmar na coleta, ver [api-deezer](../../base/api-deezer.md), seções 2 e 3].
- `bpm` e `gain` costumam vir zerados quando a Deezer não calculou o valor [Inferência, a confirmar na seção 03].

## Opções consideradas

- **(a)** Ideia 1: perfil das faixas do topo (duração, letra explícita, lançamento recente, rank × fãs).
- **(b)** Ideia 2: concentração de artistas nos charts.
- **(c)** Ideia 1 com uma pergunta da Ideia 2, todas comparando gêneros.

## Decisão

**(c).** Problema: *o que caracteriza as faixas que estão no topo dos charts da Deezer e como esse perfil muda entre gêneros*. Unidade de observação: a faixa; período: o retrato bruto coletado na T02 (data na ficha da fonte).

| ID | Pergunta |
|---|---|
| P1 | Como a duração das faixas varia entre os gêneros dos charts da Deezer na data da coleta? |
| P2 | Que parte das faixas de cada chart de gênero foi lançada nos 12 meses anteriores à coleta? |
| P3 | Faixas de artistas com mais fãs têm `rank` mais alto, no chart geral e dentro de cada gênero? |
| P4 | Quantos artistas distintos ocupam cada chart de gênero e que fatia das posições fica com os 5 artistas com mais faixas? |

A pergunta sobre letra explícita ficou de fora para manter o foco em quatro perguntas; pode voltar no RA3 se a exploração mostrar faixas explícitas suficientes por gênero. Perguntas com `bpm` ficaram de fora pelo risco de excesso de zeros.

## Consequências

- O gênero do chart de origem é a variável de grupo de todas as perguntas: a área D precisa preservá-lo ao deduplicar faixas que aparecem em mais de um chart.
- O conjunto preparado precisa manter `duration`, `release_date`, `rank`, `position`, o id do artista e `nb_fan`.
- O RA2 pode monitorar reproduções simuladas por gênero ([ADR-0005](0005-ra2-cenario-a-simulacao.md)), o que conversa com o recorte.
- Texto completo: [documentacao/ra1/01-problema-e-perguntas.md](../../documentacao/ra1/01-problema-e-perguntas.md).

---

## Ligações

- **Base:** [sugestoes-de-perguntas](../../base/sugestoes-de-perguntas.md), [api-deezer](../../base/api-deezer.md)
- **Outras decisões:** [0001](0001-fonte-de-dados-api-deezer.md), [0004](0004-retrato-bruto-versionado.md), [0005](0005-ra2-cenario-a-simulacao.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
