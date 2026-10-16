# Arquivos de entrega

| Arquivo | Entrega | Como é gerado |
|---|---|---|
| `ra1-documentacao.docx` | Fonte da parte 1 | `python scripts/gerar_docx_ra1.py`, a partir de `documentacao/ra1/` e do template do professor |
| `ra1-documentacao.pdf` | Parte 1: documento do RA1 | O mesmo script, com LibreOffice; sem ele, exportado do `.docx` pelo Word |
| `projeto_data_analytics.pdf` | Parte 2: notebook (RA1 e RA2) | Notebook inteiro executado, exportado em PDF (Colab: *Arquivo → Imprimir → Salvar como PDF*; local: `jupyter nbconvert --to webpdf --allow-chromium-download`) |
| **`entrega-ra1-ra2.pdf`** | **Entrega: o arquivo no RA2 e o link dele no RA1** | `python scripts/montar_entrega.py`, que junta as partes 1 e 2 ([ADR-0009](../docs/adr/0009-entrega-unica-em-pdf.md)) |

Não edite estes arquivos à mão: mudança de texto volta para a fonte e o arquivo é gerado de novo. Como cada um deve ficar: [orientações do documento final](../entregas/orientacoes-documento-final.md).
