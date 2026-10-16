---
id: adr-0002
titulo: "ADR-0002 — Notebook único montado por script a partir de um arquivo por seção"
tipo: decisao
decisao: "0002"
status: proposta
data: 2026-10-15
decisor: proposta para o grupo
entregas: [RA1, RA2]
areas: [A, B, C, D]
fontes: [3, 4]
relacionados: [adr-0008]
---
# ADR-0002 — Notebook único montado por script a partir de um arquivo por seção

- **Status:** proposta · **Data:** 15/10/2026

## Contexto

- O RA1 exige o `.ipynb` com todas as células executadas; o RA2 exige o PDF do notebook com as seções do RA1 e do RA2. O professor deu um template de notebook único (`modelos/template_projeto_data_analytics.ipynb`) que já tem as seções 1 a 12 [Fato, fonte 4]. O PDF do notebook é a segunda parte do PDF único enviado nas duas entregas ([ADR-0009](0009-entrega-unica-em-pdf.md)).
- Um `.ipynb` é um JSON grande. Quatro pessoas editando o mesmo arquivo geram conflito de merge difícil de resolver, e o diff não é legível na revisão do PR.

## Opções consideradas

- **(a)** Todos editam o mesmo `.ipynb`, um de cada vez.
- **(b)** Cada pessoa tem o seu notebook, e alguém cola tudo no final.
- **(c)** Cada seção do template vira um arquivo `.py` no formato *percent* (`# %%`), dono de uma área; um script monta o notebook na ordem do template.

## Decisão

**(c).** As seções ficam em `notebook/secoes/`, uma por arquivo, e `python scripts/montar_notebook.py` gera `notebook/projeto_data_analytics.ipynb`. Os enunciados do professor são mantidos como células Markdown, e as respostas do grupo substituem o `[Preencha aqui.]`.

## Consequências

- Cada área edita só os seus arquivos; o PR mostra um diff de texto simples.
- Os arquivos *percent* rodam célula a célula no VS Code, PyCharm ou Spyder, e também são lidos pelo `jupytext`, se alguém preferir.
- O notebook entregue é **gerado** e precisa ser executado do início ao fim (no Colab ou com `jupyter nbconvert --execute`) antes da entrega. A execução final é uma tarefa geral do plano.
- A numeração das seções segue o template do professor, que pula a seção 6; não renumeramos.
- As variáveis compartilhadas entre seções seguem o contrato do `CONTEXT.md`, seção 6.

---

## Ligações

- **Plano:** [plano-de-tarefas](../../entregas/plano-de-tarefas.md) · **Orientações do PDF:** [orientacoes-documento-final](../../entregas/orientacoes-documento-final.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
