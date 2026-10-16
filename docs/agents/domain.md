# Documentação de domínio

Como as skills de engenharia (e qualquer assistente de IA) devem usar a documentação de domínio deste repositório.

## Antes de explorar, leia

- **`CONTEXT.md`** na raiz: entregas, fonte de dados, glossário, decisões vigentes, contrato entre as seções do notebook e o que ler para cada tarefa.
- **`docs/adr/`**: as decisões que tocam a área em que você vai trabalhar. O índice está em [`docs/adr/README.md`](../adr/README.md).
- **`enunciados/`**: o que o professor pede. Os enunciados têm precedência sobre as decisões.

Este repositório tem **um contexto só** (não há `CONTEXT-MAP.md`):

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-fonte-de-dados-api-deezer.md
│   └── ...
├── base/            base de conhecimento (API, qualidade, streaming, fontes)
└── enunciados/      enunciados do RA1 e do RA2
```

## Use o vocabulário do glossário

Quando o que você escreve nomeia um conceito do projeto (título de issue, célula do notebook, nome de coluna, mensagem de commit), use o termo como está no glossário do `CONTEXT.md`, seção 4: **faixa**, **chart**, **retrato bruto**, **conjunto preparado**, **evento de reprodução**, **janela tumbling/sliding**, IDs **Q**, **D** e **P**. Não troque por sinônimos.

Se o conceito de que você precisa não está no glossário, há duas possibilidades: você está inventando um termo que o projeto não usa (reconsidere) ou há uma lacuna de verdade (registre na issue da tarefa para o grupo decidir).

## Aponte conflito com ADR

Se o que você escreve contradiz uma decisão, diga isso de forma explícita, em vez de passar por cima em silêncio:

> _Contradiz o ADR-0004 (retrato bruto versionado), mas vale reabrir porque…_

Decisão com status "proposta" ainda orienta o trabalho; só o grupo muda o status.
