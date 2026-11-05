#> Seção do notebook: RA3 — abertura da parte e 13. Análise estatística descritiva
#> Área responsável: C · Tarefa: T16 (entregas/plano-de-tarefas-ra3.md) · Critérios R13.1–R13.6
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> O template não tem o RA3: o enunciado desta seção é o requisito 2.1 de enunciados/ra3.md (ADR-0012). Não mude o sentido.
#> Leia antes: base/analise-e-ml.md, seções 1 e 2 (medidas coerentes com cada variável).

# %% [markdown]
# ---
#
# # RA3 — Analysis, Visualization and Machine Learning
#
# Utilize os dados preparados e processados nas etapas anteriores para produzir análises estatísticas, visualizações e interpretações que contribuam para responder ao problema definido. Explore também uma aplicação simples de Machine Learning, por classificação ou regressão, para investigar uma possibilidade de previsão a partir dos dados.

# %% [markdown]
# ## 13. Análise estatística descritiva
#
# Realize uma análise estatística dos dados, contemplando:
#
# - **Tendência central:** utilização de média e/ou mediana para compreender valores representativos.
# - **Dispersão:** utilização de medidas como amplitude ou desvio-padrão para analisar a variabilidade.
# - **Distribuição:** investigação da frequência, concentração ou distribuição dos valores.
#
# As medidas utilizadas devem ser coerentes com as características dos dados e com o problema investigado. Apresente os resultados e explique o que eles representam no contexto do projeto.

# %%
# Releitura do conjunto preparado para a análise
#> Esta célula vem pronta da estrutura: as seções 14 a 16 usam df_analise (CONTEXT.md, seção 6).
colunas_inteiras_analise = ["id_faixa", "id_chart", "posicao_chart", "id_artista", "id_album",
                            "duracao_s", "rank", "numero_fas"]
colunas_texto_analise = ["titulo", "genero", "tipo_chart", "artista"]
colunas_booleanas_analise = ["lancamento_posterior_coleta", "duracao_fora_limites_iqr"]
df_analise = pd.read_csv(
    PASTA_PREPARADOS / "faixas_preparadas.csv", encoding="utf-8",
    dtype={**{c: "int64" for c in colunas_inteiras_analise},
           **{c: "string" for c in colunas_texto_analise},
           **{c: "bool" for c in colunas_booleanas_analise}},
    parse_dates=["data_lancamento", "data_coleta"],
)
print(f"{len(df_analise)} ocorrências faixa-chart, {df_analise['id_faixa'].nunique()} faixas distintas, "
      f"{df_analise.loc[df_analise['tipo_chart'].eq('genero'), 'genero'].nunique()} charts de gênero "
      f"e {df_analise['tipo_chart'].eq('geral').sum()} ocorrências no chart geral.")

# %%
# Utilize quantas células de código forem necessárias para esta etapa.

# %% [markdown]
# **Resposta do grupo:**
#
# [Preencha aqui.]
