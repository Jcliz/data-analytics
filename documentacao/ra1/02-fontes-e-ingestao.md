# Fontes de dados e ingestão

<!--
Área B (T02) · Critérios C2.1 a C2.5 · Leia: base/api-deezer.md, ADR-0001 e ADR-0004.
Evidência = notebook §2 + título da célula (ex.: notebook §2, célula "Coleta dos charts por gênero") ou caminho do arquivo.
Fonte única do projeto: F1 = API pública da Deezer (ADR-0001). O template pede uma ficha por fonte; aqui há uma só.
Os campos "Preencha após a coleta" saem do metadados.json do retrato e das saídas das células
"Metadados do retrato lido" e "Verificação do carregamento".
-->

## Ficha da fonte

**Identificação:** F1 • Charts de faixas da Deezer (geral e um por gênero), com os detalhes de cada faixa, álbum e artista.

**Origem e acesso:** Deezer • API pública `https://api.deezer.com`, sem autenticação nem chave (documentação: https://developers.deezer.com/api) • data de acesso: 16/10/2026.

**Formato e volume:** JSON via API REST, gravado como recebido (57,7 MB no retrato de 16/10/2026) • 2.800 itens em 28 charts, com 2.581 faixas, 2.292 álbuns e 1.688 artistas únicos • atributos da faixa (`id`, `title`, `duration`, `rank`, `explicit_lyrics`, `preview`, `position`, `bpm`, `isrc`, `release_date`), do álbum (`genre_id`, `genres`, `label`, `release_date`, `record_type`, `nb_tracks`) e do artista (`name`, `nb_fan`, `nb_album`); o `df_bruto` tem 102 colunas.

**Cobertura:** charts do dia da coleta, sem histórico; cada um traz as 100 faixas mais populares no momento da requisição (`total` = 100 em todos) • país aparente: US (Estados Unidos) • charts: o geral (gênero 0) e os gêneros de `/genre`.

**Condições de uso:** API pública; os dados pertencem à Deezer e aos detentores de direitos e são usados só para fins acadêmicos, sem redistribuir as prévias de áudio. A coleta respeita o limite de chamadas com pausa entre requisições.

## Relação com o problema

Todos os campos das quatro perguntas (seção 01) vieram no retrato de 16/10/2026 e estão no `df_bruto`, e cada item guarda o chart de gênero de origem:

- **P1** (duração por gênero): `duration` e o gênero do chart (`chart_id_genero`, `chart_nome_genero`).
- **P2** (lançamentos dos 12 meses anteriores à coleta, por gênero): `detalhe_faixa_release_date`, o gênero do chart e a data da coleta, no `metadados.json`.
- **P3** (fãs do artista e `rank`): `rank`, `detalhe_artista_nb_fan` e o gênero do chart.
- **P4** (concentração de artistas por chart): `artist_id`, `position` e o gênero do chart.

Por ser de um único dia e país aparente (US), a fonte não apoia perguntas sobre evolução no tempo nem comparações entre países.

## Procedimento de ingestão

| Etapa | Procedimento ou parâmetro | Evidência no repositório |
|---|---|---|
| 1 | Acesso: `GET` em `https://api.deezer.com`, pausa de 0,15 s, até 4 tentativas com espera crescente; o objeto `error` devolvido com HTTP 200 é tratado (código 4, limite de chamadas, ganha nova tentativa; os demais são registrados) | notebook §2, célula "Parâmetros da coleta e acesso à API" |
| 2 | Charts: `/genre` lista os gêneros e `/chart/{id}/tracks` traz o geral e cada gênero, paginado por `index` e `limit=100`, até o fim ou 300 itens; `/infos` registra o país aparente | notebook §2, célula "Coleta dos charts por gênero" |
| 3 | Detalhes: `/track/{id}`, `/album/{id}` e `/artist/{id}` para cada faixa, álbum e artista únicos | notebook §2, célula "Coleta dos detalhes de faixas, álbuns e artistas" |
| 4 | Retrato bruto: respostas cruas em `dados/brutos/AAAA-MM-DD/` (`infos.json`, `generos.json`, `charts.json`, `faixas.json`, `albuns.json`, `artistas.json`) e `metadados.json` (início e fim, país, parâmetros, chamadas por endpoint, novas tentativas e erros). As etapas 2 a 4 só rodam com `BAIXAR_DA_API = True` | notebook §2, célula "Gravação do retrato bruto"; `dados/brutos/2026-10-16/` |
| 5 | Leitura: com `BAIXAR_DA_API = False` (padrão), lê o retrato mais recente de `dados/brutos/` e mostra o `metadados.json` | notebook §2, células "Leitura do retrato bruto mais recente" e "Metadados do retrato lido" |
| 6 | `df_bruto`: uma linha por item de chart, com a origem (`chart_id_genero`, `chart_nome_genero`, `chart_ordem`) e os campos de faixa, álbum e artista juntados pelo id (prefixos `detalhe_faixa_`, `detalhe_album_`, `detalhe_artista_`), sem limpeza e com as repetições entre charts | notebook §2, célula "Montagem do df_bruto" |
| 7 | Verificação: linhas contra os metadados, faixas, álbuns e artistas únicos, itens sem detalhe, colunas por origem e itens por chart | notebook §2, célula "Verificação do carregamento" |

## Resultado da ingestão

A coleta de 16/10/2026 (21h03 a 21h41 UTC) fez 6.591 chamadas, sem novas tentativas nem erros (`dados/brutos/2026-10-16/metadados.json`). Os 28 charts (o geral e 27 gêneros) vieram com 100 itens cada, numa página: é o que a API oferece (`total` = 100), abaixo do teto de 300. O `df_bruto` tem 2.800 linhas e 102 colunas, com 2.581 faixas, 2.292 álbuns e 1.688 artistas únicos, e nenhum item sem detalhe (notebook §2, célula "Verificação do carregamento"). O retrato fica versionado em `dados/brutos/AAAA-MM-DD/` e toda execução lê o mesmo. A única etapa manual é a coleta, feita uma vez no Google Colab ou na máquina de um integrante (a API exige acesso direto à internet), com o retrato enviado ao repositório.
