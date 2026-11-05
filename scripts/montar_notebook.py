"""Monta o notebook entregue a partir das seções em notebook/secoes/ (ADR-0002).

Uso: python scripts/montar_notebook.py [--ra3] [--saida CAMINHO]
     Saída padrão: notebook/projeto_data_analytics.ipynb (RA1 e RA2, de notebook/secoes/).
     Com --ra3: notebook/ra3-deezer.ipynb, o notebook próprio do RA3, de notebook/secoes-ra3/ (ADR-0012).
     Sem saídas; execute depois no Colab ou com nbconvert.

Cada seção é um arquivo .py no formato percent: "# %%" abre célula de código e "# %% [markdown]" abre
célula de texto (cada linha de texto começa com "# "). Os arquivos entram em ordem alfabética.
Orientações não vão para o notebook: linhas que começam com "#>" (em código e em texto) e comentários <!-- --> no texto.
Célula de código que fica vazia depois disso é descartada.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SECOES = RAIZ / 'notebook' / 'secoes'
SAIDA = RAIZ / 'notebook' / 'projeto_data_analytics.ipynb'
SECOES_RA3 = RAIZ / 'notebook' / 'secoes-ra3'
SAIDA_RA3 = RAIZ / 'notebook' / 'ra3-deezer.ipynb'
INICIO = re.compile(r'^# %%(?P<md> \[markdown\])?.*$')


def celulas(arquivo):
    """Lê um arquivo percent e devolve [(tipo, texto)]."""
    atual, saida = None, []
    for linha in arquivo.read_text(encoding='utf-8').splitlines():
        m = INICIO.match(linha)
        if m:
            atual = ['markdown' if m.group('md') else 'code', []]
            saida.append(atual)
        elif atual is not None:
            atual[1].append(linha)
    resultado = []
    for tipo, linhas in saida:
        linhas = [l for l in linhas if not l.lstrip().startswith('#>')]
        if tipo == 'markdown':
            texto = '\n'.join(re.sub(r'^# ?', '', l) if l.startswith('#') else l for l in linhas)
            texto = re.sub(r'\n?<!--.*?-->', '', texto, flags=re.S)
        else:
            texto = '\n'.join(linhas)
        texto = texto.strip('\n')
        if texto.strip():
            resultado.append((tipo, texto))
    return resultado


def notebook(arquivos):
    cells = []
    for arquivo in arquivos:
        for i, (tipo, texto) in enumerate(celulas(arquivo)):
            linhas = texto.split('\n')
            cell = {
                'cell_type': tipo,
                'id': hashlib.sha1(f'{arquivo.name}:{i}'.encode()).hexdigest()[:8],
                'metadata': {},
                'source': [l + '\n' for l in linhas[:-1]] + [linhas[-1]],
            }
            if tipo == 'code':
                cell.update(execution_count=None, outputs=[])
            cells.append(cell)
    return {
        'cells': cells,
        'metadata': {
            'colab': {'provenance': []},
            'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
            'language_info': {'name': 'python'},
        },
        'nbformat': 4,
        'nbformat_minor': 5,
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--ra3', action='store_true', help='monta o notebook do RA3 (notebook/secoes-ra3/)')
    ap.add_argument('--saida', type=Path)
    args = ap.parse_args()
    secoes, padrao = (SECOES_RA3, SAIDA_RA3) if args.ra3 else (SECOES, SAIDA)
    args.saida = args.saida or padrao
    arquivos = sorted(secoes.glob('*.py'))
    nb = notebook(arquivos)
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    codigo = sum(c['cell_type'] == 'code' for c in nb['cells'])
    print(f'{args.saida.relative_to(RAIZ)}: {len(arquivos)} seções, {len(nb["cells"])} células ({codigo} de código)')


if __name__ == '__main__':
    main()
