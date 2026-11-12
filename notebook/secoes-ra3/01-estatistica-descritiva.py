#> Notebook do RA3 — 1. Análise estatística descritiva (requisito 1 do enunciado)
#> Área responsável: C · Tarefa: T16 (entregas/plano-de-tarefas-ra3.md) · Critérios R1.1–R1.5
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Não há template do RA3: o enunciado desta seção é o requisito 2.1 de enunciados/ra3.md (ADR-0012). Não mude o sentido.
#> Leia antes: base/analise-e-ml.md, seções 1 e 2.

# %% [markdown]
# ## 1. Análise estatística descritiva
#
# Realize uma análise estatística dos dados, contemplando:
#
# - **Tendência central:** utilização de média e/ou mediana para compreender valores representativos.
# - **Dispersão:** utilização de medidas como amplitude ou desvio-padrão para analisar a variabilidade.
# - **Distribuição:** investigação da frequência, concentração ou distribuição dos valores.
#
# As medidas utilizadas devem ser coerentes com as características dos dados e com o problema investigado. Apresente os resultados e explique o que eles representam no contexto do projeto.

# %%
#> Esta célula e a seguinte vêm prontas da estrutura (CONTEXT.md, seção 6): as seções 2 a 4 usam RAIZ, ARQUIVO_PREPARADO e df_analise.
# Preparação do ambiente: bibliotecas, pastas do projeto e origem dos dados
import subprocess
import sys
from pathlib import Path

import pandas as pd

URL_REPOSITORIO = "https://github.com/Jcliz/machine-learning-ra3.git"
PASTA_CLONE = "machine-learning-ra3"
RAMO = "main"  # no Colab, troque pelo ramo do repositório que quiser executar
NO_COLAB = "google.colab" in sys.modules

if NO_COLAB:
    if Path(PASTA_CLONE).exists():
        # Clone de uma execução anterior nesta sessão do Colab: traz a versão mais nova do ramo
        subprocess.run(["git", "-C", PASTA_CLONE, "pull", "-q", "origin", RAMO], check=False)
    else:
        subprocess.run(["git", "clone", "-q", "-b", RAMO, URL_REPOSITORIO], check=True)

# O conjunto preparado fica em dados/ no repositório da entrega e em dados/preparados/ no de desenvolvimento
candidatos = [Path(PASTA_CLONE), Path.cwd(), Path.cwd().parent]
encontrados = [
    (p.resolve(), arquivo.resolve())
    for p in candidatos if (p / "requirements.txt").exists()
    for arquivo in (p / "dados" / "faixas_preparadas.csv", p / "dados" / "preparados" / "faixas_preparadas.csv")
    if arquivo.exists()
]
if not encontrados:
    raise FileNotFoundError(
        "Conjunto preparado não encontrado (dados/faixas_preparadas.csv ao lado do requirements.txt). "
        f"Rode o notebook de dentro do clone (raiz ou notebook/) ou, no Colab, confira o ramo '{RAMO}'."
    )
RAIZ, ARQUIVO_PREPARADO = encontrados[0]
PASTA_PREPARADOS = ARQUIVO_PREPARADO.parent

pd.set_option("display.max_columns", 30)
pd.set_option("display.width", 120)
print(f"Raiz do projeto: {RAIZ.name}")  # só o nome da pasta: o caminho completo é da máquina de quem executa
print(f"Ambiente: {'Google Colab' if NO_COLAB else 'local'} · Python {sys.version.split()[0]} · pandas {pd.__version__}")

# %%
# Releitura do conjunto preparado para a análise
colunas_inteiras_analise = ["id_faixa", "id_chart", "posicao_chart", "id_artista", "id_album",
                            "duracao_s", "rank", "numero_fas"]
