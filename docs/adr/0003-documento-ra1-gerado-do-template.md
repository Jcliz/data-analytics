---
id: adr-0003
titulo: "ADR-0003 — Documento do RA1 em Markdown, gerado no template .docx"
tipo: decisao
decisao: "0003"
status: proposta
data: 2026-10-15
decisor: proposta para o grupo
entregas: [RA1]
areas: [A, B, C, D]
fontes: [3, 5]
relacionados: [adr-0002]
---
# ADR-0003 — Documento do RA1 em Markdown, gerado no template `.docx`

- **Status:** proposta · **Data:** 15/10/2026

## Contexto

- O RA1 pede a "documentação de todo o processo analítico" no `Template_RA1_Data_Analytics.docx` [Fato, fonte 3]. O template tem capa, sete seções ("RA1 / 01" a "RA1 / 07"), campos rotulados e tabelas com cabeçalho próprio [Fato, fonte 5].
- No projeto de Especificação de Software, o grupo escreveu em Markdown no repositório e montou o `.docx` por script, o que evitou conflito e manteve o histórico.

## Opções consideradas

- **(a)** Editar o `.docx` direto, compartilhado (OneDrive).
- **(b)** Markdown por seção no repositório + script que preenche o próprio template e gera o `.docx`; o PDF é exportado do `.docx`.

## Decisão

**(b).** Cada seção do template tem um arquivo em `documentacao/ra1/` com os mesmos títulos. `python scripts/gerar_docx_ra1.py` abre o template, preenche capa, campos, textos e tabelas, remove as notas de orientação em cinza e grava `output/ra1-documentacao.docx`; com o LibreOffice instalado, grava também o PDF.

## Consequências

- O visual é o do template do professor (capa, cores, cabeçalho e rodapé), porque o script escreve dentro dele.
- Blocos que o template manda duplicar (decisões de limpeza D1…Dn) são duplicados pelo script, um por bloco do Markdown.
- Ajuste fino (quebra de página, largura de tabela) pode ser feito no `.docx` gerado, desde que o conteúdo volte para o Markdown.
- O PDF final é gerado do `.docx` (no Word: *Arquivo → Exportar → PDF*; ou pelo script, com o LibreOffice).
- Esse PDF é a entrega do RA1 no Canvas, com a URL do repositório na capa (decisão do João, 15/10/2026).

---

## Ligações

- **Orientações do PDF:** [orientacoes-documento-final](../../entregas/orientacoes-documento-final.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
