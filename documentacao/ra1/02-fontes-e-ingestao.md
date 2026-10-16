# Fontes de dados e ingestão

<!--
Área B (T02) · Critérios C2.1 a C2.5 · Leia: base/api-deezer.md, ADR-0001 e ADR-0004.
Evidência = notebook §2 + título da célula (ex.: notebook §2, célula "Coleta dos charts por gênero") ou caminho do arquivo.
Fonte única do projeto: F1 = API pública da Deezer (ADR-0001). O template pede uma ficha por fonte; aqui há uma só.
Os campos "Preencha após a coleta" saem do metadados.json do retrato e das saídas das células
"Metadados do retrato lido" e "Verificação do carregamento".
-->

## Ficha da fonte

**Identificação:** F1 • Charts de faixas da Deezer (chart geral e um chart por gênero), com os detalhes de cada faixa, álbum e artista.

**Origem e acesso:** Deezer • API pública `https://api.deezer.com`, sem autenticação e sem chave (documentação: https://developers.deezer.com/api) • data de acesso: [Preencha após a coleta: data do retrato, AAAA-MM-DD].

**Formato e volume:** JSON via API REST, gravado como recebido em arquivos JSON • [Preencha após a coleta: itens nos charts, faixas, álbuns e artistas únicos] • atributos da faixa (`id`, `title`, `duration`, `rank`, `explicit_lyrics`, `preview`, `position`, `bpm`, `isrc`, `release_date`), do álbum (`genre_id`, `genres`, `label`, `release_date`, `record_type`, `nb_tracks`) e do artista (`name`, `nb_fan`, `nb_album`); o `df_bruto` tem [Preencha após a coleta: número de colunas] colunas.

**Cobertura:** charts do dia da coleta, sem histórico: cada chart traz as faixas mais populares no momento da requisição, até 300 itens por chart • país aparente da requisição: [Preencha após a coleta: país do metadados.json, lido de `/infos`] • charts incluídos: o geral (gênero 0) e os gêneros devolvidos por `/genre`.

**Condições de uso:** API pública da Deezer, sem autenticação; os dados pertencem à Deezer e aos detentores de direitos e são usados aqui só para fins acadêmicos, sem redistribuição das prévias de áudio. A coleta respeita o limite de chamadas da API com pausa entre requisições.

## Relação com o problema

A fonte descreve as faixas que estão no topo da Deezer em cada gênero, com atributos da própria faixa (duração, letra explícita, posição e `rank` no chart, data de lançamento), do álbum (gênero e gravadora) e do artista (número de fãs). Isso permite comparar perfis de faixas entre gêneros, medir a presença de lançamentos recentes e a concentração de artistas nos charts, que são os recortes discutidos para o problema. O retrato é de um único dia e de um único país aparente, então a fonte não apoia perguntas sobre evolução no tempo nem comparações entre países.

[Preencha após a T01: IDs das perguntas P1…Pn que a fonte apoia e os campos que cada uma usa.]

## Procedimento de ingestão

| Etapa | Procedimento ou parâmetro | Evidência no repositório |
|---|---|---|
| 1 | Acesso à API: `GET` em `https://api.deezer.com` com pausa de 0,15 s entre chamadas, até 4 tentativas com espera crescente, tratamento do objeto `error` que a API devolve com HTTP 200 (o código 4, limite de chamadas, ganha nova tentativa; os demais são registrados) | notebook §2, célula "Parâmetros da coleta e acesso à API" |
| 2 | Charts: `/genre` para a lista de gêneros e `/chart/{id}/tracks` para o geral e para cada gênero, paginado por `index` e `limit=100`, até acabar o chart ou chegar a 300 itens; `/infos` registra o país aparente | notebook §2, célula "Coleta dos charts por gênero" |
| 3 | Detalhes: `/track/{id}` para cada faixa única, `/album/{id}` para cada álbum único e `/artist/{id}` para cada artista único | notebook §2, célula "Coleta dos detalhes de faixas, álbuns e artistas" |
| 4 | Retrato bruto: as respostas cruas vão para `dados/brutos/AAAA-MM-DD/` (`infos.json`, `generos.json`, `charts.json`, `faixas.json`, `albuns.json`, `artistas.json`) com um `metadados.json` (início e fim da coleta, país, parâmetros, chamadas por endpoint, novas tentativas e erros). As etapas 2 a 4 só rodam com `BAIXAR_DA_API = True` | notebook §2, célula "Gravação do retrato bruto"; [Preencha após a coleta: caminho do retrato] |
| 5 | Leitura: com `BAIXAR_DA_API = False` (padrão), o notebook lê o retrato mais recente de `dados/brutos/` e mostra o `metadados.json` dele | notebook §2, células "Leitura do retrato bruto mais recente" e "Metadados do retrato lido" |
| 6 | Montagem do `df_bruto`: uma linha por item de chart, com o chart de origem (`chart_id_genero`, `chart_nome_genero`, `chart_ordem`), e os campos de faixa, álbum e artista juntados pelo id (prefixos `detalhe_faixa_`, `detalhe_album_` e `detalhe_artista_`), sem limpeza e mantendo as faixas repetidas entre charts | notebook §2, célula "Montagem do df_bruto" |
| 7 | Verificação do carregamento: linhas contra os itens dos metadados, faixas, álbuns e artistas únicos, itens sem detalhe, colunas por origem e itens por chart | notebook §2, célula "Verificação do carregamento" |

## Resultado da ingestão

[Preencha após a coleta: df_bruto.shape, faixas únicas, chamadas e erros da coleta, com os números da célula "Verificação do carregamento".] Os dados brutos ficam versionados em `dados/brutos/AAAA-MM-DD/`, e qualquer execução do notebook lê esse mesmo retrato. A única etapa manual é a coleta: ela roda uma vez, no Google Colab ou na máquina de um integrante, porque a API precisa de acesso direto à internet, e o retrato gerado é enviado ao repositório.
