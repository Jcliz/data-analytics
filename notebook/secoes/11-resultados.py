#> Seção do notebook: RA2 — 11. Resultados e interpretação
#> Área responsável: D · Tarefa: T10 (entregas/plano-de-tarefas.md)
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Mantenha os enunciados do professor; troque só o "[Preencha aqui.]" e escreva o código.

# %% [markdown]
# ## 11. Resultados e interpretação
#
# Apresente os resultados do processamento e demonstre como a análise se comporta com a chegada de novos registros.

# %%
#> Template: "Utilize quantas células de código forem necessárias para esta etapa."
#> Crie quantas células "# %%" precisar; comece cada uma com um comentário-título curto (ex.: "# Duplicados por id"),
#> que é como o documento do RA1 cita a evidência.
#> Passos esperados:
#> 1. Pelo menos 2 lotes novos (3 no total, contando o da seção 9), cada um numa célula própria:
#>    publicar_lote(gerar_eventos(...)), consulta.processAllAvailable() e a tabela em memória ordenada pela janela:
#>    spark.table(TABELA_JANELAS).select("window.start", "window.end", ...).orderBy("start").show(truncate=False)
#>    Deixe a saída de cada lote visível no PDF.
#> 2. Pelo menos um lote com evento que cai numa janela já existente, para mostrar a atualização.
#> 3. A última célula de código da seção é só o encerramento: consulta.stop() e limpeza das subpastas de
#>    PASTA_STREAMING. Separada, para a demonstração ao vivo publicar um lote antes de encerrar
#>    (entregas/roteiro-apresentacao.md, seção 2).

# %% [markdown]
# **Resposta do grupo:**
#
# [Explique brevemente o significado dos resultados e as mudanças observadas com a chegada de novos registros.]
#
# <!--
# O que cada lote mudou (quais janelas e gêneros) e por quê, com números das saídas.
# -->
