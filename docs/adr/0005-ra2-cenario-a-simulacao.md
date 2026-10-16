---
id: adr-0005
titulo: "ADR-0005 — RA2 no cenário A, com eventos de reprodução simulados"
tipo: decisao
decisao: "0005"
status: proposta
data: 2026-10-15
decisor: proposta para o grupo
entregas: [RA2]
areas: [A, B, C, D]
fontes: [6, 7, 8]
relacionados: [streaming-e-janelas]
---
# ADR-0005 — RA2 no cenário A, com eventos de reprodução simulados

- **Status:** proposta · **Data:** 15/10/2026

## Contexto

- O RA2 oferece o cenário A (dados estáticos, com simulação da chegada de registros) e o cenário B (fonte contínua real) [Fato, fonte 6].
- A API da Deezer não tem um fluxo contínuo de eventos (não há endpoint de reproduções em tempo real); o chart é um retrato [Inferência].
- O exemplo de aula grava eventos em JSON numa pasta monitorada pelo Spark Structured Streaming, com saída em memória e modo `complete` [Fato, fontes 7 e 8].

## Opções consideradas

- **(a)** Cenário B, consultando o chart em intervalos curtos (*polling*) e tratando cada consulta como evento.
- **(b)** Cenário A: gerar eventos artificiais de **reprodução de faixa** a partir do conjunto preparado do RA1, gravá-los em lotes numa pasta monitorada e processá-los com `readStream`.

## Decisão

**(b)**, com o mesmo padrão técnico das aulas: eventos `{id_evento, id_faixa, genero, artista, duracao_ouvida_s, instante}` gravados em JSON em `dados/streaming/entrada/`, lidos com esquema explícito e agregados por janela temporal.

O **tipo de janela** (tumbling ou sliding), a duração, o deslocamento e a agregação ficam para a área C (seção 10), coerentes com o objetivo definido pela área A (seção 8). Sugestão de partida: reproduções por gênero numa janela sliding de 5 minutos com deslocamento de 2 minutos, como na aula.

## Consequências

- O enunciado aceita a simulação: "para projetos com dados estáticos, a simulação de streaming é suficiente".
- Os eventos precisam ser coerentes com o projeto: faixas e gêneros reais do conjunto preparado; a frequência de cada faixa pode seguir o `rank` (mais popular, mais tocada).
- Na seção 12, o grupo pode dizer que o streaming foi um exercício didático, como o próprio template permite.

---

## Ligações

- **Base:** [streaming-e-janelas](../../base/streaming-e-janelas.md), [material de aula](../../base/material-de-aula.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
