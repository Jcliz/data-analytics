# Issue tracker: GitHub

As tarefas e pendências deste repositório ficam no **GitHub Issues** de [`Jcliz/data-analytics`](https://github.com/Jcliz/data-analytics/issues). Use o `gh` na linha de comando ou, em sessões sem `gh` (como o Claude Code na web), as ferramentas do servidor MCP do GitHub (`issue_read`, `issue_write`, `list_issues`, `add_issue_comment`). Tudo em português.

## Convenções

- **Título:** `[RA1][Área X] descrição`, `[RA2][Área X] descrição` ou `[Geral] descrição` (plano de tarefas, seção 5).
- **Corpo:** o modelo da seção 6 do [plano de tarefas](../../entregas/plano-de-tarefas.md): Objetivo, Insumos obrigatórios, Arquivos desta tarefa, Critérios de aceite (IDs de `entregas/criterios-de-aceite.md`), Dependências, Definição de pronto.
- **Rótulos:** entrega (`ra1`, `ra2` ou `geral`), área (`area-a` … `area-d`), destino (`notebook`, `documento`) e triagem ([triage-labels.md](triage-labels.md)).
- **Responsável:** só se atribui quem já é colaborador do repositório. Antes disso, o login aparece entre crases no corpo, sem `@`.

## Comandos (`gh`)

- **Criar:** `gh issue create --title "..." --body-file corpo.md --label ra1 --label area-b`
- **Ler:** `gh issue view <número> --comments`
- **Listar:** `gh issue list --state open --label ra1 --json number,title,labels,assignees`
- **Comentar:** `gh issue comment <número> --body "..."`
- **Rótulos:** `gh issue edit <número> --add-label "..."` / `--remove-label "..."`
- **Fechar:** pelo PR (`Closes #<número>` no corpo) ou `gh issue close <número> --comment "..."`

O `gh` descobre o repositório pelo `git remote -v` quando roda dentro do clone.

## Pendências entre áreas

Uma suposição sobre o trabalho de outra área vira **uma linha** na issue com o rótulo `pendencia-cruzada` da área dona (crie a issue se não existir: `[Pendência] Área X`). A linha cita o arquivo e o trecho onde a suposição aparece e fecha com o commit que resolve ou com a decisão de não fazer.

## Pull requests como superfície de triagem

**PRs como pedido de tarefa: não.** Os PRs deste repositório são do próprio grupo e sempre fecham uma issue.

O GitHub usa a mesma numeração para issues e PRs, então `#12` pode ser qualquer um dos dois: confira com `gh pr view 12` e, se não for PR, `gh issue view 12`.

## Quando uma skill disser "publique no issue tracker"

Crie uma issue no GitHub, no formato acima.

## Quando uma skill disser "busque o ticket"

Rode `gh issue view <número> --comments` (ou `issue_read` no MCP do GitHub).
