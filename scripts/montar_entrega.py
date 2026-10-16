"""Junta o documento do RA1 e o notebook num PDF único, enviado nas duas tarefas do Canvas (ADR-0009).

Uso: python scripts/montar_entrega.py [--documento D.pdf] [--notebook N.pdf] [--saida S.pdf]
     Padrões: output/ra1-documentacao.pdf, output/projeto_data_analytics.pdf, output/entrega-ra1-ra2.pdf
Precisa de pypdf (pip install pypdf).

Ordem do arquivo: primeiro o documento do RA1 (capa com a URL do repositório e seções RA1 / 01 a 07),
depois o notebook executado (identificação, RA1 e RA2). Cada parte vira um marcador no leitor de PDF.
Antes de juntar, o script avisa se alguma parte está mais velha que a sua fonte (gerada antes da última mudança).
"""
import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

RAIZ = Path(__file__).resolve().parent.parent
TITULO = 'Projeto Data Analytics — RA1 e RA2'
EQUIPE = 'Eduardo Fabri, João Correa, Rodrigo Alves e João Pedro Cardoso'  # CONTEXT.md, seção 1


def desatualizado(pdf, fontes):
    """Fontes alteradas depois que o PDF foi gerado."""
    return [f for f in fontes if f.exists() and f.stat().st_mtime > pdf.stat().st_mtime]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--documento', type=Path, default=RAIZ / 'output' / 'ra1-documentacao.pdf')
    ap.add_argument('--notebook', type=Path, default=RAIZ / 'output' / 'projeto_data_analytics.pdf')
    ap.add_argument('--saida', type=Path, default=RAIZ / 'output' / 'entrega-ra1-ra2.pdf')
    args = ap.parse_args()

    partes = [
        ('Documento do RA1', args.documento, sorted((RAIZ / 'documentacao' / 'ra1').glob('*.md')),
         'gere com: python scripts/gerar_docx_ra1.py (ou exporte o .docx pelo Word)'),
        ('Notebook (RA1 e RA2)', args.notebook, [RAIZ / 'notebook' / 'projeto_data_analytics.ipynb'],
         'exporte o notebook executado em PDF (orientações do documento final, seção 3)'),
    ]
    faltando = [(nome, pdf, como) for nome, pdf, _, como in partes if not pdf.exists()]
    for nome, pdf, como in faltando:
        print(f'erro: falta {nome}: {pdf} ({como})')
    if faltando:
        sys.exit(1)

    escritor = PdfWriter()
    for nome, pdf, fontes, _ in partes:
        for fonte in desatualizado(pdf, fontes):
            print(f'aviso: {fonte.relative_to(RAIZ)} mudou depois de {pdf.name}; gere o PDF de novo')
        inicio = len(escritor.pages)
        leitor = PdfReader(pdf)
        for pagina in leitor.pages:
            escritor.add_page(pagina)
        escritor.add_outline_item(nome, inicio)
        print(f'{nome}: {len(leitor.pages)} página(s), a partir da página {inicio + 1}')

    escritor.add_metadata({'/Title': TITULO, '/Author': EQUIPE})
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    with open(args.saida, 'wb') as saida:
        escritor.write(saida)
    print(f'gravado: {args.saida} ({len(escritor.pages)} páginas)')


if __name__ == '__main__':
    main()
