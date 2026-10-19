# Problema e perguntas analíticas

## Contexto e problema

Os charts da Deezer mostram as faixas mais ouvidas no geral e em cada gênero. Artistas, gravadoras e curadores de playlists os usam para decidir o que lançar e promover, mas o chart traz só a ordem das faixas, não o que elas têm em comum. Este projeto descreve o perfil das faixas do topo de cada gênero: duração, idade do lançamento, popularidade do artista e concentração de poucos artistas no ranking. Saber se esse perfil muda entre gêneros ajuda quem produz e divulga música a comparar a própria faixa com o que se ouve no gênero dela.

## Objetivo e recorte

**Objetivo:** montar um conjunto de dados confiável com as faixas dos charts da Deezer e os atributos da faixa, do álbum e do artista, para comparar o perfil das faixas populares entre gêneros nas etapas seguintes.

**Período:** um único retrato dos charts, na data da coleta registrada na seção 02 (ficha da fonte). O chart é ao vivo; o projeto não acompanha sua evolução.

**Unidade de observação:** a faixa (objeto `track` da API). Uma faixa pode estar em mais de um chart; o gênero de comparação é o do chart em que ela aparece.

**População coberta:** as primeiras posições do chart geral e dos charts de cada gênero listado pela API (`/genre` e `/chart/{id_genero}/tracks`), com o detalhe de cada faixa, álbum e artista.

**Limites:** só faixas dos charts, não o catálogo inteiro; charts vistos a partir do país da coleta, registrado na seção 02; sem número de reproduções, só o `rank`, índice de popularidade calculado pela Deezer; atributos de áudio como `bpm` ficam fora das perguntas, porque a API costuma devolvê-los zerados quando não os calculou.

## Perguntas analíticas

| ID | Pergunta a investigar | Dados necessários |
|---|---|---|
| P1 | Como a duração das faixas varia entre os gêneros dos charts da Deezer na data da coleta? | `duration` (segundos) da faixa; gênero do chart de origem (`/genre`, `/chart/{id_genero}/tracks`) |
| P2 | Que parte das faixas de cada chart de gênero foi lançada nos 12 meses anteriores à coleta? | `release_date` de `/track/{id}`; gênero do chart de origem; data da coleta |
| P3 | Faixas de artistas com mais fãs têm `rank` mais alto, no chart geral e dentro de cada gênero, na data da coleta? | `rank` da faixa; `nb_fan` de `/artist/{id}`; gênero do chart de origem |
| P4 | Quantos artistas distintos ocupam as posições de cada chart de gênero e que fatia dessas posições fica com os 5 artistas com mais faixas? | `artist.id` do item do chart; `position`; gênero do chart de origem |

## Viabilidade inicial

Todos os campos das perguntas existem na API pública da Deezer, sem autenticação: `duration`, `rank`, `position` e `artist.id` em `/chart/{id_genero}/tracks`, `release_date` em `/track/{id}`, `nb_fan` em `/artist/{id}` e os gêneros em `/genre` (fontes 1 e 2; `base/api-deezer.md`, seções 2 e 3). Coletar cada chart de gênero registra o gênero de origem em cada item, sem depender do gênero do álbum.

Lacunas a confirmar na seção 03: a faixa pode estar no chart geral e no do seu gênero, e a deduplicação precisa preservar o gênero de origem; `release_date` e `nb_fan` podem vir ausentes ou zerados, reduzindo a base de P2 e P3; o gênero do chart, da Deezer, pode diferir do gênero do álbum; e um único retrato não mostra tendência.
