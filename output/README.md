# Arquivos de entrega

| Arquivo | Entrega | Como é gerado |
|---|---|---|
| `ra1-documentacao.docx` | RA1 | `python scripts/gerar_docx_ra1.py`, a partir de `documentacao/ra1/` e do template do professor |
| `ra1-documentacao.pdf` | RA1 | O mesmo script, com LibreOffice; sem ele, exportado do `.docx` pelo Word |
| `projeto_data_analytics.pdf` | RA2 | Notebook inteiro executado, exportado em PDF (Colab: *Arquivo → Imprimir → Salvar como PDF*; local: `jupyter nbconvert --to webpdf`) |

Não edite estes arquivos à mão: mudança de texto volta para a fonte e o arquivo é gerado de novo. Como cada um deve ficar: [orientações do documento final](../entregas/orientacoes-documento-final.md).
