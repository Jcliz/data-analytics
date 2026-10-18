# Compreensão e qualidade

<!--
Área C (T03) · Critérios C3.1 a C3.5 · Leia: base/qualidade-de-dados.md, base/api-deezer.md §4 e ADR-0004.
Evidência = notebook §3 + título da célula. Contagens usam ocorrências nos charts do retrato de 16/10/2026.
Esta seção diagnostica os problemas; as decisões de tratamento ficam com a Área D (T04).
-->

**Unidade de observação:** ocorrência de faixa num chart de origem, no retrato de 16/10/2026: 2.800 ocorrências, 102 atributos, 2.581 faixas, 28 charts (geral e 27 gêneros). Evidência: notebook §3, célula “Visão geral e tipos observados”, sobre `dados/brutos/2026-10-16/`.

**Identificação dos registros:** `id` identifica a faixa e se repete entre charts; a chave é o par `chart_id_genero` e `id`, com zero excedentes em 2.800 (retratos futuros exigirão a data na chave). A posição pertence ao chart, não à faixa. Evidência: notebook §3, célula “Duplicidade e limite da chave”.

## Dicionário inicial dos dados

Atributos usados pelas P1–P4, pelo RA2 e por este diagnóstico; os demais (URLs, capas, países, colaboradores) ficam no bruto. Os 102 atributos e suas ausências estão nas células “Visão geral e tipos observados” e “Ausências nulas e textos vazios”. Tipos do pandas 2.2.3; textos são `object`, sem conversão de data.

| Atributo | Significado e uso | Tipo observado | Unidade ou domínio |
|---|---|---|---|
| `chart_id_genero` | Id do chart de origem; grupo das P1–P4 | int64 | Inteiro ≥ 0; 0 = geral |
| `chart_nome_genero` | Nome do chart; grupo das P1–P4 e gênero do evento RA2 | object | Texto; All = geral |
| `chart_ordem` | Ordem da ingestão; verifica a posição (P4) | int64 | Inteiro positivo, por chart |
| `id` | Id da faixa nas P1–P4; origem de id_faixa no RA2 | int64 | Inteiro positivo; repete entre charts |
| `title` | Título; identificação nas P1–P4 | object | Texto |
| `title_version` | Versão; ausência informativa | object | Texto ou nulo; vazio permitido |
| `duration` | Duração (P1); limite da duração ouvida no RA2 | int64 | Segundos, inteiro positivo |
| `rank` | Popularidade (P3); peso do sorteio no RA2 | int64 | Inteiro ≥ 0; não é a posição |
| `position` | Posição no chart (P4) | int64 | Inteiro positivo |
| `explicit_lyrics` | Conteúdo explícito; verificação de tipo | bool | Booleano |
| `preview` | URL da prévia; ausência, sem uso nas P1–P4 | object | Texto, pode ser vazio |
| `artist_id` | Id do artista (P3 e contagem da P4) | int64 | Inteiro positivo |
| `artist_name` | Nome do artista (P3–P4, evento RA2) | object | Texto; agrupar pelo id |
| `album_id` | Id do álbum; chave do enriquecimento | int64 | Inteiro positivo |
| `detalhe_faixa_id` | Id de /track; integridade da junção | int64 | Domínio de id |
| `detalhe_faixa_duration` | Duração em /track; consistência com duration | int64 | Segundos, inteiro positivo |
| `detalhe_faixa_rank` | Rank em /track; consistência com rank | int64 | Inteiro ≥ 0 |
| `detalhe_faixa_release_date` | Lançamento da faixa (P2), não do álbum | object | AAAA-MM-DD; até a coleta |
| `detalhe_faixa_bpm` | Andamento; diagnóstico, sem uso nas P1–P4 | float64 | BPM, real; zero a avaliar |
| `detalhe_faixa_gain` | Ganho; diagnóstico, sem uso nas P1–P4 | float64 | dB, real; negativo válido, zero a avaliar |
| `detalhe_album_id` | Id de /album; integridade da junção | int64 | Domínio de album_id |
| `detalhe_album_genre_id` | Gênero do álbum; não é o grupo das P1–P4 | int64 | Inteiro; ≤ 0 é genérico |
| `detalhe_album_release_date` | Lançamento do álbum; formato, não substitui a data da P2 | object | AAAA-MM-DD; até a coleta |
| `detalhe_artista_id` | Id de /artist; integridade da junção | int64 | Domínio de artist_id |
| `detalhe_artista_nb_fan` | Fãs do artista (P3) | int64 | Inteiro ≥ 0 |

## Diagnóstico de qualidade

Denominador: **2.800 ocorrências**; as verificações não se somam e repetições contam só os excedentes.

