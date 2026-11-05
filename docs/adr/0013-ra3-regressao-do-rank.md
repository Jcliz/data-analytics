---
id: adr-0013
titulo: "ADR-0013 — Machine Learning do RA3: regressão do rank da faixa"
tipo: decisao
decisao: "0013"
status: proposta
data: 2026-11-05
decisor: proposta para o grupo
entregas: [RA3]
areas: [B]
fontes: [13, 14]
relacionados: [adr-0010, adr-0012, analise-e-ml]
---
# ADR-0013 — Machine Learning do RA3: regressão do `rank` da faixa

- **Status:** proposta · **Data:** 05/11/2026 · A área responsável pela seção 16 pode trocar a abordagem, desde que registre aqui o motivo. O que o enunciado exige está nos critérios R16; o resto desta proposta (log dos fãs, separação por faixa, semente, linha de base) é escolha do grupo.

## Contexto

- O RA3 pede uma aplicação simples de aprendizagem supervisionada, por classificação ou regressão, com problema preditivo, alvo e características, separação de treino e teste, treino, previsões e pelo menos uma métrica [Fato, fonte 13].
- O conjunto preparado tem 2.800 ocorrências faixa-chart, 2.700 delas em 27 charts de gênero, sem nulos nos 16 atributos ([dicionário](../../dados/preparados/dicionario-faixas.md)).
- A P3 já pergunta se faixas de artistas com mais fãs têm `rank` mais alto ([ADR-0010](0010-problema-e-perguntas.md)). Nos charts de gênero, a correlação de Spearman entre `rank` e `numero_fas` é 0,60; com `duracao_s` é −0,13 e com `posicao_chart`, −0,12 [Fato, cálculo de 05/11/2026 sobre `faixas_preparadas.csv`, a refazer no notebook].
- Uma mesma faixa aparece em mais de um chart (2.800 ocorrências de 2.581 faixas). Se a mesma faixa ficar no treino e no teste, o modelo "decora" a resposta.

## Opções consideradas

- **(a) Regressão:** estimar o `rank` (popularidade na Deezer) a partir do número de fãs do artista, da duração, da idade da faixa na coleta e do gênero do chart.
- **(b) Classificação:** prever se a faixa foi lançada nos 12 meses anteriores à coleta (P2; cerca de 22% das ocorrências de gênero).
- **(c)** Outro conjunto de dados, como o enunciado permite quando o original não serve.

## Decisão

**(a)**, por ligar o modelo à P3 e por ter um sinal claro nos dados. Proposta de partida para a seção 16:

- **Alvo:** `rank` na escala original. Nos charts de gênero ele vai de 807 a 999.724, com média 441.632 e mediana 439.398, quase sem assimetria (0,17), então não precisa de transformação [Fato, mesmo cálculo de 05/11/2026; a seção 13 mostra os números no notebook].
- **Características:** `numero_fas` em escala logarítmica (`log1p`), porque é muito assimétrico (assimetria 3,82; mediana de 64.586 fãs e máximo de 24,1 milhões), `duracao_s`, idade da faixa em dias (`data_coleta − data_lancamento`) e o gênero do chart em variáveis indicadoras. **Não entram** `posicao_chart` (é consequência do ranking do chart, não uma característica da faixa) nem identificadores.
- **Recorte:** só `tipo_chart == "genero"`.
- **Separação:** 80% treino e 20% teste, agrupando por `id_faixa` (a mesma faixa não fica dos dois lados), com semente fixa `SEMENTE_ML`.
- **Modelo:** um simples e explicável, como regressão linear; um segundo modelo (por exemplo, árvore de decisão ou floresta aleatória) só para comparar, se houver tempo.
- **Métricas:** erro absoluto médio (MAE) e coeficiente de determinação (R²) no teste, comparados com uma linha de base que prevê a mediana do treino.

(b) fica como plano B se a regressão não superar a linha de base; (c) não é necessária, porque o conjunto original tem alvo e características adequados.

## Consequências

- O resultado conversa com a P3 e com as conclusões (seção 17): mostra quanto da popularidade os fãs do artista explicam e o que fica de fora.
- O enunciado diz que o foco está na adequação das técnicas e na interpretação dos resultados, e não na complexidade das implementações [Fato, fonte 13]. Um R² baixo, portanto, pede uma interpretação honesta do que o modelo não explica, e não um modelo mais complexo [Inferência].
- `scikit-learn` entra em `requirements.txt` ([ADR-0012](0012-ra3-no-notebook-e-entrega-por-url.md)).

---

## Ligações

- **Base:** [análise e ML](../../base/analise-e-ml.md) · **Perguntas:** [ADR-0010](0010-problema-e-perguntas.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