colunas_texto_analise = ["titulo", "genero", "tipo_chart", "artista"]
colunas_booleanas_analise = ["lancamento_posterior_coleta", "duracao_fora_limites_iqr"]
df_analise = pd.read_csv(
    ARQUIVO_PREPARADO, encoding="utf-8",
    dtype={**{c: "int64" for c in colunas_inteiras_analise},
           **{c: "string" for c in colunas_texto_analise},
           **{c: "bool" for c in colunas_booleanas_analise}},
    parse_dates=["data_lancamento", "data_coleta"],
)
print(f"{len(df_analise)} ocorrências faixa-chart, {df_analise['id_faixa'].nunique()} faixas distintas, "
      f"{df_analise.loc[df_analise['tipo_chart'].eq('genero'), 'genero'].nunique()} charts de gênero "
      f"e {df_analise['tipo_chart'].eq('geral').sum()} ocorrências no chart geral.")

# %%
#> Daqui para baixo, células da T16 (Área C). Critérios: R1.1 (centro), R1.2 (dispersão), R1.3 (distribuição),
#> R1.4 (medida coerente com a forma), R1.5 (explicação), RN.2, RN.3; recomendações RC.1, RC.2 e RC.6.
#> Sufixo _desc nas variáveis novas, para não colidir com as seções 2 a 4 (CONTEXT.md, seção 6).
# Recorte da análise e idade da faixa na coleta
from IPython.display import display


def numero_br_desc(valor, casas=1):
    """Formata um número no padrão brasileiro (1.234,5)."""
    return f"{valor:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def mostrar_desc(tabela, casas=1):
    """Mostra uma tabela com os números no padrão brasileiro, sem mudar a configuração das outras seções."""
    with pd.option_context("display.float_format", lambda valor: numero_br_desc(valor, casas)):
        display(tabela)


# Comparações entre gêneros usam só os charts de gênero; o chart geral fica como referência à parte
df_generos_desc = df_analise.loc[df_analise["tipo_chart"].eq("genero")].copy()
df_geral_desc = df_analise.loc[df_analise["tipo_chart"].eq("geral")].copy()

# Idade da faixa = dias entre o lançamento e a coleta; o lançamento posterior à coleta não tem idade
for recorte_desc in (df_generos_desc, df_geral_desc):
    recorte_desc["idade_dias"] = (recorte_desc["data_coleta"] - recorte_desc["data_lancamento"]).dt.days
    recorte_desc.loc[recorte_desc["lancamento_posterior_coleta"], "idade_dias"] = pd.NA
    recorte_desc["idade_anos"] = recorte_desc["idade_dias"] / 365.25

print(f"Charts de gênero: {len(df_generos_desc)} ocorrências em {df_generos_desc['genero'].nunique()} charts "
      f"({df_generos_desc.groupby('genero').size().min()} a {df_generos_desc.groupby('genero').size().max()} por chart), "
      f"{df_generos_desc['id_faixa'].nunique()} faixas distintas.")
print(f"Chart geral (referência à parte): {len(df_geral_desc)} ocorrências.")
print(f"Ocorrências sem idade por lançamento posterior à coleta: "
      f"{df_generos_desc['idade_dias'].isna().sum()} nos gêneros e {df_geral_desc['idade_dias'].isna().sum()} no geral.")

# %%
# Forma de cada variável e medida de centro escolhida
variaveis_desc = {
    "duracao_s": "Duração (s) — P1",
    "idade_anos": "Idade na coleta (anos) — P2",
    "rank": "Rank — P3",
    "numero_fas": "Fãs do artista — P3",
}


def resumir_desc(serie):
    """Tendência central, dispersão e forma de uma variável numérica."""
    serie = serie.dropna().astype("float64")
    q1, q3 = serie.quantile([0.25, 0.75])
    return pd.Series({
        "n": len(serie),
        "média": serie.mean(),
        "mediana": serie.median(),
        "média/mediana": serie.mean() / serie.median(),
        "desvio-padrão": serie.std(),
        "mínimo": serie.min(),
        "1º quartil": q1,
        "3º quartil": q3,
        "máximo": serie.max(),
        "amplitude": serie.max() - serie.min(),
        "IQR": q3 - q1,
        "assimetria": serie.skew(),
    })


forma_desc = pd.DataFrame({rotulo: resumir_desc(df_generos_desc[coluna])
                           for coluna, rotulo in variaveis_desc.items()}).T
