#> Seção do notebook: RA1 — 5. Transformação dos dados
#> Área responsável: D · Tarefa: T04 (#5).
#> Somente transformações de preparo; sem respostas analíticas a P1–P4.

# %% [markdown]
# ## 5. Transformação dos dados
#
# Realize as transformações necessárias à análise, como criação de colunas, filtros, agrupamentos, conversões ou junções, quando aplicáveis.

# %%
# Seleção e organização dos atributos
# D5: doze atributos do bruto e quatro campos de contexto ou qualidade.
nomes_colunas_preparadas = {
    "id": "id_faixa", "title": "titulo", "chart_id_genero": "id_chart",
    "chart_nome_genero": "genero", "tipo_chart": "tipo_chart",
    "position": "posicao_chart", "artist_id": "id_artista", "artist_name": "artista",
    "album_id": "id_album", "duration": "duracao_s", "rank": "rank",
    "detalhe_artista_nb_fan": "numero_fas",
    "detalhe_faixa_release_date": "data_lancamento", "data_coleta": "data_coleta",
    "lancamento_posterior_coleta": "lancamento_posterior_coleta",
    "duracao_fora_limites_iqr": "duracao_fora_limites_iqr",
}
df_preparado = df_preparado.loc[:, list(nomes_colunas_preparadas)].rename(
    columns=nomes_colunas_preparadas
)
assert df_preparado.columns.tolist() == list(nomes_colunas_preparadas.values())
assert len(df_preparado) == total_antes_preparacao
print(f"D5: {df_bruto.shape[1]} atributos de origem → "
      f"{df_preparado.shape[1]} atributos finais; {len(df_preparado)} linhas preservadas.")

# %%
# Padronização dos nomes e tipos
# D6: rank mantém o nome já esperado pelo gerador de eventos da seção 9.
colunas_inteiras_preparadas = [
    "id_faixa", "id_chart", "posicao_chart", "id_artista", "id_album",
    "duracao_s", "rank", "numero_fas",
]
colunas_textuais_preparadas = ["titulo", "genero", "tipo_chart", "artista"]
colunas_datas_preparadas = ["data_lancamento", "data_coleta"]
colunas_booleanas_preparadas = [
    "lancamento_posterior_coleta", "duracao_fora_limites_iqr",
]
for coluna in colunas_inteiras_preparadas:
    valores = pd.to_numeric(df_preparado[coluna], errors="raise")
    assert valores.notna().all() and np.isfinite(valores).all(), coluna
    assert valores.mod(1).eq(0).all(), f"Inteiro fracionário em {coluna}."
    df_preparado[coluna] = valores.astype("int64")
for coluna in colunas_textuais_preparadas:
    df_preparado[coluna] = df_preparado[coluna].astype("string")
for coluna in colunas_datas_preparadas:
    df_preparado[coluna] = pd.to_datetime(
        df_preparado[coluna], errors="raise"
    ).astype("datetime64[ns]")
for coluna in colunas_booleanas_preparadas:
    assert pd.api.types.is_bool_dtype(df_preparado[coluna]), coluna
display(df_preparado.dtypes.astype(str).rename("tipo").to_frame())

# %%
# Verificações finais do conjunto preparado
# D8: falhas são expostas; não há preenchimento automático nem remoção de linhas.
assert df_preparado.notna().all().all(), "O conjunto selecionado tem valores ausentes."
chave_preparada = ["data_coleta", "id_chart", "id_faixa"]
assert not df_preparado.duplicated(chave_preparada).any()
for coluna in ["id_faixa", "id_artista", "id_album", "duracao_s", "posicao_chart"]:
    assert df_preparado[coluna].gt(0).all(), coluna
for coluna in ["id_chart", "rank", "numero_fas"]:
    assert df_preparado[coluna].ge(0).all(), coluna
for coluna in colunas_textuais_preparadas:
    assert df_preparado[coluna].str.strip().ne("").all(), coluna
    assert df_preparado[coluna].eq(df_preparado[coluna].str.strip()).all(), coluna
assert df_preparado["tipo_chart"].isin(["geral", "genero"]).all()
assert df_preparado["tipo_chart"].eq("geral").eq(df_preparado["id_chart"].eq(0)).all()
assert df_preparado.groupby("id_chart")["genero"].nunique().eq(1).all()
assert df_preparado.groupby("id_artista")["artista"].nunique().eq(1).all()
assert df_preparado["lancamento_posterior_coleta"].equals(
    df_preparado["data_lancamento"].gt(df_preparado["data_coleta"])
)
assert df_preparado["duracao_fora_limites_iqr"].equals(
    df_preparado["duracao_s"].lt(limite_inferior_duracao)
    | df_preparado["duracao_s"].gt(limite_superior_duracao)
)
# A correspondência linha a linha garante que a seleção não perdeu a origem.
for origem, destino in nomes_colunas_preparadas.items():
    if destino in colunas_inteiras_preparadas:
        pd.testing.assert_series_equal(
            df_preparado[destino], df_bruto[origem].astype("int64"), check_names=False
        )
for origem, detalhe in [
    ("id", "detalhe_faixa_id"), ("album_id", "detalhe_album_id"),
    ("artist_id", "detalhe_artista_id"),
]:
    assert df_bruto[origem].eq(df_bruto[detalhe]).all(), detalhe
