"""Exporta o notebook executado em PDF (parte 2 do PDF único), quebrando as linhas longas em vez de cortá-las.

Uso: python scripts/exportar_notebook_pdf.py [--notebook N.ipynb] [--saida S.pdf]
     Padrões: notebook/projeto_data_analytics.ipynb e output/projeto_data_analytics.pdf

Faz o mesmo que `jupyter nbconvert --to webpdf` (HTML do JupyterLab impresso pelo Chromium do playwright),
com dois ajustes para nada sair cortado no PDF (critério X.5): código e saídas em texto quebram a linha na
margem, e tabela mais larga que a página vira blocos de colunas empilhados, com o índice repetido em cada um.
Na primeira vez, baixa o Chromium (`--allow-chromium-download` do nbconvert).
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
  /* Largura útil do papel Carta (8,5 pol menos as margens do Chromium): o layout da tela vira o da impressão. */
  html, body { width: 7.6in !important; max-width: 7.6in !important; }
  .bloco-colunas { margin: 0.2em 0 0.1em; font-size: 0.85em; color: #555; }
</style>
"""

# Tabela que não cabe na largura vira blocos de colunas empilhados, com a coluna de índice repetida em cada um.
DIVIDE_TABELAS = """
<script>
document.addEventListener('DOMContentLoaded', () => {
  for (const tabela of [...document.querySelectorAll('.jp-OutputArea-output table')]) {
    const area = tabela.closest('.jp-OutputArea-output');
    const disponivel = area.clientWidth - 8;
    if (tabela.scrollWidth <= disponivel) continue;
    const linhas = [...tabela.rows];
    const total = Math.max(...linhas.map(l => l.cells.length));
    const modelo = linhas.find(l => l.cells.length === total);
    const larguras = [...modelo.cells].map(c => c.getBoundingClientRect().width);
    const grupos = [];
    let grupo = [], soma = larguras[0];
    for (let i = 1; i < total; i++) {
      if (grupo.length && soma + larguras[i] > disponivel) { grupos.push(grupo); grupo = []; soma = larguras[0]; }
      grupo.push(i); soma += larguras[i];
    }
    if (grupo.length) grupos.push(grupo);
    const fragmento = document.createDocumentFragment();
    for (const g of grupos) {
      const rotulo = document.createElement('div');
      rotulo.className = 'bloco-colunas';
      rotulo.textContent = `colunas ${g[0]} a ${g[g.length - 1]} de ${total - 1}`;
      const copia = tabela.cloneNode(true);
      for (const linha of [...copia.rows]) {
        [...linha.cells].forEach((celula, i) => { if (i > 0 && !g.includes(i)) celula.remove(); });
      }
      fragmento.append(rotulo, copia);
    }
    tabela.replaceWith(fragmento);
  }
});
</script>
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--notebook', type=Path, default=RAIZ / 'notebook' / 'projeto_data_analytics.ipynb')
    ap.add_argument('--saida', type=Path, default=RAIZ / 'output' / 'projeto_data_analytics.pdf')
    args = ap.parse_args()

    notebook = nbformat.read(args.notebook, as_version=4)
    html, _ = HTMLExporter(template_name='lab').from_notebook_node(notebook)
    html = html.replace('</head>', QUEBRA_DE_LINHA + '</head>', 1).replace('</body>', DIVIDE_TABELAS + '</body>', 1)

    exportador = WebPDFExporter(allow_chromium_download=True)
    pdf = exportador.run_playwright(html)
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_bytes(pdf)
    print(f'gravado: {args.saida}')


if __name__ == '__main__':
    main()
