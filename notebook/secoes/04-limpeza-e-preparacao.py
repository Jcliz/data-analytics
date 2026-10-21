#> Seção do notebook: RA1 — 4. Limpeza e preparação dos dados
#> Área responsável: D · Tarefa: T04 (#5).
#> O bruto é preservado; esta seção cria df_preparado a partir de uma cópia.

# %% [markdown]
# ## 4. Limpeza e preparação dos dados
#
# Realize a limpeza necessária ao projeto. Verifique valores ausentes, duplicados e inconsistências e trate os problemas encontrados, quando necessário.

# %%
# Cópia de trabalho e referência do bruto
import numpy as np
import pandas as pd
from IPython.display import display

referencia_bruta_preparacao = df_bruto.copy(deep=True)
df_preparado = df_bruto.copy(deep=True)
total_antes_preparacao = len(df_bruto)
assert total_antes_preparacao > 0, "Execute a ingestão antes de preparar os dados."
print(f"Entrada: {total_antes_preparacao} ocorrências × {df_bruto.shape[1]} atributos.")

# %%
# Preservação do vínculo entre faixa e chart
# D1 (Q4–Q6): a faixa pode se repetir entre charts, mas a chave composta é única.
chave_bruta = ["chart_id_genero", "id"]
repeticoes_id_antes = int(df_bruto.duplicated("id").sum())
duplicatas_chave_antes = int(df_bruto.duplicated(chave_bruta).sum())
assert df_bruto[chave_bruta].notna().all().all(), "Chave de origem incompleta."
assert duplicatas_chave_antes == 0, "Revise o diagnóstico: há pares chart-faixa repetidos."
pd.testing.assert_frame_equal(df_preparado[chave_bruta], df_bruto[chave_bruta])
print(f"D1: {repeticoes_id_antes}/{total_antes_preparacao} excedentes por id mantidos; "
      f"{duplicatas_chave_antes}/{total_antes_preparacao} duplicatas chart-faixa.")

# %%
# Padronização dos campos textuais
# D2 (Q12): remover somente espaços nas pontas, preservando acentos e a escrita.
colunas_textuais_preparacao = ["title", "artist_name", "chart_nome_genero"]
espacos_antes_preparacao = pd.Series(False, index=df_bruto.index)
alteracoes_textuais_preparacao = []
for coluna in colunas_textuais_preparacao:
    antes = df_preparado[coluna].astype("string")
    depois = antes.str.strip()
    alteradas = antes.ne(depois).fillna(False)
    espacos_antes_preparacao |= alteradas
    for indice in df_preparado.index[alteradas]:
        alteracoes_textuais_preparacao.append({
            "id_faixa": int(df_preparado.at[indice, "id"]),
            "campo": coluna, "antes": repr(antes.at[indice]),
            "depois": repr(depois.at[indice]),
        })
    df_preparado[coluna] = depois
    assert depois.eq(depois.str.strip()).fillna(True).all()
print(f"D2: {int(espacos_antes_preparacao.sum())}/{total_antes_preparacao} "
      "ocorrências corrigidas; nenhuma linha excluída.")
display(pd.DataFrame(alteracoes_textuais_preparacao).head(10))

# %%
# Conversão e validação temporal
# D3 (Q11): conservar o lançamento e identificar datas posteriores à coleta.
texto_lancamento_preparacao = df_preparado["detalhe_faixa_release_date"].astype("string")
assert texto_lancamento_preparacao.str.fullmatch(r"\d{4}-\d{2}-\d{2}").fillna(False).all()
datas_lancamento_preparacao = pd.to_datetime(
    texto_lancamento_preparacao, format="%Y-%m-%d", errors="raise"
)
assert datas_lancamento_preparacao.notna().all()
assert datas_lancamento_preparacao.ge(pd.Timestamp("1900-01-01")).all()
assert datas_lancamento_preparacao.dt.strftime("%Y-%m-%d").eq(
    texto_lancamento_preparacao
).all()
data_retrato_preparacao = pd.Timestamp(metadados["inicio_utc"])
if data_retrato_preparacao.tzinfo is not None:
    data_retrato_preparacao = data_retrato_preparacao.tz_convert("UTC").tz_localize(None)
data_retrato_preparacao = data_retrato_preparacao.normalize()
df_preparado["detalhe_faixa_release_date"] = datas_lancamento_preparacao
df_preparado["data_coleta"] = data_retrato_preparacao
df_preparado["lancamento_posterior_coleta"] = (
    datas_lancamento_preparacao > data_retrato_preparacao
)
print(f"D3: {int(df_preparado['lancamento_posterior_coleta'].sum())}/"
      f"{total_antes_preparacao} lançamentos posteriores à coleta, preservados.")
