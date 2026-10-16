---
id: sugestoes-de-perguntas
titulo: "Sugestões de problema e perguntas analíticas"
tipo: base
status: rascunho
atualizado: 2026-10-15
fontes: [1, 3, 12]
relacionados: [api-deezer]
---
# Sugestões de problema e perguntas analíticas

> **Rascunho para a área A escolher, adaptar ou descartar.** Nada aqui é decisão. As perguntas precisam ser "suficientemente específicas para orientar as próximas etapas" [Fato, fonte 3] e respondíveis com os campos da API ([api-deezer](api-deezer.md), seção 3).

## Ideia 1 — O que caracteriza as faixas que chegam ao topo

**Problema:** artistas e gravadoras querem entender o perfil das faixas populares na Deezer: duração, conteúdo explícito, gênero, idade do lançamento.

| ID | Pergunta | Dados necessários |
|---|---|---|
| P1 | Como a duração das faixas varia entre os gêneros dos charts da Deezer na data da coleta? | `duration`, gênero do chart ou do álbum |
| P2 | Qual a proporção de faixas com letra explícita em cada gênero e como ela se relaciona com a posição no chart? | `explicit_lyrics`, gênero, `position`/`rank` |
| P3 | Faixas lançadas recentemente (últimos 12 meses) ocupam que parte dos charts, por gênero? | `release_date`, gênero |
| P4 | Há relação entre o `rank` da faixa e o número de fãs do artista? | `rank`, `artist.nb_fan` |

## Ideia 2 — Concentração de artistas nos charts

**Problema:** os charts são dominados por poucos artistas? Isso muda entre gêneros?

| ID | Pergunta | Dados necessários |
|---|---|---|
| P1 | Quantos artistas distintos ocupam o chart de cada gênero e qual a fatia dos 5 maiores? | `artist.id`, gênero |
| P2 | Quantos artistas aparecem em mais de um gênero? | `artist.id`, gênero |
| P3 | Os artistas mais presentes têm mais fãs que a média? | `artist.nb_fan` |

## Ligação com o RA2

Com qualquer das ideias, o RA2 pode monitorar **reproduções simuladas por gênero** em janelas de tempo ([ADR-0005](../docs/adr/0005-ra2-cenario-a-simulacao.md)), o que conversa com o recorte por gênero.

---

## Ligações

- **API:** [api-deezer](api-deezer.md) · **Enunciado:** [enunciados/ra1.md](../enunciados/ra1.md)