| ID | Verificação e regra | Resultado observado | Evidência no notebook §3 |
|---|---|---|---|
| Q1 | Ausência em campo essencial às P1–P4 ou RA2 | 0/2.800 (0,00%) | “Ausências nulas e textos vazios” |
| Q2 | Ausência de preview (nulo ou vazio) | 1/2.800 (0,04%) | “Ausências nulas e textos vazios” |
| Q3 | Ausência de title_version (nulo ou vazio) | 2.533/2.800 (90,46%) | “Ausências nulas e textos vazios” |
| Q4 | Excedentes por id | 219/2.800 (7,82%) | “Duplicidade e limite da chave” |
| Q5 | Excedentes pelo par chart_id_genero e id | 0/2.800 (0,00%) | “Duplicidade e limite da chave” |
| Q6 | Linhas inteiras repetidas | 0/2.800 (0,00%) | “Duplicidade e limite da chave” |
| Q7 | Tipo divergente do inteiro, real ou booleano esperado | 0/2.800 (0,00%) | “Estatísticas descritivas e domínios numéricos” |
| Q8 | Numéricos não finitos, ausentes ou fora do domínio | 0/2.800 (0,00%) | “Estatísticas descritivas e domínios numéricos” |
| Q9 | bpm igual a zero (dado não informado) | 1.890/2.800 (67,50%) | “Estatísticas descritivas e domínios numéricos” |
| Q10 | gain igual a zero (a avaliar) | 27/2.800 (0,96%) | “Estatísticas descritivas e domínios numéricos” |
| Q11 | Data fora de AAAA-MM-DD, inválida ou fora de 1900 até a coleta | 1/2.800 (0,04%) | “Datas, formatos e categorias” |
| Q12 | Espaços nas pontas de título, artista ou gênero | 1/2.800 (0,04%) | “Datas, formatos e categorias” |
| Q13 | Mais de um nome por id de artista | 0/2.800 (0,00%) | “Datas, formatos e categorias” |
| Q14 | Gênero com mais de um nome, ou nome com mais de um id | 0/2.800 (0,00%) | “Datas, formatos e categorias” |
| Q15 | Chart geral (id 0), que não é gênero | 100/2.800 (3,57%) | “Datas, formatos e categorias” |
| Q16 | Gênero do álbum genérico (id ≤ 0) | 11/2.800 (0,39%) | “Datas, formatos e categorias” |
| Q17 | Duração fora de Q1 − 1,5 IQR a Q3 + 1,5 IQR | 143/2.800 (5,11%) | “Possíveis outliers e integridade do enriquecimento” |
| Q18 | Rank fora de Q1 − 1,5 IQR a Q3 + 1,5 IQR | 0/2.800 (0,00%) | “Possíveis outliers e integridade do enriquecimento” |
| Q19 | Id ausente ou divergente na junção faixa/álbum/artista | 0/2.800 (0,00%) | “Possíveis outliers e integridade do enriquecimento” |
| Q20 | Duração do chart diferente da de /track | 0/2.800 (0,00%) | “Possíveis outliers e integridade do enriquecimento” |
| Q21 | Rank do chart diferente do de /track | 0/2.800 (0,00%) | “Possíveis outliers e integridade do enriquecimento” |

Q1 cobre `id`, `chart_id_genero`, `chart_nome_genero`, `title`, `duration`, `rank`, `position`, `artist_id`, `artist_name`, `album_id`, `detalhe_faixa_release_date` e `detalhe_artista_nb_fan`. Q7 espera inteiros nas chaves e contagens, reais em BPM e gain e booleano em `explicit_lyrics`. Q8 sinaliza não finitos, valores não positivos em duração, posição e ids, e negativos em rank, fãs ou BPM; não há teto de rank, e gain negativo é válido.

Em Q11, a faixa 4346251442, “Dirty Bird”, tem data `2026-10-28` (faixa e álbum), posterior à coleta de 16/10; talvez lançamento anunciado, causa não confirmada. Em Q17, os limites são 66,5 a 366,5 s, e as durações vão de 41 a 2.120 s. Em Q18, os limites de rank são −445.721,75 a 1.316.536,25. Evidências: células “Datas, formatos e categorias” e “Possíveis outliers e integridade do enriquecimento”.

Uma ocorrência não tem capa nem lista de faixas do álbum (1/2.800; 0,04%), metadados fora das P1–P4 e do RA2. Em `title_version`, há 57 nulos e 2.476 vazios: versão não informada, sem motivo para excluir faixa. Evidência: célula “Ausências nulas e textos vazios”.

## Impacto dos problemas identificados

Prioridade: preservar os grupos das P1–P4. Q4 não autoriza descartar as 219 ocorrências excedentes; a preparação mantém o vínculo faixa-chart. Q15 exige separar o chart geral dos gêneros, e Q16 mostra que o gênero do álbum não substitui o de origem. Q11 pede decisão para o lançamento futuro não contar nos 12 meses da P2.

Q9 e Q10 são secundários: P1–P4 e o RA2 não usam BPM nem gain. Q12 pede inspecionar antes de padronizar; Q17, revisar os extremos sem excluí-los, pois IQR não prova erro. Q2 não afeta as perguntas.

Q1, Q5–Q8, Q13–Q14 e Q18–Q21 não acharam ocorrências nos testes executados. As decisões estão na seção 04; esta seção não altera `df_bruto`.
