---
id: adr-0012
titulo: "ADR-0012 — RA3 num notebook próprio, entregue no repositório machine-learning-ra3"
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
# ADR-0012 — RA3 num notebook próprio, entregue no repositório machine-learning-ra3

- **Status:** aceita · **Data:** 05/11/2026 · **Decisor:** João Pedro Cardoso (notebook separado e repositório novo da entrega); o resto da organização é proposta da estrutura

## Contexto

- O RA3 pede três coisas no repositório: implementação (código ou notebook), documentação (técnicas, resultados e interpretações) e instruções de execução. O envio é só uma URL e a apresentação é em 18/11/2026 [Fato, fonte 13].
- O enunciado deixa escolher: "as análises poderão ser incorporadas ao projeto existente ou organizadas em arquivos específicos para o RA3" [Fato, fonte 13].
- O template do notebook só tem as partes do RA1 (seções 1 a 7) e do RA2 (seções 8 a 12); não há seção do RA3 nem template de documento do RA3 [Fato, fonte 4].
- O RA1 e o RA2 já foram entregues, com o notebook seguindo o template à risca, pelo repositório `eduardofabrii/data-analytics-ras` ([ADR-0011](0011-entregas-separadas-e-repositorio-da-entrega.md)).
- Em 05/11/2026 o João decidiu que o RA3 tem um repositório de entrega novo, `machine-learning-ra3`, só com o que é entregue, sem usar o repositório do RA1 e do RA2 para os dados. O desenvolvimento, as issues e as orientações continuam neste repositório.

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

1. **Repositório da entrega do RA3:** `https://github.com/Jcliz/machine-learning-ra3`, público, com Eduardo Fabri, João Correa e Rodrigo Alves como colaboradores. Tem **só o que é entregue**:

   | Lá | Sai daqui |
   |---|---|
   | `README.md` (documentação e instruções de execução) | `documentacao/ra3/README.md` |
   | `notebook/ra3-deezer.ipynb` (executado) | `python scripts/montar_notebook.py --ra3` |
   | `dados/faixas_preparadas.csv` e `dados/dicionario-faixas.md` | `dados/preparados/` (cópia igual, sem mudança) |
   | `requirements.txt` | `requirements-ra3.txt` |

   Issues, PRs, plano, critérios e as seções do notebook ficam só aqui.
2. **Enunciados das seções:** como não há template do RA3, o enunciado de cada seção é o texto do requisito transcrito em [enunciados/ra3.md](../../enunciados/ra3.md), sem mudar o sentido, no estilo do template do RA1 e do RA2 (enunciado, código e "Resposta do grupo").
3. **Dados:** o notebook clona o `machine-learning-ra3` no Colab e relê o conjunto preparado do RA1 com os tipos do dicionário. Acha o arquivo em `dados/faixas_preparadas.csv` (repositório da entrega) ou em `dados/preparados/faixas_preparadas.csv` (este repositório). Não usa Spark, o retrato bruto nem o repositório do RA1 e do RA2.
4. **Bibliotecas:** escolha do grupo, porque o enunciado não exige ferramenta: pandas para as medidas, matplotlib para os gráficos e scikit-learn para o modelo, todas já presentes no Colab e registradas em `requirements-ra3.txt` (e em `requirements.txt`, para quem desenvolve aqui). Pode-se trocar, desde que se registre nos dois arquivos e na issue.
5. **Documentação:** `documentacao/ra3/README.md`, em Markdown, com as técnicas, os resultados e a interpretação de cada seção, citando a célula do notebook, e as instruções de execução. Vira o `README.md` do repositório da entrega, para aparecer na página dele.
6. **Envio:** a URL do `machine-learning-ra3`, com o notebook do RA3 executado. Um PDF dele é opcional.

## Consequências

- O `verificar_entrega.py` confere os dois notebooks: o do RA1 e do RA2 continua sem pendência, e o do RA3 tem as próprias respostas em branco, menção a IA e organização interna (critérios X.7 e X.9).
- Gráficos, agregações e conclusões, que eram proibidos no RA1 (critério C5.5), ficam só no notebook do RA3.

---

## Ligações

- **Enunciado:** [enunciados/ra3.md](../../enunciados/ra3.md) · **Critérios:** [criterios-de-aceite-ra3](../../entregas/criterios-de-aceite-ra3.md) · **Plano:** [plano-de-tarefas-ra3](../../entregas/plano-de-tarefas-ra3.md)
- **Notebook:** [ADR-0002](0002-notebook-montado-por-secoes.md) · **Entrega:** [ADR-0011](0011-entregas-separadas-e-repositorio-da-entrega.md) · **Modelo:** [ADR-0013](0013-ra3-regressao-do-rank.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
