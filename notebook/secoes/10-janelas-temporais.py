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
#> Passos esperados (base/streaming-e-janelas.md §2 e §3):
#> 1. Pare consultas que tenham sobrado de uma execução anterior: for q in spark.streams.active: q.stop()
#> 2. agregado = eventos.groupBy(window("instante", duração[, deslocamento]), "genero").agg(...)
#>    Uma única janela (tumbling ou sliding), coerente com o objetivo da seção 8.
#> 3. TABELA_JANELAS = nome da tabela em memória, único por execução (a aula usa uuid4().hex).
#> 4. consulta = agregado.writeStream.outputMode("complete").format("memory").queryName(TABELA_JANELAS)
#>               .option("checkpointLocation", str(PASTA_CHECKPOINT / "janelas")).start()
#>    complete + memory é a combinação das aulas. Não use append (com janela, exige watermark e só mostra
#>    janelas fechadas) nem format("console") (escreve no log, não na célula, e não vai para o PDF).
#>    Watermark e trigger não são necessários.
#> 5. consulta.processAllAvailable() e mostre a tabela do 1º lote (publicado na seção 9):
#>    spark.table(TABELA_JANELAS).select("window.start", "window.end", ...).orderBy("start").show(truncate=False)
#> Contrato (CONTEXT.md §6): esta seção cria TABELA_JANELAS e consulta; a seção 11 publica os lotes seguintes.
