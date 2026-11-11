#> Notebook do RA3 — 2. Visualização e interpretação dos dados (requisito 2 do enunciado)
#> Área responsável: D · Tarefa: T17 (entregas/plano-de-tarefas-ra3.md) · Critérios R2.1–R2.4
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Não há template do RA3: o enunciado desta seção é o requisito 2.2 de enunciados/ra3.md (ADR-0012). Não mude o sentido.
#> Leia antes: base/analise-e-ml.md, seção 3. Use df_analise (seção 1). Um gráfico por célula, cada um seguido da interpretação.

# %% [markdown]
# ## 2. Visualização e interpretação dos dados
#
# Produza pelo menos três visualizações que contribuam para compreender diferentes características dos dados. As visualizações deverão:
#
# - Ser adequadas às informações apresentadas.
# - Possuir identificação clara das variáveis e dos resultados.
# - Ser acompanhadas de uma breve interpretação.
#
# Identifique padrões, tendências, diferenças ou comportamentos relevantes, evitando limitar a análise à simples apresentação de gráficos.

# %%
# Recorte e convenções das visualizações
from inspect import signature as assinatura

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, PercentFormatter

from IPython.display import display

#> Conferência: R2.1 (cinco gráficos), R2.2 (adequação), R2.3 (identificação),
#> R2.4 (interpretações), RN.2 (respostas preenchidas), RN.3 (números das saídas).
# Cada gráfico usa somente o conjunto relido na seção 1, sem depender de outras medidas.
df_generos_vis = df_analise.loc[df_analise["tipo_chart"].eq("genero")].copy()
df_geral_vis = df_analise.loc[df_analise["tipo_chart"].eq("geral")].copy()
data_retrato_vis = df_analise["data_coleta"].min().strftime("%d/%m/%Y")
estilo_vis = {
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 110,
}
print(f"Comparações por gênero: {len(df_generos_vis)} ocorrências faixa-chart, "
      f"{df_generos_vis['genero'].nunique()} charts. "
      f"Referência geral separada: {len(df_geral_vis)} ocorrências.")

# %% [markdown]
# **Resposta do grupo:**
#
# As comparações usam as 2.700 ocorrências dos charts de gênero; as 100 do chart geral são apresentadas separadamente na P3. Uma faixa presente em dois charts participa de ambos, pois o grupo de comparação é o chart de origem. Fonte: seção 2, célula "Recorte e convenções das visualizações".

# %%
# Duração por gênero (boxplot)
resumo_duracao_vis = (
    df_generos_vis.groupby("genero")["duracao_s"]
    .agg(ocorrencias="size", mediana_s="median", minimo_s="min", maximo_s="max")
    .sort_values("mediana_s")
)
with plt.rc_context(estilo_vis):
    figura_vis, eixo_vis = plt.subplots(figsize=(10, 10), layout="constrained")
    duracoes_vis = [
        df_generos_vis.loc[df_generos_vis["genero"].eq(genero_vis), "duracao_s"] / 60
        for genero_vis in resumo_duracao_vis.index
    ]
    # Compatibilidade com matplotlib 3.8 e com a orientação nomeada das versões recentes.
    orientacao_vis = ({"orientation": "horizontal"} if "orientation" in assinatura(eixo_vis.boxplot).parameters
                      else {"vert": False})
    caixas_vis = eixo_vis.boxplot(
        duracoes_vis, **orientacao_vis, patch_artist=True,
        medianprops={"color": "#153e52", "linewidth": 1.6},
        flierprops={"marker": ".", "markersize": 3, "alpha": 0.5},
    )
    for caixa_vis in caixas_vis["boxes"]:
        caixa_vis.set_facecolor("#b8d8e5")
    eixo_vis.set_yticks(range(1, len(resumo_duracao_vis) + 1), resumo_duracao_vis.index)
    eixo_vis.invert_yaxis()
    eixo_vis.set_xscale("log")
    eixo_vis.set_xticks([0.5, 1, 2, 4, 8, 16, 32, 64])
    eixo_vis.xaxis.set_major_formatter(FuncFormatter(lambda valor, _: f"{valor:g}".replace(".", ",")))
    eixo_vis.set_xlabel("Duração (minutos; escala logarítmica)")
    eixo_vis.set_ylabel("Chart de gênero")
    eixo_vis.set_title(f"P1 — Distribuição da duração por gênero · {data_retrato_vis}\n"
                       "Ordem da mediana; caixa = metade central; pontos = extremos")
    eixo_vis.grid(axis="x", alpha=0.2)
    plt.show()
