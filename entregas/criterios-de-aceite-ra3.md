# Critérios de aceite — RA3

> Definição de pronto do RA3. Cada tarefa do [plano do RA3](plano-de-tarefas-ra3.md) cita os IDs daqui. Os critérios do RA1 e do RA2 continuam em [criterios-de-aceite.md](criterios-de-aceite.md).
>
> **De onde vem cada item.** A seção 1 só traz o que está no [enunciado do RA3](../enunciados/ra3.md), com a seção dele entre parênteses; nada ali é regra nova. A seção 2 traz as regras que o repositório já tinha no RA1 e no RA2 e que continuam valendo. A seção 3 traz **recomendações** do grupo para fazer bem o que o enunciado pede: não são exigência da rubrica, e quem não as seguir explica por quê na issue.
>
> **Pesos:** a tabela de pontos da rubrica do Canvas ainda não foi transcrita (ver [enunciado](../enunciados/ra3.md), seção 6). Quando chegar, cada bloco da seção 1 recebe o peso entre parênteses, como no RA1.

O protocolo para agentes da seção 0 de [criterios-de-aceite.md](criterios-de-aceite.md) vale igual: um item por ID, evidência por critério (seção e célula do notebook, contagem real), segunda passagem separada da escrita e relatório final `ID | status | evidência`.

## 1. Exigências do enunciado do RA3

Os exemplos entre parênteses mostram como o item se aplica a estes dados; não são exigência.

### R13 — Análise estatística descritiva (seção 13 do notebook; enunciado 2.1)
- [ ] **R13.1** Tendência central: média e/ou mediana para compreender valores representativos (ex.: duração, idade da faixa, `rank` e fãs por gênero, ligados às perguntas P1 a P4).
- [ ] **R13.2** Dispersão: amplitude, desvio-padrão ou medida equivalente para analisar a variabilidade.
- [ ] **R13.3** Distribuição: frequência, concentração ou distribuição dos valores (ex.: proporção de lançamentos nos 12 meses anteriores à coleta, fatia dos 5 artistas com mais posições por chart).
- [ ] **R13.4** Medidas coerentes com as características dos dados e com o problema investigado.
- [ ] **R13.5** Resultados apresentados e explicados: o que representam no contexto do projeto.

### R14 — Visualização e interpretação (seção 14; enunciado 2.2)
- [ ] **R14.1** Pelo menos três visualizações que ajudem a compreender diferentes características dos dados.
- [ ] **R14.2** Cada visualização adequada à informação apresentada.
- [ ] **R14.3** Identificação clara das variáveis e dos resultados (ex.: título, nome dos eixos, legenda).
- [ ] **R14.4** Cada visualização acompanhada de uma breve interpretação, que identifica padrões, tendências, diferenças ou comportamentos relevantes, sem se limitar a apresentar o gráfico.

### R15 — Amostragem e representatividade (seção 15; enunciado 2.3)
- [ ] **R15.1** Origem e abrangência do conjunto de dados (ex.: fonte, data do retrato, charts e gêneros cobertos).
- [ ] **R15.2** Se os registros representam adequadamente o problema investigado.
- [ ] **R15.3** Possíveis limitações ou vieses que possam influenciar os resultados.
- [ ] **R15.4** Se alguma etapa usou amostra, como os registros foram selecionados. (Implementar amostragem não é obrigatório.)

### R16 — Aplicação de Machine Learning (seção 16; enunciado 2.4)
- [ ] **R16.1** Aprendizagem supervisionada por classificação ou por regressão, com o problema preditivo definido.
- [ ] **R16.2** Variável-alvo (*target*) e características (*features*) identificadas.
- [ ] **R16.3** Dados separados para treinamento e teste.
- [ ] **R16.4** Modelo treinado e previsões realizadas.
- [ ] **R16.5** Resultados avaliados com pelo menos uma métrica adequada ao problema.
- [ ] **R16.6** Se for usado outro conjunto de dados nesta seção (permitido quando o original não serve), justificativa breve da escolha.

Qualquer algoritmo ou biblioteca serve (não é obrigatório KNN, regressão linear nem scikit-learn).

### R17 — Conclusões do RA3 (seção 17; enunciado 2.5)
- [ ] **R17.1** Principais resultados das análises estatísticas e das visualizações.
- [ ] **R17.2** Interpretação do desempenho do modelo de Machine Learning.
- [ ] **R17.3** Limitações dos dados e das análises realizadas.
- [ ] **R17.4** Relação dos resultados com o problema definido no projeto (as perguntas P1 a P4).