display(df_preparado.loc[
    df_preparado["lancamento_posterior_coleta"],
    ["id", "title", "detalhe_faixa_release_date", "data_coleta"],
].head(10))

# %%
# Identificação do chart de origem
# D4 (Q14–Q16): o gênero do álbum não substitui o chart de origem.
df_preparado["tipo_chart"] = df_preparado["chart_id_genero"].map(
    lambda identificador: "geral" if identificador == 0 else "genero"
)
charts_gerais_preparacao = df_preparado["chart_id_genero"].eq(0)
assert df_preparado["tipo_chart"].eq("geral").equals(charts_gerais_preparacao)
assert df_preparado.groupby("chart_id_genero")["chart_nome_genero"].nunique().eq(1).all()
print(f"D4: {int(charts_gerais_preparacao.sum())}/{total_antes_preparacao} "
      "ocorrências identificadas como chart geral, sem exclusão.")

# %%
# Sinalização dos extremos de duração
# D7 (Q17–Q18): reproduzir a regra da seção 3, sem alterar duração ou rank.
quartis_duracao_preparacao = df_bruto["duration"].quantile([0.25, 0.75])
amplitude_duracao_preparacao = quartis_duracao_preparacao.iloc[1] - (
    quartis_duracao_preparacao.iloc[0]
)
limite_inferior_duracao = quartis_duracao_preparacao.iloc[0] - (
    1.5 * amplitude_duracao_preparacao
)
limite_superior_duracao = quartis_duracao_preparacao.iloc[1] + (
    1.5 * amplitude_duracao_preparacao
)
df_preparado["duracao_fora_limites_iqr"] = (
    df_preparado["duration"].lt(limite_inferior_duracao)
    | df_preparado["duration"].gt(limite_superior_duracao)
)
pd.testing.assert_series_equal(df_preparado["duration"], df_bruto["duration"])
pd.testing.assert_series_equal(df_preparado["rank"], df_bruto["rank"])
print(f"D7: limites {limite_inferior_duracao:g} a {limite_superior_duracao:g} s; "
      f"{int(df_preparado['duracao_fora_limites_iqr'].sum())}/"
      f"{total_antes_preparacao} ocorrências sinalizadas e mantidas.")

# %%
# Registro das decisões de preparação
decisoes_preparacao = pd.DataFrame([
    ("D1", "Q4–Q6", "Preservar o vínculo chart-faixa", "Nenhuma linha excluída"),
    ("D2", "Q12", "Remover espaços nas pontas", "Preservar a escrita dos nomes"),
    ("D3", "Q11", "Converter e sinalizar datas", "Não imputar lançamento"),
    ("D4", "Q14–Q16", "Identificar o tipo de chart", "Preservar a origem"),
    ("D5", "Q2, Q3, Q9, Q10", "Selecionar atributos na seção 5", "Não excluir faixas"),
    ("D6", "Q7, Q8", "Padronizar nomes e tipos na seção 5", "Não alterar números válidos"),
    ("D7", "Q17, Q18", "Sinalizar extremos", "Não cortar ou substituir valores"),
    ("D8", "Q1, Q13, Q19–Q21", "Revalidar consistência na seção 5", "Manter dados aprovados"),
], columns=["decisao", "diagnostico", "acao", "justificativa"])
display(decisoes_preparacao)
pd.testing.assert_frame_equal(df_bruto, referencia_bruta_preparacao)
assert len(df_preparado) == total_antes_preparacao

# %% [markdown]
# **Resposta do grupo:**
#
# As decisões D1–D8 respondem às verificações Q1–Q21. A preparação preserva a
# participação de cada faixa nos charts, corrige espaços e sinaliza situações que
# exigem cuidado, sem excluir automaticamente dados por critérios estatísticos.
#
# Preservamos as 2.800 ocorrências e o vínculo faixa-chart (D1), com 219/2.800
# excedentes por id e nenhuma duplicata pela chave composta. Corrigimos espaços
# nas pontas em 1/2.800 ocorrências (D2), convertemos o lançamento e sinalizamos
# 1/2.800 datas posteriores à coleta (D3). Identificamos separadamente as
# 100/2.800 ocorrências do chart geral (D4). As 143/2.800 durações fora dos limites
# IQR foram sinalizadas, sem exclusão nem substituição (D7).
#
# Evidências: células “Preservação do vínculo entre faixa e chart”, “Padronização
# dos campos textuais”, “Conversão e validação temporal”, “Identificação do chart
# de origem” e “Sinalização dos extremos de duração”. A seção 5 conclui D5, D6 e
# D8 com seleção, padronização, validação e gravação. O bruto permanece intacto.
