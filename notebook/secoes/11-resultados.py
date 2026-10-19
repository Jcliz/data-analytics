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
# Preparação da comparação entre lotes
from datetime import datetime
from pyspark.sql import functions as F

if not consulta.isActive:
    raise RuntimeError("Execute as seções 9 e 10 antes de demonstrar os novos lotes.")


def ler_resultados_janelas():
    """Espera os arquivos disponíveis e copia o resultado atual para comparação."""
    consulta.processAllAvailable()
    return (
        spark.table(TABELA_JANELAS)
        .select(
            F.col("window.start").alias("inicio"),
            F.col("window.end").alias("fim"),
            "genero", "reproducoes",
        )
        .orderBy("inicio", F.desc("reproducoes"), "genero")
        .toPandas()
    )


resultados_atuais = ler_resultados_janelas()
lotes_demonstrados = [primeiro_lote]


def publicar_proximo_lote(quantidade=30):
    """Publica novas reproduções e mostra o resultado completo e as mudanças por janela."""
    global resultados_atuais
    if not consulta.isActive:
        raise RuntimeError("A consulta foi encerrada. Execute novamente as seções 9 e 10.")
    if not isinstance(quantidade, int) or quantidade <= 0:
        raise ValueError("A quantidade de eventos deve ser um inteiro positivo.")

    anteriores = resultados_atuais
    inicio = datetime.strptime(lotes_demonstrados[-1][-1]["instante"], FORMATO_INSTANTE)
    novo_lote = gerar_eventos(quantidade, inicio)
    publicar_lote(novo_lote)
    atuais = ler_resultados_janelas()

    chaves = ["inicio", "fim", "genero"]
    mudancas = atuais.merge(
        anteriores, on=chaves, how="outer", suffixes=("_depois", "_antes")
    ).fillna({"reproducoes_antes": 0, "reproducoes_depois": 0})
    for coluna in ("reproducoes_antes", "reproducoes_depois"):
        mudancas[coluna] = mudancas[coluna].astype("int64")
    mudancas["novas_reproducoes"] = mudancas["reproducoes_depois"] - mudancas["reproducoes_antes"]
    assert mudancas["novas_reproducoes"].ge(0).all(), "Uma contagem anterior diminuiu."
    assert int(mudancas["novas_reproducoes"].sum()) == len(novo_lote), "O lote não foi contado integralmente."

    lotes_demonstrados.append(novo_lote)
    total_esperado = sum(len(lote) for lote in lotes_demonstrados)
    total_recebido = int(atuais["reproducoes"].sum())
    assert total_recebido == total_esperado, "Total recebido diferente dos lotes publicados."

    resumo = mudancas.groupby(["inicio", "fim"], as_index=False)[
        ["reproducoes_antes", "novas_reproducoes", "reproducoes_depois"]
    ].sum()
    print(f"Após o lote {len(lotes_demonstrados)}: {total_recebido} reproduções recebidas.")
    with pd.option_context("display.max_rows", None):
        print("Contagens por gênero e janela:")
        display(atuais)
        print("Mudanças por janela (início incluído, fim excluído):")
        display(resumo)
    resultados_atuais = atuais
    return novo_lote

# %%
# Segundo lote: atualização de uma janela existente e abertura de novos intervalos
segundo_lote = publicar_proximo_lote()
resultados_apos_segundo_lote = resultados_atuais.copy()

# %%
# Terceiro lote: novas reproduções e comparação das contagens acumuladas
terceiro_lote = publicar_proximo_lote()
resultados_apos_terceiro_lote = resultados_atuais.copy()

# %% [markdown]
# **Resposta do grupo:**
#
# As células “Segundo lote: atualização de uma janela existente e abertura de novos intervalos”
# e “Terceiro lote: novas reproduções e comparação das contagens acumuladas” publicam mais
# 30 eventos cada, em momentos distintos, e mostram a tabela após o processamento.
# Com os 30 eventos do primeiro lote, o total recebido passa de 30 para 60 e depois para 90.
#
# O segundo lote acrescenta 3 reproduções em 10:05–10:10 (de 14 para 17), 18 em
# 10:10–10:15 e 9 em 10:15–10:20. O terceiro acrescenta 7 em 10:15–10:20
# (de 9 para 16), 17 em 10:20–10:25 e 6 em 10:25–10:30. A janela 10:00–10:05
# mantém suas 16 reproduções, pois nenhum evento dos dois novos lotes pertence a esse intervalo.
# Essas contagens são apresentadas nos resumos “Mudanças por janela” das duas células.
#
# As janelas são atribuídas pelo instante de cada evento, não pelo horário em que o arquivo
# foi publicado. Assim, uma janela já exibida recebe novas contagens quando chegam eventos
# cujo instante ainda pertence a ela. A tabela por gênero permite comparar quais gêneros
# concentram as reproduções em cada intervalo; os valores representam uma simulação com
# semente fixa, e não a audiência real da Deezer.

# %% [markdown]
# **Demonstração ao vivo:** antes de executar a célula de encerramento, execute
# `publicar_proximo_lote(10)` em uma célula de código para publicar mais dez eventos
# e mostrar as mudanças. A função continua a sequência de IDs e instantes do lote anterior.
# Para repetir a demonstração desde o começo, execute novamente as seções 9, 10 e 11.

# %%
# Encerramento da consulta e limpeza das subpastas da simulação
import shutil

consulta.stop()
spark.catalog.dropTempView(TABELA_JANELAS)
for pasta in (PASTA_ENTRADA, PASTA_PUBLICACAO, PASTA_CHECKPOINT):
    destino = pasta.resolve()
    if destino.parent != (RAIZ / "dados" / "streaming").resolve():
        raise ValueError(f"Pasta fora do diretório da simulação: {destino}")
    if destino.exists():
        shutil.rmtree(destino)
print("Consulta ativa após o encerramento?", consulta.isActive)
print("Subpastas de entrada, publicação e checkpoint removidas; README preservado.")
