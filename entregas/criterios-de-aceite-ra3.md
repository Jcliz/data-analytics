# Critérios de aceite — RA3

> Definição de pronto do RA3. Cada tarefa do [plano do RA3](plano-de-tarefas-ra3.md) cita os IDs daqui. Os critérios saem do [enunciado do RA3](../enunciados/ra3.md); os do RA1 e do RA2 continuam em [criterios-de-aceite.md](criterios-de-aceite.md), e as regras gerais X.1, X.2, X.6, X.7 e X.9 de lá valem também para o RA3.
>
> **Pesos:** a tabela de pontos da rubrica do Canvas ainda não foi transcrita (ver [enunciado](../enunciados/ra3.md), seção 6). Quando chegar, cada bloco abaixo recebe o peso entre parênteses, como no RA1.

O protocolo para agentes da seção 0 de [criterios-de-aceite.md](criterios-de-aceite.md) vale igual: um item por ID, evidência por critério (seção e célula do notebook, contagem real), segunda passagem separada da escrita e relatório final `ID | status | evidência`.

## 1. Notebook, seções 13 a 17

### R13 — Análise estatística descritiva (seção 13)
- [ ] **R13.1** Dados relidos de `dados/preparados/faixas_preparadas.csv` com os tipos do dicionário, em `df_analise`; a contagem de linhas e de faixas distintas aparece na saída.
- [ ] **R13.2** Tendência central (média e/ou mediana) por gênero das variáveis das perguntas P1 a P4 (duração, idade da faixa, `rank`, número de fãs, artistas por chart).
- [ ] **R13.3** Dispersão (desvio-padrão, amplitude ou intervalo interquartil) das mesmas variáveis.
- [ ] **R13.4** Distribuição: frequência, concentração ou proporções (ex.: faixas de duração, proporção de lançamentos nos 12 meses anteriores à coleta, fatia dos 5 artistas com mais posições por chart).
- [ ] **R13.5** Escolha das medidas justificada pelas características dos dados (ex.: mediana onde há assimetria ou extremos) e comparação entre gêneros feita só com os charts de gênero, com o chart geral à parte.
- [ ] **R13.6** Resposta do grupo explica o que os números representam no contexto do projeto, com os números das saídas.

### R14 — Visualização e interpretação (seção 14)
- [ ] **R14.1** Pelo menos três visualizações, cada uma de uma característica diferente dos dados.
- [ ] **R14.2** Tipo de gráfico adequado à informação (ex.: boxplot para distribuição por grupo, barras para proporção, dispersão para relação entre duas variáveis).
- [ ] **R14.3** Identificação clara: título, eixos com nome e unidade, legenda quando houver grupos; legível no PDF do notebook.
- [ ] **R14.4** Interpretação breve depois de cada visualização, com padrão, tendência, diferença ou comportamento relevante e números, sem se limitar a descrever o gráfico.

### R15 — Amostragem e representatividade (seção 15)
- [ ] **R15.1** Origem e abrangência do conjunto: fonte, data do retrato, país aparente da coleta, charts e gêneros cobertos, limite de itens por chart, com as contagens.
- [ ] **R15.2** Se os registros representam o problema investigado (a população que eles representam e a que não representam).
- [ ] **R15.3** Limitações e vieses que podem influenciar os resultados, cada um ligado ao resultado que ele pode afetar.
- [ ] **R15.4** Amostragem: se alguma etapa usou amostra, como os registros foram selecionados; se não, dizer que o conjunto inteiro foi usado.

