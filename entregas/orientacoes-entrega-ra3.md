# Orientações da entrega do RA3

> Como o RA3 deve ficar antes de a URL ir para o Canvas. Vale para pessoas e agentes. O que o enunciado exige está nos critérios R, RD e RAP ([critérios](criterios-de-aceite-ra3.md), seção 1); o resto deste arquivo é a forma combinada pelo grupo para cumprir isso, e não regra da rubrica. Prazo e apresentação: **18/11/2026**. As orientações do RA1 e do RA2 continuam em [orientacoes-documento-final.md](orientacoes-documento-final.md).

## 1. O que vai na entrega

O Canvas pede só a **URL do repositório** ([enunciado](../enunciados/ra3.md), seção 5). O repositório citado é o da entrega do RA3, `https://github.com/Jcliz/machine-learning-ra3` ([ADR-0012](../docs/adr/0012-ra3-no-notebook-e-entrega-por-url.md)), que tem **só o que é entregue**; o desenvolvimento, as issues e estas orientações ficam neste repositório. O repositório do RA1 e do RA2 (`eduardofabrii/data-analytics-ras`) não é usado no RA3. O da entrega precisa ter as três coisas que o enunciado pede:

| O enunciado pede | Onde fica no repositório da entrega | Fonte aqui |
|---|---|---|
| **Implementação** (notebook com análises, visualizações e Machine Learning) | `notebook/ra3-deezer.ipynb`, executado (um PDF dele é opcional, para quem quiser ver sem executar) | `notebook/secoes-ra3/`, montado por `python scripts/montar_notebook.py --ra3` em `notebook/ra3-deezer.ipynb` |
| **Documentação** (técnicas, resultados e interpretações) | `README.md` | `documentacao/ra3/README.md` (cópia igual) |
| **Instruções de execução** | `README.md`, seção "Como executar" | idem |
| Dados usados pelo notebook | `dados/faixas_preparadas.csv` e `dados/dicionario-faixas.md` | `dados/preparados/` (cópia igual) |

O `requirements.txt` de lá é a cópia de `requirements-ra3.txt` (pandas, matplotlib e scikit-learn, escolha do grupo; o enunciado aceita qualquer ferramenta). Nada mais vai para lá: nem issues, nem plano, nem as seções em `.py`.

## 2. Notebook do RA3: forma combinada pelo grupo

- **Estilo do template:** não há template do RA3, então o notebook segue o estilo do template do RA1 e do RA2: identificação, abertura "RA3 — Analysis, Visualization and Machine Learning" e uma seção por requisito (1 a 5), cada uma com o enunciado (o requisito do enunciado do RA3, sem mudar o sentido), as células de código e a "Resposta do grupo". O notebook do RA1 e do RA2 fica como foi entregue.
- **Gráficos legíveis:** um gráfico por célula, com `figsize` que caiba na largura da página (até ~10 polegadas), título, eixos com nome e unidade e legenda quando houver grupos. Com 27 gêneros, barras horizontais ordenadas.
- **Tabelas curtas:** até 10 a 20 linhas por saída (`head`, `round(1)`); medidas por gênero numa tabela só, ordenada.
- **Comentário-título** na primeira linha de cada célula de código (ex.: `# Duração por gênero (boxplot)`): é como a documentação e a apresentação citam a célula.
- **Reprodutível (recomendação RC.4):** semente fixa no Machine Learning (`SEMENTE_ML`); nenhuma leitura da API (o RA3 parte do conjunto preparado).
- **Executar tudo** no Colab, do início ao fim, sem erro. O notebook do RA3 não usa Spark: a 1ª célula da seção 1 clona o `machine-learning-ra3` e acha o conjunto preparado lá.

## 3. Documentação (`documentacao/ra3/README.md`)

- Uma seção por seção do notebook do RA3 (1 a 5): técnica usada e por quê, resultado principal com o número e interpretação, citando `notebook §N, célula "…"`.
- Seção "Como executar" (exigência RD.3: o necessário para executar e verificar): abrir no Colab a partir do repositório da entrega, *Ambiente de execução → Executar tudo*; execução local com `pip install -r requirements.txt`, abrindo o notebook de dentro do clone; o que conferir no fim (números e gráficos esperados).
- Os números são os do notebook executado que vai na entrega.
- **Sem declaração de uso de IA** (X.7) e **sem citação da organização interna** (X.9): nada de área, tarefa, issue, PR, branch ou kanban; o texto cita a seção, a célula ou o arquivo.

## 4. Antes de enviar

1. `python scripts/verificar_entrega.py` sem pendência.
2. Revisão cruzada (T22) concluída, com a tabela `ID | status | evidência`.
3. `notebook/ra3-deezer.ipynb` do repositório da entrega igual ao montado aqui e executado no Colab.
4. `README.md`, `requirements.txt` e `dados/` de lá iguais às fontes daqui (seção 1).
5. URL do repositório da entrega aberta numa janela anônima antes de enviar.
