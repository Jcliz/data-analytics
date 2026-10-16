"""Confere se os commits de um intervalo seguem a regra sem coautoria de IA (ADR-0007).

Uso: python scripts/verificar_commits.py [INTERVALO]
     INTERVALO padrão: origin/main..HEAD. Sai com código 1 se achar commit fora da regra.
Usado pelo GitHub Actions (.github/workflows/verificar-commits.yml) e por scripts/verificar_entrega.py.
"""
import re
import subprocess
import sys

MENSAGEM = re.compile(
    r'^\s*(co-authored-by:.*(claude|anthropic|copilot|openai|codex|chatgpt|cursor|gemini)|claude-session:)'
    r'|generated with \[?claude',
    re.I | re.M,
)
AUTOR = re.compile(r'claude|anthropic\.com|copilot|openai\.com', re.I)
SEP = '\x1e'


def problemas(intervalo):
    saida = subprocess.run(
        ['git', 'log', '--format=%H%x1f%an <%ae>%x1f%cn <%ce>%x1f%B' + SEP, intervalo],
        capture_output=True, text=True, check=True,
    ).stdout
    for bloco in filter(str.strip, saida.split(SEP)):
        sha, autor, committer, corpo = bloco.strip().split('\x1f', 3)
        motivos = [m.group(0).strip() for m in MENSAGEM.finditer(corpo)]
        motivos += [f'autor {autor}'] if AUTOR.search(autor) else []
        motivos += [f'committer {committer}'] if AUTOR.search(committer) and 'noreply@github.com' not in committer else []
        if motivos:
            yield sha[:9], corpo.splitlines()[0], motivos


def main():
    intervalo = sys.argv[1] if len(sys.argv) > 1 else 'origin/main..HEAD'
    achados = list(problemas(intervalo))
    for sha, titulo, motivos in achados:
        print(f'{sha} "{titulo}": ' + '; '.join(motivos))
    if achados:
        print(f'\n{len(achados)} commit(s) fora da regra (ADR-0007). Refaça sem coautoria de IA e com o autor real.')
        sys.exit(1)
    print(f'ok: nenhum commit com coautoria de IA em {intervalo}')


if __name__ == '__main__':
    main()
