# Arquivos de entrega

| Arquivo | Entrega | Como é gerado |
|---|---|---|
| `ra1-documentacao.docx` | Fonte do documento do RA1 | `python scripts/gerar_docx_ra1.py`, a partir de `documentacao/ra1/` e do template do professor |
| **`ra1-documentacao.pdf`** | **Entrega do RA1: o documento, sem o notebook** | O mesmo script, com LibreOffice; sem ele, exportado do `.docx` pelo Word ([ADR-0011](../docs/adr/0011-entregas-separadas-e-repositorio-da-entrega.md)) |
| `projeto_data_analytics.pdf` | Conferência local do notebook (não é o arquivo enviado) | `python scripts/exportar_notebook_pdf.py`. O PDF do RA2 é exportado no Colab a partir do repositório da entrega |

Não edite estes arquivos à mão: mudança de texto volta para a fonte e o arquivo é gerado de novo. Como cada um deve ficar: [orientações do documento final](../entregas/orientacoes-documento-final.md).
