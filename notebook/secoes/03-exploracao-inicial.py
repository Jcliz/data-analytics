#> Seção do notebook: RA1 — 3. Exploração inicial dos dados
#> Área responsável: C · Tarefa: T03 (entregas/plano-de-tarefas.md)
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Mantenha os enunciados do professor; troque só o "[Preencha aqui.]" e escreva o código.

# %% [markdown]
# ## 3. Exploração inicial dos dados
#
# Investigue a quantidade de registros e colunas, os tipos de dados, os valores ausentes e outras características relevantes da base.

# %%
#> Template: "Utilize quantas células de código forem necessárias para esta etapa."
#> Crie quantas células "# %%" precisar; comece cada uma com um comentário-título curto (ex.: "# Duplicados por id"),
#> que é como o documento do RA1 cita a evidência.
#> Passos esperados (base/qualidade-de-dados.md):
#> 1. Visão geral: linhas, colunas, tipos (df_bruto.dtypes), memória.
#> 2. Ausentes por coluna (quantidade e %), incluindo texto vazio "" que a API usa no lugar de nulo.
#> 3. Duplicados pela chave (id da faixa) e linhas inteiras iguais.
#> 4. Estatísticas descritivas das numéricas (duration, rank, bpm, gain) e valores impossíveis (0, negativos).
#> 5. Datas (release_date) que não convertem; categorias (gênero) com grafias diferentes; possíveis outliers.
#> 6. Uma tabela-resumo "diagnóstico" com Q1…Qn (verificação, regra, resultado, proporção) que vira a tabela
#>    "Diagnóstico de qualidade" do documento (documentacao/ra1/03-compreensao-e-qualidade.md).
#> Só diagnosticar: não altere df_bruto (trabalhe numa cópia, se precisar). Nada de gráfico de resultado.

# %% [markdown]
# **Resposta do grupo:**
#
# [Registre brevemente as principais características observadas.]
#
# <!--
# Principais características observadas, com números: tamanho da base, problemas mais relevantes (Q…)
# e o que NÃO apresentou problema. Poucas frases.
# -->
