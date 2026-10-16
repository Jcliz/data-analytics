---
id: adr-0004
titulo: "ADR-0004 — Retrato bruto da API versionado"
tipo: decisao
decisao: "0004"
status: proposta
data: 2026-10-15
decisor: proposta para o grupo
entregas: [RA1, RA2]
areas: [B, C, D]
fontes: [1]
relacionados: [adr-0001, api-deezer]
---
# ADR-0004 — Retrato bruto da API versionado

- **Status:** proposta · **Data:** 15/10/2026

## Contexto

- O chart da Deezer muda todo dia e pode depender do país de onde vem a requisição [Inferência, a confirmar na primeira coleta; ver api-deezer §5]. Se o notebook consultar a API a cada execução, os números do documento deixam de bater com o notebook.
- O critério "ingestão e reprodutibilidade" (15%) e o "organização, documentação e reprodutibilidade" (10%) pedem que outra pessoa consiga refazer o fluxo [Fato, fonte 3].

## Opções consideradas

- **(a)** Consultar a API em toda execução.
- **(b)** Coletar uma vez, gravar as respostas cruas em `dados/brutos/AAAA-MM-DD/` e versionar; o notebook lê do retrato por padrão e só consulta a API com `BAIXAR_DA_API = True`.

## Decisão

**(b).** O código de coleta continua no notebook (seção 02) e é demonstrado; o retrato usado na entrega é o versionado.

## Consequências

- Os números do documento, do notebook e da apresentação são os mesmos para todos.
- A data da coleta e o país aparente da requisição entram na ficha da fonte (documento do RA1, seção 02).
- Regerar o retrato muda todas as contagens; só se faz com o grupo de acordo, e antes da execução final.
- O retrato deve caber no repositório (alguns MB). Se passar de 50 MB, o grupo reavalia (compactar em `.json.gz`).

---

## Ligações

- **Base:** [api-deezer](../../base/api-deezer.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
