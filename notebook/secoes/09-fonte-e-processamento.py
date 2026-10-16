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
#> Números tirados das saídas das células desta seção. Com o df_bruto provisório (antes da T04), os números mudam
#> quando o conjunto preparado entrar: atualize-os depois de executar de novo.
# Usamos o cenário A, de simulação, porque a API da Deezer não oferece um fluxo de reproduções em tempo real ([ADR-0005](../docs/adr/0005-ra2-cenario-a-simulacao.md)). Cada registro novo é uma reprodução de faixa, com `id_evento`, `id_faixa`, `genero`, `artista`, `duracao_ouvida_s` e `instante`. A função `gerar_eventos` sorteia faixas e gêneros reais do conjunto do RA1, com chance proporcional ao `rank` da Deezer, semente 42 e primeiro instante em 21/10/2026 às 10:00, e espaça os eventos de 5 a 30 segundos.
#
# Os registros chegam em lotes: `publicar_lote` grava cada lote como um arquivo JSON, com um evento por linha, e só então o move para `dados/streaming/entrada/`, a pasta que o Spark monitora com `spark.readStream` e esquema explícito. A consulta de recebimento conta os eventos que chegaram: antes do 1º lote a tabela está vazia e, depois dele, mostra 30 eventos, de 10:00:28 a 10:09:05, de 19 gêneros. A janela temporal é aplicada na seção 10, e os lotes seguintes chegam na seção 11.

# %%
#> Célula própria, começando com %%capture, para a barra de progresso da instalação não ir para o PDF.
#> Fora do Colab ela não instala nada: localmente, use o requirements.txt (pyspark==4.0.3, Java 17 ou mais novo).
%%capture
# Instalação do PySpark (só no Colab)
if NO_COLAB:
    %pip install -q "pyspark==4.0.3"

# %%
# Sessão do Spark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType, LongType, StringType, StructField, StructType, TimestampType

spark = (
    SparkSession.builder.master("local[2]")
    .appName("data-analytics — RA2")
    .config("spark.sql.session.timeZone", "America/Sao_Paulo")
    .config("spark.sql.shuffle.partitions", "2")
    .getOrCreate()
)
# Aplica o fuso também se já houver uma sessão aberta (reexecução da seção)
spark.conf.set("spark.sql.session.timeZone", "America/Sao_Paulo")
spark.sparkContext.setLogLevel("ERROR")

# Consultas que sobraram de uma execução anterior seguram arquivos das pastas abaixo
for consulta_antiga in spark.streams.active:
    consulta_antiga.stop()

print(f"Spark {spark.version} · fuso {spark.conf.get('spark.sql.session.timeZone')}")

# %%
#> Apague só as subpastas de execução; PASTA_STREAMING tem o README versionado.
#> O checkpoint vai junto com a entrada: um checkpoint antigo faz o Spark pular arquivos de mesmo nome.
# Pastas do streaming
import json
import shutil
from datetime import datetime, timedelta
from uuid import uuid4

import numpy as np

PASTA_ENTRADA = PASTA_STREAMING / "entrada"          # monitorada pelo Spark
PASTA_PUBLICACAO = PASTA_STREAMING / "publicacao"    # onde o lote é escrito antes de ser publicado
PASTA_CHECKPOINT = PASTA_STREAMING / "checkpoint"    # progresso das consultas
for pasta in (PASTA_ENTRADA, PASTA_PUBLICACAO, PASTA_CHECKPOINT):
    shutil.rmtree(pasta, ignore_errors=True)
    pasta.mkdir(parents=True)

print("Arquivos na entrada:", sorted(p.name for p in PASTA_ENTRADA.iterdir()))

# %%
#> Provisório até a T04 (#5) integrar o conjunto preparado: sem df_preparado e sem o CSV, a fonte dos eventos são
#> os itens dos charts de gênero do df_bruto (o chart geral "All" fica de fora, porque não é um gênero). Na execução
#> final o df_preparado existe e este ramo não roda. COLUNAS_FONTE supõe os nomes em português da T04
#> (pendência anotada na #5); se a T04 escolher outros nomes, ajuste só este dicionário.
# Faixas que alimentam os eventos
COLUNAS_FONTE = {"id_faixa": "id_faixa", "genero": "genero", "artista": "artista",
                 "duracao_s": "duracao_s", "rank": "rank"}

if "df_preparado" not in globals():
    arquivo_preparado = PASTA_PREPARADOS / "faixas_preparadas.csv"
    if arquivo_preparado.exists():
        df_preparado = pd.read_csv(arquivo_preparado)
if "df_preparado" in globals():
    faixas_fonte = df_preparado.rename(columns={v: k for k, v in COLUNAS_FONTE.items()})[list(COLUNAS_FONTE)]
    origem_faixas = "conjunto preparado do RA1"
elif "df_bruto" in globals():
    faixas_fonte = (
        df_bruto[df_bruto["chart_id_genero"] != 0]
        .rename(columns={"id": "id_faixa", "chart_nome_genero": "genero", "artist_name": "artista",
                         "duration": "duracao_s"})[list(COLUNAS_FONTE)]
    )
    origem_faixas = "df_bruto, charts de gênero (provisório até a T04)"
else:
    raise FileNotFoundError(
        "Conjunto preparado não encontrado (df_preparado ou dados/preparados/faixas_preparadas.csv). "
        "Execute as seções do RA1 antes da seção 9."
    )
faixas_fonte = faixas_fonte.dropna().reset_index(drop=True)

