---
id: api-deezer
titulo: "API da Deezer: endpoints, limites e armadilhas"
tipo: base
status: vigente
atualizado: 2026-10-15
fontes: [1, 2]
relacionados: [adr-0001, adr-0004, qualidade-de-dados]
---
# API da Deezer: endpoints, limites e armadilhas

> Marcação: [Fato] veio do código do dataaudio ou da documentação; [Inferência] é conhecimento prévio da API que **precisa ser confirmado na primeira coleta** (o ambiente onde este arquivo foi escrito não tinha acesso à API). Ao confirmar, troque por [Fato] e cite a célula.

## 1. Visão geral

- Base: `https://api.deezer.com`. Requisições `GET`, resposta em JSON, **sem autenticação** para dados públicos [Fato, fonte 2: o dataaudio não envia chave].
- Listas vêm no envelope `{"data": [...], "total": N, "next": "url da próxima página"}`, paginadas por `index` (deslocamento) e `limit` (tamanho da página) [Fato, fonte 2: `fetchChart(index, limit)` e `search(q, index, limit)`].

## 2. Endpoints úteis

| Endpoint | O que devolve | Uso sugerido | Marcação |
|---|---|---|---|
| `/chart/0/tracks?index=&limit=` | Faixas do chart geral | Núcleo da base (é o que o dataaudio usa no catálogo) | [Fato, fonte 2] |
| `/search?q=&index=&limit=` | Faixas que casam com o texto | Ampliar a base por artista ou termo | [Fato, fonte 2] |
| `/track/{id}` | Faixa completa: `isrc`, `release_date`, `bpm`, `gain`, `track_position`, `disk_number`, `available_countries`, `contributors` | Enriquecer cada faixa | [Fato, fonte 2] (endpoint); campos [Inferência] |
| `/genre` | Lista de gêneros (`id`, `name`) | Montar a lista de charts por gênero | [Inferência] |
| `/chart/{id_genero}/tracks` | Chart de um gênero | Aumentar o volume e ter o gênero de origem | [Inferência] |
| `/album/{id}` | Álbum: `genre_id`, `genres`, `label`, `release_date`, `record_type`, `nb_tracks`, `fans` | Gênero e gravadora da faixa | [Inferência] |
| `/artist/{id}` | Artista: `nb_album`, `nb_fan` | Popularidade do artista | [Inferência] |

## 3. Objeto faixa (resumo)

Campos do item de chart ou de busca [Fato para os usados pelo dataaudio: `id`, `title`, `duration`, `preview`, `artist.name`, `album.title`, `album.cover_*`; os demais são Inferência]:

`id`, `title`, `title_short`, `title_version`, `link`, `duration` (segundos), `rank` (popularidade, inteiro), `explicit_lyrics` (booleano), `explicit_content_lyrics`, `explicit_content_cover`, `preview` (URL de 30 s), `md5_image`, `position` (só no chart), `artist{id, name, ...}`, `album{id, title, cover_*, ...}`, `type`.

O dataaudio já lida com dois formatos do mesmo objeto (aninhado da API e plano persistido) e trata `preview` vazio como ausente e `duration` que pode vir como texto [Fato, fonte 2, `Track.fromJson`]. São bons indícios do que checar na qualidade.

## 4. O que esperar de qualidade (a confirmar)

| Situação | Por que acontece | Onde vira verificação |
|---|---|---|
| Mesma faixa em vários charts de gênero | Uma faixa pode estar no chart geral e no do gênero | duplicidade por `id` |
| `bpm` = 0 e `gain` = 0 | A Deezer não calculou o valor [Inferência] | valor inválido |
| `release_date` = `0000-00-00` ou ausente | Data desconhecida no catálogo [Inferência] | data inválida |
| `preview` vazio | Faixa sem prévia liberada [Fato, fonte 2] | ausência |
| `title_version` vazio na maioria | Só versões (remix, ao vivo) preenchem [Inferência] | ausência esperada, não erro |
| Gênero do álbum ausente ou genérico | Álbum sem `genre_id` [Inferência] | categoria inconsistente |
| `duration` muito curto ou muito longo | Vinhetas, mixes longos | possível outlier |
| Resposta `{"error": {...}}` com HTTP 200 | Limite de requisições ou objeto inexistente [Inferência] | falha de ingestão a tratar no código |

## 5. Limites e cuidados na coleta

- **Limite de requisições:** cerca de 50 requisições a cada 5 segundos [Inferência]. Ao exceder, a API devolve um objeto `error` (código 4, *Quota limit exceeded*) [Inferência]. Faça uma pausa curta entre chamadas e repita a chamada que falhar.
- **Erro com HTTP 200:** sempre conferir se a resposta tem a chave `error` antes de usar `data` [Inferência].
- **País da requisição:** o chart e a disponibilidade podem variar com o país de onde vem o IP (o Colab costuma sair pelos EUA) [Inferência]. Registre de onde foi feita a coleta na ficha da fonte.
- **Tamanho do chart:** o chart costuma limitar a algumas centenas de itens no máximo [Inferência]; confira `total` na primeira resposta.

## 6. Desenho sugerido da coleta (área B decide)

1. `/genre` → lista de gêneros.
2. Para cada gênero (e o geral, `0`): `/chart/{id}/tracks` com paginação até acabar ou até um teto (ex.: 100 por gênero). Guardar o gênero de origem em cada item.
3. Para cada `id` de faixa único: `/track/{id}` (campos extras). Para cada álbum único: `/album/{id}` (gênero, gravadora). Para cada artista único: `/artist/{id}` (`nb_fan`, `nb_album`).
4. Gravar cada resposta crua em `dados/brutos/AAAA-MM-DD/` (um arquivo por endpoint e página, ou um JSON por tipo de objeto), mais um `metadados.json` com data, hora, quantidade de chamadas, erros e versões.
5. Achatar para `df_bruto` (uma linha por item coletado, mantendo as duplicatas entre charts; deduplicar é decisão da área D).

Volume esperado: alguns milhares de linhas antes da deduplicação e algumas centenas a poucos milhares de faixas únicas [Inferência]. Com a pausa entre chamadas, a coleta leva alguns minutos.

---

## Ligações

- **Decisões:** [ADR-0001](../docs/adr/0001-fonte-de-dados-api-deezer.md), [ADR-0004](../docs/adr/0004-retrato-bruto-versionado.md)
- **Qualidade:** [qualidade-de-dados](qualidade-de-dados.md) · **Fontes:** [fontes](fontes.md)