### RD — Entrega no repositório (enunciado 3 e 5)
- [ ] **RD.1** Implementação: notebook (ou código) com as análises estatísticas, as visualizações e a aplicação de Machine Learning, funcional e acessível para avaliação.
- [ ] **RD.2** Documentação: descrição das técnicas utilizadas, dos resultados obtidos e das interpretações.
- [ ] **RD.3** Instruções de execução: o necessário para executar e verificar as implementações.
- [ ] **RD.4** URL do repositório enviada no Canvas até 18/11/2026.

### RAP — Avaliação somativa (enunciado 4)
- [ ] **RAP.1** Na apresentação de 18/11/2026, a equipe apresenta os resultados e demonstra as implementações.
- [ ] **RAP.2** Os integrantes sabem explicar as decisões tomadas, justificar as técnicas usadas e interpretar os resultados.

## 2. Regras do repositório que continuam valendo

Vêm das decisões e dos critérios do RA1 e do RA2, não do enunciado do RA3.

- [ ] **RN.1** Notebook montado das seções (`python scripts/montar_notebook.py`, [ADR-0002](../docs/adr/0002-notebook-montado-por-secoes.md)) e executado em ordem, sem erro, a partir de um ambiente limpo (como o N.2).
- [ ] **RN.2** Nenhum `[Preencha aqui.]` ou orientação entre colchetes sobrando nas seções 13 a 17 (como o N.3).
- [ ] **RN.3** Respostas do grupo curtas, com números tirados das saídas (como o N.4).
- [ ] **RN.4** As seções 1 a 12 e o documento do RA1, já entregues, não mudam.
- [ ] **RN.5** Repositório citado na entrega é o `eduardofabrii/data-analytics-ras`, com o notebook igual ao montado aqui ([ADR-0011](../docs/adr/0011-entregas-separadas-e-repositorio-da-entrega.md)).
- [ ] **RN.6** Regras gerais X.1 (português), X.2 (commits sem coautoria de IA), X.6 (mesmos números em todo lugar), X.7 (nenhuma declaração de uso de IA) e X.9 (nenhuma citação da organização interna) de [criterios-de-aceite.md](criterios-de-aceite.md).

RN.2 e RN.3 valem para toda tarefa que escreve no notebook, restritos à seção dela.

## 3. Recomendações do grupo (não são exigência da rubrica)

Ajudam a cumprir a seção 1 com estes dados. Quem decidir não seguir uma delas registra o motivo na issue.

- **RC.1** Comparar gêneros só com os charts de gênero, com o chart geral à parte, como o dicionário do conjunto preparado orienta.
- **RC.2** Dizer por que cada medida foi escolhida (ex.: mediana onde há assimetria ou extremos), o que torna o R13.4 visível para quem avalia.
- **RC.3** Ligar uma visualização a cada pergunta P1 a P4, para as conclusões responderem a todas.
- **RC.4** No Machine Learning: nenhuma característica derivada do alvo nem identificador; a mesma faixa não ficar no treino e no teste; semente fixa (`SEMENTE_ML`) para repetir os números; comparar a métrica com uma linha de base simples; mostrar uma tabela curta de valor real × previsto ([ADR-0013](../docs/adr/0013-ra3-regressao-do-rank.md), proposta).
- **RC.5** Documentação e instruções num arquivo só, `documentacao/ra3/README.md` ([ADR-0012](../docs/adr/0012-ra3-no-notebook-e-entrega-por-url.md), proposta), citando a seção e a célula do notebook.
- **RC.6** Comentário-título na primeira linha de cada célula de código, como no RA1 e no RA2, para a documentação e a apresentação citarem a célula.
- **RC.7** Roteiro da apresentação em `entregas/roteiro-apresentacao-ra3.md`, com quem fala e qual célula mostrar, como no RA1 e no RA2.
- **RC.8** Antes de enviar: ensaio da execução completa a partir de um clone limpo do repositório da entrega no Colab, e a URL aberta numa janela anônima.

## 4. Revisão cruzada do RA3

- [ ] **RK.1** Cada item da seção 1 tem evidência (seção e célula do notebook, arquivo, contagem).
- [ ] **RK.2** Os números da documentação, das conclusões e da apresentação batem com as saídas do notebook executado.
- [ ] **RK.3** As limitações da seção 15 aparecem nas conclusões (seção 17).
- [ ] **RK.4** Nenhuma issue `pendencia-cruzada` do RA3 aberta.
- [ ] **RK.5** `python scripts/verificar_entrega.py` sem pendência.
- [ ] **RK.6** Recomendações da seção 3 seguidas, ou o motivo de não seguir registrado na issue.
