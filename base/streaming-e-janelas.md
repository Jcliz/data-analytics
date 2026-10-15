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
- **Modos de saída:** `append` (só linhas novas), `update` (só linhas que mudaram), `complete` (a tabela de resultado inteira a cada lote). As aulas usam `complete` com saída `memory` e consultam a tabela com `spark.sql` [Fato, fontes 7 e 8].
- **Estado e checkpoint:** agregações contínuas guardam estado; `checkpointLocation` registra o progresso para recuperar de falhas [Fato, fonte 7].
- **Janela tumbling:** intervalos sem sobreposição, `window("instante", "5 minutes")`. **Sliding:** intervalos que se sobrepõem, `window("instante", "5 minutes", "2 minutes")` (duração 5, deslocamento 2) [Fato, fonte 8].

## 3. Padrão de simulação das aulas (cenário A)

1. Sessão local: `SparkSession.builder.master("local[2]")`, fuso `America/Sao_Paulo` [Fato, fonte 8].
2. Pastas: uma de **entrada** (monitorada pelo Spark), uma de **publicação** (onde o arquivo é escrito antes) e uma de **checkpoint** [Fato, fonte 7].
3. Esquema explícito (`StructType`) e `timestampFormat` na leitura JSON [Fato, fonte 8].
4. Publicar um lote = escrever um arquivo JSON (uma linha por evento) na pasta de publicação e **mover** para a de entrada, para o Spark nunca ler um arquivo pela metade [Fato, fonte 8].
5. Depois de cada lote: `consulta.processAllAvailable()` e mostrar a tabela em memória ordenada pela janela.
6. Ao final: `consulta.stop()` e limpeza das pastas temporárias [Fato, fonte 8].

## 4. Proposta para este projeto ([ADR-0005](../docs/adr/0005-ra2-cenario-a-simulacao.md))

- **Evento:** reprodução de uma faixa, `{id_evento, id_faixa, genero, artista, duracao_ouvida_s, instante}`.
- **Gerador (área B):** sorteia faixas do conjunto preparado, com peso pelo `rank` (opcional), e instantes crescentes; publica em 3 a 5 lotes, cada um com alguns eventos, alguns caindo em janelas já abertas (para mostrar a atualização).
- **Janela e agregação (área C):** por exemplo, contagem de reproduções por gênero em janela sliding de 5 min com deslocamento de 2 min; ou soma de minutos ouvidos por gênero em janela tumbling de 5 min.
- **Resultados (área D):** tabela depois de cada lote, comentando quais janelas mudaram e por quê.

---

## Ligações

- **Enunciado:** [enunciados/ra2.md](../enunciados/ra2.md) · **Material de aula:** [material-de-aula](material-de-aula.md)
