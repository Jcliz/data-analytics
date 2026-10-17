#> Área C · T09 · Contrato: lê eventos e cria TABELA_JANELAS e consulta para a seção 11.

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
# Usamos uma única janela **tumbling de 5 minutos**, sem sobreposição.
# Cada intervalo inclui seu início e exclui seu fim: um evento às 10:05:00
# entra em 10:05–10:10, e não em 10:00–10:05. O deslocamento é igual à
# duração (5 minutos), implícito nesse tipo de janela.
#
# Contamos as reproduções por `genero` usando o instante do evento (`instante`),
# conforme o objetivo da seção 8. A tabela mostra a contagem de cada gênero
# em cada intervalo e permite identificar os gêneros com maior contagem,
# inclusive empates. As contagens representam eventos simulados, não audiência
# real da Deezer. O modo `complete` reexibe toda a tabela a cada lote; a saída
# `memory` permite mostrar os resultados na célula e no PDF.

# %%
# Agregação por gênero em janela tumbling de cinco minutos
from uuid import uuid4
from pyspark.sql import functions as F

if not eventos.isStreaming:
    raise ValueError("Execute a seção 9: eventos deve ser um DataFrame em streaming.")
# Interrompe consultas remanescentes antes de iniciar a consulta desta seção.
for consulta_anterior in spark.streams.active:
    consulta_anterior.stop()

agregado_janelas = eventos.groupBy(
    F.window("instante", "5 minutes"), "genero"
).agg(F.count("*").alias("reproducoes"))

# %%
# Consulta em memória com estado das janelas
# Checkpoint próprio por execução: a saída memory começa vazia e relê os lotes da entrada.
# Reutilizar um checkpoint anterior com uma tabela memory nova perderia a demonstração do primeiro lote.
TABELA_JANELAS = "janelas_" + uuid4().hex
consulta = (
    agregado_janelas.writeStream
    .outputMode("complete")
    .format("memory")
    .queryName(TABELA_JANELAS)
    .option("checkpointLocation", str(PASTA_CHECKPOINT / TABELA_JANELAS))
    .start()
)
print(f"Consulta ativa: {consulta.isActive}; tabela em memória: {TABELA_JANELAS}")

# %%
# Tabela das janelas após o primeiro lote
consulta.processAllAvailable()
tabela_primeiro_lote = spark.table(TABELA_JANELAS)
quantidade_grupos = tabela_primeiro_lote.count()
# O limite é o número real de grupos, para que show() não esconda linhas além das primeiras 20.
tabela_primeiro_lote.select(
    F.col("window.start").alias("inicio"),
    F.col("window.end").alias("fim"), "genero", "reproducoes"
).orderBy("inicio", F.desc("reproducoes"), "genero").show(n=max(1, quantidade_grupos), truncate=False)

resumo_primeiro_lote = tabela_primeiro_lote.agg(
    F.sum("reproducoes").alias("reproducoes"),
    F.countDistinct("window").alias("janelas"),
    F.countDistinct("genero").alias("generos"),
).first()
print(f"Após o primeiro lote: {resumo_primeiro_lote['reproducoes'] or 0} reproduções; "
      f"{resumo_primeiro_lote['janelas']} janelas; {resumo_primeiro_lote['generos']} gêneros; "
      f"{quantidade_grupos} pares janela-gênero.")
# A consulta permanece ativa para os novos lotes e o encerramento da seção 11.
