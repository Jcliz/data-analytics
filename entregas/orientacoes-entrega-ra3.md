# Orientações da entrega do RA3

> Como o RA3 deve ficar antes de a URL ir para o Canvas. Vale para pessoas e agentes. Prazo e apresentação: **18/11/2026**. As orientações do RA1 e do RA2 continuam em [orientacoes-documento-final.md](orientacoes-documento-final.md).

## 1. O que vai na entrega

O Canvas pede só a **URL do repositório** ([enunciado](../enunciados/ra3.md), seção 5). O repositório citado é o da entrega, `https://github.com/eduardofabrii/data-analytics-ras` ([ADR-0012](../docs/adr/0012-ra3-no-notebook-e-entrega-por-url.md)). Ele precisa ter as três coisas que o enunciado pede:

| O enunciado pede | Onde fica no repositório da entrega | Fonte aqui |
|---|---|---|
| **Implementação** (notebook com análises, visualizações e Machine Learning) | `notebook/ra1-ra2-deezer.ipynb`, executado, seções 13 a 17; e `notebook/notebook.pdf` atualizado | `notebook/secoes/13-*.py` a `17-*.py`, montados por `python scripts/montar_notebook.py` |
| **Documentação** (técnicas, resultados e interpretações) | `documentacao/ra3/README.md` | `documentacao/ra3/README.md` (cópia igual) |
| **Instruções de execução** | `documentacao/ra3/README.md`, seção "Como executar"; o `README.md` principal aponta para ela | idem |

`requirements.txt` também é copiado igual, porque o RA3 acrescenta bibliotecas (matplotlib e scikit-learn).

## 2. Notebook (seções 13 a 17)

- **Estilo do template:** a parte "RA3 — Analysis, Visualization and Machine Learning" abre com um texto curto, como as partes do RA1 e do RA2. Cada seção tem o enunciado (o requisito do enunciado do RA3, sem mudar o sentido), as células de código e a "Resposta do grupo". As seções 1 a 12 ficam como foram entregues.
- **Gráficos legíveis no PDF:** um gráfico por célula, com `figsize` que caiba na largura da página (até ~10 polegadas), título, eixos com nome e unidade e legenda quando houver grupos. Com 27 gêneros, barras horizontais ordenadas.
- **Tabelas curtas:** até 10 a 20 linhas por saída (`head`, `round(1)`); medidas por gênero numa tabela só, ordenada.
- **Comentário-título** na primeira linha de cada célula de código (ex.: `# Duração por gênero (boxplot)`): é como a documentação e a apresentação citam a célula.
- **Reprodutível:** semente fixa no Machine Learning (`SEMENTE_ML`); nenhuma leitura da API (o RA3 parte do conjunto preparado).
- **Executar tudo** no Colab, do início ao fim, sem erro; o RA2 vem antes e precisa do Java do Colab.

## 3. Documentação (`documentacao/ra3/README.md`)

- Uma seção por parte do notebook (13 a 17): técnica usada e por quê, resultado principal com o número e interpretação, citando `notebook §N, célula "…"`.
- Seção "Como executar": abrir no Colab a partir do repositório da entrega, *Ambiente de execução → Executar tudo*, tempo aproximado; execução local com `pip install -r requirements.txt` e Java 17 para o RA2; o que conferir no fim (números e gráficos esperados).
- Os números são os do notebook executado que vai na entrega.
- **Sem declaração de uso de IA** (X.7) e **sem citação da organização interna** (X.9): nada de área, tarefa, issue, PR, branch ou kanban; o texto cita a seção, a célula ou o arquivo.

## 4. Antes de enviar

1. `python scripts/verificar_entrega.py` sem pendência.
2. Revisão cruzada (T22) concluída, com a tabela `ID | status | evidência`.
3. Notebook do repositório da entrega igual ao montado aqui, executado no Colab, e PDF dele atualizado.
4. `documentacao/ra3/README.md` e `requirements.txt` iguais nos dois repositórios.
5. URL do repositório da entrega aberta numa janela anônima antes de enviar.