display(resumo_duracao_vis)

# %% [markdown]
# **Interpretação — P1:** as medianas vão de 159,5 s em Kids a 258,5 s em Metal, com 100 ocorrências em cada chart. Os extremos chegam a 2.120 s em Indian Music; a escala logarítmica permite mostrar todas as durações sem excluir esses registros. As caixas também mostram a variabilidade dentro dos gêneros, evitando representar cada chart apenas pela média. Fonte: seção 2, célula "Duração por gênero (boxplot)".

# %%
# Lançamentos nos 12 meses anteriores à coleta
inicio_janela_vis = df_generos_vis["data_coleta"] - pd.DateOffset(months=12)
df_generos_vis["recente_vis"] = (
    df_generos_vis["data_lancamento"].ge(inicio_janela_vis)
    & df_generos_vis["data_lancamento"].le(df_generos_vis["data_coleta"])
)
resumo_recentes_vis = (
    df_generos_vis.groupby("genero")["recente_vis"]
    .agg(recentes="sum", ocorrencias="size")
)
resumo_recentes_vis["percentual"] = (
    100 * resumo_recentes_vis["recentes"] / resumo_recentes_vis["ocorrencias"]
)
resumo_recentes_vis = resumo_recentes_vis.sort_values("percentual")
with plt.rc_context(estilo_vis):
    figura_vis, eixo_vis = plt.subplots(figsize=(10, 10), layout="constrained")
    barras_vis = eixo_vis.barh(resumo_recentes_vis.index, resumo_recentes_vis["percentual"], color="#2b788e")
    eixo_vis.bar_label(
        barras_vis,
        labels=[f"{valor:.0f}%" for valor in resumo_recentes_vis["percentual"]], padding=4,
    )
    eixo_vis.set_xlim(0, 100)
    eixo_vis.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    eixo_vis.set_xlabel("Ocorrências lançadas nos 12 meses anteriores / total do chart")
    eixo_vis.set_ylabel("Chart de gênero")
    eixo_vis.set_title(f"P2 — Lançamentos recentes por gênero · {data_retrato_vis}")
    eixo_vis.grid(axis="x", alpha=0.2)
    eixo_vis.set_axisbelow(True)
    plt.show()
display(resumo_recentes_vis)
print(f"Janela inclusiva: {inicio_janela_vis.min():%d/%m/%Y} a {df_generos_vis['data_coleta'].max():%d/%m/%Y}.")
print(f"Recentes: {df_generos_vis['recente_vis'].sum()} de {len(df_generos_vis)} ocorrências. "
      f"Lançamentos posteriores à coleta, fora do numerador: "
      f"{df_generos_vis['data_lancamento'].gt(df_generos_vis['data_coleta']).sum()}.")

# %% [markdown]
# **Interpretação — P2:** Country tem 57 lançamentos recentes em 100 ocorrências (57%), enquanto Rock e Films/Games têm 2 em 100 cada (2%). No conjunto dos gêneros, são 592 de 2.700 (21,9%). A janela inclui 16/10/2025 e 16/10/2026; o lançamento posterior à coleta fica fora do numerador, mantendo o total do chart como denominador. Isso descreve a renovação do topo dos charts nesse retrato. Fonte: seção 2, célula "Lançamentos nos 12 meses anteriores à coleta".

