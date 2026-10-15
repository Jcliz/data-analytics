# RA2 — Data Stream

> Transcrição da tarefa do Canvas (10 pontos, tentativas ilimitadas, prazo 21/10/2026). O envio é um **arquivo PDF** e conta para todo o grupo PjBL.

Aplicar os conceitos de processamento de dados em streaming utilizando **Apache Spark Structured Streaming**, demonstrando a recepção de novos registros e a utilização de janelas temporais para realizar uma análise relacionada ao projeto desenvolvido no RA1.

## 1. Desenvolvimento da atividade

Cada grupo deverá implementar uma análise simples utilizando processamento em streaming. A implementação poderá seguir um dos cenários abaixo, de acordo com as características do projeto.

### Cenário A — Projetos com dados estáticos

Para projetos que utilizam bases de dados fixas, o grupo deverá simular a chegada de novos registros.

- Criar um pequeno conjunto de registros artificiais coerentes com o contexto do projeto.
- Simular a chegada desses registros em diferentes momentos.
- Processar os registros utilizando Spark Structured Streaming.
- Aplicar uma agregação por janelas temporais (*Tumbling* ou *Sliding*).
- Demonstrar os resultados do processamento.

### Cenário B — Projetos com dados em streaming

Para projetos que já utilizam fontes de dados contínuas, o grupo poderá trabalhar diretamente com sua fonte.

- Demonstrar como os novos registros são recebidos e processados.
- Aplicar uma agregação por janelas temporais (*Tumbling* ou *Sliding*).
- Apresentar os resultados e demonstrar seu comportamento com a chegada de novos registros.

## 2. Documentação

O desenvolvimento deverá ser registrado no **notebook do projeto**, disponibilizado como template da disciplina.

Na seção correspondente ao RA2, o grupo deverá apresentar:

1. **Objetivo da análise:** o que deseja monitorar ou descobrir com o processamento em streaming.
2. **Fonte e processamento:** como os novos registros são obtidos, reais ou simulados, e processados.
3. **Janelas temporais:** qual tipo de janela foi utilizado, sua duração, o deslocamento (quando aplicável) e a operação de agregação realizada.
4. **Resultados e interpretação:** o que foi observado e como os resultados se comportam com a chegada de novos dados.

As explicações devem ser breves e inseridas em células Markdown, acompanhadas das respectivas implementações em código.

## 3. Entrega e apresentação

- **Entrega:** PDF do notebook Jupyter (ipynb) contendo o desenvolvimento do projeto, com as seções RA1 e RA2 organizadas. (converta o notebook em pdf e envie nessa entrega).
- **Apresentação oral:** demonstração do funcionamento da implementação em sala de aula. (apenas para a profe com 5 minutos de duração).

Não é necessário desenvolver dashboards, integrar ferramentas adicionais como Kafka ou implementar técnicas avançadas de streaming. Uma única análise utilizando janelas temporais é suficiente.

## 4. Critérios de avaliação

| Critério | Pontuação |
|---|---|
| **Processamento em streaming:** implementação funcional da recepção e do processamento de novos registros, reais ou simulados. | 3,0 |
| **Janelas temporais:** aplicação correta de uma janela temporal e de uma operação de agregação coerente com a análise. | 3,0 |
| **Documentação e interpretação:** descrição das decisões tomadas e interpretação dos resultados obtidos. | 2,0 |
| **Demonstração:** apresentação clara do funcionamento e evidência do processamento de novos registros. | 2,0 |
| **Total** | **10,0** |

### Observações

- O grupo poderá utilizar os exemplos desenvolvidos em aula como referência, adaptando-os ao contexto do próprio projeto.
- Não é necessário utilizar os dois tipos de janela. O grupo deverá escolher apenas um.
- Para projetos com dados estáticos, a simulação de streaming é suficiente para atender aos requisitos da atividade.
- A avaliação do RA2 será concentrada no processamento em streaming e na utilização de janelas temporais, não sendo necessário refazer as análises e visualizações do RA1.
