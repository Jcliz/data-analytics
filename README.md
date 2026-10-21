# data-analytics

Trabalhos da disciplina **Data Analytics** (Projeto Baseado em Problemas, BSI PUCPR, 2026): RA1 (ingestão e preparação dos dados) e RA2 (processamento em streaming com janelas temporais). O RA3 (análise e visualização) virá depois, sobre os mesmos dados.

A fonte de dados é a **API pública da Deezer**, a mesma usada pelo app [rdsalvesPUC/dataaudio](https://github.com/rdsalvesPUC/dataaudio). O grupo coleta as faixas dos charts, guarda um retrato bruto no repositório, limpa e prepara os dados (RA1) e depois simula eventos de reprodução para processar em streaming (RA2).

Este repositório guarda três coisas:

1. as **entregas**: o notebook do projeto (montado a partir de uma seção por área) e o documento do RA1 (gerado no template `.docx` do professor), enviados em arquivos separados: o PDF do documento no RA1 e o PDF do notebook, exportado no Colab a partir do repositório da entrega ([eduardofabrii/data-analytics-ras](https://github.com/eduardofabrii/data-analytics-ras)), no RA2;
2. a **base de conhecimento** que sustenta as entregas: enunciados transcritos, decisões, notas sobre a API e sobre o material de aula;
3. o **processo** de trabalho: plano de tarefas, critérios de aceite, orientações do PDF final e regras para assistentes de IA.

| Integrante | GitHub | Área |
|---|---|---|
| João Correa | `jvecodev` | A: problema, síntese e documento do RA1 (`.docx` da entrega) |
| João Pedro Cardoso | `Jcliz` | B: fonte, ingestão e reprodutibilidade (código) |
| Eduardo Fabri | `eduardofabrii` | C: compreensão e qualidade (código) |
| Rodrigo Alves | `rdsalvesPUC` | D: limpeza e conjunto resultante (código) |

Professora: Marina de Lara. A divisão está em proposta ([ADR-0008](docs/adr/0008-divisao-em-quatro-areas.md)); o detalhe de cada área está no [plano de tarefas](entregas/plano-de-tarefas.md).

## Comece por aqui

Antes de escrever qualquer parte do notebook ou do documento, leia nesta ordem:

1. **[`CONTEXT.md`](CONTEXT.md)**: resumo do que já está decidido (entregas, fonte de dados, glossário, decisões, contrato entre as seções do notebook). A seção 9 dele diz o que ler para cada tarefa.
2. **A issue da sua tarefa.** Cada issue traz o objetivo, os arquivos que a sua área pode alterar, os critérios de aceite e as dependências.
3. **Só os arquivos indicados** para a tarefa. Não é preciso ler a base inteira.

E, uma vez por clone, ative o hook que barra commits com coautoria de IA:

```bash
git config core.hooksPath .githooks
```

## Mapa do repositório

```
.
├── README.md                  este arquivo
├── CONTEXT.md                 porta de entrada: o que está decidido e o que ler para cada tarefa
├── AGENTS.md                  regras para assistentes de IA (Codex, Copilot, Cursor e outros)
├── CLAUDE.md                  carrega o AGENTS.md e o CONTEXT.md no Claude Code; regra de commit e passo a passo
│
├── notebook/
│   ├── secoes/                uma seção do notebook por arquivo (formato percent), cada uma de uma área
│   └── projeto_data_analytics.ipynb   notebook entregue, GERADO por scripts/montar_notebook.py
├── documentacao/ra1/          documento do RA1 em Markdown, um arquivo por seção do template
├── dados/
│   ├── brutos/                retratos da API, um por data de coleta (nunca editados à mão)
│   ├── preparados/            conjunto preparado do RA1 (entrada do RA2)
│   └── streaming/             pastas temporárias do RA2 (fora do git)
├── output/                    arquivos de entrega: documento do RA1 (.docx e PDF) e o PDF do notebook para conferência local
│
├── entregas/                  plano de tarefas, critérios de aceite, orientações do PDF e roteiro da apresentação
├── enunciados/                enunciados do RA1 e do RA2 transcritos
├── base/                      base de conhecimento: API da Deezer, qualidade, streaming, material de aula, fontes
├── docs/
│   ├── adr/                   decisões do projeto, uma por arquivo
│   └── agents/                configuração das skills de IA (issues, rótulos, documentos de domínio)
├── modelos/                   templates do professor (.ipynb e .docx), sem alteração
├── claude/                    texto das instruções do projeto no claude.ai
├── scripts/                   montagem do notebook, geração do .docx, verificações
│
├── .claude/                   configuração e hook do Claude Code (sem coautoria de IA)
├── .githooks/                 hook commit-msg do git (sem coautoria de IA)
├── .github/                   modelo de PR e verificação de commits no GitHub Actions
├── requirements.txt
└── .gitignore
```

## Notebook (`notebook/`)

O professor pede **um notebook único** com as seções do RA1 e do RA2 ([template](modelos/template_projeto_data_analytics.ipynb)). Para quatro pessoas trabalharem nele sem conflito de merge, cada seção é um arquivo `.py` em `notebook/secoes/`, no formato *percent* ([ADR-0002](docs/adr/0002-notebook-montado-por-secoes.md)):

```
notebook/secoes/
├── 00a-identificacao.py          A    capa do notebook (projeto, equipe, fonte)
├── 01-contexto-e-objetivo.py     A    RA1 §1
├── 02-fonte-e-ingestao.py        B    RA1 §2  → df_bruto
├── 03-exploracao-inicial.py      C    RA1 §3
├── 04-limpeza-e-preparacao.py    D    RA1 §4  → df_preparado
├── 05-transformacao.py           D    RA1 §5
├── 07-consideracoes-ra1.py       A    RA1 §7
├── 08-objetivo-streaming.py      A    RA2 §8
├── 09-fonte-e-processamento.py   B    RA2 §9  → spark, eventos
├── 10-janelas-temporais.py       C    RA2 §10 → consulta
├── 11-resultados.py              D    RA2 §11
└── 12-consideracoes-ra2.py       A    RA2 §12
```

- `# %%` abre uma célula de código; `# %% [markdown]` abre uma célula de texto. VS Code, PyCharm e Spyder executam essas células direto.
- Linhas `#>` (em código e em texto) e comentários `<!-- ... -->` são orientações para quem escreve; o montador tira os dois do notebook gerado.
- As seções conversam por nomes fixos (`RAIZ`, `df_bruto`, `df_preparado`, `spark`, `consulta`…): o contrato está no [`CONTEXT.md`](CONTEXT.md), seção 6.
- Monte o notebook com:

  ```bash
  python scripts/montar_notebook.py
  ```

  e execute do início ao fim (no Colab: *Ambiente de execução → Executar tudo*). O arquivo `notebook/projeto_data_analytics.ipynb` nunca é editado à mão.

## Documento do RA1 (`documentacao/ra1/`)

O RA1 tem um documento próprio, no template [`Template_RA1_Data_Analytics.docx`](modelos/Template_RA1_Data_Analytics.docx). Cada seção do template é um arquivo Markdown, com os mesmos títulos e campos ([ADR-0003](docs/adr/0003-documento-ra1-gerado-do-template.md)):

```
documentacao/ra1/
├── 00-capa.md                          A
├── 01-problema-e-perguntas.md          A
├── 02-fontes-e-ingestao.md             B
├── 03-compreensao-e-qualidade.md       C
├── 04-limpeza-e-preparacao.md          D
├── 05-conjunto-resultante.md           D
├── 06-organizacao-e-reprodutibilidade.md   B
└── 07-referencias-e-anexos.md          A
```

O script preenche o template do professor com esse conteúdo e exporta o PDF:

```bash
python scripts/gerar_docx_ra1.py
```

Saída: `output/ra1-documentacao.docx` e `output/ra1-documentacao.pdf` (o PDF precisa do LibreOffice; sem ele, exporte pelo Word). Como o documento final deve ficar: [orientações do documento final](entregas/orientacoes-documento-final.md).

## Entrega: RA1 e RA2 em arquivos separados

O RA1 e o RA2 vão **em arquivos separados** ([ADR-0011](docs/adr/0011-entregas-separadas-e-repositorio-da-entrega.md)): no RA1, o PDF do documento, sem o notebook; no RA2, o PDF do notebook exportado no Colab a partir do repositório da entrega, [eduardofabrii/data-analytics-ras](https://github.com/eduardofabrii/data-analytics-ras), que recebe uma cópia igual do `.ipynb` montado aqui.

```bash
python scripts/gerar_docx_ra1.py      # RA1: output/ra1-documentacao.pdf
python scripts/montar_notebook.py     # notebook; copie para notebook/ra1-ra2-deezer.ipynb do repositório da entrega
```

## Como executar

Não é preciso acessar a API da Deezer: o notebook lê o retrato bruto já versionado em `dados/brutos/2026-10-16/` (`BAIXAR_DA_API = False`), então a execução dá os mesmos números em qualquer máquina. Os passos, com o resultado esperado de cada um, estão também no [documento do RA1, seção 06](documentacao/ra1/06-organizacao-e-reprodutibilidade.md).

### No Google Colab (ambiente de referência)

1. Abra `notebook/ra1-ra2-deezer.ipynb` no Colab (*Arquivo → Abrir notebook → GitHub*, repositório `eduardofabrii/data-analytics-ras`).
2. *Ambiente de execução → Executar tudo*. A primeira célula de código da seção 2 clona o repositório da entrega (ramo `main`) e a seção 09 instala o PySpark, o que leva alguns minutos.

### Localmente

Precisa de Python 3.9 ou mais novo e, para o RA2, de Java 17 ou mais novo.

```bash
git clone https://github.com/Jcliz/data-analytics.git
cd data-analytics
python -m venv .venv
source .venv/bin/activate          # no Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/montar_notebook.py
jupyter nbconvert --to notebook --execute --inplace notebook/projeto_data_analytics.ipynb
```

No Windows o Spark local costuma pedir também o `winutils`; para o RA2, prefira o Colab.

Para exportar o notebook em PDF localmente: `jupyter nbconvert --to webpdf --allow-chromium-download notebook/projeto_data_analytics.ipynb --output-dir output` (a primeira vez baixa o Chromium).

### Como saber se deu certo

| Onde olhar | Resultado esperado |
|---|---|
| Célula "Preparação do ambiente" (primeira célula de código da seção 2) | Mostra a raiz do projeto, o ambiente e as versões de Python e pandas. |
| Célula "Leitura do retrato bruto mais recente" (seção 2) | Lê `dados/brutos/2026-10-16` e lista os sete arquivos JSON do retrato. |
| Célula "Verificação do carregamento" (seção 2) | `df_bruto` com 2.800 linhas e 102 colunas: 2.581 faixas, 2.292 álbuns e 1.688 artistas únicos, nenhum item sem detalhe. |
| `dados/preparados/faixas_preparadas.csv` | Regravado pelas seções 04 e 05, com as linhas e colunas do documento do RA1, seção 05. |
| Notebook inteiro | Nenhuma célula com erro. |

### Se a API da Deezer estiver indisponível ou responder diferente

A reprodução não chama a API, então não depende dela. O chart muda todo dia e pode mudar com o país de onde vem a requisição (o retrato da entrega foi coletado com país aparente US), por isso os números da entrega são os do retrato versionado. Coletar de novo (`BAIXAR_DA_API = True` na primeira célula de código da seção 2) grava outra pasta em `dados/brutos/`, que passa a ser lida por ser a mais recente, e muda os números de todas as seções: combine com o grupo antes ([ADR-0004](docs/adr/0004-retrato-bruto-versionado.md)). Para voltar ao retrato da entrega, apague a pasta nova ou use um clone limpo.

### Verificações antes do PR

```bash
python scripts/verificar_entrega.py   # campos em branco, notebook desatualizado, regra de commit
python scripts/verificar_commits.py   # só a regra de commit da branch
```

## Base de conhecimento

| Camada | Onde fica | Para que serve |
|---|---|---|
| **Enunciados** | [`enunciados/`](enunciados/README.md) | O que o professor pede no RA1 e no RA2, transcrito dos PDFs. |
| **Decisões** | [`docs/adr/`](docs/adr/README.md) | O que o grupo decidiu, uma decisão por arquivo, com contexto, opções e consequências. |
| **Base** | [`base/`](base/README.md) | API da Deezer, qualidade de dados, streaming e janelas, material de aula, ideias de perguntas, fontes numeradas. |
| **Resumo** | [`CONTEXT.md`](CONTEXT.md) | O essencial das camadas acima, em uma página. |

**Precedência:** enunciados > decisões > base > rascunhos. Se uma tarefa precisar contrariar uma decisão, não mude o texto por conta própria: leve a dúvida ao grupo na issue.

- **Cite a fonte** pelo número de [`base/fontes.md`](base/fontes.md). Fonte nova entra no fim, com o próximo número; a numeração existente nunca muda.
- **Separe [Fato] de [Inferência].** Os arquivos da base marcam cada afirmação.
- **Evidência para toda afirmação sobre os dados:** a seção e a célula do notebook, com a contagem e o denominador.
- **Arquivo novo da base** segue o formato dos existentes: cabeçalho YAML e seção "Ligações" no fim, com links relativos. Decisão nova recebe o próximo número de ADR e segue o mesmo formato.

## Como trabalhamos

### Tarefas e issues

- As tarefas são issues com os rótulos `ra1`, `ra2` ou `geral`, mais o rótulo da área (`area-a` … `area-d`). A lista completa, com prazos e dependências, está no [plano de tarefas](entregas/plano-de-tarefas.md), seção 5.
- Cada issue traz os critérios de aceite por ID ([critérios de aceite](entregas/criterios-de-aceite.md)).
- Quem puxar uma tarefa geral sem responsável se atribui na issue.

### Quadro de tarefas (kanban)

As issues e os PRs ficam no quadro do GitHub Projects ligado a este repositório (aba **Projects**), com quatro colunas:

| Coluna | Quando o card vai para ela |
|---|---|
| **A fazer** | Issue criada (entra sozinha no quadro). |
| **Em andamento** | Quem pegou a tarefa se atribui e move o card. |
| **Em revisão** | PR aberto com `Closes #<n>`. |
| **Concluído** | PR integrado ou issue fechada (move sozinho). |

O andamento de cada tarefa fica no quadro, e não nos arquivos do repositório.

### Pendências entre áreas

Uma seção pode depender de algo que outra área ainda não fez (por exemplo, a exploração precisa de uma coluna que a ingestão não trouxe). O trabalho não para: registre a suposição como uma linha na issue com o rótulo `pendencia-cruzada` da área que precisa resolver, com o arquivo e o trecho. A revisão cruzada (T12) exige que nenhuma esteja aberta.

### Branches, push e pull requests

- Uma branch por tarefa, com nome curto: `tNN-palavra`: o número da tarefa com dois dígitos e uma palavra que diga o que é, tudo em minúsculas, sem acento e sem barra. Ex.: `t02-coleta`, `t11-docx`. O nome de cada tarefa está na coluna "Branch" do [plano](entregas/plano-de-tarefas.md), seção 5. Ajuste fora de tarefa: `ajuste-palavra` (ex.: `ajuste-readme`).
- **Todos os integrantes têm push na `main` e podem abrir PRs para a `main`.** Conteúdo de tarefa entra por PR, com `Closes #<n>` e a evidência de cada critério; outro integrante revisa. Push direto na `main` fica para correções pequenas (erro de digitação, link quebrado).
- Cada área edita só os seus arquivos (plano de tarefas, seção 2).

### Commits

- Mensagem em português, no imperativo, citando a tarefa: `ra1(qualidade): adiciona verificação de bpm igual a zero (#7)`.
- **Nenhum commit com Claude, ou qualquer IA, como coautor** ([ADR-0007](docs/adr/0007-commits-sem-coautoria-de-ia.md)). O autor é sempre a pessoa do grupo. O hook do git, o hook do Claude Code e o GitHub Actions recusam commits fora da regra.

### Definição de pronto de uma tarefa

1. Todos os critérios de aceite da issue atendidos, cada um com evidência (seção e célula do notebook, contagem).
2. Notebook montado e executado do início ao fim sem erro.
3. `python scripts/verificar_entrega.py` sem pendência nos arquivos da tarefa.
4. Nenhuma contradição com o `CONTEXT.md` nem com as decisões.
5. PR revisado por outro integrante.

## Assistentes de IA

O grupo usa assistentes de IA para escrever código e texto. Estes arquivos fazem todos seguirem as mesmas regras:

| Arquivo | Quem lê | O que faz |
|---|---|---|
| [`AGENTS.md`](AGENTS.md) | Codex, Copilot, Cursor e outros | Manda ler o `CONTEXT.md` e a issue, respeitar a precedência, o contrato do notebook e a regra de commit. |
| [`CLAUDE.md`](CLAUDE.md) | Claude Code | Carrega o `AGENTS.md` e o `CONTEXT.md` automaticamente; traz a regra de commit passo a passo e como desenvolver. |
| [`.claude/settings.json`](.claude/settings.json) | Claude Code | Desliga a coautoria automática e liga o hook que bloqueia commit com coautoria de IA. |
| [`claude/instrucoes-projeto.md`](claude/instrucoes-projeto.md) | Projeto no claude.ai | Texto para colar nas instruções do projeto. Não é aplicado sozinho. |
| [`docs/agents/`](docs/agents/) | Skills de engenharia | Dizem onde ficam as issues, quais rótulos de triagem existem e onde está a documentação de domínio. |
