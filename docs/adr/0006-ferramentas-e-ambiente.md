---
id: adr-0006
titulo: "ADR-0006 — pandas no RA1, PySpark 4.0.3 no RA2, Colab como referência"
tipo: decisao
decisao: "0006"
status: proposta
data: 2026-10-15
decisor: proposta para o grupo
entregas: [RA1, RA2]
areas: [A, B, C, D]
fontes: [7, 8, 9]
relacionados: [adr-0002]
---
# ADR-0006 — pandas no RA1, PySpark 4.0.3 no RA2, Colab como ambiente de referência

- **Status:** proposta · **Data:** 15/10/2026

## Contexto

- Os notebooks de aula de ingestão e qualidade usam pandas; os de streaming usam PySpark 4.0.3, que pede Python 3.9+ e Java 17+ [Fato, fontes 7, 8 e 9].
- O grupo usa Windows; o Colab já tem Java e roda o PySpark com `%pip install`.

## Decisão

- **RA1:** Python 3 com `pandas` e `requests` (ingestão, exploração, limpeza).
- **RA2:** `pyspark==4.0.3`, como nas aulas.
- **Ambiente de referência para a execução final:** Google Colab. Execução local é bem-vinda, desde que as versões batam com `requirements.txt`.

## Consequências

- `requirements.txt` lista as versões; a seção 00b do notebook instala o que faltar no Colab e clona o repositório para ter o retrato bruto.
- No Windows, quem quiser rodar o Spark localmente precisa de Java 17; quem não tiver usa o Colab.
- Gráficos não entram no RA1; se forem usados para mostrar distribuição na exploração, usar `matplotlib` sem conclusões analíticas.

---

## Ligações

- **Base:** [material de aula](../../base/material-de-aula.md)
- **Índice:** [README.md](README.md) · **Contexto geral:** [CONTEXT.md](../../CONTEXT.md)
