# Dados

| Pasta | O que guarda | Quem grava | Versionada? |
|---|---|---|---|
| `brutos/AAAA-MM-DD/` | **Retrato bruto**: as respostas da API da Deezer, em JSON, exatamente como vieram, mais um `metadados.json` (data e hora da coleta, chamadas feitas, erros). Uma pasta por data de coleta. | Seção 02 do notebook, com `BAIXAR_DA_API = True` (área B) | Sim |
| `preparados/` | **Conjunto preparado** do RA1: `faixas_preparadas.csv`, já limpo, com colunas em português. Entrada do RA2. | Seções 04 e 05 do notebook (área D) | Sim |
| `streaming/` | Pastas de execução do RA2: `entrada/` (monitorada pelo Spark), `publicacao/` (onde cada arquivo é escrito antes de ser movido) e `checkpoint/`. | Seção 09 do notebook (área B) | Não (só este README) |

Regras ([ADR-0004](../docs/adr/0004-retrato-bruto-versionado.md)):

- **Nunca edite um retrato bruto à mão.** Problema nos dados se trata na limpeza (seção 04), com a decisão registrada.
- O notebook lê o retrato **mais recente** por padrão (`BAIXAR_DA_API = False`). Coletar de novo muda os números de todas as seções: combine com o grupo antes, e só antes da execução final.
- O conjunto preparado é regravado pelo notebook. Não edite o CSV à mão.
- Se o retrato passar de 50 MB, o grupo reavalia o formato (por exemplo, `.json.gz`).