print(f"Origem: {origem_faixas}")
print(f"{len(faixas_fonte)} pares faixa-gênero · {faixas_fonte['id_faixa'].nunique()} faixas · "
      f"{faixas_fonte['genero'].nunique()} gêneros · {faixas_fonte['artista'].nunique()} artistas")

# %%
# Esquema do evento de reprodução
esquema_eventos = StructType([
    StructField("id_evento", IntegerType()),        # sequencial, único na simulação
    StructField("id_faixa", LongType()),            # id da Deezer (passa do limite de um int)
    StructField("genero", StringType()),
    StructField("artista", StringType()),
    StructField("duracao_ouvida_s", IntegerType()), # segundos ouvidos, até a duração da faixa
    StructField("instante", TimestampType()),
])
FORMATO_INSTANTE = "%Y-%m-%d %H:%M:%S"   # o mesmo de timestampFormat na leitura

# %%
#> SEMENTE e INICIO_SIMULACAO fixos: sem datetime.now() nem sorteio sem semente, para a execução final repetir os
#> números das respostas. O gerador guarda o estado entre chamadas: os lotes das seções 9 e 11 saem sempre iguais
#> se o notebook for executado de cima para baixo.
# Gerador de eventos
SEMENTE = 42
INICIO_SIMULACAO = datetime(2026, 10, 21, 10, 0)

sorteio = np.random.default_rng(SEMENTE)
proximo_id_evento = 1


def gerar_eventos(n, inicio):
    """Sorteia n reproduções das faixas de faixas_fonte, com instantes crescentes a partir de inicio.

    A chance de cada faixa segue o rank da Deezer (faixa mais popular, mais tocada). Entre um evento e o
    seguinte passam de 5 a 30 segundos; a duração ouvida vai de 30 segundos até a faixa inteira.
    """
    global proximo_id_evento
    pesos = faixas_fonte["rank"] / faixas_fonte["rank"].sum()
    escolhidas = faixas_fonte.iloc[sorteio.choice(len(faixas_fonte), size=n, p=pesos)]
    intervalos = np.cumsum(sorteio.integers(5, 31, size=n))
    lote = []
    for (_, faixa), segundos in zip(escolhidas.iterrows(), intervalos):
        duracao = int(faixa["duracao_s"])
        lote.append({
            "id_evento": proximo_id_evento,
            "id_faixa": int(faixa["id_faixa"]),
            "genero": faixa["genero"],
            "artista": faixa["artista"],
            "duracao_ouvida_s": int(sorteio.integers(min(30, duracao), duracao + 1)),
            "instante": (inicio + timedelta(seconds=int(segundos))).strftime(FORMATO_INSTANTE),
        })
        proximo_id_evento += 1
    return lote


# %%
# Publicação de um lote
lotes_publicados = 0


def publicar_lote(eventos):
    """Grava o lote em JSON (uma linha por evento) em PASTA_PUBLICACAO e move para PASTA_ENTRADA.

    O arquivo só aparece na entrada depois de escrito e fechado, então o Spark nunca lê um lote pela metade.
    """
    global lotes_publicados
    lotes_publicados += 1
    nome = f"lote_{lotes_publicados:03d}.json"
    arquivo = PASTA_PUBLICACAO / nome
    with arquivo.open("w", encoding="utf-8") as saida:
        for evento in eventos:
            saida.write(json.dumps(evento, ensure_ascii=False) + "\n")
    arquivo.replace(PASTA_ENTRADA / nome)
    print(f"Lote {lotes_publicados} publicado: {nome}, {len(eventos)} eventos, "
          f"de {eventos[0]['instante']} a {eventos[-1]['instante']}")
    return PASTA_ENTRADA / nome


# %%
# Leitura em streaming
eventos = (
    spark.readStream
    .schema(esquema_eventos)
    .option("timestampFormat", "yyyy-MM-dd HH:mm:ss")
    .json(str(PASTA_ENTRADA))
)
print("É um DataFrame em streaming?", eventos.isStreaming)
eventos.printSchema()

# %%
#> Consulta só desta seção, para demonstrar o recebimento; a janela é a consulta da seção 10.
# Consulta de recebimento
TABELA_RECEBIMENTO = "recebimento_" + uuid4().hex
recebimento = (
    eventos.agg(
        F.count("*").alias("eventos_recebidos"),
        F.min("instante").alias("primeiro_instante"),
        F.max("instante").alias("ultimo_instante"),
    )
    .writeStream.format("memory")
    .queryName(TABELA_RECEBIMENTO)
    .outputMode("complete")
    .option("checkpointLocation", str(PASTA_CHECKPOINT / "recebimento"))
    .start()
)
print("Consulta ativa?", recebimento.isActive)
print("Arquivos na entrada:", sorted(p.name for p in PASTA_ENTRADA.iterdir()))
spark.table(TABELA_RECEBIMENTO).show(truncate=False)

# %%
# 1º lote
primeiro_lote = gerar_eventos(30, INICIO_SIMULACAO)
publicar_lote(primeiro_lote)
display(pd.DataFrame(primeiro_lote).head(10))

# %%
# Recebimento do 1º lote
recebimento.processAllAvailable()
spark.table(TABELA_RECEBIMENTO).show(truncate=False)
print("Eventos por gênero no 1º lote:")
display(pd.DataFrame(primeiro_lote)["genero"].value_counts().rename("eventos").to_frame())

# %%
#> Encerra só a consulta de recebimento. eventos, a entrada (com o 1º lote) e o checkpoint da seção 10 continuam.
# Encerramento da consulta de recebimento
recebimento.stop()
spark.catalog.dropTempView(TABELA_RECEBIMENTO)
print("Consulta de recebimento ativa?", recebimento.isActive)
