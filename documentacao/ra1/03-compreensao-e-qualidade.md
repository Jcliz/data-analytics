# Compreensão e qualidade

<!--
Área C (T03) · Critérios C3.1 a C3.5 · Leia: base/qualidade-de-dados.md, base/api-deezer.md §4 e ADR-0004.
Evidência = notebook §3 + título da célula. Contagens usam ocorrências nos charts do retrato de 16/10/2026.
Esta seção diagnostica os problemas; as decisões de tratamento ficam com a Área D (T04).
-->

**Unidade de observação:** uma linha do bruto representa uma ocorrência de faixa em um chart de origem, no retrato de 16/10/2026. São 2.800 ocorrências, 102 atributos, 2.581 faixas e 28 charts (o geral e 27 gêneros). Evidência: notebook §3, célula “Visão geral e tipos observados”, executada sobre o retrato de `dados/brutos/2026-10-16/`.

**Identificação dos registros:** `id` identifica a faixa, mas se repete entre charts. A chave candidata no retrato é o par `chart_id_genero` e `id`: zero ocorrências excedentes em 2.800. Para combinar retratos futuros será preciso incluir a data da coleta na chave. A posição pertence ao chart, não à faixa em geral. Evidência: notebook §3, célula “Duplicidade e limite da chave”.

## Dicionário inicial dos dados

A tabela cobre os atributos usados pelas perguntas P1–P4, pela simulação do RA2 e pelas verificações deste diagnóstico. Os demais atributos são metadados técnicos preservados no bruto (URLs, capas, listas de países e colaboradores e campos redundantes); não entram nas perguntas nem nos eventos. O inventário completo dos 102 atributos, com tipo observado, e a tabela de ausências de todos eles estão nas células “Visão geral e tipos observados” e “Ausências nulas e textos vazios”. Tipos abaixo observados com pandas 2.2.3; textos são `object`, não datas já convertidas.

| Atributo | Significado e uso | Tipo observado | Unidade ou domínio |
|---|---|---|---|
| `chart_id_genero` | Identificador do chart de origem; grupo das P1–P4 | int64 | Inteiro não negativo; 0 = geral |
| `chart_nome_genero` | Nome do chart de origem; grupo das P1–P4 e gênero do evento RA2 | object | Texto; All é o chart geral |
| `chart_ordem` | Ordem registrada pela ingestão; verificação da posição para P4 | int64 | Inteiro positivo, por chart |
| `id` | Identificador da faixa nas P1–P4 e origem de id_faixa no RA2 | int64 | Inteiro positivo; repetível entre charts |
| `title` | Título da faixa; identificação e inspeção das P1–P4 | object | Texto |
| `title_version` | Versão da faixa; inspeção de ausência informativa | object | Texto ou nulo; vazio é permitido na fonte |
| `duration` | Duração da faixa na P1; limite da duração ouvida no RA2 | int64 | Segundos, inteiro positivo |
| `rank` | Popularidade da faixa na P3; peso do sorteio no RA2 | int64 | Inteiro não negativo; não é a posição no chart |
| `position` | Posição no chart de origem na P4 | int64 | Inteiro positivo |
| `explicit_lyrics` | Indicador de conteúdo explícito; verificação de tipo | bool | Booleano |
| `preview` | URL da prévia; verificação de ausência, sem uso nas P1–P4 | object | Texto, pode estar vazio |
| `artist_id` | Identificador do artista na P3 e na contagem de artistas da P4 | int64 | Inteiro positivo |
| `artist_name` | Nome do artista; identificação das P3–P4 e evento RA2 | object | Texto; agrupar artistas pelo id |
| `album_id` | Identificador do álbum; chave do enriquecimento das P1–P4 | int64 | Inteiro positivo |
| `detalhe_faixa_id` | Id retornado por /track; integridade do enriquecimento | int64 | Mesmo domínio de id |
| `detalhe_faixa_duration` | Duração em /track; conferir consistência com duration da P1 | int64 | Segundos, inteiro positivo |
| `detalhe_faixa_rank` | Rank em /track; conferir consistência com rank da P3 | int64 | Inteiro não negativo |
| `detalhe_faixa_release_date` | Lançamento da faixa na P2; não confundir com lançamento do álbum | object | Texto AAAA-MM-DD; validar até a coleta |
| `detalhe_faixa_bpm` | Andamento; diagnóstico de qualidade, sem uso nas P1–P4 | float64 | Batidas por minuto, real; zero requer avaliação |
| `detalhe_faixa_gain` | Ajuste de ganho; diagnóstico, sem uso nas P1–P4 | float64 | dB, real; negativo permitido, zero a avaliar |
| `detalhe_album_id` | Id em /album; integridade do enriquecimento | int64 | Mesmo domínio de album_id |
| `detalhe_album_genre_id` | Gênero do álbum; diagnóstico, não é o grupo das P1–P4 | int64 | Inteiro; valor não positivo é genérico |
| `detalhe_album_release_date` | Lançamento do álbum; diagnóstico de formato, não substitui a data da P2 | object | Texto AAAA-MM-DD; validar até a coleta |
| `detalhe_artista_id` | Id em /artist; integridade do enriquecimento | int64 | Mesmo domínio de artist_id |
| `detalhe_artista_nb_fan` | Quantidade de fãs do artista na P3 | int64 | Inteiro não negativo |

