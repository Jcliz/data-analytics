# RA1 — Data Ingestion and Data Quality

> Transcrição da tarefa do Canvas (10 pontos, tentativas ilimitadas, prazo 21/10/2026). O envio é por **URL** (o formulário do Canvas só tem o campo "Insira o URL da web") e conta para todo o grupo PjBL.

## PjBL – RA1: Ingestão e Preparação dos Dados

### Objetivo

O objetivo do RA1 é definir o problema analítico, identificar e compreender os dados necessários para o projeto e desenvolver a primeira etapa do fluxo de dados: **obtenção, ingestão, avaliação da qualidade, limpeza e preparação dos dados**.

Ao final desta etapa, a equipe deverá possuir um **conjunto de dados confiável, documentado e preparado para as etapas de transformação e análise**, que serão desenvolvidas nos próximos RAs.

### Entrega

Cada equipe deverá entregar o repositório do projeto contendo a implementação desenvolvida durante o RA1 e a documentação dos itens apresentados a seguir.

1. Código fonte .ipynb com todas as células executadas
2. Documentação de todo o processo analítico: Template_RA1_Data_Analytics.docx (https://pucpr.instructure.com/courses/71291/files/6698464?wrap=1)

### 1. Definição do problema e perguntas analíticas

Apresentar o contexto do projeto e descrever claramente o problema que será investigado por meio dos dados.

Definir as principais **perguntas analíticas** que o projeto pretende responder.

As perguntas devem ser suficientemente específicas para orientar as próximas etapas do projeto.

### 2. Fontes de dados

Identificar e descrever o(s) conjunto(s) de dados utilizados no projeto.

Para cada fonte de dados, apresentar:

- fonte e origem dos dados;
- formato (CSV, JSON, API, banco de dados etc.);
- principais atributos/variáveis;
- quantidade aproximada de registros;
- relação dos dados com o problema proposto.

Quando aplicável, deverá ser disponibilizado o link ou referência de onde os dados foram obtidos.

### 3. Ingestão dos dados

Demonstrar como os dados são carregados para o ambiente do projeto.

Sempre que possível, o processo de ingestão deverá ser **reproduzível por meio de código**.

Podem ser utilizados, por exemplo:

- leitura de arquivos CSV, JSON ou outros formatos;
- consumo de APIs;
- consultas a bancos de dados;
- carregamento a partir de outras fontes externas.

### 4. Compreensão e avaliação da qualidade dos dados

Realizar uma exploração inicial dos dados e identificar problemas relevantes de qualidade.

A avaliação deverá considerar, quando aplicável:

- valores ausentes;
- registros duplicados;
- tipos de dados incorretos;
- formatos inconsistentes;
- valores inválidos ou impossíveis;
- categorias inconsistentes;
- possíveis outliers;
- outros problemas identificados pela equipe.

Nem todos os conjuntos de dados apresentarão todos esses problemas. A equipe deverá identificar e discutir **os aspectos que realmente forem relevantes para seus dados**.

### 5. Limpeza e preparação dos dados

Implementar os procedimentos necessários para tratar os problemas identificados durante a avaliação da qualidade.

As principais decisões tomadas pela equipe deverão ser **justificadas**.

Entre os possíveis procedimentos estão:

- remoção ou tratamento de valores ausentes;
- remoção de registros duplicados;
- correção de tipos de dados;
- padronização de formatos;
- correção ou padronização de categorias;
- tratamento de valores inválidos;
- tratamento de outliers, quando apropriado.

O objetivo **não é aplicar a maior quantidade possível de técnicas**, mas tomar decisões adequadas às características dos dados e ao problema do projeto.

### 6. Conjunto de dados resultante do RA1

Gerar ou identificar claramente o conjunto de dados resultante da etapa de preparação.

A equipe deverá demonstrar que os dados resultantes apresentam qualidade e consistência suficientes para serem utilizados nas próximas etapas do projeto.

**Importante:** transformações analíticas, agregações, construção de indicadores, visualizações e obtenção de conclusões **não fazem parte da entrega do RA1**. Esses elementos serão desenvolvidos nas próximas etapas do PjBL.

## Rubrica de avaliação

A avaliação do RA1 será realizada durante a apresentação da equipe em sala, considerando os critérios abaixo:

| Critério | Peso | O que será avaliado |
|---|---|---|
| Problema e perguntas analíticas | 20% | Clareza na definição do problema e das perguntas que o projeto pretende investigar com os dados. |
| Compreensão dos dados | 20% | Capacidade de explicar a origem dos dados, o que representam e quais atributos são relevantes para o projeto. |
| Qualidade e preparação dos dados | 35% | Identificação dos principais problemas de qualidade presentes na base, tratamento realizado e justificativa das decisões tomadas. |
| Ingestão e reprodutibilidade | 15% | Demonstração de como os dados são carregados e organização do processo de forma que possa ser reproduzido. |
| Organização, documentação e reprodutibilidade | 10% | Projeto bem organizado e documentado, permitindo reproduzir o fluxo desenvolvido no RA1. |

### Escala de avaliação

Cada critério será avaliado utilizando a seguinte escala:

- **4 — Excelente:** atende completamente ao critério e demonstra domínio.
- **3 — Adequado:** atende bem ao critério, com pequenas lacunas.
- **2 — Parcial:** atende parcialmente ao critério ou apresenta justificativas frágeis.
- **1 — Insuficiente:** apresenta lacunas significativas.
- **0 — Não apresentado.**

**Observação:** não é necessário aplicar todas as técnicas de limpeza e preparação apresentadas em aula. A equipe deverá identificar os problemas que realmente existem em sua base e justificar as decisões tomadas para tratá-los.

## Escopo do RA1

**Fontes de Dados → Ingestão → Compreensão dos Dados → Avaliação da Qualidade → Limpeza e Preparação → Dados Preparados**

O conjunto de dados preparado no RA1 será utilizado como ponto de partida para o **RA2 – Transformação e Processamento dos Dados**.
