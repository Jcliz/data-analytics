#> Área C · T03 · Diagnóstico sem alterar df_bruto.

# %% [markdown]
# ## 3. Exploração inicial dos dados
#
# Investigue a quantidade de registros e colunas, os tipos de dados, os valores ausentes e outras características relevantes da base.
#
# Uma linha representa uma ocorrência de faixa em um chart no retrato da coleta.
# A chave candidata é o par `chart_id_genero` e `id`, dentro desse retrato.
# `id` identifica a faixa, mas não é único entre charts. As verificações abaixo
# contam ocorrências, não faixas distintas, salvo indicação explícita.

# %%
# Visão geral e tipos observados
import json
import numpy as np
import pandas as pd
from IPython.display import display

numero_linhas = len(df_bruto)
if numero_linhas == 0:
    raise ValueError("O diagnóstico exige um df_bruto não vazio; execute a seção 2.")
print(f"Retrato: {numero_linhas} linhas × {df_bruto.shape[1]} colunas; "
      f"{df_bruto['id'].nunique()} faixas; {df_bruto['chart_id_genero'].nunique()} charts.")
print(f"Memória, incluindo objetos: {df_bruto.memory_usage(deep=True).sum():,} bytes.")
inventario = df_bruto.dtypes.astype(str).rename("tipo_observado").to_frame()
display(inventario.reset_index(names="atributo"))

# %%
# Ausências nulas e textos vazios
# Listas e dicionários são objetos válidos: não são tratados como texto.
def texto_vazio(valor):
    return isinstance(valor, str) and not valor.strip()

mascara_ausencias = df_bruto.isna() | df_bruto.apply(lambda coluna: coluna.map(texto_vazio))
ausencias = pd.DataFrame({
    "nulos": df_bruto.isna().sum(),
    "textos_vazios": df_bruto.apply(lambda coluna: coluna.map(texto_vazio)).sum(),
    "total_ausentes": mascara_ausencias.sum(),
})
ausencias["percentual"] = 100 * ausencias["total_ausentes"] / numero_linhas
display(ausencias.reset_index(names="atributo"))

# %%
# Duplicidade e limite da chave
# Serialização canônica permite comparar linhas com listas/dicionários, sem modificar o bruto.
linhas_canonicas = df_bruto.apply(
    lambda coluna: coluna.map(lambda valor: json.dumps(valor, ensure_ascii=False, sort_keys=True)
                             if isinstance(valor, (list, dict)) else valor)
)
duplicadas_inteiras = linhas_canonicas.duplicated()
duplicadas_id = df_bruto.duplicated("id")
duplicadas_chart = df_bruto.duplicated(["chart_id_genero", "id"])
print(f"Ocorrências excedentes por id: {duplicadas_id.sum()}/{numero_linhas}; "
      f"por par chart-faixa: {duplicadas_chart.sum()}/{numero_linhas}; "
      f"linhas inteiras iguais: {duplicadas_inteiras.sum()}/{numero_linhas}.")

# %%
# Estatísticas descritivas e domínios numéricos
colunas_numericas = ["duration", "rank", "position", "detalhe_faixa_bpm",
                    "detalhe_faixa_gain", "detalhe_artista_nb_fan"]
numericos = df_bruto[colunas_numericas].apply(pd.to_numeric, errors="coerce")
display(numericos.describe().T)
# São regras de integridade, não indicadores analíticos das perguntas P1 a P4.
colunas_inteiras = ["id", "chart_id_genero", "chart_ordem", "duration", "rank", "position",
                   "artist_id", "album_id", "detalhe_faixa_id", "detalhe_album_id",
                   "detalhe_artista_id", "detalhe_artista_nb_fan"]
tipos_invalidos = pd.Series(False, index=df_bruto.index)
for coluna in colunas_inteiras:
    valores = pd.to_numeric(df_bruto[coluna], errors="coerce")
    tipos_invalidos |= valores.isna() | ~np.isfinite(valores) | valores.mod(1).ne(0)
# Strings conversíveis também são divergências do tipo esperado, mesmo sem perda na conversão.
for coluna in colunas_inteiras + ["detalhe_faixa_bpm", "detalhe_faixa_gain"]:
    tipos_invalidos |= ~df_bruto[coluna].map(
        lambda valor: isinstance(valor, (int, float, np.integer, np.floating))
        and not isinstance(valor, (bool, np.bool_))
    )