## Diagnóstico de qualidade

Todas as proporções abaixo usam **2.800 ocorrências** como denominador; as verificações podem atingir a mesma linha e não devem ser somadas. Repetições contam apenas as ocorrências excedentes após a primeira. Não se trata de resultados das perguntas analíticas.

| ID | Verificação e regra | Resultado observado | Evidência no notebook §3 |
|---|---|---|---|
| Q1 | Ausência em pelo menos um campo essencial às P1–P4 ou RA2 | 0/2.800 (0,00%) | Célula “Ausências nulas e textos vazios” |
| Q2 | Ausência de preview (nulo ou texto vazio) | 1/2.800 (0,04%) | Célula “Ausências nulas e textos vazios” |
| Q3 | Ausência de title_version (nulo ou texto vazio) | 2.533/2.800 (90,46%) | Célula “Ausências nulas e textos vazios” |
| Q4 | Ocorrências excedentes por id, após a primeira | 219/2.800 (7,82%) | Célula “Duplicidade e limite da chave” |
| Q5 | Ocorrências excedentes pelo par chart_id_genero e id | 0/2.800 (0,00%) | Célula “Duplicidade e limite da chave” |
| Q6 | Linhas inteiras repetidas, após a primeira | 0/2.800 (0,00%) | Célula “Duplicidade e limite da chave” |
| Q7 | Tipo divergente de numérico inteiro/real ou booleano esperado | 0/2.800 (0,00%) | Célula “Estatísticas descritivas e domínios numéricos” |
| Q8 | Numéricos não finitos/ausentes ou fora dos domínios descritos | 0/2.800 (0,00%) | Célula “Estatísticas descritivas e domínios numéricos” |
| Q9 | bpm igual a zero (sinal de dado não informado) | 1.890/2.800 (67,50%) | Célula “Estatísticas descritivas e domínios numéricos” |
| Q10 | gain igual a zero (a avaliar, não erro comprovado) | 27/2.800 (0,96%) | Célula “Estatísticas descritivas e domínios numéricos” |
| Q11 | Data fora de AAAA-MM-DD, inválida ou fora de 1900 até a coleta | 1/2.800 (0,04%) | Célula “Datas, formatos e categorias” |
| Q12 | Espaços nas pontas de título, artista ou gênero | 1/2.800 (0,04%) | Célula “Datas, formatos e categorias” |
| Q13 | Mais de um nome para um id de artista | 0/2.800 (0,00%) | Célula “Datas, formatos e categorias” |
| Q14 | Gênero com mais de um nome ou nome normalizado com mais de um id | 0/2.800 (0,00%) | Célula “Datas, formatos e categorias” |
| Q15 | Chart geral id 0: não representa um gênero específico | 100/2.800 (3,57%) | Célula “Datas, formatos e categorias” |
| Q16 | Gênero do álbum genérico (id menor ou igual a zero) | 11/2.800 (0,39%) | Célula “Datas, formatos e categorias” |
| Q17 | Duração fora de Q1 − 1,5 IQR a Q3 + 1,5 IQR | 143/2.800 (5,11%) | Célula “Possíveis outliers e integridade do enriquecimento” |
| Q18 | Rank fora de Q1 − 1,5 IQR a Q3 + 1,5 IQR | 0/2.800 (0,00%) | Célula “Possíveis outliers e integridade do enriquecimento” |
| Q19 | Id ausente ou divergente na junção de faixa/álbum/artista | 0/2.800 (0,00%) | Célula “Possíveis outliers e integridade do enriquecimento” |
| Q20 | Duração do chart diferente da duração em /track | 0/2.800 (0,00%) | Célula “Possíveis outliers e integridade do enriquecimento” |
| Q21 | Rank do chart diferente do rank em /track | 0/2.800 (0,00%) | Célula “Possíveis outliers e integridade do enriquecimento” |