# Regra do grupo: com assimetria acima de 1 em módulo, a média se afasta do centro; vale a mediana com o IQR
forma_desc["centro escolhido"] = forma_desc["assimetria"].abs().gt(1).map(
    {True: "mediana + IQR", False: "média ≈ mediana + desvio-padrão"})
mostrar_desc(forma_desc.T, casas=2)  # uma coluna por variável, uma linha por medida

# %%
# P1 — Duração por gênero: centro, dispersão e extremos
duracao_desc = df_generos_desc.groupby("genero").agg(
    mediana_s=("duracao_s", "median"),
    media_s=("duracao_s", "mean"),
    q1_s=("duracao_s", lambda serie: serie.quantile(0.25)),
    q3_s=("duracao_s", lambda serie: serie.quantile(0.75)),
    desvio_s=("duracao_s", "std"),
    minimo_s=("duracao_s", "min"),
    maximo_s=("duracao_s", "max"),
    extremos_iqr=("duracao_fora_limites_iqr", "sum"),
)
duracao_desc["iqr_s"] = duracao_desc["q3_s"] - duracao_desc["q1_s"]
duracao_desc["amplitude_s"] = duracao_desc["maximo_s"] - duracao_desc["minimo_s"]
duracao_desc["media_menos_mediana_s"] = duracao_desc["media_s"] - duracao_desc["mediana_s"]
duracao_desc = duracao_desc.sort_values("mediana_s")
mostrar_desc(duracao_desc[["mediana_s", "media_s", "media_menos_mediana_s", "iqr_s", "desvio_s",
                           "minimo_s", "maximo_s", "amplitude_s", "extremos_iqr"]])

menor_desc, maior_desc = duracao_desc.index[0], duracao_desc.index[-1]
print(f"Mediana da duração entre gêneros: de {numero_br_desc(duracao_desc['mediana_s'].min())} s ({menor_desc}) "
      f"a {numero_br_desc(duracao_desc['mediana_s'].max())} s ({maior_desc}); "
      f"diferença de {numero_br_desc(duracao_desc['mediana_s'].max() - duracao_desc['mediana_s'].min())} s.")
print(f"Maior IQR: {duracao_desc['iqr_s'].idxmax()} ({numero_br_desc(duracao_desc['iqr_s'].max())} s); "
      f"menor IQR: {duracao_desc['iqr_s'].idxmin()} ({numero_br_desc(duracao_desc['iqr_s'].min())} s).")
print(f"Maior distância entre média e mediana: {duracao_desc['media_menos_mediana_s'].idxmax()} "
      f"(+{numero_br_desc(duracao_desc['media_menos_mediana_s'].max())} s).")
print(f"Chart geral (referência): mediana {numero_br_desc(df_geral_desc['duracao_s'].median())} s, "
      f"IQR {numero_br_desc(df_geral_desc['duracao_s'].quantile(0.75) - df_geral_desc['duracao_s'].quantile(0.25))} s.")

# %%
# P1 — Frequência da duração por intervalos de minutos
limites_duracao_desc = [0, 120, 180, 240, 300, 420, float("inf")]
rotulos_duracao_desc = ["até 2 min", "2 a 3 min", "3 a 4 min", "4 a 5 min", "5 a 7 min", "mais de 7 min"]
intervalo_duracao_desc = pd.cut(df_generos_desc["duracao_s"], bins=limites_duracao_desc,
                                labels=rotulos_duracao_desc, right=True)
frequencia_duracao_desc = intervalo_duracao_desc.value_counts(sort=False).rename_axis("duração").to_frame("ocorrências")
frequencia_duracao_desc["% do total"] = 100 * frequencia_duracao_desc["ocorrências"] / len(df_generos_desc)
frequencia_duracao_desc["% acumulado"] = frequencia_duracao_desc["% do total"].cumsum()
mostrar_desc(frequencia_duracao_desc)
entre_2_e_5_desc = df_generos_desc["duracao_s"].between(121, 300).mean()
print(f"Ocorrências entre 2 e 5 minutos: {numero_br_desc(100 * entre_2_e_5_desc)}% "
      f"({df_generos_desc['duracao_s'].between(121, 300).sum()} de {len(df_generos_desc)}).")

