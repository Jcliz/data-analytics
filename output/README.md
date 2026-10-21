# Arquivos de entrega

| Arquivo | Entrega | Como é gerado |
|---|---|---|
| `ra1-documentacao.docx` | Fonte do documento do RA1 | `python scripts/gerar_docx_ra1.py`, a partir de `documentacao/ra1/` e do template do professor |
| `ra1-documentacao.pdf` | Documento do RA1, sem o notebook | O mesmo script, com LibreOffice; sem ele, exportado do `.docx` pelo Word ([ADR-0011](../docs/adr/0011-entregas-separadas-e-repositorio-da-entrega.md)) |
| `projeto_data_analytics.pdf` | Notebook executado no Colab | PDF do notebook executado no Google Colab a partir do repositório da entrega (o mesmo arquivo está em `output/pdf/ra1-ra2-deezer.pdf` de lá). Para conferir localmente: `python scripts/exportar_notebook_pdf.py` |
| **`entrega-ra1.docx`**, **`entrega-ra1.pdf`** | **Entrega do RA1:** só o documento | `python scripts/montar_entregas.py` |
| **`entrega-ra2.docx`**, **`entrega-ra2.pdf`** | **Entrega do RA2:** o documento do RA1 seguido do notebook executado | `python scripts/montar_entregas.py` (no `.docx`, as páginas do notebook entram como imagens) |

Não edite estes arquivos à mão: mudança de texto volta para a fonte e o arquivo é gerado de novo. Como cada um deve ficar: [orientações do documento final](../entregas/orientacoes-documento-final.md).
