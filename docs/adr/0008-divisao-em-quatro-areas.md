---
id: adr-0008
titulo: "ADR-0008 — Trabalho dividido em quatro áreas, uma por integrante"
tipo: decisao
decisao: "0008"
status: proposta
data: 2026-10-15
decisor: proposta para o grupo
entregas: [RA1, RA2]
areas: [A, B, C, D]
fontes: [3, 6]
relacionados: [adr-0002]
---
# ADR-0008 — Trabalho dividido em quatro áreas, uma por integrante

- **Status:** proposta · **Data:** 15/10/2026

## Contexto

- O RA1 e o RA2 são entregas do grupo, mas a avaliação é na apresentação, e cada integrante precisa saber explicar a sua parte.
- A rubrica do RA1 pesa: problema e perguntas 20%, compreensão dos dados 20%, qualidade e preparação 35%, ingestão e reprodutibilidade 15%, organização 10% [Fato, fonte 3].

## Decisão

Quatro áreas seguindo o fluxo do enunciado ("Fontes → Ingestão → Compreensão → Qualidade → Limpeza → Dados preparados"), cada uma com uma parte do RA1 e uma do RA2:

| Área | RA1 | RA2 |
|---|---|---|
| **A** — Problema e síntese | Problema, recorte e perguntas; identificação e considerações do notebook; documento do RA1 em `.docx` para a entrega (referências, consolidação e PDF) | Objetivo da análise em streaming (8) e considerações (12) |
| **B** — Fonte, ingestão e reprodutibilidade | Ficha da fonte, coleta pela API, retrato bruto; organização e reprodutibilidade | Fonte e processamento: gerador de eventos e `readStream` (9) |
| **C** — Compreensão e qualidade | Exploração inicial, dicionário de dados, diagnóstico Q1…Qn | Janela temporal e agregação (10) |
| **D** — Limpeza e conjunto resultante | Decisões D1…Dn, transformações de preparo, conjunto preparado | Resultados e interpretação (11) |

Tarefas gerais (revisão cruzada, execução final, PDF do notebook e envio) ficam sem dono fixo: quem puxar se atribui. O documento do RA1 em `.docx` é da área A, por decisão do João (15/10/2026). A atribuição de pessoas a áreas está no [plano de tarefas](../../entregas/plano-de-tarefas.md).

## Consequências

- A qualidade e a preparação (35%) ficam com duas áreas (C diagnostica, D trata), que se alinham pelos IDs Q e D.
- Dependências: B → C → D no RA1; o RA2 depende do conjunto preparado (D), mas B e C podem começar com uma amostra.
- Cada área edita só os seus arquivos (seção 2 do plano); dependências vão para issues `pendencia-cruzada`.

---

## Ligações

- **Plano:** [plano-de-tarefas](../../entregas/plano-de-tarefas.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
