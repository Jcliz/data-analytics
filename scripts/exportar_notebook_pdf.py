"""Exporta o notebook executado em PDF (parte 2 do PDF único), quebrando as linhas longas em vez de cortá-las.

Uso: python scripts/exportar_notebook_pdf.py [--notebook N.ipynb] [--saida S.pdf]
     Padrões: notebook/projeto_data_analytics.ipynb e output/projeto_data_analytics.pdf

Faz o mesmo que `jupyter nbconvert --to webpdf` (HTML do JupyterLab impresso pelo Chromium do playwright),
com uma regra de estilo a mais: código e saídas em texto quebram a linha na margem, para nada sair cortado
no PDF (critério X.5). Na primeira vez, baixa o Chromium (`--allow-chromium-download` do nbconvert).
"""
import argparse
from pathlib import Path

import nbformat
from nbconvert import HTMLExporter, WebPDFExporter

RAIZ = Path(__file__).resolve().parent.parent

QUEBRA_DE_LINHA = """
<style>
  pre, .jp-InputArea-editor pre, .jp-OutputArea-output pre, .highlight pre {
    white-space: pre-wrap !important;
    overflow-wrap: anywhere !important;
  }
</style>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--notebook', type=Path, default=RAIZ / 'notebook' / 'projeto_data_analytics.ipynb')
    ap.add_argument('--saida', type=Path, default=RAIZ / 'output' / 'projeto_data_analytics.pdf')
    args = ap.parse_args()

    notebook = nbformat.read(args.notebook, as_version=4)
    html, _ = HTMLExporter(template_name='lab').from_notebook_node(notebook)
    html = html.replace('</head>', QUEBRA_DE_LINHA + '</head>', 1)

    exportador = WebPDFExporter(allow_chromium_download=True)
    pdf = exportador.run_playwright(html)
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_bytes(pdf)
    print(f'gravado: {args.saida}')


if __name__ == '__main__':
    main()
