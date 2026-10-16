---
id: material-de-aula
titulo: "Material de aula: resumo e onde cada um ajuda"
tipo: base
status: vigente
atualizado: 2026-10-15
fontes: [7, 8, 9, 10, 11, 12]
relacionados: [qualidade-de-dados, streaming-e-janelas]
---
# Material de aula: resumo e onde cada um ajuda

> Os arquivos originais (PDFs e notebooks) estão no contexto do projeto, fora do repositório. Este resumo diz o que cada um traz e para qual tarefa serve.

| Material | O que traz | Ajuda em |
|---|---|---|
| *Fundamentals of Data Analytics* (slides) [12] | Estrutura da disciplina (RA1 ingestão e preparação; RA2 transformação e streaming; RA3 análise e visualização); quatro tipos de análise (descritiva, diagnóstica, preditiva, prescritiva); dados estruturados, semiestruturados (JSON) e não estruturados | Problema e perguntas (A): perguntas descritivas e diagnósticas cabem bem |
| *Data Ingestion and Data Quality* (slides + notebook Titanic) [10] | Ingestão batch × streaming; problemas comuns de qualidade; ciclo carregar → conhecer → inspecionar → identificar → decidir → transformar → validar; tabelas de diagnóstico, decisões e validação em pandas | Ingestão (B), qualidade (C), limpeza (D). O notebook é o modelo de estilo: uma tabela de problemas, uma de decisões e uma de validações |
| *From Data Preparation to Data Transformation* (slides) + *Data Transformation* (notebook) [11] | Limpeza × transformação; criar variáveis, agregar, `merge`, formatos long e wide; "transformações começam com perguntas" | Seção 5 do notebook (D): só transformações de preparo no RA1 |
| *Apache Spark for Data Analytics* (slides + notebook) [9] | pandas × Spark; DataFrame, transformações × ações, avaliação preguiçosa, Spark SQL, partições | RA2 (B, C) |
| *Spark Structured Streaming* (slides + notebook e-commerce) [7] | `readStream`/`writeStream`, micro-lotes, modos de saída, estado, checkpoint; vendas chegando uma por vez numa pasta monitorada | RA2, seção 9 (B) |
| *Sliding Windows* (slides + notebook) [8] | Tumbling × sliding, `window(ts, duração, deslocamento)`, publicação de lotes por arquivo e leitura da tabela em memória | RA2, seções 10 e 11 (C, D) |

---

## Ligações

- **Qualidade:** [qualidade-de-dados](qualidade-de-dados.md) · **Streaming:** [streaming-e-janelas](streaming-e-janelas.md) · **Fontes:** [fontes](fontes.md)
