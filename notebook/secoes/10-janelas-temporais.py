#> Seção do notebook: RA2 — 10. Aplicação de janelas temporais
#> Área responsável: C · Tarefa: T09 (entregas/plano-de-tarefas.md)
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Mantenha os enunciados do professor; troque só o "[Preencha aqui.]" e escreva o código.

# %% [markdown]
# ## 10. Aplicação de janelas temporais
#
# - Utilize uma janela **Tumbling** (intervalos sem sobreposição) ou **Sliding** (intervalos que podem se sobrepor).
# - Informe o tipo e a duração da janela e o deslocamento, quando aplicável.
# - Implemente uma agregação coerente com a análise, como contagem, soma ou média.
# - Explique brevemente o que será calculado em cada intervalo.
#
# O foco é demonstrar a compreensão do conceito; não é necessário justificar tecnicamente a duração escolhida.

# %% [markdown]
# **Resposta do grupo:**
#
# [Informe o tipo, a duração, o deslocamento (quando aplicável) e o que será calculado em cada janela.]
#
# <!--
# Tipo (tumbling ou sliding), duração, deslocamento e a agregação (ex.: contagem de reproduções por
# gênero em janela sliding de 5 min com deslocamento de 2 min). Só uma janela (enunciado do RA2).
# -->

# %%
#> Template: "Utilize quantas células de código forem necessárias para esta etapa."
#> Crie quantas células "# %%" precisar; comece cada uma com um comentário-título curto (ex.: "# Duplicados por id"),
#> que é como o documento do RA1 cita a evidência.
#> Passos esperados:
#> 1. eventos = spark.readStream.schema(...).option("timestampFormat", ...).json(entrada)
#> 2. agregado = eventos.groupBy(window("instante", duração[, deslocamento]), "genero").agg(...)
#> 3. consulta = agregado.writeStream.outputMode("complete").format("memory").queryName(...)
#>               .option("checkpointLocation", ...).start()
#> Contrato (CONTEXT.md §6): esta seção cria consulta; a seção 11 publica os lotes e encerra.