tipos_invalidos |= ~df_bruto["explicit_lyrics"].map(lambda valor: isinstance(valor, (bool, np.bool_)))
invalidos_numericos = (
    numericos.isna().any(axis=1) | ~np.isfinite(numericos).all(axis=1)
    | numericos["duration"].le(0) | numericos["rank"].lt(0)
    | numericos["position"].le(0) | numericos["detalhe_artista_nb_fan"].lt(0)
    | numericos["detalhe_faixa_bpm"].lt(0)
)
for coluna in ["id", "artist_id", "album_id"]:
    invalidos_numericos |= pd.to_numeric(df_bruto[coluna], errors="coerce").le(0)
bpm_zero = numericos["detalhe_faixa_bpm"].eq(0)
gain_zero = numericos["detalhe_faixa_gain"].eq(0)
# gain é um ajuste em dB: negativo é permitido; zero é sinalizado para avaliação, não prova de erro.

# %%
# Datas, formatos e categorias
colunas_datas = ["detalhe_faixa_release_date", "detalhe_album_release_date"]
datas = df_bruto[colunas_datas].apply(lambda coluna: pd.to_datetime(coluna, format="%Y-%m-%d", errors="coerce"))
formatos_data = df_bruto[colunas_datas].apply(
    lambda coluna: coluna.astype("string").str.fullmatch(r"\d{4}-\d{2}-\d{2}").fillna(False)
)
data_coleta = pd.Timestamp(metadados["inicio_utc"]).tz_convert("UTC").tz_localize(None).normalize()
datas_invalidas = (~formatos_data | datas.isna() | datas.lt(pd.Timestamp("1900-01-01"))
                   | datas.gt(data_coleta)).any(axis=1)
textos = df_bruto[["title", "artist_name", "chart_nome_genero"]].astype("string")
espacos = textos.ne(textos.apply(lambda coluna: coluna.str.strip())).any(axis=1)
nomes_por_artista = df_bruto.groupby("artist_id")["artist_name"].nunique()
variacoes_artista = df_bruto["artist_id"].isin(nomes_por_artista[nomes_por_artista.gt(1)].index)
nomes_por_genero = df_bruto.groupby("chart_id_genero")["chart_nome_genero"].nunique()
categorias_inconsistentes = df_bruto["chart_id_genero"].isin(nomes_por_genero[nomes_por_genero.gt(1)].index)
nomes_normalizados = df_bruto["chart_nome_genero"].astype("string").str.strip().str.casefold()
ids_por_nome = df_bruto.groupby(nomes_normalizados)["chart_id_genero"].nunique()
categorias_inconsistentes |= nomes_normalizados.isin(ids_por_nome[ids_por_nome.gt(1)].index)
chart_geral = df_bruto["chart_id_genero"].eq(0)
genero_album_generico = pd.to_numeric(df_bruto["detalhe_album_genre_id"], errors="coerce").le(0)

# %%
# Possíveis outliers e integridade do enriquecimento
# Limites IQR são sinais para inspeção; extremos não são removidos.
limites_outliers = []
for coluna in ["duration", "rank"]:
    primeiro_quartil, terceiro_quartil = numericos[coluna].quantile([0.25, 0.75])
    amplitude = terceiro_quartil - primeiro_quartil
    inferior, superior = primeiro_quartil - 1.5 * amplitude, terceiro_quartil + 1.5 * amplitude
    mascara = numericos[coluna].lt(inferior) | numericos[coluna].gt(superior)
    limites_outliers.append({"atributo": coluna, "inferior": inferior, "superior": superior,
                             "ocorrencias": int(mascara.sum()), "denominador": numero_linhas})
    if coluna == "duration":
        outliers_duracao = mascara
    else:
        outliers_rank = mascara
display(pd.DataFrame(limites_outliers))
display(df_bruto.loc[outliers_duracao, ["id", "title", "duration", "chart_nome_genero"]])
integridade = pd.Series(False, index=df_bruto.index)
for origem, detalhe in [("id", "detalhe_faixa_id"), ("album_id", "detalhe_album_id"),
                        ("artist_id", "detalhe_artista_id")]:
    integridade |= df_bruto[origem].isna() | df_bruto[detalhe].isna() | df_bruto[origem].ne(df_bruto[detalhe])
divergencia_duracao = df_bruto["duration"].ne(df_bruto["detalhe_faixa_duration"])
divergencia_rank = df_bruto["rank"].ne(df_bruto["detalhe_faixa_rank"])

# %%
# Diagnóstico de qualidade Q1 a Q21
campos_essenciais = ["id", "chart_id_genero", "chart_nome_genero", "title", "duration", "rank",
                    "position", "artist_id", "artist_name", "album_id", "detalhe_faixa_release_date",
                    "detalhe_artista_nb_fan"]
