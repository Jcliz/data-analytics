#> Seção do notebook: RA1 — 1. Contexto e objetivo
#> Área responsável: A · Tarefa: T01 (entregas/plano-de-tarefas.md)
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Mantenha os enunciados do professor; troque só o "[Preencha aqui.]" e escreva o código.

# %% [markdown]
# ---
#
# # RA1 — Data Ingestion, Cleaning and Initial Analysis
#
# Nesta etapa, carregue, prepare e explore os dados do projeto.

# %% [markdown]
# ## 1. Contexto e objetivo
#
# Apresente brevemente o problema investigado e o que o grupo pretende descobrir com os dados.

# %% [markdown]
# **Resposta do grupo:**
#
# Os charts da Deezer mostram as faixas mais ouvidas em cada gênero, mas não o que elas têm em comum. O grupo quer descrever o perfil dessas faixas e ver se ele muda entre gêneros. O recorte é um único retrato dos charts da Deezer, o chart geral e o de cada gênero, na data da coleta registrada na seção 2. A unidade de observação é a faixa. As perguntas são:
#
# - **P1:** como a duração das faixas varia entre os gêneros;
# - **P2:** que parte das faixas de cada gênero foi lançada nos 12 meses anteriores à coleta;
# - **P3:** se faixas de artistas com mais fãs têm `rank` mais alto, no geral e dentro de cada gênero;
# - **P4:** quantos artistas distintos ocupam cada chart de gênero e que fatia das posições fica com os 5 artistas com mais faixas.
#
# O detalhe do recorte e das lacunas está na seção 01 do documento do RA1.
