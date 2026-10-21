---
id: adr-0009
titulo: "ADR-0009 — Entrega única: um PDF com o documento do RA1 e o notebook"
tipo: decisao
decisao: "0009"
status: substituída
data: 2026-10-15
decisor: João Pedro Cardoso
entregas: [RA1, RA2]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0002, adr-0003, adr-0011]
---
# ADR-0009 — Entrega única: um PDF com o documento do RA1 e o notebook

- **Status:** substituída pelo [ADR-0011](0011-entregas-separadas-e-repositorio-da-entrega.md) em 21/10/2026 · **Data:** 15/10/2026 · **Decisor:** João Pedro Cardoso

## Contexto

- O enunciado do RA1 pede o notebook `.ipynb` com todas as células executadas e o documento no template `Template_RA1_Data_Analytics.docx` ([enunciados/ra1.md](../../enunciados/ra1.md), "Entrega").
- O enunciado do RA2 pede o PDF do notebook com as seções do RA1 e do RA2 organizadas ([enunciados/ra2.md](../../enunciados/ra2.md), seção 3).
- O grupo vai enviar o RA1 e o RA2 no mesmo arquivo (João, 15/10/2026).
- A tarefa do RA1 no Canvas só aceita uma URL (campo "Insira o URL da web"); a do RA2 recebe um arquivo PDF [Fato, RA1.pdf p. 3 e RA2.pdf].

## Opções

- **(a)** Um PDF com o documento do RA1 e, em seguida, o notebook executado (RA1 e RA2).
- **(b)** Um PDF só do notebook; o documento do template fica apenas no repositório.
- **(c)** Dois PDFs: o documento no RA1 e o notebook no RA2.

## Decisão

**(a).** O arquivo enviado nas duas tarefas do Canvas é `output/entrega-ra1-ra2.pdf`, montado por `python scripts/montar_entrega.py` nesta ordem:

1. documento do RA1 (`output/ra1-documentacao.pdf`, gerado do template), com a URL do repositório na capa;
2. notebook executado (`output/projeto_data_analytics.pdf`), com a identificação e as seções do RA1 e do RA2.

## Consequências

- O mesmo PDF vai nas duas tarefas: no RA2, o arquivo; no RA1, que só aceita URL, o link do mesmo arquivo no repositório, na tag `entrega`: `https://github.com/Jcliz/data-analytics/blob/entrega/output/entrega-ra1-ra2.pdf`. Por isso o PDF único é versionado em `output/`.
- As duas partes continuam sendo geradas como antes (ADR-0002 e ADR-0003); o script só as junta e põe um marcador para cada parte.
- O script avisa quando uma parte foi gerada antes da última mudança na sua fonte; nesse caso, gere a parte de novo antes de juntar.
- O PDF único segue as orientações das duas partes e não tem declaração de uso de IA (critério X.7).

---

## Ligações

- **Orientações do PDF:** [orientacoes-documento-final](../../entregas/orientacoes-documento-final.md)
- **Notebook:** [ADR-0002](0002-notebook-montado-por-secoes.md) · **Documento do RA1:** [ADR-0003](0003-documento-ra1-gerado-do-template.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
