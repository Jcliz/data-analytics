---
id: analise-e-ml
titulo: "Análise descritiva, visualização e Machine Learning no RA3"
tipo: base
status: vigente
atualizado: 2026-11-05
fontes: [12, 13, 14, 15]
relacionados: [adr-0010, adr-0012, adr-0013, material-de-aula]
---
# Análise descritiva, visualização e Machine Learning no RA3

> O que medir, que gráfico usar e como montar o modelo com **estes** dados. Os números marcados [Fato] foram calculados em 05/11/2026 sobre `dados/preparados/faixas_preparadas.csv`; no texto entregue, use os números das saídas do notebook.

## 1. Os dados que o RA3 recebe

- 2.800 ocorrências faixa-chart: 100 no chart geral e 2.700 em 27 charts de gênero, exatamente 100 por gênero [Fato]. A comparação entre gêneros usa só `tipo_chart == "genero"`; o geral serve de referência à parte (dicionário, "Leitura e limites de uso").
- 2.581 faixas distintas no arquivo e 2.578 nos charts de gênero [Fato]: a mesma faixa pode aparecer em mais de um gênero. Contar ocorrências e contar faixas dá números diferentes; diga qual é.
- Releitura com tipos: as oito colunas inteiras como `int64`, as datas com `parse_dates` (dicionário, "Leitura e limites de uso").

## 2. Medidas coerentes com cada variável (seção 1 do notebook do RA3)

| Variável | Perguntas | Forma observada | Tendência central | Dispersão | Distribuição |
|---|---|---|---|---|---|
| `duracao_s` | P1 | Assimetria 6,39; mínimo 41 s, mediana 213 s, máximo 2.120 s; extremos sinalizados por `duracao_fora_limites_iqr` [Fato] | **Mediana** por gênero (a média é puxada pelos extremos); mostrar a média ao lado para evidenciar a diferença | Intervalo interquartil (IQR) e amplitude; desvio-padrão com a ressalva dos extremos | Frequência por faixas de duração; mediana por gênero vai de 159,5 s (Kids) a 258,5 s (Metal) [Fato] |
| Idade da faixa na coleta (dias) | P2 | Lançamentos futuros sinalizados por `lancamento_posterior_coleta` | Mediana da idade por gênero | IQR | **Proporção** de ocorrências lançadas nos 12 meses anteriores à coleta (cerca de 22% nos gêneros [Fato]) |
| `rank` | P3 | Quase uniforme entre 807 e 999.724; média 441.632, mediana 439.398, assimetria 0,17 [Fato] | Média ou mediana (próximas) | Desvio-padrão (271.063 [Fato]) | Histograma por faixas de `rank` |
| `numero_fas` | P3 | Muito assimétrica (3,82): mediana 64.586, máximo 24,1 milhões, mínimo 0 [Fato] | **Mediana** | IQR; desvio-padrão só em escala log | Distribuição em escala log; correlação de **Spearman** com `rank` (0,60 [Fato]), que não exige relação linear |
| `id_artista` por chart | P4 | Até 100 posições por chart | Artistas distintos por gênero | Amplitude entre gêneros | **Concentração:** fatia das posições dos 5 artistas com mais faixas em cada chart |

Regra prática: com assimetria forte ou extremos, a mediana e o IQR representam melhor; a média entra para comparar, nunca sozinha. Diga no texto por que escolheu cada medida (o enunciado pede medidas "coerentes com as características dos dados").

## 3. Visualizações (seção 2)

O enunciado pede pelo menos três, de características diferentes, com identificação clara das variáveis e dos resultados e uma breve interpretação [Fato, fonte 13]. Título, eixos com nome e unidade e legenda quando houver grupos são a forma que o grupo usa para cumprir a "identificação clara". Sugestões, uma por pergunta:

| Pergunta | Gráfico | Por quê |
|---|---|---|
| P1 | Boxplot de `duracao_s` por gênero, ordenado pela mediana | Mostra mediana, IQR e extremos de 27 grupos de uma vez |
| P2 | Barras horizontais da proporção de lançamentos recentes por gênero | Compara proporções entre muitos grupos |
| P3 | Dispersão de `rank` × `numero_fas` (eixo x em escala log), com a correlação no título | Mostra a relação e a nuvem de exceções |
| P4 | Barras da fatia dos 5 artistas com mais posições por gênero | Mostra concentração |

Com 27 gêneros, prefira barras horizontais e ordenadas; evite pizza e cores demais. O grupo usa `matplotlib` (pandas `.plot` também serve); o enunciado aceita qualquer ferramenta. Cada gráfico numa célula própria com um comentário-título (`# Duração por gênero (boxplot)`), que é como a documentação o cita.

## 4. Machine Learning (seção 4)

Proposta em [ADR-0013](../docs/adr/0013-ra3-regressao-do-rank.md): regressão do `rank` a partir de fãs (log), duração, idade e gênero. O enunciado exige problema, alvo e características, separação treino e teste, treino com previsões e uma métrica [Fato, fonte 13]; os cuidados abaixo são recomendações do grupo (critério RC.4), não exigência:

- **Vazamento:** não use `posicao_chart` nem identificadores como característica.
- **Faixas repetidas:** separe treino e teste por `id_faixa` (`GroupShuffleSplit` do scikit-learn, com `random_state=SEMENTE_ML`), para a mesma faixa não ficar dos dois lados [Fato, fonte 14].
- **Linha de base:** compare o modelo com um que prevê sempre a mediana do treino (`DummyRegressor(strategy="median")`) [Fato, fonte 14]. Sem isso, um MAE sozinho não diz se o modelo ajuda.
- **Métricas:** MAE (na mesma unidade do `rank`, fácil de explicar) e R² (fração da variação explicada) [Fato, fonte 14].
- **Previsões:** mostre uma tabela curta (5 a 10 linhas) com valor real, previsto e erro.
- **Interpretação:** o que o desempenho significa para a P3 e o que o modelo não captura (o `rank` da Deezer tem fórmula não publicada [Inferência]).

## 5. Representatividade (seção 3)

Pontos que os dados já mostram: um retrato de um único dia (16/10/2026), de um único país aparente da coleta, limitado aos 100 primeiros de cada chart (limite da API), e 27 gêneros escolhidos pela própria Deezer (documento do RA1, seções 02 e 05). A população representada é "as faixas no topo dos charts da Deezer naquele dia", e não o catálogo inteiro nem a audiência de outros países. O conjunto inteiro é usado; não há amostragem, a não ser a separação treino e teste da seção 4.

---

## Ligações

- **Decisões:** [ADR-0010](../docs/adr/0010-problema-e-perguntas.md), [ADR-0012](../docs/adr/0012-ra3-no-notebook-e-entrega-por-url.md), [ADR-0013](../docs/adr/0013-ra3-regressao-do-rank.md)
- **Dados:** [dicionário do conjunto preparado](../dados/preparados/dicionario-faixas.md) · **Material de aula:** [material-de-aula](material-de-aula.md) · **Fontes:** [fontes](fontes.md)