Q1 cobre `id`, `chart_id_genero`, `chart_nome_genero`, `title`, `duration`, `rank`, `position`, `artist_id`, `artist_name`, `album_id`, `detalhe_faixa_release_date` e `detalhe_artista_nb_fan`. Q7 verifica inteiros numéricos nas chaves, ordem, duração, rank, posição e fãs; reais numéricos em BPM e gain; e booleanos em `explicit_lyrics`. Q8 sinaliza ausentes/não finitos, duração e posição não positivas, ids de faixa/artista/álbum não positivos, rank/fãs/BPM negativos. Não pressupomos um teto universal de rank nem que gain negativo seja inválido.

Em Q11, a faixa 4346251442, “Dirty Bird”, tem data `2026-10-28` na faixa e no álbum, posterior à coleta de 16/10. A data é sintaticamente válida; o sinal indica uma inconsistência temporal para o recorte da P2, podendo representar lançamento anunciado. A causa não foi confirmada. Em Q17, os limites IQR de duração são 66,5 a 366,5 segundos; a duração observada varia de 41 a 2.120 segundos. Em Q18, os limites de rank são −445.721,75 a 1.316.536,25, sem ocorrências externas. Evidências: células “Datas, formatos e categorias” e “Possíveis outliers e integridade do enriquecimento”.

A tabela completa de ausências também registra uma ocorrência sem capa e sem lista de faixas do álbum (1/2.800; 0,04%), inclusive nas colunas repetidas do enriquecimento. Esses metadados técnicos não alimentam P1–P4 ou o evento do RA2. Em `title_version`, são 57 nulos e 2.476 textos vazios; a ausência pode significar que não há versão complementar informada, e não exige excluir uma faixa. Evidência: célula “Ausências nulas e textos vazios”.

## Impacto dos problemas identificados

A prioridade é preservar os grupos das P1–P4: Q4 não autoriza descartar os charts das 219 ocorrências excedentes. A preparação deve manter o vínculo faixa-chart, por pares ou por lista explícita de origens. Q15 exige distinguir o chart geral das comparações por gênero; Q16 reforça que o gênero do álbum não substitui o gênero de origem. Q11 requer uma decisão documentada para que o lançamento futuro não entre como lançamento já ocorrido nos 12 meses anteriores à coleta da P2.

Q9 e Q10 são secundários para P1–P4 e para o RA2, que não usam BPM nem gain. BPM zero é suspeita de dado não informado, não evidência confirmada de como a API calcula o campo; gain zero isoladamente não prova erro. Q12 pede inspecionar o espaço no texto antes de padronizar. Q17 pede revisar os extremos, mantendo-os quando forem faixas válidas: o critério IQR não demonstra erro. Q2 não afeta as perguntas nem exige excluir a faixa.

Q1, Q5–Q8, Q13–Q14 e Q18–Q21 não encontraram ocorrências problemáticas segundo as regras descritas. Isso limita a conclusão aos campos e testes executados. As decisões de manter ou corrigir cada Q estão documentadas na seção 04. Esta seção diagnostica e não altera `df_bruto`.