# %%
# Fãs do artista e popularidade: chart geral e conjunto dos gêneros
# Spearman equivale à correlação de Pearson dos postos, com postos médios nos empates.
correlacoes_gerais_vis = []
with plt.rc_context(estilo_vis):
    figura_vis, eixos_vis = plt.subplots(1, 2, figsize=(14, 6), sharey=True, layout="constrained")
    for eixo_vis, (nome_vis, recorte_vis) in zip(
        eixos_vis, [("Chart geral", df_geral_vis), ("Charts de gênero reunidos", df_generos_vis)]
    ):
        correlacao_vis = recorte_vis["numero_fas"].rank().corr(recorte_vis["rank"].rank())
        correlacoes_gerais_vis.append({
            "recorte": nome_vis, "ocorrencias": len(recorte_vis),
            "fas_iguais_zero": int(recorte_vis["numero_fas"].eq(0).sum()),
            "spearman": correlacao_vis,
        })
        eixo_vis.scatter(recorte_vis["numero_fas"], recorte_vis["rank"], s=16, alpha=0.35, color="#2b788e")
        eixo_vis.set_xscale("symlog", linthresh=1)
        eixo_vis.set_xticks(
            [0, 10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000],
            ["0", "10", "100", "1 mil", "10 mil", "100 mil", "1 milhão", "10 milhões"],
            rotation=30, ha="right",
        )
        # Margens na área do gráfico preservam os círculos inteiros, inclusive os de zero fãs.
        eixo_vis.set_xlim(-0.5, df_analise["numero_fas"].max() * 2)
        eixo_vis.set_ylim(-50_000, 1_050_000)
        eixo_vis.set_yticks(
            [0, 250_000, 500_000, 750_000, 1_000_000],
            ["0", "250 mil", "500 mil", "750 mil", "1 milhão"],
        )
        eixo_vis.set_xlabel("Fãs do artista\nDe 10 em diante, cada marca multiplica a quantidade por 10")
        eixo_vis.set_title(f"{nome_vis}\n{len(recorte_vis):,} ocorrências faixa-chart".replace(",", "."))
        eixo_vis.grid(alpha=0.15)
    eixos_vis[0].set_ylabel("Pontuação de popularidade da faixa (rank)\nQuanto maior, mais popular")
    figura_vis.suptitle(f"P3 — Artistas com mais fãs têm músicas mais populares? · {data_retrato_vis}")
    plt.show()
display(pd.DataFrame(correlacoes_gerais_vis).round({"spearman": 3}))

# %%
# Exemplos de fãs e popularidade
# Exemplos observados nos charts de gênero, sem tratá-los como perfil de todo o conjunto.
exemplos_popularidade_vis = pd.concat([
    df_generos_vis.loc[df_generos_vis["numero_fas"].le(1_000)]
    .nlargest(1, "rank").assign(leitura="Poucos fãs, pontuação alta"),
    df_generos_vis.loc[df_generos_vis["numero_fas"].ge(1_000_000)]
    .nsmallest(1, "rank").assign(leitura="Muitos fãs, pontuação baixa"),
])
display(exemplos_popularidade_vis[["leitura", "genero", "artista", "titulo", "numero_fas", "rank"]])

# %% [markdown]
# **Como ler:** cada ponto é uma ocorrência de faixa em um chart. À direita estão artistas com mais fãs; acima estão faixas com maior pontuação de popularidade (`rank`), que não é a posição de 1º, 2º ou 3º no chart. No eixo horizontal, 1 mil significa 1.000 fãs e 1 milhão significa 1.000.000. A partir de 10, cada marca multiplica a quantidade por dez; essa escala permite mostrar artistas de tamanhos muito diferentes. Os pontos de zero fãs também são mantidos.
#
# **Interpretação — P3, visão geral:** a associação é positiva: Spearman de 0,53 nas 100 ocorrências do chart geral e 0,60 nas 2.700 dos charts de gênero reunidos. Isso indica uma tendência, não uma exigência de ter muitos fãs. Por exemplo, "BADDIES IN BELGICA", de ISSAH, tem 150 fãs do artista e 948.653 pontos; a faixa de Frank Sinatra exibida na tabela tem 2.487.314 fãs do artista e 2.757 pontos. São dois exemplos observados, não estimativas de frequência. A quantidade de fãs não garante nem é condição necessária para uma pontuação alta neste retrato. O resultado reunido mistura gêneros e não demonstra causalidade. Fontes: seção 2, células "Fãs do artista e popularidade: chart geral e conjunto dos gêneros" e "Exemplos de fãs e popularidade".

# %%
# Associação entre fãs e popularidade dentro de cada gênero
correlacoes_genero_vis = pd.DataFrame([
    {"genero": genero_vis, "ocorrencias": len(grupo_vis),
     "mediana_fas_por_ocorrencia": grupo_vis["numero_fas"].median(),
     "spearman": grupo_vis["numero_fas"].rank().corr(grupo_vis["rank"].rank())}
    for genero_vis, grupo_vis in df_generos_vis.groupby("genero")
]).set_index("genero").sort_values("spearman")
with plt.rc_context(estilo_vis):
    figura_vis, eixo_vis = plt.subplots(figsize=(10, 10), layout="constrained")
    barras_vis = eixo_vis.barh(correlacoes_genero_vis.index, correlacoes_genero_vis["spearman"], color="#2b788e")
    eixo_vis.bar_label(
        barras_vis,
        labels=[f"{valor:.2f}".replace(".", ",") for valor in correlacoes_genero_vis["spearman"]], padding=4,
    )
    eixo_vis.set_xlim(-1, 1)
    eixo_vis.set_xticks(
        [-1, 0, 1],
        ["−1\nTendência inversa", "0\nSem tendência crescente ou decrescente", "+1\nCrescem juntos"],
    )
    eixo_vis.axvline(0, color="dimgray", linewidth=0.8)
    eixo_vis.set_xlabel("Correlação de Spearman: força da associação, não quantidade de fãs")
    eixo_vis.set_ylabel("Chart de gênero")
    eixo_vis.set_title(f"P3 — Onde fãs e popularidade caminham mais juntos? · {data_retrato_vis}\n"
                       "Maior barra = associação mais forte; não significa mais fãs")
    eixo_vis.grid(axis="x", alpha=0.2)
    eixo_vis.set_axisbelow(True)
    plt.show()
