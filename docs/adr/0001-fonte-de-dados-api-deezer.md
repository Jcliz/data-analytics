---
id: adr-0001
titulo: "ADR-0001 — Fonte de dados: API pública da Deezer"
tipo: decisao
decisao: "0001"
status: aceita
data: 2026-10-15
decisor: João Pedro Cardoso
entregas: [RA1, RA2]
areas: [A, B, C, D]
fontes: [1, 2]
relacionados: [api-deezer, adr-0004]
---
# ADR-0001 — Fonte de dados: API pública da Deezer

- **Status:** aceita · **Data:** 15/10/2026 · **Decisor:** João Pedro Cardoso

## Contexto

- O RA1 pede uma fonte de dados real, descrita e carregada de forma reproduzível; o RA2 reaproveita os dados do RA1.
- O grupo já conhece a API da Deezer pelo app [dataaudio](https://github.com/rdsalvesPUC/dataaudio) (Desenvolvimento Mobile Híbrido), que consome `/chart/0/tracks`, `/search` e `/track/{id}` [Fato, fonte 2].

## Opções consideradas

- **(a)** Um conjunto pronto (CSV do Kaggle ou similar).
- **(b)** A API pública da Deezer, coletada pelo próprio notebook.

## Decisão

**(b).** A API da Deezer é a base de dados do RA1 e do RA2. O dataaudio é a referência para endpoints e para o formato dos objetos (`Track`, artista e álbum aninhados).

## Consequências

- A ingestão é por API (o enunciado do RA1 cita "consumo de APIs" como exemplo), o que vale para o critério de ingestão e reprodutibilidade.
- A API não exige chave, então não há segredo no repositório.
- A resposta muda com o tempo e pode variar com o país de onde se faz a requisição; isso é tratado pelo retrato bruto ([ADR-0004](0004-retrato-bruto-versionado.md)).
- Os dados pertencem à Deezer e aos detentores de direitos; o uso é acadêmico, como no dataaudio.

---

## Ligações

- **Base:** [api-deezer](../../base/api-deezer.md), [fontes](../../base/fontes.md)
- **Outras decisões:** [0004](0004-retrato-bruto-versionado.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