verificacoes = [
    ("Q1", "Ausência em pelo menos um campo essencial às P1–P4 ou RA2", mascara_ausencias[campos_essenciais].any(axis=1), "Ausências nulas e textos vazios"),
    ("Q2", "Ausência de preview (nulo ou texto vazio)", mascara_ausencias["preview"], "Ausências nulas e textos vazios"),
    ("Q3", "Ausência de title_version (nulo ou texto vazio)", mascara_ausencias["title_version"], "Ausências nulas e textos vazios"),
    ("Q4", "Ocorrências excedentes por id, após a primeira", duplicadas_id, "Duplicidade e limite da chave"),
    ("Q5", "Ocorrências excedentes pelo par chart_id_genero e id", duplicadas_chart, "Duplicidade e limite da chave"),
    ("Q6", "Linhas inteiras repetidas, após a primeira", duplicadas_inteiras, "Duplicidade e limite da chave"),
    ("Q7", "Tipo divergente de numérico inteiro/real ou booleano esperado", tipos_invalidos, "Estatísticas descritivas e domínios numéricos"),
    ("Q8", "Numéricos não finitos/ausentes ou fora dos domínios descritos", invalidos_numericos, "Estatísticas descritivas e domínios numéricos"),
    ("Q9", "bpm igual a zero (sinal de dado não informado)", bpm_zero, "Estatísticas descritivas e domínios numéricos"),
    ("Q10", "gain igual a zero (a avaliar, não erro comprovado)", gain_zero, "Estatísticas descritivas e domínios numéricos"),
    ("Q11", "Data fora de AAAA-MM-DD, inválida ou fora de 1900 até a coleta", datas_invalidas, "Datas, formatos e categorias"),
    ("Q12", "Espaços nas pontas de título, artista ou gênero", espacos, "Datas, formatos e categorias"),
    ("Q13", "Mais de um nome para um id de artista", variacoes_artista, "Datas, formatos e categorias"),
    ("Q14", "Gênero com mais de um nome ou nome normalizado com mais de um id", categorias_inconsistentes, "Datas, formatos e categorias"),
    ("Q15", "Chart geral id 0: não representa um gênero específico", chart_geral, "Datas, formatos e categorias"),
    ("Q16", "Gênero do álbum genérico (id menor ou igual a zero)", genero_album_generico, "Datas, formatos e categorias"),
    ("Q17", "Duração fora de Q1 − 1,5 IQR a Q3 + 1,5 IQR", outliers_duracao, "Possíveis outliers e integridade do enriquecimento"),
    ("Q18", "Rank fora de Q1 − 1,5 IQR a Q3 + 1,5 IQR", outliers_rank, "Possíveis outliers e integridade do enriquecimento"),
    ("Q19", "Id ausente ou divergente na junção de faixa/álbum/artista", integridade, "Possíveis outliers e integridade do enriquecimento"),
    ("Q20", "Duração do chart diferente da duração em /track", divergencia_duracao, "Possíveis outliers e integridade do enriquecimento"),
    ("Q21", "Rank do chart diferente do rank em /track", divergencia_rank, "Possíveis outliers e integridade do enriquecimento"),
]
diagnostico = pd.DataFrame([
    {"ID": identificador, "regra": regra, "quantidade": int(mascara.sum()),
     "denominador": numero_linhas, "percentual": 100 * mascara.sum() / numero_linhas,
     "celula": celula}
    for identificador, regra, mascara, celula in verificacoes
])
display(diagnostico)
print("As proporções usam ocorrências nos charts e podem se sobrepor; não devem ser somadas.")

# %% [markdown]
# **Resposta do grupo:**
#
# No retrato de 16/10/2026, são 2.800 ocorrências, 102 colunas e 2.581 faixas.
# Há 219/2.800 repetições excedentes por `id` (7,82%), mas nenhuma pela chave
# chart-faixa. BPM é zero em 1.890/2.800 ocorrências (67,50%); `title_version`
# está ausente em 2.533/2.800 (90,46%). Uma ocorrência tem lançamento posterior
# à coleta, e 143/2.800 (5,11%) têm duração fora dos limites IQR.
# Evidências: células “Visão geral e tipos observados” e “Diagnóstico de qualidade Q1 a Q21”.
# A repetição por `id` exige preservar o chart de origem
# na preparação, pois ele define os grupos das perguntas P1 a P4. O chart geral deve
# ser identificado separadamente dos gêneros. BPM zero e versões sem texto precisam
# de interpretação; valores extremos de duração são candidatos à inspeção, sem
# exclusão automática. O diagnóstico completo e as prioridades estão no documento
# “Compreensão e qualidade”, com as mesmas contagens do quadro Q1 a Q21.
