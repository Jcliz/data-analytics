---
id: adr-0012
titulo: "ADR-0012 — RA3 num notebook próprio, com documentação e instruções no repositório da entrega"
tipo: decisao
decisao: "0012"
status: aceita
data: 2026-11-05
decisor: João Pedro Cardoso
entregas: [RA3]
areas: [A, B, C, D]
fontes: [4, 13]
relacionados: [adr-0002, adr-0006, adr-0008, adr-0010, adr-0011, adr-0013]
---
# ADR-0012 — RA3 num notebook próprio, com documentação e instruções no repositório da entrega

- **Status:** aceita · **Data:** 05/11/2026 · **Decisor:** João Pedro Cardoso (notebook separado); o resto da organização é proposta da estrutura

## Contexto

- O RA3 pede três coisas no repositório: implementação (código ou notebook), documentação (técnicas, resultados e interpretações) e instruções de execução. O envio é só uma URL e a apresentação é em 18/11/2026 [Fato, fonte 13].
- O enunciado deixa escolher: "as análises poderão ser incorporadas ao projeto existente ou organizadas em arquivos específicos para o RA3" [Fato, fonte 13].
- O template do notebook só tem as partes do RA1 (seções 1 a 7) e do RA2 (seções 8 a 12); não há seção do RA3 nem template de documento do RA3 [Fato, fonte 4].
- O RA1 e o RA2 já foram entregues, com o notebook seguindo o template à risca ([ADR-0011](0011-entregas-separadas-e-repositorio-da-entrega.md)).

## Opções consideradas

- **(a)** Um notebook próprio do RA3, que lê o conjunto preparado do RA1.
- **(b)** Continuar o notebook do RA1 e do RA2 com seções 13 a 17.

## Decisão

**(a)**, escolhida pelo João em 05/11/2026. O notebook do RA1 e do RA2 fica exatamente como foi entregue, igual ao template. O RA3 ganha um notebook próprio, montado por seções como o outro ([ADR-0002](0002-notebook-montado-por-secoes.md)):

| Arquivo em `notebook/secoes-ra3/` | Conteúdo | Requisito do enunciado |
|---|---|---|
| `00-identificacao.py` | Identificação (mesmos campos do template) e abertura "RA3 — Analysis, Visualization and Machine Learning" | — |
| `01-estatistica-descritiva.py` | 1. Análise estatística descritiva; a 1ª célula prepara o ambiente e a 2ª relê o conjunto preparado em `df_analise` | 2.1 |
| `02-visualizacoes.py` | 2. Visualização e interpretação dos dados | 2.2 |
| `03-representatividade.py` | 3. Amostragem e representatividade | 2.3 |
| `04-machine-learning.py` | 4. Aplicação de Machine Learning | 2.4 |
| `05-conclusoes.py` | 5. Conclusões do RA3 | 2.5 |

1. **Montagem:** `python scripts/montar_notebook.py --ra3` grava `notebook/ra3-deezer.ipynb`, copiado igual para o mesmo caminho do repositório da entrega.
2. **Enunciados das seções:** como não há template do RA3, o enunciado de cada seção é o texto do requisito transcrito em [enunciados/ra3.md](../../enunciados/ra3.md), sem mudar o sentido, no estilo do template do RA1 e do RA2 (enunciado, código e "Resposta do grupo").
3. **Dados:** o notebook clona o repositório da entrega no Colab (como a seção 2 do outro) e relê `dados/preparados/faixas_preparadas.csv` com os tipos do dicionário. Não usa Spark nem o retrato bruto.
4. **Bibliotecas:** escolha do grupo, porque o enunciado não exige ferramenta: pandas para as medidas, matplotlib para os gráficos e scikit-learn para o modelo, todas já presentes no Colab e registradas em `requirements.txt`. Pode-se trocar, desde que se registre em `requirements.txt` e na issue.
5. **Documentação:** `documentacao/ra3/README.md`, em Markdown, com as técnicas, os resultados e a interpretação de cada seção, citando a célula do notebook, e as instruções de execução. É copiado igual para o repositório da entrega, no mesmo caminho, e o README principal de lá aponta para ele.
6. **Envio:** a URL do repositório da entrega, com o notebook do RA3 executado. Um PDF dele é opcional.

## Consequências

- O `verificar_entrega.py` confere os dois notebooks: o do RA1 e do RA2 continua sem pendência, e o do RA3 tem as próprias respostas em branco, menção a IA e organização interna (critérios X.7 e X.9).
- Gráficos, agregações e conclusões, que eram proibidos no RA1 (critério C5.5), ficam só no notebook do RA3.

---

## Ligações

- **Enunciado:** [enunciados/ra3.md](../../enunciados/ra3.md) · **Critérios:** [criterios-de-aceite-ra3](../../entregas/criterios-de-aceite-ra3.md) · **Plano:** [plano-de-tarefas-ra3](../../entregas/plano-de-tarefas-ra3.md)
- **Notebook:** [ADR-0002](0002-notebook-montado-por-secoes.md) · **Entrega:** [ADR-0011](0011-entregas-separadas-e-repositorio-da-entrega.md) · **Modelo:** [ADR-0013](0013-ra3-regressao-do-rank.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
