#> Notebook do RA3 — 4. Aplicação de Machine Learning (requisito 4 do enunciado)
#> Área responsável: B · Tarefa: T19 (entregas/plano-de-tarefas-ra3.md) · Critérios R4.1–R4.6
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Não há template do RA3: o enunciado desta seção é o requisito 2.4 de enunciados/ra3.md (ADR-0012). Não mude o sentido.
#> Abordagem do ADR-0013 (regressão do rank). Recomendações RC.4 seguidas: SEMENTE_ML, separação por id_faixa, linha de base,
#> tabela real × previsto e nenhuma característica derivada do alvo (posicao_chart e identificadores ficam de fora).
#> Os números das respostas saem das células abaixo; se a semente ou o conjunto mudar, atualize as duas respostas.

# %% [markdown]
# ## 4. Aplicação de Machine Learning
#
# Implemente uma aplicação simples de aprendizagem supervisionada, por **classificação** (prever uma categoria ou classe) ou **regressão** (estimar um valor numérico). A implementação deverá contemplar:
#
# 1. Definição do problema preditivo.
# 2. Identificação da variável-alvo (*target*) e das características utilizadas (*features*).
# 3. Separação dos dados para treinamento e teste.
# 4. Treinamento de um modelo e realização de previsões.
# 5. Avaliação dos resultados utilizando pelo menos uma métrica adequada ao problema.
#
# Caso o conjunto de dados original não possua características adequadas para uma aplicação supervisionada, outro conjunto de dados pode ser utilizado exclusivamente nesta etapa, com uma breve justificativa.

# %% [markdown]
# **Resposta do grupo:**
#
# **Problema preditivo:** regressão. A partir de atributos conhecidos da faixa e do artista, o modelo estima o `rank`, índice de popularidade que a Deezer atribui à faixa. É a pergunta P3 transformada em previsão: quanto do `rank` os fãs do artista, junto com outros atributos, conseguem explicar.
#
# **Variável-alvo:** `rank`, na escala original, nas 2.700 ocorrências dos 27 charts de gênero (o chart geral fica de fora para não repetir as mesmas faixas em outro recorte).
#
# **Características:** número de fãs do artista em escala logarítmica (`log_fas`, porque `numero_fas` é muito assimétrico), duração em segundos (`duracao_s`), idade da faixa na data da coleta em dias (`idade_dias`) e o gênero do chart em variáveis indicadoras. A posição no chart não entra, porque é consequência do próprio ranking, e os identificadores também não.
#
# O conjunto original tem alvo e características adequados, então não foi usado outro conjunto de dados.

# %%
# Bibliotecas e semente do Machine Learning
import numpy as np
import sklearn
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import GroupShuffleSplit

SEMENTE_ML = 42  # fixa a separação treino e teste e a floresta aleatória, para a execução repetir os números
print(f"scikit-learn {sklearn.__version__} · semente {SEMENTE_ML}")

# %%
# Recorte dos charts de gênero, variável-alvo e características
df_modelo = df_analise.loc[df_analise["tipo_chart"].eq("genero")].copy()
df_modelo["log_fas"] = np.log1p(df_modelo["numero_fas"])
df_modelo["idade_dias"] = (df_modelo["data_coleta"] - df_modelo["data_lancamento"]).dt.days

def formatar(valor):
    """Número inteiro com ponto de milhar, como no texto em português."""
    return f"{valor:,.0f}".replace(",", ".")


caracteristicas_numericas = ["log_fas", "duracao_s", "idade_dias"]
indicadoras_genero = pd.get_dummies(df_modelo["genero"], prefix="genero", drop_first=True, dtype=int)
X = pd.concat([df_modelo[caracteristicas_numericas], indicadoras_genero], axis=1)
y = df_modelo["rank"]

print(f"{len(X)} ocorrências, {X.shape[1]} características "
      f"({len(caracteristicas_numericas)} numéricas e {indicadoras_genero.shape[1]} indicadoras de gênero)")
print(f"Alvo rank: mínimo {formatar(y.min())}, mediana {formatar(y.median())}, máximo {formatar(y.max())}")
print(f"Faixas com lançamento posterior à coleta (idade negativa): {df_modelo['idade_dias'].lt(0).sum()}")

# %%
# Separação treino e teste agrupada por faixa
separador = GroupShuffleSplit(n_splits=1, test_size=0.2, random_state=SEMENTE_ML)
indices_treino, indices_teste = next(separador.split(X, y, groups=df_modelo["id_faixa"]))
X_treino, X_teste = X.iloc[indices_treino], X.iloc[indices_teste]
y_treino, y_teste = y.iloc[indices_treino], y.iloc[indices_teste]

faixas_treino = set(df_modelo["id_faixa"].iloc[indices_treino])
faixas_teste = set(df_modelo["id_faixa"].iloc[indices_teste])
print(f"Treino: {len(X_treino)} ocorrências ({len(faixas_treino)} faixas) · "
      f"teste: {len(X_teste)} ocorrências ({len(faixas_teste)} faixas)")
print(f"Faixas presentes nos dois lados: {len(faixas_treino & faixas_teste)}")

# %%
# Treinamento dos modelos e previsões no teste
modelos = {
    "Linha de base (mediana do treino)": DummyRegressor(strategy="median"),
    "Regressão linear": LinearRegression(),
    "Floresta aleatória (comparação)": RandomForestRegressor(n_estimators=300, min_samples_leaf=5,
                                                             random_state=SEMENTE_ML, n_jobs=-1),
}
previsoes = {}
for nome, modelo in modelos.items():
    modelo.fit(X_treino, y_treino)
    previsoes[nome] = modelo.predict(X_teste)