# %%
# P2 — Idade da faixa e lançamentos dos 12 meses anteriores à coleta
# Mesma janela da seção 2: inclusiva, de 12 meses antes da coleta até a coleta, sem o lançamento posterior
inicio_janela_desc = df_generos_desc["data_coleta"] - pd.DateOffset(months=12)
df_generos_desc["recente_12m"] = (df_generos_desc["data_lancamento"].ge(inicio_janela_desc)
                                  & ~df_generos_desc["lancamento_posterior_coleta"])
idade_desc = df_generos_desc.groupby("genero").agg(
    mediana_anos=("idade_anos", "median"),
    q1_anos=("idade_anos", lambda serie: serie.quantile(0.25)),
    q3_anos=("idade_anos", lambda serie: serie.quantile(0.75)),
    recentes=("recente_12m", "sum"),
    ocorrencias=("recente_12m", "size"),
)
idade_desc["iqr_anos"] = idade_desc["q3_anos"] - idade_desc["q1_anos"]
idade_desc["% recentes"] = 100 * idade_desc["recentes"] / idade_desc["ocorrencias"]
idade_desc = idade_desc.sort_values("% recentes", ascending=False)
mostrar_desc(idade_desc[["recentes", "ocorrencias", "% recentes", "mediana_anos", "q1_anos", "q3_anos", "iqr_anos"]])

print(f"Lançamentos dos 12 meses anteriores nos gêneros: {df_generos_desc['recente_12m'].sum()} de "
      f"{len(df_generos_desc)} ({numero_br_desc(100 * df_generos_desc['recente_12m'].mean())}%), "
      f"janela de {inicio_janela_desc.min():%d/%m/%Y} a {df_generos_desc['data_coleta'].max():%d/%m/%Y}.")
print(f"Proporção por gênero: mediana {numero_br_desc(idade_desc['% recentes'].median())}%, "
      f"de {numero_br_desc(idade_desc['% recentes'].min(), 0)}% a {numero_br_desc(idade_desc['% recentes'].max(), 0)}% "
      f"(amplitude de {numero_br_desc(idade_desc['% recentes'].max() - idade_desc['% recentes'].min(), 0)} pontos).")
print(f"Idade mediana por gênero: de {numero_br_desc(idade_desc['mediana_anos'].min())} anos "
      f"({idade_desc['mediana_anos'].idxmin()}) a {numero_br_desc(idade_desc['mediana_anos'].max())} anos "
      f"({idade_desc['mediana_anos'].idxmax()}).")

# %%
# P3 — Distribuição do rank e dos fãs do artista
# Rank em cinco faixas iguais de 200 mil: mostra se os valores se concentram ou se espalham
faixas_rank_desc = pd.cut(df_generos_desc["rank"], bins=range(0, 1_000_001, 200_000), include_lowest=True,
                          labels=["0 a 200 mil", "200 a 400 mil", "400 a 600 mil", "600 a 800 mil", "800 mil a 1 milhão"])
frequencia_rank_desc = faixas_rank_desc.value_counts(sort=False).rename_axis("rank").to_frame("ocorrências")
frequencia_rank_desc["% do total"] = 100 * frequencia_rank_desc["ocorrências"] / len(df_generos_desc)
mostrar_desc(frequencia_rank_desc)

# Fãs por ordem de grandeza: a escala multiplicativa resume uma variável que vai de 0 a dezenas de milhões
faixas_fas_desc = pd.cut(df_generos_desc["numero_fas"], bins=[-1, 0, 1_000, 10_000, 100_000, 1_000_000, float("inf")],
                         labels=["0", "1 a 1 mil", "1 mil a 10 mil", "10 mil a 100 mil", "100 mil a 1 milhão",
                                 "mais de 1 milhão"])
