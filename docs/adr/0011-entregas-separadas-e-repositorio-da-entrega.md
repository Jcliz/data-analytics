---
id: adr-0011
titulo: "ADR-0011 — Documento do RA1 sem o notebook; PDF do notebook exportado no Colab do repositório da entrega"
tipo: decisao
decisao: "0011"
status: aceita
data: 2026-10-21
decisor: João Pedro Cardoso
entregas: [RA1, RA2]
areas: [A, B, C, D]
fontes: []
relacionados: [adr-0002, adr-0003, adr-0006, adr-0009]
---
# ADR-0011 — Documento do RA1 sem o notebook; PDF do notebook exportado no Colab do repositório da entrega

- **Status:** aceita · **Data:** 21/10/2026 · **Decisor:** João Pedro Cardoso · **Substitui:** [ADR-0009](0009-entrega-unica-em-pdf.md)

## Contexto

- O ADR-0009 juntava o documento do RA1 e o notebook num PDF único (`output/entrega-ra1-ra2.pdf`), enviado nas duas tarefas.
- Em 21/10/2026 o João pediu que o PDF da entrega do RA1 tenha só o documento, sem o notebook, e que o PDF do notebook seja exportado no Google Colab.
- O repositório citado no texto entregue passou a ser `https://github.com/eduardofabrii/data-analytics-ras`, enxuto: notebook, dados e `requirements.txt`. Este repositório (`Jcliz/data-analytics`) continua sendo o de desenvolvimento: seções do notebook, documento, scripts, issues e PRs.

## Decisão

1. **RA1:** o PDF do documento, `output/ra1-documentacao.pdf`, gerado do template (ADR-0003), sem o notebook. A capa e a seção 06 citam o repositório da entrega.
2. **RA2:** o PDF do notebook inteiro (identificação, RA1 e RA2) exportado no Colab a partir de `notebook/ra1-ra2-deezer.ipynb` do repositório da entrega.
3. **Notebook:** é montado aqui (`python scripts/montar_notebook.py`) e copiado igual para o repositório da entrega. A primeira célula de código da seção 2 clona o repositório da entrega no Colab.
4. O `scripts/montar_entrega.py` e o `output/entrega-ra1-ra2.pdf` saem do repositório. O notebook executado no Colab e o PDF dele ficam nos dois repositórios: aqui em `notebook/projeto_data_analytics.ipynb` e `output/projeto_data_analytics.pdf`, e no repositório da entrega em `notebook/ra1-ra2-deezer.ipynb` e `output/pdf/ra1-ra2-deezer.pdf`.

## Consequências

- O link do RA1 no Canvas (a tarefa só aceita URL) ainda precisa ser definido pelo grupo: o PDF do documento no repositório da entrega ou neste, na tag `entrega`.
- Qualquer mudança no notebook é feita aqui nas seções e copiada de novo para o repositório da entrega; os dois `.ipynb` ficam iguais.
- O texto entregue continua sem declaração de uso de IA (critério X.7) e sem citar a organização interna (critério X.9).

---

## Ligações

- **Substitui:** [ADR-0009](0009-entrega-unica-em-pdf.md)
- **Notebook:** [ADR-0002](0002-notebook-montado-por-secoes.md) · **Documento do RA1:** [ADR-0003](0003-documento-ra1-gerado-do-template.md)
- **Orientações:** [orientacoes-documento-final](../../entregas/orientacoes-documento-final.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
