"""Lista o que ainda falta para a entrega: campos em branco, notebook desatualizado ou não executado e commits fora da regra.

Uso: python scripts/verificar_entrega.py [--intervalo origin/main..HEAD]
Sai com código 1 se houver pendência. Critérios relacionados: N.2, N.3, X.2, K.7 (entregas/criterios-de-aceite.md).
"""
import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ / 'scripts'))
import montar_notebook  # noqa: E402

# Campo do template ainda não preenchido: texto entre colchetes que não é link, caixa de seleção nem índice.
CAMPO = re.compile(r'\[(?!x\]|X\]| \])([^\]\n]{3,})\](?!\()')


def pendencias_texto(texto):
    return [m.group(0) for m in CAMPO.finditer(texto)]


def secoes():
    achados = {}
    for arquivo in sorted((RAIZ / 'notebook' / 'secoes').glob('*.py')):
        texto = '\n'.join(t for tipo, t in montar_notebook.celulas(arquivo) if tipo == 'markdown')
        campos = [c for c in pendencias_texto(texto) if 'Preencha' in c or c.startswith('[Registre')
                  or c.startswith('[Indique') or c.startswith('[Explique') or c.startswith('[Informe')]
        codigo = [t for tipo, t in montar_notebook.celulas(arquivo) if tipo == 'code']
        if campos:
            achados[arquivo.relative_to(RAIZ)] = f'{len(campos)} resposta(s) em branco'
        elif not codigo and arquivo.name not in {'00a-identificacao.py', '01-contexto-e-objetivo.py',
                                                    '07-consideracoes-ra1.py', '08-objetivo-streaming.py',
                                                    '12-consideracoes-ra2.py'}:
            achados[arquivo.relative_to(RAIZ)] = 'sem célula de código'
    return achados


def documento():
    achados = {}
    for arquivo in sorted((RAIZ / 'documentacao' / 'ra1').glob('*.md')):
        texto = re.sub(r'<!--.*?-->', '', arquivo.read_text(encoding='utf-8'), flags=re.S)
        campos = pendencias_texto(texto)
        if campos:
            achados[arquivo.relative_to(RAIZ)] = f'{len(campos)} campo(s) entre colchetes, ex.: {campos[0][:60]}'
    return achados


def notebook():
    caminho = RAIZ / 'notebook' / 'projeto_data_analytics.ipynb'
    if not caminho.exists():
        return ['notebook não gerado: rode python scripts/montar_notebook.py']
    atual = json.loads(caminho.read_text(encoding='utf-8'))
    esperado = montar_notebook.notebook(sorted((RAIZ / 'notebook' / 'secoes').glob('*.py')))
    fonte = lambda nb: [(c['cell_type'], ''.join(c['source']).strip()) for c in nb['cells']]
    problemas = []
    if fonte(atual) != fonte(esperado):
        problemas.append('notebook desatualizado em relação a notebook/secoes/: monte de novo e execute')
    codigo = [c for c in atual['cells'] if c['cell_type'] == 'code']
    contadores = [c.get('execution_count') for c in codigo]
    if any(n is None for n in contadores):
        problemas.append(f'{contadores.count(None)} de {len(codigo)} célula(s) de código sem execução')
    elif contadores != sorted(contadores):
        problemas.append('células executadas fora de ordem: reinicie e execute tudo')
    erros = sum(1 for c in codigo for o in c.get('outputs', []) if o.get('output_type') == 'error')
    if erros:
        problemas.append(f'{erros} célula(s) com erro na saída')
    return problemas


def commits(intervalo):
    r = subprocess.run([sys.executable, str(RAIZ / 'scripts' / 'verificar_commits.py'), intervalo],
                       capture_output=True, text=True)
    return [] if r.returncode == 0 else [r.stdout.strip() or r.stderr.strip()]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--intervalo', default='origin/main..HEAD')
    args = ap.parse_args()
    total = 0
    for titulo, itens in [('Notebook (seções)', secoes()), ('Documento do RA1', documento())]:
        print(f'\n## {titulo}')
        for arquivo, msg in itens.items():
            print(f'- {arquivo}: {msg}')
        print('- ok' if not itens else '')
        total += len(itens)
    for titulo, itens in [('Notebook gerado', notebook()), ('Commits', commits(args.intervalo))]:
        print(f'\n## {titulo}')
        for msg in itens:
            print(f'- {msg}')
        print('- ok' if not itens else '')
        total += len(itens)
    print(f'\n{total} pendência(s).')
    sys.exit(1 if total else 0)


if __name__ == '__main__':
    main()