print(f"{len(modelos)} modelos treinados com {len(X_treino)} ocorrências; "
      f"{len(X_teste)} previsões por modelo no teste.")

# %%
# Avaliação no teste: erro absoluto médio (MAE) e coeficiente de determinação (R²)
metricas = pd.DataFrame(
    {nome: {"MAE": mean_absolute_error(y_teste, p), "R²": r2_score(y_teste, p)} for nome, p in previsoes.items()}
).T
mae_base = metricas.loc["Linha de base (mediana do treino)", "MAE"]
metricas["Redução do MAE frente à linha de base (%)"] = (1 - metricas["MAE"] / mae_base) * 100
metricas.round({"MAE": 0, "R²": 3, "Redução do MAE frente à linha de base (%)": 1})

# %%
# Previsões da regressão linear: amostra de valores reais e previstos no teste
previsto_linear = previsoes["Regressão linear"]
amostra_previsoes = df_modelo.iloc[indices_teste][["titulo", "artista", "genero", "numero_fas", "rank"]].copy()
amostra_previsoes["rank_previsto"] = previsto_linear.round().astype(int)
amostra_previsoes["erro"] = amostra_previsoes["rank_previsto"] - amostra_previsoes["rank"]
amostra_previsoes.sample(8, random_state=SEMENTE_ML).reset_index(drop=True)

# %%
# Coeficientes da regressão linear nas características numéricas
regressao = modelos["Regressão linear"]
coeficientes = pd.Series(regressao.coef_, index=X.columns)
efeito_fas_10x = coeficientes["log_fas"] * np.log(10)  # dez vezes mais fãs somam log(10) ao log_fas
print("Coeficientes (mudança no rank previsto por unidade, com as demais características fixas):")
print(coeficientes[caracteristicas_numericas].round(1).to_string())
print(f"Artista com 10 vezes mais fãs: rank previsto {formatar(efeito_fas_10x)} maior")
print(f"Cada minuto a mais de duração: rank previsto {formatar(coeficientes['duracao_s'] * 60)}")
print(f"Cada ano a mais de idade: rank previsto {formatar(coeficientes['idade_dias'] * 365)}")

# %%
# Contribuição de cada grupo de características: regressões lineares com os mesmos treino e teste
colunas_genero = list(indicadoras_genero.columns)
grupos_caracteristicas = {
    "Todas as características": list(X.columns),
    "Só log_fas": ["log_fas"],
    "Só as indicadoras de gênero": colunas_genero,
    "Só duracao_s e idade_dias": ["duracao_s", "idade_dias"],
    "Todas, exceto log_fas": [c for c in X.columns if c != "log_fas"],
    "Todas, exceto o gênero": caracteristicas_numericas,
}
contribuicao = pd.DataFrame(
    {nome: {"Características": len(colunas),
            "R² no teste": r2_score(y_teste, LinearRegression().fit(X_treino[colunas], y_treino)
                                    .predict(X_teste[colunas]))}
     for nome, colunas in grupos_caracteristicas.items()}
).T
contribuicao["Características"] = contribuicao["Características"].astype(int)
contribuicao.round({"R² no teste": 3})

# %% [markdown]
# **Resposta do grupo:**
#
# **Métricas:** erro absoluto médio (MAE), na mesma unidade do `rank`, e coeficiente de determinação (R²), a fração da variação do `rank` que o modelo explica. Ambas foram medidas nas 537 ocorrências de teste (516 faixas que o modelo não viu no treino; nenhuma faixa ficou nos dois lados).
#
# **Desempenho:** a regressão linear erra em média 147.956 pontos de `rank`, contra 227.294 de uma linha de base que prevê sempre a mediana do treino, uma redução de 34,9%. O R² de 0,521 indica que o modelo explica cerca de metade da variação do `rank`. A floresta aleatória, usada só para comparar, chega a MAE de 144.687 e R² de 0,539: o ganho pequeno sugere que a relação é quase toda linear e que a regressão linear, mais fácil de explicar, basta.
#
# **Contribuição das características:** o R² de 0,521 é do modelo com as 29 características juntas, e não só dos fãs. Com os mesmos treino e teste, `log_fas` sozinho chega a R² de 0,376, as indicadoras de gênero sozinhas a 0,389, e duração e idade juntas a apenas 0,021. Tirar `log_fas` do modelo completo baixa o R² para 0,398, e tirar o gênero baixa para 0,392. Os fãs do artista e o gênero do chart contribuem de forma parecida e complementar, e duração e idade quase nada acrescentam.
#
# **Interpretação:** o coeficiente de `log_fas` é uma associação ajustada pelas demais características, e não um efeito causal: entre faixas do mesmo gênero, com a mesma duração e a mesma idade, a de um artista com 10 vezes mais fãs tem `rank` previsto 74.885 maior. Isso reforça a relação da P3 dentro de cada gênero. Metade da variação fica sem explicação, e a tabela de previsões mostra erros de até cerca de 200 mil pontos, como o de Coldplay, superestimado pelo número de fãs. Isso é esperado, já que a fórmula do `rank` da Deezer não é publicada e depende de reproduções recentes que o conjunto não tem. O modelo serve para mostrar quanto da popularidade os atributos disponíveis explicam juntos, e não para prever com precisão o `rank` de uma faixa.
