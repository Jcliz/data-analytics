---
id: base-indice
titulo: "Base de conhecimento"
tipo: indice
status: vigente
atualizado: 2026-10-15
relacionados: [api-deezer, qualidade-de-dados, streaming-e-janelas, material-de-aula, sugestoes-de-perguntas, fontes]
---
# Base de conhecimento

> O que sustenta o trabalho além dos enunciados: como a fonte de dados funciona, o que o material de aula ensina e o que esperar de qualidade e de streaming. Abra só o arquivo que a sua tarefa pede (`CONTEXT.md`, seção 9).

| Arquivo | Para que serve | Áreas |
|---|---|---|
| [api-deezer.md](api-deezer.md) | Endpoints, paginação, limites, objetos e armadilhas da API da Deezer; desenho sugerido da coleta | A, B, C, D |
| [qualidade-de-dados.md](qualidade-de-dados.md) | Problemas de qualidade a investigar nesta base, com a regra de verificação e o tratamento possível | C, D |
| [streaming-e-janelas.md](streaming-e-janelas.md) | Structured Streaming, janelas tumbling e sliding, modos de saída e o padrão de simulação das aulas | A, B, C, D (RA2) |
| [material-de-aula.md](material-de-aula.md) | Resumo dos slides e notebooks da disciplina e onde cada um ajuda | todas |
| [sugestoes-de-perguntas.md](sugestoes-de-perguntas.md) | Ideias de problema e perguntas analíticas, para a área A escolher | A |
| [fontes.md](fontes.md) | Lista única de fontes, numeradas | todas |

## Regras

- **[Fato]** é o que foi lido numa fonte da lista ou observado nos dados (com célula). **[Inferência]** é dedução ou conhecimento prévio ainda não conferido; confira antes de usar como número no documento.
- Fonte nova entra no fim de `fontes.md`, com o próximo número. A numeração existente não muda.
- Arquivo novo segue o formato destes: cabeçalho YAML (`id`, `titulo`, `tipo`, `status`, `atualizado`, `relacionados`) e seção "Ligações" no fim.
- Ao confirmar uma [Inferência] com os dados reais, troque a marcação para [Fato] e cite a célula do notebook.

---

## Ligações

- **Contexto geral:** [CONTEXT.md](../CONTEXT.md) · **Decisões:** [docs/adr/README.md](../docs/adr/README.md)
