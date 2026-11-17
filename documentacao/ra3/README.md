# RA3 — Análise, visualização e Machine Learning

**Projeto:** Perfil das faixas populares nos charts da Deezer por gênero  
**Equipe:** Eduardo Fabri, João Correa, Rodrigo Alves e João Pedro Cardoso  
**Notebook:** [`notebook/ra3-deezer.ipynb`](notebook/ra3-deezer.ipynb)

O RA3 parte do conjunto preparado no RA1: 2.800 ocorrências de faixas nos charts da Deezer (o chart geral e 27 charts de gênero, com 100 posições cada), coletadas pela API pública em 16/10/2026. O notebook descreve e compara os gêneros com estatística descritiva e visualizações, discute a representatividade do conjunto e testa um modelo de regressão que estima a popularidade da faixa (`rank`). As análises respondem a quatro perguntas:

| ID | Pergunta |
|---|---|
| P1 | Como a duração das faixas varia entre os gêneros? |
| P2 | Que parte das faixas de cada gênero foi lançada nos 12 meses anteriores à coleta? |
| P3 | Faixas de artistas com mais fãs têm `rank` mais alto, no geral e em cada gênero? |
| P4 | Quantos artistas distintos ocupam cada chart de gênero e que fatia das posições fica com os 5 com mais faixas? |

As comparações entre gêneros usam só as 2.700 ocorrências dos 27 charts de gênero; o chart geral aparece à parte. O `rank` é a pontuação de popularidade que a Deezer dá à faixa (quanto maior, mais popular), e não a posição no chart. As citações abaixo indicam a seção do notebook e o comentário-título da célula, que é a primeira linha de cada célula de código.

## 1. Análise estatística descritiva (notebook §1)

**Técnicas.** Medidas de tendência central (média e mediana), de dispersão (desvio-padrão, amplitude e IQR, a largura da metade central) e de distribuição (assimetria, frequência por intervalos e correlação de Spearman). A medida de centro foi escolhida pela forma de cada variável: duração, idade da faixa e fãs do artista têm assimetria positiva (6,39, 1,83 e 3,82), então o valor representativo é a mediana e a dispersão é o IQR. O `rank` é quase simétrico (0,17; média de 441.632 e mediana de 439.398), então média e desvio-padrão (271.063) o descrevem bem (célula "Forma de cada variável e medida de centro escolhida").

**Resultados e interpretação:**

- **P1:** a duração mediana é de 213 s, e 86,1% das ocorrências têm de 2 a 5 minutos. A mediana vai de 159,5 s (Kids) a 258,5 s (Metal), e o IQR vai de 40 s (Asian Music) a 239,8 s (Classical) (células "P1 — Duração por gênero: centro, dispersão e extremos" e "P1 — Frequência da duração por intervalos de minutos").
- **P2:** 592 de 2.700 ocorrências (21,9%) foram lançadas nos 12 meses anteriores à coleta, de 2% (Rock e Films/Games) a 57% (Country). A idade mediana é de 5,9 anos; a média, de 10,4, é puxada por gravações antigas (célula "P2 — Idade da faixa e lançamentos dos 12 meses anteriores à coleta").
- **P3:** os fãs são muito desiguais: os 10% de ocorrências com mais fãs somam 71,4% de todos os fãs. O Spearman entre `rank` e fãs é de 0,60 nos gêneros e de 0,53 no chart geral, e é positivo nos 27 gêneros (de 0,06 a 0,67). Usamos Spearman porque ele compara a ordem dos valores; o Pearson cai para 0,38 por causa da relação não linear e dos extremos de fãs (células "P3 — Distribuição do rank e dos fãs do artista" e "P3 — Correlação de Spearman entre rank e fãs do artista").
- **P4:** cada chart de gênero tem, na mediana, 69 artistas distintos, de 35 (Metal) a 94 (Classical). Os 5 artistas com mais posições ficam com 21% das posições na mediana, de 11% (Jazz e Classical) a 47% (Metal) (célula "P4 — Artistas distintos e fatia dos 5 artistas com mais posições por chart").

## 2. Visualizações (notebook §2)

Cinco gráficos em `matplotlib`, cada um seguido de uma interpretação no notebook:

| Gráfico (célula) | Por que esse tipo | O que mostra |
|---|---|---|
| Boxplot da duração por gênero ("Duração por gênero (boxplot)") | Compara centro, dispersão e valores afastados de 27 grupos lado a lado; o eixo em escala logarítmica acomoda faixas de menos de 1 minuto até 35 minutos | P1: medianas de cerca de 2min40s (Kids) a 4min19s (Metal); Classical tem a metade central mais larga, de cerca de 3min04s a 7min04s |
| Barras de lançamentos recentes ("Lançamentos nos 12 meses anteriores à coleta") | Proporção por categoria, ordenada e com o percentual no rótulo | P2: Country tem 57% de lançamentos do último ano; Rock e Films/Games, 2% |
| Dispersão de fãs × `rank`, chart geral e gêneros ("Fãs do artista e popularidade: chart geral e conjunto dos gêneros") | Relação entre duas variáveis numéricas, mostrando a tendência e as exceções; o eixo dos fãs é logarítmico a partir de 10 e mantém os zeros | P3: tendência positiva (Spearman de 0,53 no geral e 0,60 nos gêneros), com exceções nos dois sentidos, como uma faixa de artista com 150 fãs e `rank` de 948.653 ("Exemplos de fãs e popularidade") |
| Barras da correlação por gênero ("Associação entre fãs e popularidade dentro de cada gênero") | Um valor de −1 a +1 por categoria, com a referência no zero | P3: a associação vai de 0,06 (Traditional Mexicano) a 0,67 (Jazz). Barra maior quer dizer associação mais forte, e não mais fãs: a mediana de fãs é de 778,5 em Jazz e de 613.963 em Pop, cuja correlação é de 0,24 |
| Barras de concentração ("Concentração das posições nos cinco artistas mais presentes") | Proporção por categoria, com o número de artistas distintos no rótulo | P4: em Metal, 5 artistas ocupam 47 de 100 posições, com 35 artistas no chart; em Jazz e Classical, 11%, com 93 e 94 artistas |

## 3. Amostragem e representatividade (notebook §3)

**Origem e abrangência.** Os dados são um retrato único da API pública da Deezer, coletado em 16/10/2026: o chart geral e os 27 charts de gênero listados pela Deezer, cada um com as 100 primeiras posições, que é o máximo que a API devolve. São 2.800 ocorrências, 2.581 faixas, 1.688 artistas e 2.292 álbuns, com lançamentos de 1930 a 2026 (célula "Origem e abrangência do conjunto"). A API respondeu como se a coleta viesse dos Estados Unidos, e o chart depende do país da requisição.

**Representatividade.** Para o problema, que é o perfil das faixas do topo dos charts por gênero, o conjunto é o próprio topo de cada chart naquele dia, sem amostragem, e todos os charts têm as mesmas 100 posições. 2.394 faixas (92,8%) aparecem num só chart, e 97 das 100 faixas do chart geral também estão num chart de gênero, por isso o geral fica à parte (célula "Repetição de faixas entre charts"). O conjunto não representa o catálogo da Deezer, a audiência de outros países nem a evolução no tempo.

**Limitações e vieses.** Um só dia e um só país aparente. Os gêneros são categorias editoriais com níveis de popularidade muito diferentes: a mediana do `rank` vai de 73.231 (Jazz) a 830.084 (Pop) (célula "Diferenças de perfil entre os charts de gênero"). O corte nas 100 primeiras posições deixa de fora as faixas pouco populares. A posição no chart não segue o `rank`: o Spearman entre os dois tem mediana de −0,21 nos 28 charts (célula "Posição no chart e rank da faixa"). 8 ocorrências têm artistas com 0 fãs, valor mantido como veio da fonte.

**Amostragem.** Nenhuma etapa sorteia registros: as seções 1 a 3 usam as 2.800 ocorrências. A única separação é a de treino e teste da seção 4.

## 4. Machine Learning (notebook §4)

| Etapa | Escolha |
|---|---|
| Problema | Regressão: estimar o `rank` da faixa a partir de atributos da faixa e do artista (a P3 transformada em previsão) |
| Alvo | `rank`, na escala original, nas 2.700 ocorrências dos charts de gênero (de 807 a 999.724) |
| Características (29) | `log_fas` (logaritmo de 1 + fãs do artista, porque os fãs são muito assimétricos), `duracao_s`, `idade_dias` (dias entre o lançamento e a coleta) e 26 indicadoras do gênero do chart. Não entram a posição no chart, que é consequência do próprio ranking, nem os identificadores |
| Separação | 80% treino e 20% teste com `GroupShuffleSplit` agrupado por faixa: 2.163 ocorrências de treino e 537 de teste, nenhuma faixa nos dois lados; semente fixa `SEMENTE_ML = 42` (célula "Separação treino e teste agrupada por faixa") |
| Modelos | Regressão linear (o modelo principal, por ser explicável), uma floresta aleatória só para comparar e uma linha de base que prevê sempre a mediana do treino |
| Métricas | Erro absoluto médio (MAE), na unidade do `rank`, e coeficiente de determinação (R²), a fração da variação do `rank` explicada |

**Resultados** (célula "Avaliação no teste: erro absoluto médio (MAE) e coeficiente de determinação (R²)"):

| Modelo | MAE | R² | Redução do MAE frente à linha de base |
|---|---|---|---|
| Linha de base (mediana do treino) | 227.294 | 0,000 | — |
| Regressão linear | 147.956 | 0,521 | 34,9% |
| Floresta aleatória (comparação) | 144.687 | 0,539 | 36,3% |

