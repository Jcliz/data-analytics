"""Hooks do Claude Code que garantem commits sem coautoria de IA (ADR-0007).

--iniciar     (SessionStart) ativa .githooks e avisa se o autor configurado for uma IA.
sem argumento (PreToolUse, Bash) bloqueia `git commit` com coautoria de IA na mensagem
              ou com autor de IA configurado.
"""
import json
import re
import subprocess
import sys

MENSAGEM = re.compile(
    r'co-authored-by:[^\n"\']*(claude|anthropic|copilot|openai|codex|chatgpt|cursor|gemini)'
    r'|claude-session:|generated with \[?claude',
    re.I,
)
AUTOR = re.compile(r'claude|anthropic\.com|copilot|openai\.com', re.I)
INSTRUCAO = (
    'Regra do grupo (ADR-0007, CLAUDE.md): nenhum commit pode ter IA como coautora. '
    'Pare, remova as linhas Co-Authored-By/Claude-Session/"Generated with" e faça o commit '
    'só com o autor real. Se o autor configurado for o Claude, rode antes '
    'git config user.name "<integrante>" e git config user.email "<email>" neste repositório.'
)


def git(*args):
    r = subprocess.run(['git', *args], capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ''


def autores_de_ia():
    return [p for p in ('GIT_AUTHOR_IDENT', 'GIT_COMMITTER_IDENT') if AUTOR.search(git('var', p))]


def iniciar():
    git('config', 'core.hooksPath', '.githooks')
    ruins = autores_de_ia()
    if ruins:
        print(json.dumps({'hookSpecificOutput': {
            'hookEventName': 'SessionStart',
            'additionalContext': f'Atenção: {", ".join(ruins)} aponta para uma IA ({git("var", "GIT_AUTHOR_IDENT")}). ' + INSTRUCAO,
        }}))


def antes_do_bash():
    dados = json.load(sys.stdin)
    comando = (dados.get('tool_input') or {}).get('command', '')
    if not re.search(r'\bgit\b[^\n;&|]*\bcommit\b', comando):
        return
    motivos = []
    if MENSAGEM.search(comando):
        motivos.append('a mensagem do commit tem coautoria ou assinatura de IA')
    if autores_de_ia() and not re.search(r'--author|user\.name', comando):
        motivos.append('o autor configurado no git é uma IA')
    if motivos:
        print(json.dumps({'hookSpecificOutput': {
            'hookEventName': 'PreToolUse',
            'permissionDecision': 'deny',
            'permissionDecisionReason': 'Commit bloqueado: ' + '; '.join(motivos) + '. ' + INSTRUCAO,
        }}))


if __name__ == '__main__':
    iniciar() if '--iniciar' in sys.argv else antes_do_bash()