frequencia_fas_desc = faixas_fas_desc.value_counts(sort=False).rename_axis("fãs do artista").to_frame("ocorrências")
frequencia_fas_desc["% do total"] = 100 * frequencia_fas_desc["ocorrências"] / len(df_generos_desc)
mostrar_desc(frequencia_fas_desc)
fas_desc = df_generos_desc["numero_fas"]
maiores_10_desc = fas_desc.sort_values(ascending=False).head(len(fas_desc) // 10).sum() / fas_desc.sum()
print(f"Fãs: média {numero_br_desc(fas_desc.mean(), 0)} × mediana {numero_br_desc(fas_desc.median(), 0)}; "
      f"os 10% de ocorrências com mais fãs somam {numero_br_desc(100 * maiores_10_desc)}% de todos os fãs.")

# %%
# P3 — Correlação de Spearman entre rank e fãs do artista
# Spearman compara postos: não exige relação linear e não é dominada pelos artistas com dezenas de milhões de fãs
spearman_generos_desc = df_generos_desc["rank"].corr(df_generos_desc["numero_fas"], method="spearman")
pearson_generos_desc = df_generos_desc["rank"].corr(df_generos_desc["numero_fas"], method="pearson")
spearman_geral_desc = df_geral_desc["rank"].corr(df_geral_desc["numero_fas"], method="spearman")
spearman_por_genero_desc = (
    df_generos_desc.groupby("genero")[["rank", "numero_fas"]]
    .apply(lambda chart: chart["rank"].corr(chart["numero_fas"], method="spearman"))
    .sort_values(ascending=False)
    .rename("spearman rank × fãs")
    .to_frame()
)
mostrar_desc(spearman_por_genero_desc, casas=2)
print(f"Conjunto dos charts de gênero: Spearman {numero_br_desc(spearman_generos_desc, 2)} "
      f"(Pearson, para comparar: {numero_br_desc(pearson_generos_desc, 2)}).")
print(f"Chart geral (referência): Spearman {numero_br_desc(spearman_geral_desc, 2)}.")
print(f"Por gênero: mediana {numero_br_desc(spearman_por_genero_desc.iloc[:, 0].median(), 2)}, "
      f"de {numero_br_desc(spearman_por_genero_desc.iloc[:, 0].min(), 2)} ({spearman_por_genero_desc.index[-1]}) "
      f"a {numero_br_desc(spearman_por_genero_desc.iloc[:, 0].max(), 2)} ({spearman_por_genero_desc.index[0]}); "
      f"{spearman_por_genero_desc.iloc[:, 0].gt(0).sum()} de {len(spearman_por_genero_desc)} positivas.")

# %%
# P4 — Artistas distintos e fatia dos 5 artistas com mais posições por chart
def concentracao_desc(chart):
    """Artistas distintos e fatia das posições dos 5 artistas com mais faixas no chart."""
    posicoes_por_artista = chart["id_artista"].value_counts()
    # Empates no topo: todos os artistas com o maior número de posições
    lideres = posicoes_por_artista.index[posicoes_por_artista.eq(posicoes_por_artista.iloc[0])]
    return pd.Series({
        "posições": len(chart),
        "artistas distintos": posicoes_por_artista.size,
        "posições dos 5 maiores": posicoes_por_artista.head(5).sum(),
        "% dos 5 maiores": 100 * posicoes_por_artista.head(5).sum() / len(chart),
        "posições do líder": posicoes_por_artista.iloc[0],
        "artistas líderes": ", ".join(sorted(chart.loc[chart["id_artista"].isin(lideres), "artista"].unique())),
    })


concentracao_generos_desc = (
    df_generos_desc.groupby("genero")[["id_artista", "artista"]]
    .apply(concentracao_desc)
    .sort_values("% dos 5 maiores", ascending=False)
)
mostrar_desc(concentracao_generos_desc)
concentracao_geral_desc = concentracao_desc(df_geral_desc)
fatia_desc = concentracao_generos_desc["% dos 5 maiores"].astype("float64")
artistas_desc = concentracao_generos_desc["artistas distintos"].astype("int64")
print(f"Artistas distintos por chart de gênero: mediana {numero_br_desc(artistas_desc.median(), 0)}, "
      f"de {artistas_desc.min()} ({artistas_desc.idxmin()}) a {artistas_desc.max()} ({artistas_desc.idxmax()}).")
print(f"Fatia dos 5 maiores: mediana {numero_br_desc(fatia_desc.median(), 0)}%, média {numero_br_desc(fatia_desc.mean())}%, "
      f"de {numero_br_desc(fatia_desc.min(), 0)}% ({fatia_desc.idxmin()}) a {numero_br_desc(fatia_desc.max(), 0)}% "
      f"({fatia_desc.idxmax()}).")
print(f"Chart geral (referência): {concentracao_geral_desc['artistas distintos']} artistas distintos, "
      f"5 maiores com {numero_br_desc(concentracao_geral_desc['% dos 5 maiores'], 0)}% das posições.")

# %% [markdown]
# **Resposta do grupo:**
#
# **Escolha das medidas.** Duração, idade da faixa e fãs do artista têm assimetria positiva (6,39, 1,83 e 3,82): poucos valores muito altos puxam a média, que nos fãs chega a 18 vezes a mediana. Nessas variáveis, o valor representativo é a mediana e a dispersão é o IQR (a faixa da metade central); média, desvio-padrão e amplitude ficam ao lado para mostrar o peso dos extremos. O `rank` é quase simétrico (0,17; média 441.632 e mediana 439.398), então média e desvio-padrão (271.063) o descrevem bem. Os gêneros são comparados só nos 27 charts de gênero, com 100 ocorrências cada; o chart geral fica à parte. Fonte: seção 1, célula "Forma de cada variável e medida de centro escolhida".
#
# **P1 — duração.** A duração mediana é 213 s, e 86,1% das ocorrências têm de 2 a 5 minutos. Entre gêneros, a mediana vai de 159,5 s (Kids) a 258,5 s (Metal). A variação interna também muda: o IQR vai de 40 s (Asian Music) a 239,8 s (Classical), onde faixas longas deixam a média 86,7 s acima da mediana. Fonte: seção 1, células "P1 — Duração por gênero: centro, dispersão e extremos" e "P1 — Frequência da duração por intervalos de minutos".
#
# **P2 — idade.** 592 de 2.700 ocorrências (21,9%) foram lançadas nos 12 meses anteriores à coleta, de 2% (Rock e Films/Games) a 57% (Country) por gênero. A idade mediana é 5,9 anos, e a média, 10,4, é puxada por gravações antigas. Fonte: seção 1, célula "P2 — Idade da faixa e lançamentos dos 12 meses anteriores à coleta".
#
# **P3 — rank e fãs.** O `rank` se espalha de 807 a 999.724, então estar entre as 100 primeiras não garante `rank` alto. Os fãs são muito desiguais: os 10% de ocorrências com mais fãs somam 71,4% de todos os fãs. A correlação de Spearman entre `rank` e fãs é 0,60 nos gêneros e 0,53 no chart geral, e é positiva nos 27 gêneros (de 0,06 a 0,67). Usamos Spearman porque compara a ordem dos valores; a de Pearson cai para 0,38 com a relação não linear e os extremos de fãs. Artistas com mais fãs tendem a ter faixas com `rank` mais alto, com força moderada, sem que isso prove causa. Fonte: seção 1, células "P3 — Distribuição do rank e dos fãs do artista" e "P3 — Correlação de Spearman entre rank e fãs do artista".
#
# **P4 — concentração.** Cada chart de gênero tem, na mediana, 69 artistas distintos. Os 5 artistas com mais posições ficam com 21% das posições na mediana, de 11% (Jazz e Classical) a 47% (Metal); no chart geral, 20%. Fonte: seção 1, célula "P4 — Artistas distintos e fatia dos 5 artistas com mais posições por chart".
#
# No retrato da coleta, a faixa típica do topo tem de 3 a 4 minutos e é de um artista com dezenas de milhares de fãs; os gêneros se diferenciam mais na idade das faixas e na concentração de artistas.