assert df_preparado["duracao_s"].eq(df_bruto["detalhe_faixa_duration"]).all()
assert df_preparado["rank"].eq(df_bruto["detalhe_faixa_rank"]).all()
assert df_preparado["data_lancamento"].dt.strftime("%Y-%m-%d").eq(
    df_bruto["detalhe_faixa_release_date"].astype("string")
).all()
assert df_preparado["data_coleta"].eq(data_retrato_preparacao).all()
pd.testing.assert_frame_equal(df_bruto, referencia_bruta_preparacao)
print(f"Validações aprovadas em {len(df_preparado)} ocorrências: "
      "tipos, domínios, ausências, chave, datas, sinalizações e integridade.")

# %%
# Comparação antes e depois da preparação
espacos_depois_preparacao = pd.Series(False, index=df_preparado.index)
for coluna in colunas_textuais_preparadas:
    espacos_depois_preparacao |= df_preparado[coluna].ne(
        df_preparado[coluna].str.strip()
    )
comparacao_preparacao = pd.DataFrame([
    ("Registros", total_antes_preparacao, len(df_preparado)),
    ("Atributos", df_bruto.shape[1], df_preparado.shape[1]),
    ("Ocorrências com espaços nas pontas", int(espacos_antes_preparacao.sum()),
     int(espacos_depois_preparacao.sum())),
    ("Duplicatas chart-faixa", duplicatas_chave_antes,
     int(df_preparado.duplicated(chave_preparada).sum())),
    ("Excedentes por id da faixa", repeticoes_id_antes,
     int(df_preparado.duplicated("id_faixa").sum())),
    ("Ocorrências do chart geral", int(charts_gerais_preparacao.sum()),
     int(df_preparado["tipo_chart"].eq("geral").sum())),
    ("Lançamentos posteriores à coleta",
     int(datas_lancamento_preparacao.gt(data_retrato_preparacao).sum()),
     int(df_preparado["lancamento_posterior_coleta"].sum())),
    ("Durações fora dos limites IQR",
     int((df_bruto["duration"].lt(limite_inferior_duracao)
          | df_bruto["duration"].gt(limite_superior_duracao)).sum()),
     int(df_preparado["duracao_fora_limites_iqr"].sum())),
], columns=["medida", "antes", "depois"])
display(comparacao_preparacao)
print(f"Denominador das medidas por ocorrência: {total_antes_preparacao} antes "
      f"e {len(df_preparado)} depois; as medidas podem se sobrepor.")

# %%
# Gravação e releitura do conjunto preparado
arquivo_preparado = PASTA_PREPARADOS / "faixas_preparadas.csv"
# Fim de linha "\n" fixo: o arquivo sai igual no Windows, no Linux e no Colab
df_preparado.to_csv(arquivo_preparado, index=False, encoding="utf-8", date_format="%Y-%m-%d",
                    lineterminator="\n")
tipos_releitura_preparacao = {
    **{coluna: "int64" for coluna in colunas_inteiras_preparadas},
    **{coluna: "string" for coluna in colunas_textuais_preparadas},
    **{coluna: "bool" for coluna in colunas_booleanas_preparadas},
}
releitura_preparacao = pd.read_csv(
    arquivo_preparado, encoding="utf-8", dtype=tipos_releitura_preparacao,
    parse_dates=colunas_datas_preparadas,
)
pd.testing.assert_frame_equal(df_preparado, releitura_preparacao)
tamanho_preparado = f"{arquivo_preparado.stat().st_size:,}".replace(",", ".")
print(f"Arquivo: {arquivo_preparado.relative_to(RAIZ)} · UTF-8, separador vírgula, "
      f"{tamanho_preparado} bytes.")
print(f"Releitura validada: {len(releitura_preparacao)} linhas × "
      f"{releitura_preparacao.shape[1]} colunas, sem perda de valores.")
display(df_preparado.head(5))

# %% [markdown]
# **Resposta do grupo:**
#
# Selecionamos os atributos, padronizamos nomes e tipos e gravamos o conjunto
# preparado. A unidade continua sendo uma ocorrência de faixa por chart e data
# de coleta. As perguntas analíticas serão respondidas posteriormente.
#
# O conjunto preparado está em `dados/preparados/faixas_preparadas.csv`, com
# 2.800 ocorrências e 16 colunas: 12 atributos selecionados do bruto e quatro
# campos de contexto ou qualidade. Nenhuma linha foi excluída. Os espaços nas
# pontas passaram de 1/2.800 para 0/2.800 ocorrências. A chave data-chart-faixa
# permaneceu sem duplicatas; as 219/2.800 repetições por id foram preservadas.
# Evidências: células “Comparação antes e depois da preparação” e “Gravação e
# releitura do conjunto preparado”.
#
# As 100/2.800 ocorrências do chart geral estão identificadas em `tipo_chart`.
# A data futura (1/2.800) e os extremos de duração (143/2.800) foram mantidos e
# sinalizados, sem confirmação de suas causas. O CSV não inclui BPM, ganho,
# prévia ou versão complementar; esses dados continuam no bruto. O gerador do
# RA2 precisa filtrar o chart geral ao usar o preparado, mantendo somente
# `tipo_chart == "genero"` para os eventos por gênero.
