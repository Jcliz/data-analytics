"""Monta o notebook entregue a partir das seções em notebook/secoes/ (ADR-0002).

Uso: python scripts/montar_notebook.py [--saida CAMINHO]
     Saída padrão: notebook/projeto_data_analytics.ipynb (sem saídas; execute depois no Colab ou com nbconvert).

Cada seção é um arquivo .py no formato percent: "# %%" abre célula de código e "# %% [markdown]" abre
célula de texto (cada linha de texto começa com "# "). Os arquivos entram em ordem alfabética.
Orientações não vão para o notebook: linhas de código que começam com "#>" e comentários <!-- --> no texto.
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
        if tipo == 'markdown':
            texto = '\n'.join(re.sub(r'^# ?', '', l) if l.startswith('#') else l for l in linhas)
            texto = re.sub(r'\n?<!--.*?-->', '', texto, flags=re.S)
        else:
            texto = '\n'.join(l for l in linhas if not l.lstrip().startswith('#>'))
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
    ap.add_argument('--saida', type=Path, default=SAIDA)
    args = ap.parse_args()
    arquivos = sorted(SECOES.glob('*.py'))
    nb = notebook(arquivos)
    args.saida.parent.mkdir(parents=True, exist_ok=True)
    args.saida.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    codigo = sum(c['cell_type'] == 'code' for c in nb['cells'])
    print(f'{args.saida.relative_to(RAIZ)}: {len(arquivos)} seções, {len(nb["cells"])} células ({codigo} de código)')


if __name__ == '__main__':
    main()
