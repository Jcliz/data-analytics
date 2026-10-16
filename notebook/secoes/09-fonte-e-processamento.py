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
#> 1. Instalação (só no Colab), numa célula própria começando com %%capture para a barra de progresso não ir
#>    para o PDF: %pip install -q "pyspark==4.0.3". Leva alguns minutos.
#> 2. SparkSession local[2], fuso America/Sao_Paulo, .config("spark.sql.shuffle.partitions", "2") e
#>    spark.sparkContext.setLogLevel("ERROR"), como nas aulas.
#> 3. PASTA_ENTRADA, PASTA_PUBLICACAO e PASTA_CHECKPOINT dentro de PASTA_STREAMING. No início, apague só essas
#>    subpastas (nunca PASTA_STREAMING, que tem o README versionado), e o checkpoint junto com a entrada.
#> 4. Se df_preparado não existir, leia dados/preparados/faixas_preparadas.csv; se o arquivo faltar, pare com
#>    uma mensagem clara (assert ou FileNotFoundError dizendo para rodar o RA1 antes).
#> 5. esquema_eventos (StructType) do evento {id_evento, id_faixa, genero, artista, duracao_ouvida_s, instante}.
#> 6. gerar_eventos(n, inicio): sorteia n faixas de df_preparado com random_state=SEMENTE e instantes crescentes a
#>    partir de inicio. SEMENTE e INICIO_SIMULACAO são fixos (ex.: 42 e datetime(2026, 10, 21, 10, 0)): sem
#>    datetime.now() nem sorteio sem semente, para a execução final dar os números citados nas respostas.
#> 7. publicar_lote(lista_de_eventos): escreve JSON (uma linha por evento) em PASTA_PUBLICACAO e MOVE para
#>    PASTA_ENTRADA, para o Spark nunca ler um arquivo pela metade.
#> 8. eventos = spark.readStream.schema(esquema_eventos).option("timestampFormat", ...).json(str(PASTA_ENTRADA))
#> 9. Recebimento: uma consulta simples (contagem de eventos recebidos, outputMode("complete"), format("memory"),
#>    checkpoint em PASTA_CHECKPOINT / "recebimento"); publique o 1º lote, processAllAvailable(), mostre a
#>    contagem com spark.table(...).show() e encerre essa consulta no fim da seção (stop()).
#> Contrato (CONTEXT.md §6): esta seção cria spark, as pastas, SEMENTE, INICIO_SIMULACAO, esquema_eventos,
#> gerar_eventos, publicar_lote e eventos. A janela é da seção 10; os lotes seguintes, da seção 11.
