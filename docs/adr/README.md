---
id: adr-indice
titulo: "Decisões do projeto (ADRs)"
tipo: decisao-indice
status: vigente
atualizado: 2026-10-16
relacionados: [adr-0001, adr-0002, adr-0003, adr-0004, adr-0005, adr-0006, adr-0007, adr-0008, adr-0009, adr-0010]
---
# Decisões do projeto (ADRs)

> Uma decisão por arquivo. **As decisões prevalecem** sobre a base de conhecimento (`base/`) e sobre rascunhos; só os enunciados do professor (`enunciados/`) estão acima delas. Decisão nova: próximo número, mesmo formato (cabeçalho YAML, contexto, opções, decisão, consequências, ligações). Decisão que muda outra: a antiga passa a "substituída por ADR-NNNN".

**Status:** "aceita" = decidida pelo grupo; "proposta" = já orienta o trabalho, mas pode mudar até o grupo confirmar.

| ADR | Decisão | Status | Afeta |
|---|---|---|---|
| [0001](0001-fonte-de-dados-api-deezer.md) | Fonte de dados: API pública da Deezer | aceita | RA1, RA2 |
| [0002](0002-notebook-montado-por-secoes.md) | Notebook único montado por script a partir de um arquivo por seção | proposta | RA1, RA2 |
| [0003](0003-documento-ra1-gerado-do-template.md) | Documento do RA1 em Markdown, gerado no template `.docx`; PDF exportado do `.docx` | proposta | RA1 |
| [0004](0004-retrato-bruto-versionado.md) | Retrato bruto da API versionado; notebook lê dele por padrão | proposta | RA1, RA2 |
| [0005](0005-ra2-cenario-a-simulacao.md) | RA2 no cenário A, com eventos de reprodução simulados | proposta | RA2 |
| [0006](0006-ferramentas-e-ambiente.md) | pandas no RA1, PySpark 4.0.3 no RA2, Colab como ambiente de referência | proposta | RA1, RA2 |
| [0007](0007-commits-sem-coautoria-de-ia.md) | Nenhum commit com IA como coautora | aceita | todos |
| [0008](0008-divisao-em-quatro-areas.md) | Trabalho dividido em quatro áreas, uma por integrante | proposta | todos |
| [0009](0009-entrega-unica-em-pdf.md) | Entrega única: um PDF com o documento do RA1 e o notebook | aceita | RA1, RA2 |
| [0010](0010-problema-e-perguntas.md) | Problema e perguntas analíticas: perfil das faixas populares por gênero (P1 a P4) | proposta | RA1, RA2 |

---

## Ligações

- **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
- **Base de conhecimento:** [base/README.md](../../base/README.md)
- **Plano de tarefas:** [entregas/plano-de-tarefas.md](../../entregas/plano-de-tarefas.md)