display(correlacoes_genero_vis.round({"spearman": 3}))

# %% [markdown]
# **Interpretação — P3, por gênero:** a correlação é positiva nos 27 charts, mas varia de 0,06 em Traditional Mexicano a 0,67 em Jazz, com 100 ocorrências em cada um. Em Jazz, a ordenação das faixas por fãs do artista acompanha mais de perto a ordenação por popularidade. Esse valor não é quantidade de fãs, percentual ou garantia de pontuação alta. Nas 100 ocorrências de Jazz, a mediana de fãs do artista é 778,5; nas 100 de Pop, é 613.963, embora Pop tenha correlação menor, de 0,24. Portanto, a força da associação não ordena os gêneros por quantidade de fãs. São medidas descritivas, sem teste de significância ou garantia de generalização. Fonte: seção 2, célula "Associação entre fãs e popularidade dentro de cada gênero".

# %%
# Concentração das posições nos cinco artistas mais presentes
contagem_artistas_vis = (
    df_generos_vis.groupby(["id_chart", "genero", "id_artista"])
    .size().rename("posicoes").reset_index()
)
# Desempate por identificador; o total das cinco maiores contagens não muda em empates.
cinco_artistas_vis = (
    contagem_artistas_vis.sort_values(["posicoes", "id_artista"], ascending=[False, True])
    .groupby(["id_chart", "genero"]).head(5)
)
resumo_concentracao_vis = df_generos_vis.groupby(["id_chart", "genero"]).agg(
    ocorrencias=("id_faixa", "size"), artistas_distintos=("id_artista", "nunique")
)
resumo_concentracao_vis["posicoes_cinco_artistas"] = (
    cinco_artistas_vis.groupby(["id_chart", "genero"])["posicoes"].sum()
)
resumo_concentracao_vis["percentual"] = (
    100 * resumo_concentracao_vis["posicoes_cinco_artistas"] / resumo_concentracao_vis["ocorrencias"]
)
resumo_concentracao_vis = resumo_concentracao_vis.reset_index().set_index("genero").sort_values("percentual")
with plt.rc_context(estilo_vis):
    figura_vis, eixo_vis = plt.subplots(figsize=(10, 10), layout="constrained")
    barras_vis = eixo_vis.barh(resumo_concentracao_vis.index, resumo_concentracao_vis["percentual"], color="#2b788e")
    eixo_vis.bar_label(
        barras_vis,
        labels=[f"{valor:.0f}%" for valor in resumo_concentracao_vis["percentual"]], padding=4,
    )
    eixo_vis.set_xlim(0, 100)
    eixo_vis.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    eixo_vis.set_xlabel("Posições dos cinco artistas com mais faixas / total do chart")
    eixo_vis.set_ylabel("Chart de gênero")
    eixo_vis.set_title(f"P4 — Concentração de artistas por gênero · {data_retrato_vis}")
    eixo_vis.grid(axis="x", alpha=0.2)
    eixo_vis.set_axisbelow(True)
    plt.show()
display(resumo_concentracao_vis)

# %% [markdown]
# **Interpretação — P4:** em Metal, os cinco artistas com mais faixas ocupam 47 das 100 posições (47%), e há 35 artistas distintos. Em Jazz e Classical, os cinco concentram 11 de 100 posições cada (11%), com 93 e 94 artistas distintos, respectivamente. Assim, charts com o mesmo tamanho podem ter concentração de artistas bastante diferente. A medida conta posições, não participação nas reproduções ou na audiência. Fonte: seção 2, célula "Concentração das posições nos cinco artistas mais presentes".
