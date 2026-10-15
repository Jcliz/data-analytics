#> Seção do notebook: RA2 — 9. Fonte de dados e processamento
#> Área responsável: B · Tarefa: T08 (entregas/plano-de-tarefas.md)
#> Formato percent: "# %%" abre célula de código e "# %% [markdown]" abre célula de texto.
#> Linhas "#>" e comentários <!-- --> são orientações: o montador (scripts/montar_notebook.py) as remove.
#> Mantenha os enunciados do professor; troque só o "[Preencha aqui.]" e escreva o código.

# %% [markdown]
# ## 9. Fonte de dados e processamento
#
# - Informe o cenário escolhido: dados reais em streaming ou simulação.
# - Explique brevemente como os novos registros chegam.
# - Implemente o processamento em tempo real.
# - Demonstre o recebimento de novos registros.

# %% [markdown]
# **Resposta do grupo:**
#
# [Preencha aqui.]
#
# <!--
# Cenário A (simulação). Como os eventos de reprodução são gerados a partir de dados/preparados e como
# chegam (arquivos JSON publicados numa pasta monitorada pelo Spark).
# -->

# %%
#> Template: "Utilize quantas células de código forem necessárias para esta etapa."
#> Crie quantas células "# %%" precisar; comece cada uma com um comentário-título curto (ex.: "# Duplicados por id"),
#> que é como o documento do RA1 cita a evidência.
#> Passos esperados (base/streaming-e-janelas.md §3 e §4):
#> 1. %pip install -q "pyspark==4.0.3" (no Colab) e SparkSession local[2], fuso America/Sao_Paulo.
#> 2. Pastas entrada/, publicacao/ e checkpoint/ dentro de PASTA_STREAMING (limpar no início).
#> 3. Esquema explícito (StructType) do evento {id_evento, id_faixa, genero, artista, duracao_ouvida_s, instante}.
#> 4. Função publicar_lote(eventos): escreve JSON (uma linha por evento) em publicacao/ e MOVE para entrada/.
#> 5. Função que sorteia eventos de df_preparado (ou de dados/preparados/faixas_preparadas.csv), com instantes
#>    crescentes; publicar o 1º lote e mostrar que foi recebido.
#> Contrato (CONTEXT.md §6): esta seção cria spark. A janela e a consulta são da seção 10.
