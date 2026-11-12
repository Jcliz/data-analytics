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
from math import ceil as arredondar_para_cima

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
# Os gráficos comparam as músicas que estavam no topo dos charts na data da coleta. Se uma música aparece em dois charts, ela entra nas duas comparações. São 2.700 registros nos charts de gênero e 100 no chart geral, que é mostrado separadamente na P3. Cada registro representa uma faixa em um chart. Fonte: seção 2, célula "Recorte e convenções das visualizações".

# %%
# Duração por gênero (boxplot)
resumo_duracao_vis = (
    df_generos_vis.groupby("genero")["duracao_s"]
    .agg(ocorrencias="size", mediana_s="median", minimo_s="min", maximo_s="max")
    .sort_values("mediana_s")
)
quartis_duracao_vis = df_generos_vis.groupby("genero")["duracao_s"].quantile([0.25, 0.75]).unstack()
resumo_duracao_vis["mediana_min"] = resumo_duracao_vis["mediana_s"] / 60
resumo_duracao_vis["inicio_caixa_min"] = quartis_duracao_vis[0.25] / 60
resumo_duracao_vis["fim_caixa_min"] = quartis_duracao_vis[0.75] / 60
resumo_duracao_vis["maximo_min"] = resumo_duracao_vis["maximo_s"] / 60
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
        duracoes_vis, **orientacao_vis, patch_artist=True, whis=1.5,
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
                       "Caixa = metade central; pontos = além das hastes (1,5 × IQR por gênero)")
    eixo_vis.grid(axis="x", alpha=0.2)
    plt.show()
display(resumo_duracao_vis[["ocorrencias", "mediana_min", "inicio_caixa_min", "fim_caixa_min", "maximo_min"]].round(2))

# %% [markdown]
# **Interpretação — P1:** a duração típica das músicas muda de um gênero para outro. Em Kids, a duração do meio da lista é de aproximadamente 2 minutos e 40 segundos; em Metal, é de 4 minutos e 19 segundos. Isso não significa que toda música de Metal seja mais longa que qualquer música de Kids: há músicas de durações diferentes dentro de cada gênero, como mostram as caixas e os pontos.
#
# Classical tem maior variação na metade central das músicas, que vai de cerca de 3 minutos e 4 segundos a 7 minutos e 4 segundos. Em Asian Music, essa parte fica entre 2 minutos e 44 segundos e 3 minutos e 24 segundos. A caixa mais larga mostra essa diferença de durações dentro do próprio gênero.
#
# Os pontos são músicas que ficam além das hastes da caixa, pela regra de 1,5 vez o intervalo entre o primeiro e o terceiro quartil (IQR). São durações mais afastadas do centro, que não indicam erro por si só. Esses limites são calculados por gênero e não precisam coincidir com a sinalização de qualidade já gravada no conjunto preparado.
#
# As medianas são 159,5 s em Kids e 258,5 s em Metal, com 100 faixas em cada chart. A faixa mais longa dos charts de gênero tem 2.120 s (35 minutos e 20 segundos), em Indian Music. Ela foi mantida, mas esse caso isolado não resume o gênero inteiro. Fonte: seção 2, célula "Duração por gênero (boxplot)".

# %%
# Lançamentos nos 12 meses anteriores à coleta
inicio_janela_vis = df_generos_vis["data_coleta"] - pd.DateOffset(months=12)
df_generos_vis["recente_vis"] = (
    df_generos_vis["data_lancamento"].ge(inicio_janela_vis)
    & ~df_generos_vis["lancamento_posterior_coleta"]
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
      f"{df_generos_vis['lancamento_posterior_coleta'].sum()}.")

# %% [markdown]
# **Interpretação — P2:** alguns charts têm mais espaço para músicas lançadas recentemente. Em Country, mais da metade das faixas foi lançada no último ano: 57 de 100. Em Rock e Films/Games, foram apenas 2 de 100 em cada chart. Portanto, estar no topo não significa necessariamente ser uma novidade; o peso dos lançamentos recentes varia entre os gêneros.
#
# Ao todo, 592 dos 2.700 registros de faixas nos charts de gênero (21,9%) são lançamentos entre 16/10/2025 e 16/10/2026, incluindo essas duas datas. A única faixa com lançamento posterior à coleta continua no total do seu chart, mas não conta como lançamento já ocorrido. Essa comparação descreve a idade dos lançamentos na coleta, sem acompanhar entradas e saídas dos charts ao longo do tempo. Fonte: seção 2, célula "Lançamentos nos 12 meses anteriores à coleta".

