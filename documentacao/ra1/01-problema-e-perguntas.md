# Problema e perguntas analíticas

## Contexto e problema

Os charts da Deezer mostram quais faixas os ouvintes mais escutam, no ranking geral e em cada gênero musical. Artistas, gravadoras e curadores de playlists usam esses rankings para decidir o que lançar e o que promover, mas o chart só traz a ordem das faixas, sem dizer o que elas têm em comum. Este projeto descreve o perfil das faixas que estão no topo de cada gênero: duração, idade do lançamento, popularidade do artista e o quanto poucos artistas ocupam o ranking. Saber se esse perfil muda de um gênero para outro ajuda quem produz e divulga música a comparar a própria faixa com o que está sendo ouvido no gênero dela.

## Objetivo e recorte

**Objetivo:** montar um conjunto de dados confiável com as faixas dos charts da Deezer e os atributos da faixa, do álbum e do artista, que permita comparar o perfil das faixas populares entre gêneros nas etapas seguintes.

**Período:** um único retrato dos charts, na data da coleta registrada na seção 02 (ficha da fonte). O chart é ao vivo; o projeto não acompanha a evolução no tempo.

**Unidade de observação:** a faixa (objeto `track` da API). Uma mesma faixa pode estar em mais de um chart, e o gênero de comparação é o do chart em que ela aparece.

**População coberta:** as primeiras posições do chart geral e dos charts de cada gênero listado pela API (`/genre` e `/chart/{id_genero}/tracks`), com o detalhe de cada faixa, álbum e artista.

**Limites:** só faixas que estão nos charts, e não o catálogo inteiro; os charts são os vistos a partir do país de onde a coleta é feita, que a seção 02 registra; a API não informa número de reproduções, só o `rank`, um índice de popularidade calculado pela Deezer; atributos de áudio como `bpm` não entram nas perguntas porque a API costuma devolvê-los zerados quando a Deezer não os calculou.

## Perguntas analíticas

| ID | Pergunta a investigar | Dados necessários |
|---|---|---|
| P1 | Como a duração das faixas varia entre os gêneros dos charts da Deezer na data da coleta? | `duration` (segundos) da faixa; gênero do chart de origem (`/genre`, `/chart/{id_genero}/tracks`) |
| P2 | Que parte das faixas de cada chart de gênero foi lançada nos 12 meses anteriores à coleta? | `release_date` de `/track/{id}`; gênero do chart de origem; data da coleta |
| P3 | Faixas de artistas com mais fãs têm `rank` mais alto, no chart geral e dentro de cada gênero, na data da coleta? | `rank` da faixa; `nb_fan` de `/artist/{id}`; gênero do chart de origem |
| P4 | Quantos artistas distintos ocupam as posições de cada chart de gênero e que fatia dessas posições fica com os 5 artistas com mais faixas? | `artist.id` do item do chart; `position`; gênero do chart de origem |

## Viabilidade inicial

Todos os campos das perguntas existem na API pública da Deezer, sem autenticação: `duration`, `rank`, `position` e `artist.id` vêm em cada item de `/chart/{id_genero}/tracks`, `release_date` vem de `/track/{id}` e `nb_fan` vem de `/artist/{id}`; a lista de gêneros vem de `/genre` (documentação da API e app DataAudio, fontes 1 e 2; resumo em `base/api-deezer.md`, seções 2 e 3). Como o projeto coleta o chart de cada gênero, o gênero de origem fica registrado em cada item, sem depender do gênero do álbum.

As lacunas previstas, a confirmar na avaliação de qualidade (seção 03), são quatro. Primeiro, uma faixa pode estar no chart geral e no do seu gênero, então comparar gêneros pede contar a faixa em cada chart onde ela está, e a deduplicação precisa preservar o gênero de origem. Segundo, `release_date` e `nb_fan` podem vir ausentes ou zerados em parte dos registros, o que reduziria a base de P2 e P3. Terceiro, o gênero do chart é uma classificação da Deezer, e uma faixa do chart "Pop" pode ter outro gênero no álbum. Quarto, um único retrato não permite falar de tendência; as perguntas descrevem os charts de um dia.
