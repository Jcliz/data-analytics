---
id: streaming-e-janelas
titulo: "Streaming e janelas temporais (RA2)"
tipo: base
status: vigente
atualizado: 2026-10-15
fontes: [6, 7, 8]
relacionados: [adr-0005, adr-0006]
---
# Streaming e janelas temporais (RA2)

## 1. O que o enunciado cobra

- Uma análise simples com Spark Structured Streaming: receber registros novos (reais ou simulados), aplicar **uma** agregação por janela temporal (tumbling **ou** sliding) e mostrar o resultado mudando com a chegada dos registros [Fato, fonte 6].
- Não precisa de dashboard, Kafka nem técnicas avançadas; não precisa refazer análises do RA1 [Fato, fonte 6].
- Critérios: processamento em streaming 3,0; janelas temporais 3,0; documentação e interpretação 2,0; demonstração 2,0 [Fato, fonte 6].

## 2. Conceitos das aulas

- **Stream como tabela sem fim:** `spark.readStream` cria um DataFrame em streaming; as transformações são as mesmas do batch (`filter`, `withColumn`, `groupBy`) [Fato, fonte 7].
- **Micro-lotes:** eventos que chegam num intervalo curto são processados juntos [Fato, fonte 7].
- **Modos de saída:** `append` (só linhas novas), `update` (só linhas que mudaram), `complete` (a tabela de resultado inteira a cada lote). As aulas usam `complete` com saída `memory` e leem a tabela com `spark.table(nome)` [Fato, fontes 7 e 8].
- **Por que `complete` + `memory` neste projeto:** com janela, `append` exige `withWatermark` e só emite janelas já fechadas, então a tabela ficaria vazia na demonstração; `format("console")` escreve no log do processo, e não na célula, e não aparece no PDF [Inferência, a partir das fontes 7 e 8]. Nem as aulas nem este projeto precisam de watermark ou de `trigger`.
- **Estado e checkpoint:** agregações contínuas guardam estado; `checkpointLocation` registra o progresso para recuperar de falhas [Fato, fonte 7].
- **Janela tumbling:** intervalos sem sobreposição, `window("instante", "5 minutes")`. **Sliding:** intervalos que se sobrepõem, `window("instante", "5 minutes", "2 minutes")` (duração 5, deslocamento 2) [Fato, fonte 8].

## 3. Padrão de simulação das aulas (cenário A)

1. Sessão local: `SparkSession.builder.master("local[2]")`, fuso `America/Sao_Paulo`, `.config("spark.sql.shuffle.partitions", "2")` e `spark.sparkContext.setLogLevel("ERROR")` [Fato, fontes 7 e 8]. Sem as 2 partições, cada lote da agregação usa 200 e fica lento no Colab [Inferência].
2. Pastas: uma de **entrada** (monitorada pelo Spark), uma de **publicação** (onde o arquivo é escrito antes) e uma de **checkpoint** [Fato, fonte 7].
3. Esquema explícito (`StructType`) e `timestampFormat` na leitura JSON [Fato, fonte 8].
4. Publicar um lote = escrever um arquivo JSON (uma linha por evento) na pasta de publicação e **mover** para a de entrada, para o Spark nunca ler um arquivo pela metade [Fato, fonte 8].
5. Depois de cada lote: `consulta.processAllAvailable()` e mostrar a tabela em memória ordenada pela janela, com o início e o fim da janela em colunas separadas: `spark.table(nome).select("window.start", "window.end", ...).orderBy("start").show(truncate=False)` [Fato, fontes 7 e 8].
6. Nome da consulta único por execução (a aula usa `uuid4().hex`), para reexecutar a seção sem o erro "query already active" [Fato, fonte 8].
7. Ao final: `consulta.stop()` e limpeza das pastas temporárias; o checkpoint é apagado junto com a entrada, porque um checkpoint antigo faz o Spark pular arquivos de mesmo nome [Fato, fonte 8].

## 4. Proposta para este projeto ([ADR-0005](../docs/adr/0005-ra2-cenario-a-simulacao.md))

- **Evento:** reprodução de uma faixa, `{id_evento, id_faixa, genero, artista, duracao_ouvida_s, instante}`.
- **Gerador (área B, seção 9):** sorteia faixas do conjunto preparado, com peso pelo `rank` (opcional), com semente fixa (`SEMENTE`) e instantes crescentes a partir de um instante fixo (`INICIO_SIMULACAO`), sem `datetime.now()`, para a execução final repetir os números das respostas. A seção 9 publica o 1º lote e mostra que ele foi recebido.
- **Divisão dos lotes:** 1º lote na seção 9 (recebimento), tabela da janela do 1º lote na seção 10 e pelo menos 2 lotes novos na seção 11, alguns eventos caindo em janelas já abertas (para mostrar a atualização). O encerramento fica numa última célula separada da seção 11.
- **Janela e agregação (área C):** por exemplo, contagem de reproduções por gênero em janela sliding de 5 min com deslocamento de 2 min; ou soma de minutos ouvidos por gênero em janela tumbling de 5 min.
- **Resultados (área D):** tabela depois de cada lote, comentando quais janelas mudaram e por quê.

---

## Ligações

- **Enunciado:** [enunciados/ra2.md](../enunciados/ra2.md) · **Material de aula:** [material-de-aula](material-de-aula.md)