# %%
# Fãs do artista e popularidade: chart geral e conjunto dos gêneros
# Spearman equivale à correlação de Pearson dos postos, com postos médios nos empates.
correlacoes_gerais_vis = []
limite_popularidade_vis = max(100_000, arredondar_para_cima(df_analise["rank"].max() / 100_000) * 100_000)
marcacoes_popularidade_vis = [limite_popularidade_vis * parte_vis / 4 for parte_vis in range(5)]
rotulos_popularidade_vis = [
    ("0" if valor_vis == 0 else
     f"{valor_vis / 1_000_000:g} milhão" if valor_vis == 1_000_000 else
     f"{valor_vis / 1_000_000:g} milhões" if valor_vis > 1_000_000 else
     f"{valor_vis / 1_000:g} mil").replace(".", ",")
    for valor_vis in marcacoes_popularidade_vis
]
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
        eixo_vis.set_ylim(-0.05 * limite_popularidade_vis, 1.05 * limite_popularidade_vis)
        eixo_vis.set_yticks(marcacoes_popularidade_vis, rotulos_popularidade_vis)
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
# **Como ler:** cada bolinha representa uma faixa em um chart. Mais à direita significa mais fãs do artista; mais acima significa maior popularidade da música. Essa popularidade é a pontuação `rank` da Deezer: não é a posição de 1º ou 2º lugar, nem uma contagem de ouvintes ou reproduções. No eixo horizontal, 1 mil significa 1.000 fãs e 1 milhão significa 1.000.000. A partir de 10, cada marca multiplica a quantidade por dez, para que artistas com dezenas e com milhões de fãs caibam na mesma figura. Os pontos de zero fãs também são mantidos.
#
# **Interpretação — P3, visão geral:** a quantidade de fãs, sozinha, não determina a popularidade da música. Ter dez vezes mais fãs não implica ter dez vezes mais popularidade. Ainda existe uma tendência no conjunto: artistas com mais fãs tendem a ter faixas mais populares. Mas há exceções, e artistas com poucos fãs também podem ter músicas muito populares.
#
# Por exemplo, "BADDIES IN BELGICA", de ISSAH, tem 150 fãs do artista e 948.653 pontos de popularidade. A faixa de Frank Sinatra exibida na tabela tem 2.487.314 fãs do artista e 2.757 pontos. Esses dois casos ilustram por que o número de fãs não basta para prever o resultado de uma música; não dizem com que frequência as exceções acontecem.
#
# A tendência positiva é resumida pela correlação de Spearman: 0,53 nos 100 registros do chart geral e 0,60 nos 2.700 dos charts de gênero reunidos. Esses valores medem quanto as duas ordenações caminham juntas; não significam que 53% ou 60% da popularidade seja causada pelos fãs. O retrato mostra uma associação e não permite afirmar que mais fãs causem mais popularidade. Fontes: seção 2, células "Fãs do artista e popularidade: chart geral e conjunto dos gêneros" e "Exemplos de fãs e popularidade".

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
# **Interpretação — P3, por gênero:** Jazz aparece em primeiro porque, dentro desse chart, a tendência de artistas com mais fãs terem músicas mais populares é mais forte. Isso não quer dizer que Jazz tenha mais fãs que os outros gêneros. Em Traditional Mexicano, essa tendência é bem menos nítida: saber que um artista tem mais fãs ajuda pouco a acompanhar a ordem de popularidade das faixas.
#
# A medida dessa associação é 0,67 em Jazz e 0,06 em Traditional Mexicano, considerando 100 faixas em cada chart. Quanto mais perto de +1, mais as duas ordenações caminham juntas; perto de zero, essa tendência é pouco marcada. Os 27 charts têm valores positivos neste retrato, mas nenhum chega à correspondência perfeita de +1.
#
# A diferença entre associação e quantidade de fãs aparece também na tabela: a mediana de fãs do artista nas 100 faixas de Jazz é 778,5; nas 100 de Pop, é 613.963, embora a associação em Pop seja menor, de 0,24. Assim, estar no topo deste gráfico não significa ter o maior número de fãs. Esses resultados descrevem os charts na data da coleta e não garantem que o padrão se repita em outras datas. Fonte: seção 2, célula "Associação entre fãs e popularidade dentro de cada gênero".

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
        labels=[
            f"{linha_vis.percentual:.0f}% · {linha_vis.artistas_distintos} artistas"
            for linha_vis in resumo_concentracao_vis.itertuples()
        ], padding=4,
    )
    eixo_vis.set_xlim(0, 100)
    eixo_vis.xaxis.set_major_formatter(PercentFormatter(xmax=100, decimals=0))
    eixo_vis.set_xlabel("Posições dos cinco artistas com mais faixas / total do chart")
    eixo_vis.set_ylabel("Chart de gênero")
    eixo_vis.set_title(f"P4 — Concentração de artistas por gênero · {data_retrato_vis}\n"
                       "Rótulos: fatia dos cinco mais presentes · total de artistas no chart")
    eixo_vis.grid(axis="x", alpha=0.2)
    eixo_vis.set_axisbelow(True)
    plt.show()
display(resumo_concentracao_vis)

# %% [markdown]
# **Interpretação — P4:** em alguns charts, os mesmos artistas aparecem várias vezes. Em Metal, apenas cinco artistas ocupam quase metade da lista: 47 das 100 posições. Em Jazz e Classical, os cinco artistas mais presentes ocupam 11 das 100 posições em cada chart. Nesses dois casos, a lista distribui mais posições entre artistas diferentes.
#
# Isso também aparece na quantidade de nomes: Metal tem 35 artistas distintos, Jazz tem 93 e Classical tem 94, todos em charts de 100 faixas. Portanto, listas do mesmo tamanho podem dar espaço a quantidades bem diferentes de artistas. Estamos contando posições ocupadas; o gráfico não informa a participação desses artistas nas reproduções ou na audiência. Fonte: seção 2, célula "Concentração das posições nos cinco artistas mais presentes".