### R16 — Aplicação de Machine Learning (seção 16)
- [ ] **R16.1** Problema preditivo definido (classificação ou regressão) e ligado ao problema do projeto.
- [ ] **R16.2** Variável-alvo e características identificadas, sem vazamento (nenhuma característica derivada do alvo nem identificador), com o motivo de cada escolha.
- [ ] **R16.3** Separação de treino e teste com proporção informada e semente fixa (`SEMENTE_ML`); a mesma faixa não fica no treino e no teste.
- [ ] **R16.4** Modelo treinado e previsões feitas sobre o teste, com uma tabela curta de valor real × previsto.
- [ ] **R16.5** Pelo menos uma métrica adequada ao problema, comparada com uma linha de base simples.
- [ ] **R16.6** Interpretação do desempenho: o que a métrica significa, o que o modelo explica e o que não explica.
- [ ] **R16.7** Bibliotecas novas registradas em `requirements.txt`; os números se repetem numa nova execução.

### R17 — Conclusões do RA3 (seção 17)
- [ ] **R17.1** Principais resultados das análises estatísticas e das visualizações.
- [ ] **R17.2** Interpretação do desempenho do modelo.
- [ ] **R17.3** Limitações dos dados e das análises.
- [ ] **R17.4** Relação dos resultados com o problema e com cada pergunta P1 a P4.

### RN — Notebook
- [ ] **RN.1** A abertura da parte "RA3" e as seções 13 a 17 seguem o estilo do template (enunciado, código, "Resposta do grupo"); as seções 1 a 12 não mudam.
- [ ] **RN.2** Todas as células executadas em ordem, sem erro, a partir de um ambiente limpo, incluindo o RA1 e o RA2.
- [ ] **RN.3** Nenhum `[Preencha aqui.]` ou orientação entre colchetes sobrando nas seções 13 a 17.
- [ ] **RN.4** Respostas curtas, com números tirados das saídas; cada célula de código começa com um comentário-título.

RN.3 e RN.4 valem para toda tarefa que escreve no notebook, restritos à seção dela.

## 2. Repositório da entrega

### RD — Documentação e instruções de execução
- [ ] **RD.1** `documentacao/ra3/README.md` descreve as técnicas usadas em cada seção (13 a 17), os resultados e a interpretação, citando a seção e a célula do notebook; números iguais aos do notebook executado.
- [ ] **RD.2** Instruções de execução no mesmo arquivo: onde abrir (Colab e local), dependências (`requirements.txt`, Java só para o RA2), ordem de execução, tempo aproximado e como conferir que deu certo.
- [ ] **RD.3** Repositório da entrega (`eduardofabrii/data-analytics-ras`) público e atualizado: notebook igual ao montado aqui e executado, PDF do notebook atualizado, `documentacao/ra3/README.md` e `requirements.txt` iguais aos daqui, README principal apontando para a documentação do RA3.
- [ ] **RD.4** URL enviada no Canvas até 18/11/2026, conferida numa janela anônima.

### RAP — Apresentação (avaliação somativa em 18/11/2026)
- [ ] **RAP.1** Roteiro em `entregas/roteiro-apresentacao-ra3.md` (criado na tarefa do roteiro), com um bloco por requisito (estatística, visualizações, representatividade, Machine Learning, conclusões), quem fala e qual célula mostrar; cada integrante explica as decisões e as técnicas da sua parte e sabe interpretar os resultados.

## 3. Revisão cruzada do RA3

- [ ] **RK.1** Cada pergunta P1 a P4 tem medida na seção 13, visualização na 14 e resposta na 17.
- [ ] **RK.2** Os números da documentação, das conclusões e da apresentação batem com as saídas do notebook executado.
- [ ] **RK.3** As limitações da seção 15 aparecem nas conclusões (17) e na interpretação do modelo (16).
- [ ] **RK.4** Nenhuma issue `pendencia-cruzada` do RA3 aberta.
- [ ] **RK.5** `python scripts/verificar_entrega.py` sem pendência.
- [ ] **RK.6** Ensaio da execução completa a partir de um clone limpo do repositório da entrega no Colab, com o resultado anotado no relatório da revisão.
- [ ] **RK.7** Regras gerais conferidas: português (X.1), commits sem coautoria de IA (X.2), nenhuma declaração de uso de IA (X.7), nenhuma citação da organização interna (X.9).