**Interpretação.** A regressão linear explica cerca de metade da variação do `rank` e erra 34,9% menos que a linha de base. A floresta aleatória melhora pouco, o que indica uma relação quase toda linear. Com os mesmos treino e teste, `log_fas` sozinho chega a um R² de 0,376, o gênero sozinho a 0,389, e duração e idade juntas a 0,021: os fãs do artista e o gênero contribuem de forma parecida e complementar (célula "Contribuição de cada grupo de características: regressões lineares com os mesmos treino e teste"). Entre faixas do mesmo gênero, com a mesma duração e a mesma idade, a de um artista com 10 vezes mais fãs tem `rank` previsto 74.885 maior. Isso é uma associação, e não um efeito causal (célula "Coeficientes da regressão linear nas características numéricas"). Há erros de até cerca de 200 mil pontos, como o de uma faixa de Coldplay superestimada pelo número de fãs (célula "Previsões da regressão linear: amostra de valores reais e previstos no teste"). A fórmula do `rank` não é publicada e depende de reproduções que o conjunto não tem. Por isso, o modelo mede quanto os atributos disponíveis explicam a popularidade, mas não serve para prever com precisão o `rank` de uma faixa.

## 5. Conclusões (notebook §5)

- **Perfil do topo:** no retrato de 16/10/2026, a faixa típica do topo dos charts de gênero tem de 3 a 4 minutos (mediana de 213 s), foi lançada há cerca de 6 anos (idade mediana de 5,9 anos) e é de um artista com dezenas de milhares de fãs.
- **O que muda entre gêneros:** a duração é o traço mais estável, com as medianas mudando 1,6 vez entre os gêneros. Os gêneros se diferenciam mais pela idade das faixas (a fatia de lançamentos recentes muda 28,5 vezes, de 2% a 57%) e pela concentração de artistas (4,3 vezes, de 11% a 47%).
- **Fãs e popularidade:** a popularidade do artista acompanha a da faixa (Spearman de 0,60 nos gêneros), mas explica só uma parte dela. Esse peso muda com o gênero (de 0,06 a 0,67), e o modelo, com fãs, gênero, duração e idade, explica cerca de metade da variação do `rank` (R² de 0,521).
- **Limitações:** um só dia e um só país aparente, só as 100 primeiras posições de cada chart, gêneros com níveis de popularidade muito diferentes e resultados que mostram associação, e não causa.

## 6. Como executar

**Conteúdo do repositório:**

| Arquivo | O que é |
|---|---|
| `notebook/ra3-deezer.ipynb` | Notebook do RA3, já executado (seções 1 a 5) |
| `dados/faixas_preparadas.csv` | Conjunto preparado no RA1 (2.800 linhas × 16 colunas), lido pelo notebook |
| `dados/dicionario-faixas.md` | Dicionário das colunas do conjunto preparado |
| `requirements.txt` | Bibliotecas: pandas, matplotlib, scikit-learn e jupyter (Python 3.9 ou mais novo) |

O notebook não acessa a API da Deezer: lê só o `dados/faixas_preparadas.csv`, então os números se repetem a cada execução. A separação treino e teste e a floresta aleatória usam a semente fixa `SEMENTE_ML = 42`.

**No Google Colab:**

1. Abra https://colab.research.google.com/github/Jcliz/machine-learning-ra3/blob/main/notebook/ra3-deezer.ipynb
2. Clique em *Ambiente de execução → Executar tudo*. A primeira célula de código clona este repositório e encontra o conjunto preparado. As bibliotecas já vêm instaladas no Colab.

**Localmente:**

```bash
git clone https://github.com/Jcliz/machine-learning-ra3.git
cd machine-learning-ra3
python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab notebook/ra3-deezer.ipynb
```

No Jupyter, execute todas as células de cima para baixo (*Run → Run All Cells*). O notebook precisa ser aberto de dentro do clone (da raiz ou da pasta `notebook/`) para encontrar o `dados/faixas_preparadas.csv`. A execução completa leva poucos segundos.

**O que conferir no fim:**

- As 29 células de código rodam sem erro, e a seção 2 mostra 5 gráficos.
- Seção 1, célula "Releitura do conjunto preparado para a análise": 2.800 ocorrências faixa-chart, 2.581 faixas distintas, 27 charts de gênero e 100 ocorrências no chart geral.
- Seção 1, célula "P3 — Correlação de Spearman entre rank e fãs do artista": Spearman de 0,60 nos gêneros e de 0,53 no chart geral.
- Seção 4, célula "Separação treino e teste agrupada por faixa": 2.163 ocorrências de treino e 537 de teste, com 0 faixas nos dois lados.
- Seção 4, célula "Avaliação no teste: erro absoluto médio (MAE) e coeficiente de determinação (R²)": regressão linear com MAE de 147.956 e R² de 0,521; linha de base com MAE de 227.294.
