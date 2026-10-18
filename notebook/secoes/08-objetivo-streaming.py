#> Seção do notebook: RA2 — 8. Objetivo da análise em streaming
#> Área responsável: A · Tarefa: T07 (entregas/plano-de-tarefas.md)
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Mantenha os enunciados do professor; troque só o "[Preencha aqui.]" e escreva o código.

# %% [markdown]
# ---
#
# # RA2 — Streaming Data Processing and Time Windows
#
# Utilize os dados e o contexto do projeto para demonstrar o processamento em streaming e a aplicação de janelas temporais. Escolha um dos cenários:
#
# - **Cenário A — Dados estáticos:** simule a chegada de novos registros utilizando dados artificiais coerentes com o contexto do projeto.
# - **Cenário B — Dados em streaming:** utilize sua própria fonte de dados contínuos, sem necessidade de simulação.

# %% [markdown]
# ## 8. Objetivo da análise em streaming
#
# Responda brevemente:
#
# - O que o grupo deseja monitorar ou analisar?
# - Qual informação espera obter com o processamento em streaming?

# %% [markdown]
# **Resposta do grupo:**
#
# No RA1, o grupo compara entre gêneros o perfil das faixas que estão no topo dos charts da Deezer. No RA2, o grupo quer **monitorar as reproduções dessas faixas por gênero ao longo do tempo**. Como a API da Deezer não oferece um fluxo de reproduções, usamos o cenário A: eventos de reprodução simulados, sorteados entre as faixas e os gêneros do conjunto preparado do RA1.
#
# Com o processamento em streaming, esperamos saber, a cada janela de tempo, **quantas reproduções cada gênero acumula** e **qual gênero concentra mais reproduções naquele intervalo**, e ver esses números mudarem conforme novos lotes de eventos chegam. O tipo e a duração da janela estão na seção 10.
