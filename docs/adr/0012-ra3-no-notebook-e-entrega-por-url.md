---
id: adr-0012
titulo: "ADR-0012 — RA3 nas seções 13 a 17 do mesmo notebook, com documentação e instruções no repositório da entrega"
tipo: decisao
decisao: "0012"
status: proposta
data: 2026-11-05
decisor: proposta para o grupo
entregas: [RA3]
areas: [A, B, C, D]
fontes: [4, 13]
relacionados: [adr-0002, adr-0006, adr-0008, adr-0010, adr-0011, adr-0013]
---
# ADR-0012 — RA3 nas seções 13 a 17 do mesmo notebook, com documentação e instruções no repositório da entrega

- **Status:** proposta · **Data:** 05/11/2026

## Contexto

- O RA3 pede três coisas no repositório: implementação (código ou notebook), documentação (técnicas, resultados e interpretações) e instruções de execução. O envio é só uma URL e a apresentação é em 18/11/2026 [Fato, fonte 13].
- O enunciado deixa escolher: "as análises poderão ser incorporadas ao projeto existente ou organizadas em arquivos específicos para o RA3" [Fato, fonte 13].
- O template do notebook só tem as partes do RA1 (seções 1 a 7) e do RA2 (seções 8 a 12); não há seção do RA3 nem template de documento do RA3 [Fato, fonte 4].
- O RA1 e o RA2 já foram entregues. O notebook montado por seções ([ADR-0002](0002-notebook-montado-por-secoes.md)) e o repositório da entrega `eduardofabrii/data-analytics-ras` ([ADR-0011](0011-entregas-separadas-e-repositorio-da-entrega.md)) já funcionam.

## Opções consideradas

- **(a)** Um notebook novo só do RA3, que lê o conjunto preparado.
- **(b)** Continuar o mesmo notebook com a parte "RA3", seções 13 a 17, uma por requisito do enunciado.

## Decisão

**(b)**. O RA3 continua o notebook do projeto, depois da seção 12, no mesmo estilo do template (título da parte, enunciado de cada seção, células de código e "Resposta do grupo"):

| Seção | Requisito do enunciado | Arquivo |
|---|---|---|
| Abertura "RA3 — Analysis, Visualization and Machine Learning" e 13. Análise estatística descritiva | 2.1 | `notebook/secoes/13-estatistica-descritiva.py` |
| 14. Visualização e interpretação dos dados | 2.2 | `14-visualizacoes.py` |
| 15. Amostragem e representatividade | 2.3 | `15-representatividade.py` |
| 16. Aplicação de Machine Learning | 2.4 | `16-machine-learning.py` |
| 17. Conclusões do RA3 | 2.5 | `17-conclusoes-ra3.py` |

1. **Enunciados das seções:** como o template não tem o RA3, o enunciado de cada seção é o texto do requisito transcrito em [enunciados/ra3.md](../../enunciados/ra3.md), sem mudar o sentido. As seções 1 a 12 não mudam.
2. **Dados:** a seção 13 relê `dados/preparados/faixas_preparadas.csv` com os tipos do dicionário e cria `df_analise`, usado nas seções 13 a 16. Assim o RA3 parte do conjunto preparado do RA1 e não depende do estado do Spark do RA2.
3. **Bibliotecas:** pandas para as medidas, matplotlib para os gráficos e scikit-learn para o modelo, todas já presentes no Colab e registradas em `requirements.txt`. Pode-se trocar o algoritmo ou a biblioteca do modelo, desde que se registre em `requirements.txt` e na issue.
4. **Documentação:** `documentacao/ra3/README.md`, em Markdown, com as técnicas, os resultados e a interpretação de cada seção, citando a célula do notebook, e as instruções de execução. É copiado igual para o repositório da entrega, no mesmo caminho, e o README principal de lá aponta para ele.
5. **Envio:** a URL do repositório da entrega, com o notebook executado (`notebook/ra1-ra2-deezer.ipynb`, igual ao montado aqui) e o PDF dele atualizado, para quem avaliar sem executar.

## Consequências

- O mesmo `verificar_entrega.py` acusa resposta em branco, menção a IA e organização interna também no RA3 (critérios X.7 e X.9).
- O nome do arquivo no repositório da entrega (`ra1-ra2-deezer.ipynb`) fica igual, para não quebrar links já enviados no RA1 e no RA2.
- Gráficos, agregações e conclusões, que eram proibidos no RA1 (critério C5.5), passam a ser o conteúdo das seções 13 a 17; as seções 1 a 7 continuam sem eles.

---

## Ligações

- **Enunciado:** [enunciados/ra3.md](../../enunciados/ra3.md) · **Critérios:** [criterios-de-aceite-ra3](../../entregas/criterios-de-aceite-ra3.md) · **Plano:** [plano-de-tarefas-ra3](../../entregas/plano-de-tarefas-ra3.md)
- **Notebook:** [ADR-0002](0002-notebook-montado-por-secoes.md) · **Entrega:** [ADR-0011](0011-entregas-separadas-e-repositorio-da-entrega.md) · **Modelo:** [ADR-0013](0013-ra3-regressao-do-rank.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
